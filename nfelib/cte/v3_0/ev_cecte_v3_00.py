from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCecteDescEvento(Enum):
    COMPROVANTE_DE_ENTREGA_DO_CT_E = "Comprovante de Entrega do CT-e"


@dataclass
class EvCecte:
    """
    Schema XML de validação do evento comprovante de entrega eletrônico do CT-e
    110180.

    :ivar desc_evento: Descrição do Evento - “Comprovante de Entrega do
        CT-e”
    :ivar n_prot: Número do Protocolo de autorização do CT-e
    :ivar dh_entrega: Data e hora de conclusão da entrega da NF-e
        Formato AAAA-MM-DDTHH:MM:DD TZD
    :ivar n_doc: Número do Documento de identificação da pessoa que
        recebeu a entrega
    :ivar x_nome: Nome da pessoa que recebeu a entrega
    :ivar latitude: Latitude do ponto de entrega
    :ivar longitude: Longitude do ponto de entrega
    :ivar hash_entrega: Hash (SHA1) no formato Base64 resultante da
        concatenação: Chave de acesso do CT-e + Base64 da imagem
        capturada da entrega (Exemplo: imagem capturada da assinatura
        eletrônica, digital do recebedor, foto, etc) O hashCSRT é o
        resultado das funções SHA-1 e base64 do token CSRT fornecido
        pelo fisco + chave de acesso do DF-e. (Implementação em futura
        NT) Observação: 28 caracteres são representados no schema como
        20 bytes do tipo base64Binary
    :ivar dh_hash_entrega: Data e hora de geração do hash entrega
        Formato AAAA-MM-DDTHH:MM:DD TZD
    :ivar inf_entrega: Grupo de informações das NF-e que foram entregues
        ao Destinatário Informar o grupo apenas para CT-e com tipo de
        serviço Normal
    """
    class Meta:
        name = "evCECTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvCecteDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    n_prot: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProt",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
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
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
        }
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
        }
    )
    hash_entrega: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashEntrega",
            "type": "Element",
            "required": True,
            "length": 20,
            "format": "base64",
        }
    )
    dh_hash_entrega: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhHashEntrega",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    inf_entrega: List["EvCecte.InfEntrega"] = field(
        default_factory=list,
        metadata={
            "name": "infEntrega",
            "type": "Element",
            "max_occurs": 2000,
        }
    )

    @dataclass
    class InfEntrega:
        """
        :ivar ch_nfe: Chave de acesso da NF-e entregue
        """
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
