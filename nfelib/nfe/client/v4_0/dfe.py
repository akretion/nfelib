# Copyright (C) 2019  Luis Felipe Mileo - KMEE
# Copyright (C) 2025  Raphaël Valyi - Akretion

import logging
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import (
    FiscalClient,
    Tamb,
)

# --- Content Bindings ---
from nfelib.nfe.client.v4_0.servers import Endpoint

# --- Server Definitions ---
from nfelib.nfe.client.v4_0.servers import servers as SERVERS_NFE

# --- SOAP Bindings ---
from nfelib.nfe.soap.v4_0.nfedistribuicaodfe import (
    NfeDistribuicaoDfeSoapNfeDistDfeInteresse,
)

# --- Dist DF-e ---
from nfelib.nfe_dist_dfe.bindings.v1_0 import DistDfeInt, RetDistDfeInt

_logger = logging.getLogger(__name__)


class DfeClient(FiscalClient):
    """A façade for the NFe SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "55")
        super().__init__(
            service="nfe",
            versao="4.00",
            **kwargs,
        )

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Construct the full HTTPS URL for the specified service."""
        server_key = "AN"
        try:
            server_data = SERVERS_NFE[server_key]
        except KeyError:
            raise ValueError(
                f"No server configuration found for key: {server_key} "
                "(derived from UF {self.uf})"
            )

        if self.ambiente == Tamb.PROD.value:
            server_host = server_data["prod_server"]
        else:
            server_host = server_data["dev_server"]

        try:
            path = server_data["endpoints"][endpoint_type]
        except KeyError:
            raise ValueError(
                f"Endpoint {endpoint_type.name} not configured for server key: "
                "{server_key}"
            )

        location = f"https://{server_host}{path}"
        _logger.debug(
            f"Determined location for {endpoint_type.name} (UF: {self.uf}, "
            "Amb: {self.ambiente}): {location}"
        )
        return location

    def send(
        self,
        action_class: type,
        obj: Any,
        placeholder_exp: Optional[str] = None,
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Build and send a request for the input object.

        Args:
            action_class: type generated with xsdata for the SOAP wsdl action
                          (e.g., NfeStatusServico4SoapNfeStatusServicoNf).
            obj: The *content* model instance (e.g., ConsStatServ) or a dictionary.
                 This will be wrapped inside nfeDadosMsg.
            placeholder_content: A string content to be injected in the payload.
                                 Used for signed content to avoid signature issues.
            placeholder_exp: Placeholder expression where to inject placeholder_content.
            kwargs: Additional keyword arguments for FiscalClient.send.

        Returns:
            The *content* response model instance (e.g., RetConsStatServ).
        """
        try:
            # Determine the correct endpoint enum based on the action class
            action_to_endpoint_map: dict[type, Endpoint] = {
                NfeDistribuicaoDfeSoapNfeDistDfeInteresse: Endpoint.NFEDISTRIBUICAODFE,
            }
            endpoint_type = action_to_endpoint_map[action_class]
            location = self._get_location(endpoint_type)

        except KeyError:
            raise ValueError(
                "Could not determine Endpoint for action_class: {action_class.__name__}"
            )

        wrapped_obj: dict[str, Any]
        if isinstance(obj, DistDfeInt):
            wrapped_obj = {
                "Body": {"nfeDistDFeInteresse": {"nfeDadosMsg": {"content": [obj]}}}
            }
        else:
            wrapped_obj = {"Body": {"nfeDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class,
            location,
            wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )

        result_container = (
            response.body.nfeDistDFeInteresseResponse.nfeDistDFeInteresseResult
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
        """Consultar Distribução de NFe.

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

        distNSU = consNSU = consChNFe = None
        if ultimo_nsu:
            distNSU = DistDfeInt.DistNsu(ultNSU=ultimo_nsu)
        if nsu_especifico:
            consNSU = DistDfeInt.ConsNsu(NSU=nsu_especifico)
        if chave:
            consChNFe = DistDfeInt.ConsChNfe(chNFe=chave)

        if (distNSU and consNSU) or (distNSU and consChNFe) or (consNSU and consChNFe):
            # TODO: Raise?
            return None

        return self.send(
            NfeDistribuicaoDfeSoapNfeDistDfeInteresse,
            DistDfeInt(
                versao=self.versao,
                tpAmb=self.ambiente,
                cUFAutor=self.uf,
                CNPJ=cnpj_cpf if len(cnpj_cpf) > 11 else None,
                CPF=cnpj_cpf if len(cnpj_cpf) <= 11 else None,
                distNSU=distNSU,
                consNSU=consNSU,
                consChNFe=consChNFe,
            ),
        )
