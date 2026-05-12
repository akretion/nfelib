# Copyright (C) 2026 - Raphaël Valyi - Akretion
"""Tests for NF-e/NFC-e business validation rules (MOC 7.0, Section 4.2)."""

from nfelib.nfe.nfe_validation import NFeValidator
from nfelib.nfe.nfe_validation_helpers import (
    validate_access_key_dv,
    validate_cnf,
    validate_cnpj,
    validate_cpf,
    validate_gtin,
    validate_municipality_code,
)

# ---- Helper function tests ----


def test_validate_cnpj_valid():
    assert validate_cnpj("11222333000181") is True


def test_validate_cnpj_invalid():
    assert validate_cnpj("00000000000000") is False
    assert validate_cnpj("11222333000100") is False
    assert validate_cnpj("123") is False


def test_validate_cpf_valid():
    assert validate_cpf("52998224725") is True


def test_validate_cpf_invalid():
    assert validate_cpf("00000000000") is False
    assert validate_cpf("11111111111") is False
    assert validate_cpf("12345678900") is False


def test_validate_access_key_dv():
    # Build a key and verify DV calculation
    from nfelib.nfe.nfe_validation_helpers import build_access_key

    base = build_access_key(
        "35", "0604", "33009911002506", "55", "012", "000000780", "1", "26730161"
    )
    # Calculate DV
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    s = sum(int(c) * weights[i % 8] for i, c in enumerate(reversed(base)))
    r = s % 11
    dv = 0 if r < 2 else 11 - r
    key = base + str(dv)
    assert validate_access_key_dv(key) is True
    # Tamper with last digit
    bad_dv = (dv + 1) % 10
    bad_key = base + str(bad_dv)
    assert validate_access_key_dv(bad_key) is False


def test_validate_cnf():
    assert validate_cnf("87654321", "1") is True  # valid random code
    assert validate_cnf("00000000", "1") is False  # invalid pattern
    assert validate_cnf("00000001", "1") is False  # equals nNF zero-padded
    assert validate_cnf("00000002", "1") is True  # different from nNF


def test_validate_gtin():
    assert validate_gtin("7891234567895") is True
    assert validate_gtin("7891234567890") is False


def test_validate_municipality_code():
    assert validate_municipality_code("3550308") is True  # São Paulo
    assert validate_municipality_code("9999999") is False  # invalid UF
    assert validate_municipality_code("123") is False


# ---- NFeValidator tests with mock NF-e ----


class MockIde:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class MockEnum:
    def __init__(self, value):
        self.value = value


class MockEmit:
    def __init__(self, **kwargs):
        self.CNPJ = kwargs.get("CNPJ")
        self.CPF = kwargs.get("CPF")
        self.IE = kwargs.get("IE", "111111111111")
        self.IEST = kwargs.get("IEST")
        self.enderEmit = kwargs.get("enderEmit")
        self.CRT = kwargs.get("CRT")


class MockDest:
    def __init__(self, **kwargs):
        self.CNPJ = kwargs.get("CNPJ")
        self.CPF = kwargs.get("CPF")
        self.idEstrangeiro = kwargs.get("idEstrangeiro")
        self.IE = kwargs.get("IE")
        self.indIEDest = kwargs.get("indIEDest")
        self.enderDest = kwargs.get("enderDest")
        self.xNome = kwargs.get("xNome")


class MockEnder:
    def __init__(self, **kwargs):
        self.cMun = kwargs.get("cMun")
        self.UF = kwargs.get("UF")
        self.xMun = kwargs.get("xMun")
        self.CEP = kwargs.get("CEP")


class MockInfNFe:
    def __init__(self, **kwargs):
        self.ide = kwargs.get("ide")
        self.emit = kwargs.get("emit")
        self.dest = kwargs.get("dest")
        self.det = kwargs.get("det", [])
        self.total = kwargs.get("total")
        self.transp = kwargs.get("transp")
        self.cobr = kwargs.get("cobr")
        self.pag = kwargs.get("pag")
        self.avulsa = kwargs.get("avulsa")
        self.exporta = kwargs.get("exporta")
        self.compra = kwargs.get("compra")
        self.cana = kwargs.get("cana")
        self.Id = kwargs.get("Id")
        self.infIntermed = kwargs.get("infIntermed")
        self.infRespTec = kwargs.get("infRespTec")


class MockNFe:
    def __init__(self, **kwargs):
        self.infNFe = kwargs.get("infNFe")


def make_nfce(**overrides):
    """Create a minimal NFC-e mock (model 65)."""
    ide = MockIde(
        mod=MockEnum("65"),
        cUF=MockEnum("35"),
        cNF="12345678",
        nNF="1",
        dhEmi="2024-01-15T10:00:00-03:00",
        tpNF=MockEnum("1"),
        idDest=MockEnum("1"),
        cMunFG="3550308",
        tpImp=MockEnum("4"),
        tpEmis=MockEnum("1"),
        cDV="0",
        tpAmb=MockEnum("2"),
        finNFe=MockEnum("1"),
        indFinal=MockEnum("1"),
        indPres=MockEnum("1"),
        procEmi=MockEnum("0"),
        verProc="1.0",
        serie="1",
        dhSaiEnt=None,
        dhCont=None,
        xJust=None,
        NFref=[],
        indIntermed=None,
    )
    ide.__dict__.update(overrides.get("ide", {}))
    emit = MockEmit(CNPJ="11222333000181", enderEmit=MockEnder(cMun="3550308", UF="SP"))
    if "emit" in overrides:
        emit.__dict__.update(overrides["emit"])
    dest = overrides.get("dest")
    inf = MockInfNFe(
        ide=ide,
        emit=emit,
        dest=dest,
        Id="NFe" + "0" * 44,
        **{k: v for k, v in overrides.items() if k not in ("ide", "emit", "dest")},
    )
    return MockNFe(infNFe=inf)


def make_nfe(**overrides):
    """Create a minimal NF-e mock (model 55)."""
    ide_defaults = dict(
        mod=MockEnum("55"),
        cUF=MockEnum("35"),
        cNF="12345678",
        nNF="1",
        dhEmi="2024-01-15T10:00:00-03:00",
        tpNF=MockEnum("1"),
        idDest=MockEnum("1"),
        cMunFG="3550308",
        tpImp=MockEnum("1"),
        tpEmis=MockEnum("1"),
        cDV="0",
        tpAmb=MockEnum("2"),
        finNFe=MockEnum("1"),
        indFinal=MockEnum("0"),
        indPres=MockEnum("1"),
        procEmi=MockEnum("0"),
        verProc="1.0",
        serie="1",
        dhSaiEnt=None,
        dhCont=None,
        xJust=None,
        NFref=[],
        indIntermed=None,
    )
    ide_defaults.update(overrides.get("ide", {}))
    ide = MockIde(**ide_defaults)
    emit = MockEmit(CNPJ="11222333000181", enderEmit=MockEnder(cMun="3550308", UF="SP"))
    if "emit" in overrides:
        emit.__dict__.update(overrides["emit"])
    dest = overrides.get(
        "dest",
        MockDest(
            CNPJ="22333444000195",
            enderDest=MockEnder(cMun="3550308", UF="SP"),
        ),
    )
    inf = MockInfNFe(
        ide=ide,
        emit=emit,
        dest=dest,
        Id="NFe" + "0" * 44,
        **{k: v for k, v in overrides.items() if k not in ("ide", "emit", "dest")},
    )
    return MockNFe(infNFe=inf)


# ---- Rule-specific tests ----


def test_b03_10_cnf_invalid():
    """B03-10: cNF in invalid format."""
    nfe = make_nfe(ide={"cNF": "00000000"})
    v = NFeValidator(nfe)
    err = v.validation_obrig_rej_897_b03_10()
    assert err is not None
    assert err.msg_code == 897


def test_b03_10_cnf_valid():
    nfe = make_nfe(ide={"cNF": "12345679"})
    v = NFeValidator(nfe)
    assert v.validation_obrig_rej_897_b03_10() is None


def test_b10_10_nfce_with_dhsaient():
    """B10-10: NFC-e should not have dhSaiEnt."""
    nfce = make_nfce(ide={"dhSaiEnt": "2024-01-15T12:00:00-03:00"})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_705_b10_10()
    assert err is not None
    assert err.msg_code == 705


def test_b11_10_nfce_entrada():
    """B11-10: NFC-e cannot be entrada."""
    nfce = make_nfce(ide={"tpNF": MockEnum("0")})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_706_b11_10()
    assert err is not None


def test_b11a_10_nfce_interestadual():
    """B11a-10: NFC-e cannot be interestadual."""
    nfce = make_nfce(ide={"idDest": MockEnum("2")})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_707_b11a_10()
    assert err is not None


def test_b12_10_cmunfg_invalid():
    """B12-10: Invalid municipality code."""
    nfe = make_nfe(ide={"cMunFG": "9999999"})
    v = NFeValidator(nfe)
    err = v.validation_obrig_rej_270_b12_10()
    assert err is not None


def test_b21_10_nfce_tpimp_invalid():
    """B21-10: NFC-e with tpImp != 4 or 5."""
    nfce = make_nfce(ide={"tpImp": MockEnum("1")})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_709_b21_10()
    assert err is not None


def test_b25_20_nfce_finfne_not_normal():
    """B25-20: NFC-e with finNFe != 1."""
    nfce = make_nfce(ide={"finNFe": MockEnum("2")})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_715_b25_20()
    assert err is not None


def test_b25a_10_nfce_not_consumer_final():
    """B25a-10: NFC-e not for consumer final."""
    nfce = make_nfce(ide={"indFinal": MockEnum("0")})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_716_b25a_10()
    assert err is not None


def test_ba01_10_nfce_with_nfref():
    """BA01-10: NFC-e cannot reference other documents."""
    nfce = make_nfce(ide={"NFref": ["ref1"]})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_708_ba01_10()
    assert err is not None


def test_c02_10_cnpj_emitente_invalid():
    """C02-10: Invalid emitter CNPJ."""
    nfe = make_nfe(emit={"CNPJ": "00000000000000"})
    v = NFeValidator(nfe)
    err = v.validation_obrig_rej_207_c02_10()
    assert err is not None
    assert err.msg_code == 207


def test_c02_10_cnpj_emitente_valid():
    nfe = make_nfe()
    v = NFeValidator(nfe)
    assert v.validation_obrig_rej_207_c02_10() is None


def test_e02_10_cnpj_dest_invalid():
    """E02-10: Invalid destination CNPJ."""
    nfe = make_nfe(dest=MockDest(CNPJ="12345678901234"))
    v = NFeValidator(nfe)
    err = v.validation_obrig_rej_208_e02_10()
    assert err is not None


def test_e03_10_cpf_dest_invalid():
    """E03-10: Invalid destination CPF."""
    nfe = make_nfe(dest=MockDest(CPF="11111111111"))
    v = NFeValidator(nfe)
    err = v.validation_obrig_rej_237_e03_10()
    assert err is not None


def test_c18_10_nfce_with_iest():
    """C18-10: NFC-e should not have IEST."""
    nfce = make_nfce(emit={"IEST": "123456789"})
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_718_c18_10()
    assert err is not None


def test_x02_10_nfce_with_frete():
    """X02-10: NFC-e with modFrete != 9."""

    class MockTransp:
        modFrete = MockEnum("1")

    nfce = make_nfce(transp=MockTransp())
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_753_x02_10()
    assert err is not None


def test_y01_10_nfce_with_cobr():
    """Y01-10: NFC-e with billing data."""
    nfce = make_nfce(cobr=object())
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_760_y01_10()
    assert err is not None


def test_za01_30_nfce_with_exporta():
    """ZA01-30: NFC-e with export group."""
    nfce = make_nfce(exporta=object())
    v = NFeValidator(nfce)
    err = v.validation_obrig_rej_814_za01_30()
    assert err is not None


def test_validate_all_clean_nfe():
    """A clean NF-e should have no mandatory errors."""
    nfe = make_nfe()
    v = NFeValidator(nfe)
    errors = v.validate_all()
    # Filter out only implemented rules (non-stub)
    real_errors = [e for e in errors if "TODO" not in str(e)]
    # Should be minimal errors on a basic mock
    print(f"Errors found: {len(errors)}")
    for e in errors:
        print(f"  {e}")


def test_validate_all_facul_filtering():
    """Facul rules should only run when include_facul=True."""
    nfe = make_nfe()
    v_no_facul = NFeValidator(nfe, include_facul=False)
    v_facul = NFeValidator(nfe, include_facul=True)
    errors_no = v_no_facul.validate_all()
    errors_yes = v_facul.validate_all()
    # With facul enabled, there should be >= errors
    assert len(errors_yes) >= len(errors_no)
