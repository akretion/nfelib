# Copyright (C) 2026  Renato Lima - Akretion <renato.lima@akretion.com.br>

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ValidationError:
    """Result of a failed business validation rule."""

    rule_id: str  # e.g. "B03-10"
    msg_code: int  # e.g. 897
    effect: str  # "Rej." or "Den."
    description: str  # e.g. "Rejeição: Código numérico em formato inválido."
    field_path: str = ""  # e.g. "ide/cNF"
    item: int = 0  # nItem (for per-item rules)

    def __str__(self) -> str:
        s = f"[{self.rule_id}] {self.msg_code} - {self.description}"
        if self.item:
            s += f" [nItem:{self.item}]"
        return s


# ---------------------------------------------------------------------------
# CNPJ / CPF validation
# ---------------------------------------------------------------------------

_CNPJ_WEIGHTS_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
_CNPJ_WEIGHTS_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validate_cnpj(cnpj: str) -> bool:
    """Validate CNPJ check digits. Expects 14-digit string."""
    if not cnpj or not cnpj.isdigit() or len(cnpj) != 14:
        return False
    if cnpj == "0" * 14:
        return False
    digits = [int(c) for c in cnpj]
    s = sum(d * w for d, w in zip(digits[:12], _CNPJ_WEIGHTS_1)) % 11
    d1 = 0 if s < 2 else 11 - s
    if digits[12] != d1:
        return False
    s = sum(d * w for d, w in zip(digits[:13], _CNPJ_WEIGHTS_2)) % 11
    d2 = 0 if s < 2 else 11 - s
    return digits[13] == d2


_CPF_INVALID_PATTERNS = {str(i) * 11 for i in range(10)}


def validate_cpf(cpf: str) -> bool:
    """Validate CPF check digits. Expects 11-digit string."""
    if not cpf or not cpf.isdigit() or len(cpf) != 11:
        return False
    if cpf in _CPF_INVALID_PATTERNS:
        return False
    digits = [int(c) for c in cpf]
    s = sum(d * (10 - i) for i, d in enumerate(digits[:9])) % 11
    d1 = 0 if s < 2 else 11 - s
    if digits[9] != d1:
        return False
    s = sum(d * (11 - i) for i, d in enumerate(digits[:10])) % 11
    d2 = 0 if s < 2 else 11 - s
    return digits[10] == d2


# ---------------------------------------------------------------------------
# Access Key (Chave de Acesso) DV - Module 11
# ---------------------------------------------------------------------------


def validate_access_key_dv(key: str) -> bool:
    """Validate the check digit (position 44) of a 44-digit access key."""
    if not key or len(key) != 44 or not key.isdigit():
        return False
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    s = 0
    for i, c in enumerate(reversed(key[:43])):
        s += int(c) * weights[i % 8]
    remainder = s % 11
    expected = 0 if remainder < 2 else 11 - remainder
    return int(key[43]) == expected


def build_access_key(
    cuf: str,
    aamm: str,
    cnpj_cpf: str,
    mod: str,
    serie: str,
    nnf: str,
    tpemis: str,
    cnf: str,
) -> str:
    """Build the 43-digit base of an access key (without DV)."""
    cnpj_cpf_padded = cnpj_cpf.zfill(14)
    return (
        cuf.zfill(2)
        + aamm.zfill(4)
        + cnpj_cpf_padded
        + mod.zfill(2)
        + serie.zfill(3)
        + nnf.zfill(9)
        + tpemis
        + cnf.zfill(8)
    )


# ---------------------------------------------------------------------------
# GTIN (EAN) check digit validation
# ---------------------------------------------------------------------------


def validate_gtin(gtin: str) -> bool:
    """Validate GTIN check digit (EAN-8, EAN-13, EAN-14)."""
    if not gtin or not gtin.isdigit() or len(gtin) not in (8, 12, 13, 14):
        return False
    digits = [int(c) for c in gtin]
    check = digits[-1]
    body = digits[:-1]
    s = 0
    for i, d in enumerate(reversed(body)):
        s += d * (3 if i % 2 == 0 else 1)
    expected = (10 - s % 10) % 10
    return check == expected


# GS1 valid prefixes (simplified - main ranges)
_VALID_GS1_PREFIXES = set()
# Brazil: 789, 790
for p in range(789, 791):
    _VALID_GS1_PREFIXES.add(str(p))
# Other common ranges (0-9xx are generally valid)
for p in range(0, 1000):
    _VALID_GS1_PREFIXES.add(str(p).zfill(3))


def validate_gtin_prefix(gtin: str) -> bool:
    """Validate GS1 prefix of a GTIN. Simplified - always returns True
    as full prefix validation requires the official GS1 prefix table.
    """
    # NOTE: Full validation requires the GS1 prefix table published
    # on the NF-e portal. This simplified version always passes.
    return True


# ---------------------------------------------------------------------------
# SUFRAMA inscription validation
# ---------------------------------------------------------------------------


def validate_suframa(isuf: str) -> bool:
    """Validate SUFRAMA inscription check digit."""
    if not isuf or not isuf.isdigit() or len(isuf) != 9:
        return False
    digits = [int(c) for c in isuf]
    weights = [9, 8, 7, 6, 5, 4, 3, 2]
    s = sum(d * w for d, w in zip(digits[:8], weights))
    remainder = s % 11
    dv = 0 if remainder < 2 else 11 - remainder
    return digits[8] == dv


_SUFRAMA_UFS = {"AC", "AM", "RO", "RR"}
_SUFRAMA_AP_MUNIC = {"1600303", "1600600"}


def validate_suframa_uf(uf: str, cmun: str = "") -> bool:
    """Check if UF (and optionally município) is in the SUFRAMA area."""
    if uf in _SUFRAMA_UFS:
        return True
    return bool(uf == "AP" and cmun in _SUFRAMA_AP_MUNIC)


# ---------------------------------------------------------------------------
# Municipality code (IBGE) basic validation
# ---------------------------------------------------------------------------

# UF code to abbreviation mapping (IBGE)
UF_CODE_MAP = {
    "11": "RO",
    "12": "AC",
    "13": "AM",
    "14": "RR",
    "15": "PA",
    "16": "AP",
    "17": "TO",
    "21": "MA",
    "22": "PI",
    "23": "CE",
    "24": "RN",
    "25": "PB",
    "26": "PE",
    "27": "AL",
    "28": "SE",
    "29": "BA",
    "31": "MG",
    "32": "ES",
    "33": "RJ",
    "35": "SP",
    "41": "PR",
    "42": "SC",
    "43": "RS",
    "50": "MS",
    "51": "MT",
    "52": "GO",
    "53": "DF",
}

UF_ABBREV_TO_CODE = {v: k for k, v in UF_CODE_MAP.items()}

VALID_UF_CODES = set(UF_CODE_MAP.keys())


def validate_municipality_code(cmun: str) -> bool:
    """Basic validation: 7 digits and UF prefix is valid."""
    if not cmun or len(cmun) != 7 or not cmun.isdigit():
        return False
    return cmun[:2] in VALID_UF_CODES


def municipality_matches_uf(cmun: str, uf: str) -> bool:
    """Check if the first 2 digits of cMun correspond to the UF."""
    if not cmun or len(cmun) < 2:
        return False
    expected_code = UF_ABBREV_TO_CODE.get(uf)
    if not expected_code:
        return False
    return cmun[:2] == expected_code


# ---------------------------------------------------------------------------
# cNF invalid patterns (B03-10)
# ---------------------------------------------------------------------------

_CNF_INVALID_PATTERNS = {
    "00000000",
    "11111111",
    "22222222",
    "33333333",
    "44444444",
    "55555555",
    "66666666",
    "77777777",
    "88888888",
    "99999999",
    "12345678",
    "23456789",
    "34567890",
    "45678901",
    "56789012",
    "67890123",
    "78901234",
    "89012345",
    "90123456",
    "01234567",
}


def validate_cnf(cnf: str, nnf: str) -> bool:
    """Validate cNF format per B03-10."""
    if cnf in _CNF_INVALID_PATTERNS:
        return False
    return cnf != nnf.zfill(8)


# ---------------------------------------------------------------------------
# CFOP reference tables
# ---------------------------------------------------------------------------

# CFOPs valid for NFC-e (model 65) - I08-150
NFCE_VALID_CFOPS = {
    "5101",
    "5102",
    "5103",
    "5104",
    "5115",
    "5405",
    "5656",
    "5667",
    "5933",
}

# CFOPs for devolution of merchandise (simplified list)
CFOP_DEVOLUTION = {
    "1201",
    "1202",
    "1203",
    "1204",
    "1208",
    "1209",
    "1410",
    "1411",
    "1503",
    "1504",
    "1553",
    "1660",
    "1661",
    "1662",
    "2201",
    "2202",
    "2203",
    "2204",
    "2208",
    "2209",
    "2410",
    "2411",
    "2503",
    "2504",
    "2553",
    "2660",
    "2661",
    "2662",
    "5201",
    "5202",
    "5208",
    "5209",
    "5410",
    "5411",
    "5412",
    "5413",
    "5503",
    "5553",
    "5555",
    "5556",
    "5660",
    "5661",
    "5662",
    "6201",
    "6202",
    "6208",
    "6209",
    "6410",
    "6411",
    "6412",
    "6413",
    "6503",
    "6553",
    "6555",
    "6556",
    "6660",
    "6661",
    "6662",
}


# CFOPs for importation (starts with 3)
def is_cfop_importacao(cfop: str) -> bool:
    """Check if CFOP indicates importation."""
    return cfop.startswith("3")


def is_cfop_exportacao(cfop: str) -> bool:
    """Check if CFOP indicates exportation."""
    return cfop.startswith("7")


def is_cfop_entrada(cfop: str) -> bool:
    """Check if CFOP indicates an incoming transaction."""
    return cfop[:1] in ("1", "2", "3")


def is_cfop_saida(cfop: str) -> bool:
    """Check if CFOP indicates an outgoing transaction."""
    return cfop[:1] in ("5", "6", "7")


def is_cfop_interestadual(cfop: str) -> bool:
    """Check if CFOP indicates an interstate transaction."""
    return cfop[:1] in ("2", "6")


def is_cfop_interna(cfop: str) -> bool:
    """Check if CFOP indicates an internal transaction."""
    return cfop[:1] in ("1", "5")


def is_cfop_exterior(cfop: str) -> bool:
    """Check if CFOP indicates an external transaction."""
    return cfop[:1] in ("3", "7")


# Importação CFOPs exception list (for DI/II/IPI rules)
CFOP_IMPORT_EXCEPTIONS = {"3201", "3202", "3211", "3503", "3553"}

# CFOPs for SUFRAMA desoneração (N28-20)
CFOP_SUFRAMA = {
    "1203",
    "1204",
    "1208",
    "1209",
    "2203",
    "2204",
    "2208",
    "2209",
    "5109",
    "5110",
    "5120",
    "5151",
    "5152",
    "5651",
    "5652",
    "5654",
    "5655",
    "5658",
    "5659",
    "5910",
    "6905",
    "6109",
    "6110",
    "6120",
    "6122",
    "6123",
    "6151",
    "6152",
    "6651",
    "6652",
    "6654",
    "6655",
    "6658",
    "6659",
    "6910",
    "6923",
}


# ---------------------------------------------------------------------------
# Rounding helper (with R$ 0.01 tolerance)
# ---------------------------------------------------------------------------


def values_match(val1: float, val2: float, tolerance: float = 0.01) -> bool:
    """Check if two monetary values match within tolerance."""
    return abs(val1 - val2) <= tolerance


def safe_decimal(value) -> float:
    """Convert a value to float safely, treating None as 0.0."""
    if value is None:
        return 0.0
    try:
        return float(str(value))
    except (ValueError, TypeError):
        return 0.0


# ---------------------------------------------------------------------------
# UF regions (for interstate ICMS rate validation)
# ---------------------------------------------------------------------------

# Sul e Sudeste (exceto ES)
UF_SUL_SUDESTE = {"MG", "RJ", "SP", "PR", "SC", "RS"}
# Norte, Nordeste, Centro-Oeste e ES
UF_NORTE_NE_CO_ES = {
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "RN",
    "RO",
    "RR",
    "SE",
    "TO",
}

# UFs that don't allow indIEDest=2 (ISENTO) in interstate operations
UF_NO_IE_ISENTO_INTERESTADUAL = {
    "AM",
    "BA",
    "CE",
    "GO",
    "MG",
    "MS",
    "MT",
    "PA",
    "PE",
    "RN",
    "SE",
    "SP",
}


# ---------------------------------------------------------------------------
# BACEN country codes (Tabela de Países - used in cPais fields)
# Source: BACEN catalog used by NF-e MOC. Brazil = 1058.
# ---------------------------------------------------------------------------

# Subset of the BACEN/IBGE country code table used in NF-e
VALID_BACEN_COUNTRY_CODES = {
    "0132",
    "0175",
    "0230",
    "0248",
    "0370",
    "0400",
    "0418",
    "0434",
    "0477",
    "0531",
    "0590",
    "0639",
    "0647",
    "0655",
    "0663",
    "0671",
    "0701",
    "0728",
    "0736",
    "0779",
    "0809",
    "0817",
    "0833",
    "0850",
    "0884",
    "0906",
    "0930",
    "0973",
    "1015",
    "1023",
    "1031",
    "1058",
    "1082",
    "1112",
    "1155",
    "1171",
    "1198",
    "1201",
    "1236",
    "1244",
    "1252",
    "1279",
    "1287",
    "1295",
    "1317",
    "1325",
    "1376",
    "1414",
    "1457",
    "1490",
    "1508",
    "1511",
    "1554",
    "1571",
    "1597",
    "1600",
    "1635",
    "1651",
    "1694",
    "1732",
    "1767",
    "1775",
    "1783",
    "1791",
    "1805",
    "1821",
    "1848",
    "1856",
    "1902",
    "1937",
    "1961",
    "2003",
    "2054",
    "2089",
    "2097",
    "2100",
    "2127",
    "2135",
    "2151",
    "2178",
    "2194",
    "2232",
    "2240",
    "2259",
    "2291",
    "2321",
    "2356",
    "2380",
    "2399",
    "2402",
    "2445",
    "2453",
    "2461",
    "2470",
    "2496",
    "2518",
    "2534",
    "2550",
    "2569",
    "2585",
    "2607",
    "2631",
    "2640",
    "2666",
    "2690",
    "2712",
    "2755",
    "2810",
    "2852",
    "2895",
    "2917",
    "2933",
    "2976",
    "3018",
    "3050",
    "3093",
    "3131",
    "3174",
    "3212",
    "3239",
    "3247",
    "3255",
    "3263",
    "3271",
    "3280",
    "3301",
    "3344",
    "3379",
    "3417",
    "3450",
    "3484",
    "3506",
    "3514",
    "3557",
    "3573",
    "3595",
    "3611",
    "3654",
    "3697",
    "3727",
    "3751",
    "3794",
    "3832",
    "3867",
    "3883",
    "3891",
    "3913",
    "3921",
    "3964",
    "4006",
    "4030",
    "4073",
    "4111",
    "4154",
    "4197",
    "4235",
    "4278",
    "4316",
    "4340",
    "4383",
    "4405",
    "4421",
    "4456",
    "4472",
    "4499",
    "4502",
    "4545",
    "4588",
    "4600",
    "4618",
    "4626",
    "4669",
    "4677",
    "4707",
    "4715",
    "4723",
    "4758",
    "4774",
    "4790",
    "4821",
    "4839",
    "4863",
    "4880",
    "4936",
    "4960",
    "4979",
    "5010",
    "5053",
    "5070",
    "5088",
    "5096",
    "5118",
    "5126",
    "5134",
    "5177",
    "5215",
    "5258",
    "5282",
    "5312",
    "5355",
    "5380",
    "5428",
    "5436",
    "5444",
    "5452",
    "5487",
    "5495",
    "5509",
    "5525",
    "5541",
    "5568",
    "5576",
    "5584",
    "5607",
    "5615",
    "5631",
    "5665",
    "5690",
    "5738",
    "5754",
    "5762",
    "5800",
    "5860",
    "5894",
    "5932",
    "5991",
    "6033",
    "6076",
    "6114",
    "6130",
    "6157",
    "6173",
    "6238",
    "6289",
    "6300",
    "6327",
    "6408",
    "6416",
    "6432",
    "6467",
    "6505",
    "6548",
    "6564",
    "6572",
    "6599",
    "6602",
    "6637",
    "6645",
    "6653",
    "6700",
    "6750",
    "6769",
    "6793",
    "6807",
    "6815",
    "6858",
    "6904",
    "6912",
    "6920",
    "6939",
    "6955",
    "6971",
    "7005",
    "7030",
    "7056",
    "7102",
    "7153",
    "7196",
    "7234",
    "7277",
    "7315",
    "7358",
    "7382",
    "7404",
    "7420",
    "7447",
    "7480",
    "7501",
    "7544",
    "7560",
    "7595",
    "7641",
    "7676",
    "7706",
    "7722",
    "7730",
    "7757",
    "7765",
    "7803",
    "7838",
    "7854",
    "7870",
    "7889",
    "7919",
    "7927",
    "7935",
    "7951",
    "7994",
    "8001",
    "8052",
    "8079",
    "8109",
    "8150",
    "8168",
    "8176",
    "8184",
    "8214",
    "8249",
    "8273",
    "8281",
    "8311",
    "8338",
    "8354",
    "8362",
    "8370",
    "8397",
    "8419",
    "8427",
    "8451",
    "8478",
    "8494",
    "8508",
    "8516",
    "8524",
    "8559",
    "8567",
    "8583",
    "8605",
    "8630",
    "8664",
    "8672",
    "8699",
    "8702",
    "8737",
    "8753",
    "8796",
    "8834",
    "8850",
    "8877",
    "8885",
    "8907",
    "8958",
    "8966",
    "9000",
    "9016",
    "9032",
    "9075",
    "9113",
    "9130",
    "9172",
    "9199",
    "9215",
    "9237",
    "9245",
    "9260",
    "9288",
    "9296",
    "9334",
    "9393",
    "9407",
    "9430",
    "9455",
    "9461",
    "9480",
    "9504",
    "9512",
    "9520",
    "9539",
    "9547",
    "9555",
    "9571",
    "9598",
    "9601",
    "9628",
    "9636",
    "9644",
    "9660",
    "9695",
    "9733",
    "9741",
    "9750",
    "9768",
    "9792",
    "9800",
    "9827",
    "9843",
    "9851",
    "9878",
    "9886",
    "9894",
    "9932",
    "9959",
    "9967",
    "9975",
}

BRAZIL_COUNTRY_CODE = "1058"


def validate_country_code(cpais: str) -> bool:
    """Check if cPais is a known valid BACEN country code (4-digit string)."""
    if not cpais:
        return False
    # Normalise to 4-digit zero-padded string
    try:
        code_int = int(cpais)
        if code_int <= 0:
            return False
    except (ValueError, TypeError):
        return False
    padded = str(code_int).zfill(4)
    return padded in VALID_BACEN_COUNTRY_CODES
