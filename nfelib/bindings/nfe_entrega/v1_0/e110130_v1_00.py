from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.nfe_entrega.v1_0.tipos_basico_v1_03 import TcorgaoIbge

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento(Enum):
    COMPROVANTE_DE_ENTREGA_DA_NF_E = "Comprovante de Entrega da NF-e"


class DetEventoTpAutor(Enum):
    """
    1=Empresa Emitente; 2=Empresa Destinatária; 3=Empresa; 5=Fisco; 6=RFB;
    9=Outros;
    """
    VALUE_1 = "1"


class DetEventoVersao(Enum):
    VALUE_1_00 = "1.00"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento de Comprovante de Entrega da NF-e.

    :ivar desc_evento:
    :ivar c_orgao_autor:
    :ivar tp_autor:
    :ivar ver_aplic: Versão do Aplicativo do Autor do Evento
    :ivar dh_entrega: Data e hora do final da entrega. Formato AAAA-
        MMDDThh:mm:ssTZD
    :ivar n_doc:
    :ivar x_nome: Nome da pessoa que assinou o Comprovante de Entrega da
        NF-e
    :ivar lat_gps: Latitude do ponto de entrega
    :ivar long_gps: Longitude do ponto de entrega
    :ivar hash_comprovante: Hash (SHA1) no formato Base64 resultante da
        concatenação: Chave de acesso da NFe + Base64 da imagem
        capturada da entrega (Exemplo: imagem capturada da assinatura
        eletrônica, digital do recebedor, foto, etc) O hashCSRT é o
        resultado das funções SHA-1 e base64 do token CSRT fornecido
        pelo fisco + chave de acesso do DF-e. (Implementação em futura
        NT) Observação: 28 caracteres são representados no schema como
        20 bytes do tipo base64Binary
    :ivar dh_hash_comprovante: Data e hora da geração do hash do
        Comprovante de Entrega da NF-e. Formato AAAA-MMDDThh:mm:ssTZD.
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    desc_evento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
        }
    )
    c_orgao_autor: Optional[TcorgaoIbge] = field(
        default=None,
        metadata={
            "name": "cOrgaoAutor",
            "type": "Element",
            "required": True,
        }
    )
    tp_autor: Optional[DetEventoTpAutor] = field(
        default=None,
        metadata={
            "name": "tpAutor",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dh_entrega: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhEntrega",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    n_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "nDoc",
            "type": "Element",
            "required": True,
            "min_length": 2,
            "max_length": 20,
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    lat_gps: Optional[str] = field(
        default=None,
        metadata={
            "name": "latGPS",
            "type": "Element",
            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
        }
    )
    long_gps: Optional[str] = field(
        default=None,
        metadata={
            "name": "longGPS",
            "type": "Element",
            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
        }
    )
    hash_comprovante: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashComprovante",
            "type": "Element",
            "required": True,
            "length": 20,
            "format": "base64",
        }
    )
    dh_hash_comprovante: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhHashComprovante",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    versao: Optional[DetEventoVersao] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
