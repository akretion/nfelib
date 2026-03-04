# Copyright (C) 2026  Raphaël Valyi - Akretion

import logging
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import (
    FiscalClient,
    Tamb,
)

# --- Content Bindings ---
from nfelib.cte.client.v4_0.servers import Endpoint

# --- Server Definitions ---
from nfelib.cte.client.v4_0.servers import servers as SERVERS_CTE

# --- SOAP Bindings ---
from nfelib.cte.soap.v4_0.ctedistribuicaodfe import (
    CteDistribuicaoDfeSoapCteDistDfeInteresse,
)

# --- Dist DF-e ---
from nfelib.cte_dist_dfe.bindings.v1_0 import DistDfeInt, RetDistDfeInt

_logger = logging.getLogger(__name__)


class DfeClient(FiscalClient):
    """A façade for the CTe SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "55")
        super().__init__(
            service="nfe",
            versao="1.01",
            **kwargs,
        )

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Construct the full HTTPS URL for the specified service."""
        server_key = "AN"
        try:
            server_data = SERVERS_CTE[server_key]
        except KeyError:
            raise ValueError(
                f"No server configuration found for key: {server_key} "
                "(derived from UF {self.uf})"
            )

        if self.ambiente == Tamb.PROD.value:
            endpoints = server_data["prod_endpoints"]
        else:
            endpoints = server_data.get("dev_endpoints", server_data["prod_endpoints"])

        try:
            return endpoints[endpoint_type]
        except KeyError:
            raise ValueError(
                f"Endpoint {endpoint_type.name} not configured for server key: "
                "{server_key}"
            )

    def send(self, action_class, obj, **kwargs):
        action_to_endpoint_map = {
            CteDistribuicaoDfeSoapCteDistDfeInteresse: Endpoint.CTEDISTRIBUICAODFE,
        }
        endpoint_type = action_to_endpoint_map[action_class]
        location = self._get_location(endpoint_type)

        wrapped_obj: dict[str, Any]
        if isinstance(obj, DistDfeInt):
            wrapped_obj = {
                # Notice the 'cteDistDFeInteresse' and 'cteDadosMsg' vs CTe
                "Body": {"cteDistDFeInteresse": {"cteDadosMsg": {"content": [obj]}}}
            }
        else:
            wrapped_obj = {"Body": {"cteDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class,
            location,
            wrapped_obj,
            **kwargs,
        )

        # Unwrapping response logic
        soap_envelope = response.resposta if self.wrap_response else response
        result_container = (
            soap_envelope.body.cteDistDFeInteresseResponse.cteDistDFeInteresseResult
        )

        result_container = (
            soap_envelope.body.cteDistDFeInteresseResponse.cteDistDFeInteresseResult
        )

        if not self.wrap_response:
            return result_container.content[0]

        response.resposta = result_container.content[0]

        return response

    def consultar_distribuicao(
        self,
        cnpj_cpf: str,
        ultimo_nsu: str = "",
        nsu_especifico: str = "",
        chave: str = "",
    ) -> Optional[RetDistDfeInt]:
        """Consultar Distribução de CTe.

        :param cnpj_cpf: CPF ou CNPJ a ser consultado
        :param ultimo_nsu: Último NSU para pesquisa. Formato: '999999999999999'
        :param nsu_especifico: NSU Específico para pesquisa.
                                Formato: '999999999999999'
        :param chave: Chave de acesso do documento
        :return: Retorna uma estrutura contendo as estruturas de envio
        e retorno preenchidas
        """
        if not ultimo_nsu and not nsu_especifico and not chave:
            return None

        distNSU = consNSU = None
        if ultimo_nsu:
            distNSU = DistDfeInt.DistNsu(ultNSU=ultimo_nsu)
        if nsu_especifico:
            consNSU = DistDfeInt.ConsNsu(NSU=nsu_especifico)

        if distNSU and consNSU:
            # TODO: Raise?
            return None

        return self.send(
            CteDistribuicaoDfeSoapCteDistDfeInteresse,
            DistDfeInt(
                versao=self.versao,
                tpAmb=self.ambiente,
                cUFAutor=self.uf,
                CNPJ=cnpj_cpf if len(cnpj_cpf) > 11 else None,
                CPF=cnpj_cpf if len(cnpj_cpf) <= 11 else None,
                distNSU=distNSU,
                consNSU=consNSU,
            ),
        )
