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
    """A façade for the CTe DF-e distribution webservice."""

    def __init__(self, **kwargs: Any):
        # The CT-e 4.00 webservices, CTeDistribuicaoDFe included, expect a
        # SOAP 1.2 envelope (unlike the NF-e DF-e distribution); the WSDL also
        # publishes a SOAP 1.1 port, so this can be overridden through kwargs.
        kwargs.setdefault("soap12_envelope", True)
        super().__init__(
            service="cte",
            versao="1.00",
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
                "(the CT-e DF-e distribution is only available on the "
                "Ambiente Nacional)"
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
                f"{server_key}"
            )

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
                          (e.g., CteDistribuicaoDfeSoapCteDistDfeInteresse).
            obj: The *content* model instance (e.g., DistDfeInt) or a dictionary.
                 This will be wrapped inside cteDadosMsg.
            placeholder_content: A string content to be injected in the payload.
                                 Used for signed content to avoid signature issues.
            placeholder_exp: Placeholder expression where to inject placeholder_content.
            kwargs: Additional keyword arguments for FiscalClient.send.

        Returns:
            The *content* response model instance (e.g., RetDistDfeInt).
        """
        try:
            # Determine the correct endpoint enum based on the action class
            action_to_endpoint_map: dict[type, Endpoint] = {
                CteDistribuicaoDfeSoapCteDistDfeInteresse: (
                    Endpoint.CTEDISTRIBUICAODFE
                ),
            }
            endpoint_type = action_to_endpoint_map[action_class]
            location = self._get_location(endpoint_type)

        except KeyError:
            raise ValueError(
                "Could not determine Endpoint for action_class: "
                f"{action_class.__name__}"
            )

        wrapped_obj: dict[str, Any]
        if isinstance(obj, DistDfeInt):
            # Notice the 'cteDistDFeInteresse' and 'cteDadosMsg' wrapper
            # elements of the CT-e webservice.
            wrapped_obj = {
                "Body": {"cteDistDFeInteresse": {"cteDadosMsg": {"content": [obj]}}}
            }
        else:
            wrapped_obj = {"Body": {"cteDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class,
            location,
            wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )

        # wrap_response=True keeps backward compatibility with erpbrasil.edoc
        # so that consumers migrating to brazil_fiscal_client don't need a
        # large refactor. In that mode the parent returns a WrappedResponse
        # whose parsed SOAP envelope is in .resposta; otherwise it returns
        # the parsed SOAP envelope directly.
        soap_envelope = response.resposta if self.wrap_response else response

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
    ) -> Optional[RetDistDfeInt]:
        """Consultar Distribução de CTe.

        Unlike the NF-e, the CT-e DF-e distribution has no query by access key:
        only the last NSU or a specific NSU can be asked for.

        :param cnpj_cpf: CPF ou CNPJ a ser consultado
        :param ultimo_nsu: Último NSU para pesquisa. Formato: '999999999999999'
        :param nsu_especifico: NSU Específico para pesquisa.
                                Formato: '999999999999999'
        :return: Retorna uma estrutura contendo as estruturas de envio
        e retorno preenchidas
        """
        if not ultimo_nsu and not nsu_especifico:
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
