# FILEPATH: nfelib/cte/client/v4_0/cte.py
# Copyright (C) 2025  Raphaël Valyi - Akretion

import logging
from typing import Any

from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb
from lxml import etree

# --- Content Bindings ---
from nfelib.cte.bindings.v4_0.cons_sit_cte_v4_00 import ConsSitCte
from nfelib.cte.bindings.v4_0.cons_stat_serv_cte_v4_00 import ConsStatServCte
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import Tcte
from nfelib.cte.bindings.v4_0.ret_cons_sit_cte_v4_00 import RetConsSitCte
from nfelib.cte.bindings.v4_0.ret_cons_stat_serv_cte_v4_00 import RetConsStatServCte
from nfelib.cte.bindings.v4_0.ret_cte_v4_00 import RetCte

# --- Server Definitions ---
from nfelib.cte.client.v4_0.servers import Endpoint
from nfelib.cte.client.v4_0.servers import servers as SERVERS_CTE

# --- SOAP Bindings ---
from nfelib.cte.soap.v4_0.cteconsultav4 import CteConsultaV4Soap12CteConsultaCt
from nfelib.cte.soap.v4_0.cterecepcaosincv4 import CteRecepcaoSincV4Soap12CteRecepcao
from nfelib.cte.soap.v4_0.ctestatusservicov4 import (
    CteStatusServicoV4Soap12CteStatusServicoCt,
)

_logger = logging.getLogger(__name__)


def _get_server_key_for_uf(uf_ibge_code: str) -> str:
    """Gets the server key ('MT', 'SVRS', etc.) for a given UF."""
    uf_map = {
        "51": "MT",
        "50": "MS",
        "31": "MG",
        "41": "PR",
        "43": "RS",
        "35": "SP",
        "16": "AP",
        "26": "PE",
        "14": "RR",
    }
    # Fallback to SVRS for many states
    return uf_map.get(uf_ibge_code, "SVRS")


# TODO The event methods in CteClient should follow the same high-level pattern
# proposed for NfeClient: accept data primitives (chave, protocolo, etc.) and
# handle the creation and signing of the detEvento internally.


class CteClient(FiscalClient):
    """A façade for the CTe v4.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        # Default to model 57 (CT-e) if not specified
        self.mod = kwargs.pop("mod", "57")
        self.soap12_envelope = (True,)
        super().__init__(service="cte", versao="4.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_key = _get_server_key_for_uf(self.uf)
        try:
            server_data = SERVERS_CTE[server_key]
        except KeyError:
            raise ValueError(
                f"No server configuration found for key: {server_key} (derived from UF {self.uf})"
            )

        server_host = (
            server_data["prod_server"]
            if self.ambiente == Tamb.PROD.value
            else server_data["dev_server"]
        )
        path = server_data["endpoints"][endpoint_type]
        location = f"https://{server_host}{path}"
        _logger.debug(f"Determined location for {endpoint_type.name}: {location}")
        return location

    def send(
        self,
        action_class: type,
        obj: Any,
        **kwargs: Any,
    ) -> Any:
        """Builds and sends a request, wrapping the payload in cteDadosMsg."""
        action_to_endpoint_map = {
            CteStatusServicoV4Soap12CteStatusServicoCt: Endpoint.CTESTATUSSERVICOV4,
            CteConsultaV4Soap12CteConsultaCt: Endpoint.CTECONSULTAV4,
            CteRecepcaoSincV4Soap12CteRecepcao: Endpoint.CTERECEPCAOSINCV4,
        }
        endpoint_type = action_to_endpoint_map[action_class]
        location = self._get_location(endpoint_type)

        if isinstance(obj, Tcte):
            wrapped_obj = {"Body": {"cteDadosMsg": {"value": obj}}}
        else:
            wrapped_obj = {"Body": {"cteDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class=action_class,
            location=location,
            wrapped_obj=wrapped_obj,
            **kwargs,
        )

        # The actual result is nested inside the response structure
        if not self.wrap_response:
            if isinstance(obj, ConsStatServCte):
                return response.body.cteStatusServicoCTResult.content[0]
            return response.body.content[0].content[0]

        if isinstance(obj, ConsStatServCte):
            response.resposta = response.body.cteStatusServicoCTResult.content
        else:
            response.resposta = response.resposta.body.content[0].content[0]
        return response

    def status_servico(self) -> RetConsStatServCte:
        """Consulta o status do serviço CT-e."""
        payload = ConsStatServCte(tpAmb=Tamb(self.ambiente), versao=self.versao)
        return self.send(CteStatusServicoV4Soap12CteStatusServicoCt, payload)

    def consulta_documento(
        self, chave: str
    ) -> RetConsSitCte:  # NOTE consulta_documento in erpbrasil
        """Consulta a situação de um CT-e pela chave de acesso."""
        payload = ConsSitCte(tpAmb=Tamb(self.ambiente), chCTe=chave, versao=self.versao)
        return self.send(CteConsultaV4Soap12CteConsultaCt, payload)

    def envia_documento(
        self, cte_obj: Tcte
    ) -> RetCte:  # NOTE enviar_documento in erpbrasil
        """Envia um único CT-e de forma síncrona.

        Args:
            cte_obj: The Tcte object to be signed and sent.

        Returns:
            The processing result from the SEFAZ.
        """
        signed_xml = cte_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=cte_obj.infCte.Id,
        )
        # FIXME this is wrong, see erpbrasil envia_documento and gzip

        # The webservice expects the signed CTe object directly inside cteDadosMsg
        return self.send(
            CteRecepcaoSincV4Soap12CteRecepcao, etree.fromstring(signed_xml)
        )

    # TODO enviar_lote_evento, cancela_documento, carta_correcao, consulta_recibo, get_documento_id, monta_qrcode, monta_cte_proc
