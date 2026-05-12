# Copyright (C) 2026  Renato Lima - Akretion <renato.lima@akretion.com.br>

from __future__ import annotations

from typing import Union

from nfelib.nfe.nfe_validation_helpers import (
    BRAZIL_COUNTRY_CODE,
    CFOP_DEVOLUTION,
    NFCE_VALID_CFOPS,
    VALID_UF_CODES,
    ValidationError,
    is_cfop_entrada,
    is_cfop_exterior,
    is_cfop_interestadual,
    is_cfop_interna,
    is_cfop_saida,
    municipality_matches_uf,
    safe_decimal,
    validate_access_key_dv,
    validate_cnf,
    validate_cnpj,
    validate_country_code,
    validate_cpf,
    validate_gtin,
    validate_municipality_code,
    validate_suframa,
    validate_suframa_uf,
    values_match,
)

ValidationResult = Union[ValidationError, list[ValidationError], None]


def _v(val):
    """Get enum .value or str, handling None."""
    if val is None:
        return None
    return str(val.value) if hasattr(val, "value") else str(val)


def _mod(nfe) -> str:
    """Get model as string (55 or 65)."""
    try:
        return _v(nfe.infNFe.ide.mod) or ""
    except AttributeError:
        return ""


class NFeValidator:
    """Validates NF-e/NFC-e business rules per MOC 7.0 section 4.2.

    Usage:
        validator = NFeValidator(nfe_binding, include_facul=False)
        errors = validator.validate_all()
    """

    def __init__(self, nfe, include_facul: bool = False):
        self.nfe = nfe
        self.include_facul = include_facul
        self._inf = getattr(nfe, "infNFe", None)
        self._ide = getattr(self._inf, "ide", None) if self._inf else None
        self._emit = getattr(self._inf, "emit", None) if self._inf else None
        self._dest = getattr(self._inf, "dest", None) if self._inf else None
        self._total = getattr(self._inf, "total", None) if self._inf else None
        self._transp = getattr(self._inf, "transp", None) if self._inf else None
        self._cobr = getattr(self._inf, "cobr", None) if self._inf else None
        self._pag = getattr(self._inf, "pag", None) if self._inf else None
        self._det = getattr(self._inf, "det", None) or [] if self._inf else []

    def validate_all(self) -> list[ValidationError]:
        """Run all validation rules and return list of errors."""
        errors: list[ValidationError] = []
        for name in sorted(dir(self)):
            if not name.startswith("validation_"):
                continue
            if "_facul_" in name and not self.include_facul:
                continue
            method = getattr(self, name)
            if not callable(method):
                continue
            result = method()
            if result:
                if isinstance(result, list):
                    errors.extend(r for r in result if r)
                else:
                    errors.append(result)
        return errors

    def _err(self, rule_id, msg, effect, desc, field="", item=0):
        return ValidationError(rule_id, msg, effect, desc, field, item)

    def _is_nfce(self):
        return _mod(self.nfe) == "65"

    def _is_nfe(self):
        return _mod(self.nfe) == "55"

    # ============================================================
    # Group A
    # ============================================================

    def validation_obrig_rej_502_a03_10(self) -> ValidationResult:
        """A03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Campo Id inválido: - Chave de Acesso do campo Id difere da
        concatenação dos campos correspondentes. Observação: No caso da Nota Fiscal
        Avulsa da Série 890-899, considerar o CNPJ da SEFAZ para a UF correspondente.
        Nos demais casos, considerar o CNPJ/CPF do emitente. (NT 2018.001)
        Erro: 502: Rejeição: Erro na Chave de Acesso - Campo Id não corresponde à
        concatenação dos campos correspondentes
        """
        if not self._inf or not self._ide:
            return None
        key_id = getattr(self._inf, "Id", "") or ""
        key_id = key_id.replace("NFe", "")
        if len(key_id) != 44:
            return self._err(
                "A03-10", 502, "Rej.", "Rejeição: Campo Id inválido", "infNFe/Id"
            )
        ide = self._ide
        emit = self._emit
        cnpj_cpf = ""
        if emit:
            cnpj_cpf = getattr(emit, "CNPJ", None) or getattr(emit, "CPF", None) or ""
        dhEmi = _v(getattr(ide, "dhEmi", None)) or ""
        aamm = dhEmi[2:4] + dhEmi[5:7] if len(dhEmi) >= 7 else ""
        from nfelib.nfe.nfe_validation_helpers import build_access_key

        expected = build_access_key(
            _v(getattr(ide, "cUF", None)) or "",
            aamm,
            cnpj_cpf,
            _v(getattr(ide, "mod", None)) or "",
            _v(getattr(ide, "serie", None)) or "",
            _v(getattr(ide, "nNF", None)) or "",
            _v(getattr(ide, "tpEmis", None)) or "",
            _v(getattr(ide, "cNF", None)) or "",
        )
        if key_id[:43] != expected:
            return self._err(
                "A03-10", 502, "Rej.", "Rejeição: Campo Id inválido", "infNFe/Id"
            )
        return None

    # ============================================================
    # Group B
    # ============================================================

    def validation_obrig_rej_226_b02_10(self) -> ValidationResult:
        """B02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código da UF do Emitente difere da UF do Web Service
        Erro: 226: Rejeição: Código da UF do Emitente diverge da UF autorizadora
        """
        # TODO: implement validation logic for B02-10
        return None

    def validation_obrig_rej_476_b02_20(self) -> ValidationResult:
        """B02-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código da UF do Emitente difere da UF da primeira NF-e do
        Lote Observação: Esta validação tem sentido unicamente para a SEFAZ Virtual, que
        deve evitar um Lote, com NF-e de diferentes UF.
        Erro: 476: Rejeição: Código da UF diverge da UF da primeira NF-e do Lote
        """
        # TODO: implement validation logic for B02-20
        return None

    def validation_obrig_rej_897_b03_10(self) -> ValidationResult:
        """B03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Verificar formação do cNF: cNF não pode ser igual a
        00000000, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777,
        88888888, 99999999, 12345678, 23456789, 34567890, 45678901, 56789012, 67890123,
        78901234, 89012345, 90123456, 01234567. cNF não pode ser igual a nNF (id: B08).
        (NT 2019.001 v1.00, v1.50)
        Erro: 897: Rejeição: Código numérico em formato inválido.
        """
        if not self._ide:
            return None
        cnf = _v(getattr(self._ide, "cNF", None)) or ""
        nnf = _v(getattr(self._ide, "nNF", None)) or ""
        if not validate_cnf(cnf, nnf):
            return self._err(
                "B03-10",
                897,
                "Rej.",
                "Rejeição: Código numérico em formato inválido",
                "ide/cNF",
            )
        return None

    def validation_obrig_rej_702_b06_10(self) -> ValidationResult:
        """B06-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e não é aceita pela UF do Emitente
        Erro: 702: Rejeição: NFC-e não é aceita pela UF do Emitente
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B06-10
        return None

    def validation_obrig_rej_765_b06_20(self) -> ValidationResult:
        """B06-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Lote de documentos enviados só poderá conter NF-e ou NFC-e
        Erro: 765: Rejeição: Lote só poderá conter NF-e ou NFC-e
        """
        # TODO: implement validation logic for B06-20
        return None

    def validation_facul_rej_450_b06_30(self) -> ValidationResult:
        """B06-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se a SEFAZ optar por ambientes separados de autorização: -
        NFC-e enviada para ambiente de autorização da NF-e
        Erro: 450: Rejeição: Modelo da NF-e diferente de 55
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B06-30
        return None

    def validation_facul_rej_775_b06_40(self) -> ValidationResult:
        """B06-40.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: Se a SEFAZ optar por ambientes separados de autorização: -
        NF-e enviada para ambiente de autorização da NFC-e
        Erro: 775: Rejeição: Modelo da NFC-e diferente de 65
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B06-40
        return None

    def validation_obrig_rej_703_b09_10(self) -> ValidationResult:
        """B09-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Data-Hora de Emissão posterior ao horário de recepção na
        SEFAZ. Observação: Aceita uma tolerância de até 5 minutos, devido ao sincronismo
        de horário do servidor da Empresa e o servidor da SEFAZ.
        Erro: 703: Rejeição: Data-Hora de Emissão posterior ao horário de recebimento
        """
        # TODO: implement validation logic for B09-10
        return None

    def validation_obrig_rej_228_b09_20(self) -> ValidationResult:
        """B09-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com Tipo de Emissão = 1-Normal (ou 6-SVC-AN, 7-SVC-RS)
        (NT2012.003): - Data de Emissão ocorrida há mais de 30 dias (ou outro limite
        definido pela SEFAZ) Exceção 1: A critério da UF,a rejeição acima pode ser
        efetuada para qualquer Tipo de Emissão. Exceção 2: A critério da UF, pode ser
        aceita a NF-e com Data de Emissão muito atrasada, desde que tenha sido emitida
        em contingência (tpEmis=2, 4, 5). Neste caso, a SEFAZ Autorizadora irá retornar
        cStat=”150- Autorizado Uso da NF-e, autorização fora de prazo” (NT 2012.003).
        (NT 2015.002)
        Erro: 228: Rejeição: Data de Emissão muito atrasada
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B09-20
        return None

    def validation_obrig_rej_315_b09_30(self) -> ValidationResult:
        """B09-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Data de Emissão anterior ao início da autorização de NF-e na
        UF. Observação:O início da operação da NF-e ocorreu em diferentes momentos,
        conforme a UF (a primeira NF-e autorizada no País foi em 14/09/2006). (NT
        2015.002)
        Erro: 315: Rejeição: Data de Emissão anterior ao início da autorização de Nota
        Fiscal na UF
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B09-30
        return None

    def validation_obrig_rej_704_b09_40(self) -> ValidationResult:
        """B09-40.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Tipo de Emissão=1-Normal (ou 3-SCAN, ou 6-SVC-AN,
        7-SVC-RS) e Data-Hora de Emissão com atraso superior a 5 minutos em relação ao
        horário de recepção na SEFAZ. Exceção 1: A critério da UF, a rejeição acima pode
        ser efetuada para qualquer Tipo de Emissão. Exceção 2: A critério da UF, pode
        ser aceita a NFC-e com Data de Emissão muito atrasada, desde que tenham sido
        emitida em contingência (tpEmis=4, 9). A NFC-e transmitida para a SEFAZ
        Autorizadora após o prazo de 24 horas deveretornar cStat=”150- Autorizado Uso da
        NF-e, autorização fora de prazo”. Observação 1: A emissão da NFC-e deve ocorrer
        de forma on-line, real-time, com uma tolerância de até 5 minutos, devido ao
        sincronismo de horário do servidor da Empresa e o servidor da SEFAZ
        Autorizadora. (NT 2015.002)
        Erro: 704: Rejeição: NFC-e com Data-Hora de emissão atrasada
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B09-40
        return None

    def validation_obrig_rej_315_b09_50(self) -> ValidationResult:
        """B09-50.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Data de Emissão anterior ao início da autorização de NFC-e
        na UF. Observação:O início da operação da NFC-e ocorreu em diferentes momentos,
        conforme a UF (a primeira NFC-e autorizada no País foi em 01/03/2013). (NT
        2015.002)
        Erro: 315: Rejeição: Data de Emissão anterior ao início da autorização de Nota
        Fiscal na UF
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B09-50
        return None

    def validation_obrig_rej_705_b10_10(self) -> ValidationResult:
        """B10-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com data de entrada/saída.
        Erro: 705: Rejeição: NFC-e com data de entrada/saída
        """
        if not self._is_nfce():
            return None
        if self._ide and getattr(self._ide, "dhSaiEnt", None):
            return self._err(
                "B10-10",
                705,
                "Rej.",
                "Rejeição: NFC-e com data de entrada/saída",
                "ide/dhSaiEnt",
            )
        return None

    def validation_facul_rej_504_b10_20(self) -> ValidationResult:
        """B10-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado Data de Entrada / Saída (dhSaiEnt): - Data
        Entrada / Saída posterior a 30 dias da Data de Autorização
        Erro: 504: Rejeição: Data de Entrada/Saída posterior ao permitido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B10-20
        return None

    def validation_facul_rej_505_b10_30(self) -> ValidationResult:
        """B10-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado Data de Entrada / Saída (dhSaiEnt): - Data
        Entrada / Saída anterior a 30 dias da Data de Autorização Observação: Para as
        SEFAZ que aceitam NF-e emitida em contingência a mais de 30 dias, esta rejeição
        deverá considerar tpEmi=1, 3, 6, 7
        Erro: 505: Rejeição: Data de Entrada/Saída anterior ao permitido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B10-30
        return None

    def validation_facul_rej_506_b10_40(self) -> ValidationResult:
        """B10-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado Data de Entrada / Saída (tag:dhSaiEnt) para
        NF-e de Saída (tag:tpNF=1): - Data de Saída (dSaiEnt) menor que a Data de
        Emissão (dhEmi)
        Erro: 506: Rejeição: Data de Saída menor que a Data de Emissão
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B10-40
        return None

    def validation_obrig_rej_706_b11_10(self) -> ValidationResult:
        """B11-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e para operação de entrada (tag:tpNF=0)
        Erro: 706: Rejeição: NFC-e para operação de entrada
        """
        if not self._is_nfce():
            return None
        if self._ide and _v(getattr(self._ide, "tpNF", None)) == "0":
            return self._err(
                "B11-10",
                706,
                "Rej.",
                "Rejeição: NFC-e para operação de entrada",
                "ide/tpNF",
            )
        return None

    def validation_obrig_rej_707_b11a_10(self) -> ValidationResult:
        """B11a-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e para operação interestadual ou com o exterior
        (tag:idDest<>1)
        Erro: 707: Rejeição: NFC-e para operação interestadual ou com o exterior
        """
        if not self._is_nfce():
            return None
        if self._ide and _v(getattr(self._ide, "idDest", None)) != "1":
            return self._err(
                "B11a-10",
                707,
                "Rej.",
                "Rejeição: NFC-e para operação interestadual ou com o exterior",
                "ide/idDest",
            )
        return None

    def validation_obrig_rej_270_b12_10(self) -> ValidationResult:
        """B12-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código do Município do Fato Gerador de ICMS inexistente
        (Tabela Municípios IBGE) (NT 2015.002)
        Erro: 270: Rejeição: Código Município do Fato Gerador de ICMS inexistente
        """
        if not self._ide:
            return None
        cmun = _v(getattr(self._ide, "cMunFG", None)) or ""
        if cmun and not validate_municipality_code(cmun):
            return self._err(
                "B12-10",
                270,
                "Rej.",
                "Rejeição: Código Município do Fato Gerador inexistente",
                "ide/cMunFG",
            )
        return None

    def validation_obrig_rej_271_b12_20(self) -> ValidationResult:
        """B12-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código do Município do Fato Gerador (2 primeiras posições)
        difere do Código da UF do emitente
        Erro: 271: Rejeição: Código Município do Fato Gerador: difere da UF do emitente
        """
        if not self._ide or not self._emit:
            return None
        cmun = _v(getattr(self._ide, "cMunFG", None)) or ""
        cuf = _v(getattr(self._ide, "cUF", None)) or ""
        if cmun and cuf and cmun[:2] != cuf:
            return self._err(
                "B12-20",
                271,
                "Rej.",
                "Rejeição: Código do Município do FG difere da UF do emitente",
                "ide/cMunFG",
            )
        return None

    def validation_obrig_rej_709_b21_10(self) -> ValidationResult:
        """B21-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com tipo de impressão diferente de 4 e 5 (tag:tpImp<>
        4 e 5)
        Erro: 709: Rejeição: NFC-e com formato de DANFE inválido
        """
        if not self._is_nfce():
            return None
        tpImp = _v(getattr(self._ide, "tpImp", None))
        if tpImp and tpImp not in ("4", "5"):
            return self._err(
                "B21-10",
                709,
                "Rej.",
                "Rejeição: NFC-e com tipo de impressão inválido",
                "ide/tpImp",
            )
        return None

    def validation_obrig_rej_710_b21_20(self) -> ValidationResult:
        """B21-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com tipo de impressão 4 ou 5 (tag:tpImp= 4 ou 5)
        Erro: 710: Rejeição: NF-e com formato de DANFE inválido
        """
        if not self._is_nfe():
            return None
        tpImp = _v(getattr(self._ide, "tpImp", None))
        if tpImp and tpImp in ("4", "5"):
            return self._err(
                "B21-20",
                710,
                "Rej.",
                "Rejeição: NF-e com tipo de impressão de NFC-e",
                "ide/tpImp",
            )
        return None

    def validation_obrig_rej_711_b22_10(self) -> ValidationResult:
        """B22-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com contingência off-line (tag:tpEmis=9)
        Erro: 711: Rejeição: NF-e com contingência off-line
        """
        if not self._is_nfe():
            return None
        if self._ide and _v(getattr(self._ide, "tpEmis", None)) == "9":
            return self._err(
                "B22-10",
                711,
                "Rej.",
                "Rejeição: NF-e com contingência off-line",
                "ide/tpEmis",
            )
        return None

    def validation_facul_rej_712_b22_20(self) -> ValidationResult:
        """B22-20.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: NFC-e com contingência off-line para a UF (tag:tpEmis=9 e UF
        não aceita este tipo de contingência)
        Erro: 712: Rejeição: NFC-e com contingência off-line para a UF
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B22-20
        return None

    def validation_obrig_rej_570_b22_30(self) -> ValidationResult:
        """B22-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Na autorização pela SEFAZ: - não aceitar o conteúdo
        tpEmis=3-SCAN (NT 2010/004), 6-SVC-AN ou 7- SVC-RS
        Erro: 570: Rejeição: Tipo de Emissão 3, 6 ou 7 só é válido nas contingências
        SCAN/SVC
        """
        # TODO: implement validation logic for B22-30
        return None

    def validation_facul_rej_714_b22_34(self) -> ValidationResult:
        """B22-34.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: Na autorização pela SEFAZ: - rejeitar a NFC-e com opção de
        contingência inválida (tag:tpEmis=2, 4, 5) Observação: A contingência EPEC
        (tag:tpEmis=4) poderá ser aceita, a critério da UF. (NT 2015.002)
        Erro: 714: Rejeição: NFC-e com contingência inválida (tpEmis=2, 4 (a critério da
        UF) ou 5)
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B22-34
        return None

    def validation_obrig_rej_713_b22_60(self) -> ValidationResult:
        """B22-60.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Na autorização pela SVC: - não aceitar o conteúdo da tag
        tpEmis diferente de 6 para a SVC-AN ou 7 para a SVC-RS
        Erro: 713: Rejeição: Tipo de Emissão diferente de 6 ou 7 para contingência da
        SVC acessada
        """
        # TODO: implement validation logic for B22-60
        return None

    def validation_obrig_rej_783_b22_70(self) -> ValidationResult:
        """B22-70.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Na autorização pela SVC: - não aceitar autorização de NFC-e
        Erro: 783: Rejeição: NFC-e não é autorizada pela SVC
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B22-70
        return None

    def validation_obrig_rej_253_b23_10(self) -> ValidationResult:
        """B23-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Chave de Acesso obtida pela concatenação dos campos
        correspondentes com dígito verificador (DV) inválido
        Erro: 253: Rejeição: Digito Verificador da chave de acesso composta inválida
        """
        if not self._inf:
            return None
        key_id = getattr(self._inf, "Id", "") or ""
        key_id = key_id.replace("NFe", "")
        if len(key_id) == 44 and not validate_access_key_dv(key_id):
            return self._err(
                "B23-10",
                253,
                "Rej.",
                "Rejeição: DV da Chave de Acesso inválido",
                "infNFe/Id",
            )
        return None

    def validation_obrig_rej_252_b24_10(self) -> ValidationResult:
        """B24-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Tipo do ambiente da NF-e difere do ambiente do Web Service
        Erro: 252: Rejeição: Ambiente informado diverge do Ambiente de recebimento
        """
        # TODO: implement validation logic for B24-10
        return None

    def validation_obrig_rej_715_b25_20(self) -> ValidationResult:
        """B25-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com finalidade diferente de normal (tag:finNFe <> 1)
        Erro: 715: Rejeição: NFC-e com finalidade inválida
        """
        if not self._is_nfce():
            return None
        fin = _v(getattr(self._ide, "finNFe", None))
        if fin and fin != "1":
            return self._err(
                "B25-20",
                715,
                "Rej.",
                "Rejeição: NFC-e com finalidade diferente de normal",
                "ide/finNFe",
            )
        return None

    def validation_obrig_rej_254_b25_30(self) -> ValidationResult:
        """B25-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se NF-e complementar (tag:finNFe=2): - Não informado NF
        referenciada (NF-e, NFC-e, NF modelo 1)
        Erro: 254: Rejeição: NF-e complementar não possui NF referenciada
        """
        if not self._is_nfe() or not self._ide:
            return None
        if _v(getattr(self._ide, "finNFe", None)) != "2":
            return None
        nfref_list = getattr(self._ide, "NFref", None) or []
        if not nfref_list:
            return self._err(
                "B25-30",
                254,
                "Rej.",
                "Rejeição: NF-e complementar sem NF referenciada",
                "ide/NFref",
            )
        has_valid_ref = False
        for ref in nfref_list:
            if (
                getattr(ref, "refNFe", None) is not None
                or getattr(ref, "refNF", None) is not None
            ):
                has_valid_ref = True
                break
        if not has_valid_ref:
            return self._err(
                "B25-30",
                254,
                "Rej.",
                "Rejeição: NF-e complementar sem NF referenciada",
                "ide/NFref",
            )
        return None

    def validation_obrig_rej_255_b25_40(self) -> ValidationResult:
        """B25-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se NF-e complementar (tag:finNFe=2): - NF referenciada com
        mais de uma ocorrência (NF-e, NFC-e, NF modelo 1)
        Erro: 255: Rejeição: NF-e complementar possui mais de uma NF referenciada
        """
        if not self._is_nfe() or not self._ide:
            return None
        if _v(getattr(self._ide, "finNFe", None)) != "2":
            return None
        nfref_list = getattr(self._ide, "NFref", None) or []
        count = 0
        for ref in nfref_list:
            if (
                getattr(ref, "refNFe", None) is not None
                or getattr(ref, "refNF", None) is not None
            ):
                count += 1
        if count > 1:
            return self._err(
                "B25-40",
                255,
                "Rej.",
                "Rejeição: NF-e complementar com mais de uma NF referenciada",
                "ide/NFref",
            )
        return None

    def validation_obrig_rej_269_b25_50(self) -> ValidationResult:
        """B25-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se NF-e complementar (tag:finNFe=2): - CNPJ/CPF emitente da
        NF Referenciada difere do CNPJ/CPF emitente desta NF-e (NF-e, NFC-e, NF modelo
        1) (NT 2018.001)
        Erro: 269: Rejeição: CNPJ/CPF Emitente da NF Complementar difere do CNPJ/CPF da
        NF Referenciada
        """
        if not self._is_nfe() or not self._ide or not self._emit:
            return None
        if _v(getattr(self._ide, "finNFe", None)) != "2":
            return None
        emit_cnpj = getattr(self._emit, "CNPJ", None) or ""
        emit_cpf = getattr(self._emit, "CPF", None) or ""
        nfref_list = getattr(self._ide, "NFref", None) or []
        for ref in nfref_list:
            ref_nfe_key = _v(getattr(ref, "refNFe", None)) or ""
            if len(ref_nfe_key) == 44:
                # CNPJ/CPF is positions 6-19 (14 digits)
                ref_cnpj_cpf = ref_nfe_key[6:20]
                if emit_cnpj and ref_cnpj_cpf != emit_cnpj:
                    return self._err(
                        "B25-50",
                        269,
                        "Rej.",
                        "Rejeição: NF-e complementar com emitente diferente na NF referenciada",
                        "ide/NFref/refNFe",
                    )
                if emit_cpf and ref_cnpj_cpf.lstrip("0") != emit_cpf.lstrip("0"):
                    return self._err(
                        "B25-50",
                        269,
                        "Rej.",
                        "Rejeição: NF-e complementar com emitente diferente na NF referenciada",
                        "ide/NFref/refNFe",
                    )
        return None

    def validation_facul_rej_678_b25_60(self) -> ValidationResult:
        """B25-60.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se NF-e complementar (tag:finNFe=2): - UF da NF-e
        referenciada diferente da UF do emitente (NF-e, NFC-e, NF modelo 1) (NT
        2013/003)
        Erro: 678: Rejeição: NF referenciada com UF diferente da NF-e complementar
        """
        if not self._is_nfe() or not self._ide or not self._emit:
            return None
        if _v(getattr(self._ide, "finNFe", None)) != "2":
            return None
        emit_uf = _v(getattr(self._ide, "cUF", None)) or ""
        nfref_list = getattr(self._ide, "NFref", None) or []
        errors = []
        for ref in nfref_list:
            ref_nfe_key = _v(getattr(ref, "refNFe", None)) or ""
            if len(ref_nfe_key) == 44:
                # cUF is first 2 digits of the access key
                ref_cuf = ref_nfe_key[:2]
                if emit_uf and ref_cuf and ref_cuf != emit_uf:
                    errors.append(
                        self._err(
                            "B25-60",
                            678,
                            "Rej.",
                            "Rejeição: NF-e complementar com UF diferente na NF referenciada",
                            "ide/NFref/refNFe",
                        )
                    )
        return errors or None

    def validation_obrig_rej_321_b25_70(self) -> ValidationResult:
        """B25-70.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se NF-e de devolução de mercadoria (tag:finNFe=4): - Não
        informado documento fiscal referenciado (NF-e, NFC-e, NF modelo 1, NF Produtor,
        ECF) Observação: não aplicar esta regra para os CFOP 1.201, 1.202, 1.410, 1.411,
        5,921 e 6,921 (NT 2013/005 v 1.20)
        Erro: 321: Rejeição: NF-e de devolução de mercadoria não possui documento fiscal
        referenciado
        """
        if not self._is_nfe() or not self._ide:
            return None
        if _v(getattr(self._ide, "finNFe", None)) != "4":
            return None
        nfref_list = getattr(self._ide, "NFref", None) or []
        if not nfref_list:
            return self._err(
                "B25-70",
                321,
                "Rej.",
                "Rejeição: NF-e de devolução sem documento fiscal referenciado",
                "ide/NFref",
            )
        return None

    def validation_obrig_rej_716_b25a_10(self) -> ValidationResult:
        """B25a-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e para operação não destinada a Consumidor Final
        (tag:indFinal=0)
        Erro: 716: Rejeição: NFC-e em operação não destinada a consumidor final
        """
        if not self._is_nfce():
            return None
        if self._ide and _v(getattr(self._ide, "indFinal", None)) == "0":
            return self._err(
                "B25a-10",
                716,
                "Rej.",
                "Rejeição: NFC-e para operação não destinada a Consumidor Final",
                "ide/indFinal",
            )
        return None

    def validation_obrig_rej_794_b25b_10(self) -> ValidationResult:
        """B25b-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com indicativo de NFC-e com entrega a domicílio
        (tag:indPres=4)
        Erro: 794: Rejeição: NF-e com indicativo de NFC-e com entrega a domicílio
        """
        if not self._is_nfe():
            return None
        if self._ide and _v(getattr(self._ide, "indPres", None)) == "4":
            return self._err(
                "B25b-10",
                794,
                "Rej.",
                "Rejeição: NF-e com indicativo de NFC-e entrega a domicílio",
                "ide/indPres",
            )
        return None

    def validation_obrig_rej_717_b25b_20(self) -> ValidationResult:
        """B25b-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e em uma operação não presencial (tag:indPres<>1 e 4)
        Erro: 717: Rejeição: NFC-e em operação não presencial
        """
        if not self._is_nfce():
            return None
        ip = _v(getattr(self._ide, "indPres", None))
        if ip and ip not in ("1", "4"):
            return self._err(
                "B25b-20",
                717,
                "Rej.",
                "Rejeição: NFC-e em operação não presencial",
                "ide/indPres",
            )
        return None

    def validation_obrig_rej_785_b25b_30(self) -> ValidationResult:
        """B25b-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com operação de entrega a domicílio, não permitida
        para a UF (parametrizável).
        Erro: 785: Rejeição: NFC-e com entrega a domicílio não permitida pela UF
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for B25b-30
        return None

    def validation_obrig_rej_864_b25b_40(self) -> ValidationResult:
        """B25b-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com indicativo de Operação presencial, fora do
        estabelecimento (tag:indPres=5) e não informada campos refNFe (id:BA02) ou refNF
        (id:BA03) (NT 2016.002)
        Erro: 864: Rejeição: NF-e com indicativo de Operação presencial, fora do
        estabelecimento e não informada NF referenciada
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for B25b-40
        return None

    def validation_obrig_rej_434_b25c_10(self) -> ValidationResult:
        """B25c-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Informado indicativo de presença, tag: indPres, IGUAL a
        2, 3, 4 ou 9 - Obrigatório o preenchimento do campo Indicativo do Intermediador
        (tag: indIntermed) Observação: Regra de validação valida a partir de 01/02/2021
        para homologação e 01/09/2021 para produção
        Erro: 434: Rejeição: NF-e sem indicativo do intermediador (Incluída na NT
        2020.006)
        """
        if not self._ide:
            return None
        indPres = _v(getattr(self._ide, "indPres", None))
        if indPres in ("2", "3", "4", "9"):
            indIntermed = _v(getattr(self._ide, "indIntermed", None))
            if not indIntermed:
                return self._err(
                    "B25c-10",
                    434,
                    "Rej.",
                    "Rejeição: NF-e sem indicativo do intermediador",
                    "ide/indIntermed",
                )
        return None

    def validation_obrig_rej_435_b25c_20(self) -> ValidationResult:
        """B25c-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Informado indicativo de presença, tag: indPres, DIFERENTE
        de 2, 3, 4 ou 9 - Proibido o preenchimento do campo Indicativo do Intermediador
        (tag: indIntermed)
        Erro: 435: Rejeição: NF-e não pode ter o indicativo do intermediador (Incluída
        na NT 2020.006)
        """
        if not self._ide:
            return None
        indPres = _v(getattr(self._ide, "indPres", None))
        if indPres not in ("2", "3", "4", "9"):
            indIntermed = _v(getattr(self._ide, "indIntermed", None))
            if indIntermed:
                return self._err(
                    "B25c-20",
                    435,
                    "Rej.",
                    "Rejeição: NF-e não pode ter o indicativo do intermediador",
                    "ide/indIntermed",
                )
        return None

    def validation_obrig_rej_244_b26_10(self) -> ValidationResult:
        """B26-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Processo de Emissão pelo Contribuinte (procEmi<>1 e 2): -
        Série da NF-e difere da faixa de 0-889 ou 920-969 (NT 2018.001)
        Erro: 244: Rejeição: Processo de Emissão pelo Contribuinte incompatível com a
        Série da NF
        """
        if not self._ide:
            return None
        procEmi = _v(getattr(self._ide, "procEmi", None))
        if procEmi in ("1", "2"):
            return None
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (0 <= serie <= 889 or 920 <= serie <= 969):
            return self._err(
                "B26-10",
                244,
                "Rej.",
                "Rejeição: Processo de Emissão pelo Contribuinte incompatível com a Série da NF",
                "ide/serie",
            )
        return None

    def validation_obrig_rej_451_b26_20(self) -> ValidationResult:
        """B26-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Processo de Emissão pelo Fisco (procEmi=1 ou 2): - Série
        difere da faixa 890-919 (NF Avulsa) (NT 2018.001)
        Erro: 451: Rejeição: Processo de Emissão pelo Fisco incompatível com a Série da
        NF
        """
        if not self._ide:
            return None
        procEmi = _v(getattr(self._ide, "procEmi", None))
        if procEmi not in ("1", "2"):
            return None
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (890 <= serie <= 919):
            return self._err(
                "B26-20",
                451,
                "Rej.",
                "Rejeição: Processo de Emissão pelo Fisco incompatível com a Série da NF",
                "ide/serie",
            )
        return None

    def validation_obrig_rej_370_b26_30(self) -> ValidationResult:
        """B26-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Processo de Emissão pelo Fisco (procEmi=1 ou 2): - Tipo
        de Emissão difere de 1-Emissão Normal ou Emissão na SVC (tpEmis<>1, 6 e 7) (NT
        2018.001/ NT 2015.002)
        Erro: 370: Rejeição: Processo de emissão pelo Fisco com Tipo de Emissão inválido
        """
        if not self._ide:
            return None
        procEmi = _v(getattr(self._ide, "procEmi", None))
        if procEmi not in ("1", "2"):
            return None
        tpEmis = _v(getattr(self._ide, "tpEmis", None))
        if tpEmis and tpEmis not in ("1", "6", "7"):
            return self._err(
                "B26-30",
                370,
                "Rej.",
                "Rejeição: Processo de emissão pelo Fisco com Tipo de Emissão inválido",
                "ide/tpEmis",
            )
        return None

    def validation_obrig_rej_571_b26_40(self) -> ValidationResult:
        """B26-40.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se Processo de Emissão pelo Fisco (procEmi=1 ou 2): -
        Certificado de Transmissão sem o CNPJ da SEFAZ para a UF (NT 2018.001)
        Erro: 571: Rejeição: Processo de emissão pelo Fisco com Certificado de
        Transmissão incompatível
        """
        # TODO: implement validation logic for B26-40
        return None

    def validation_obrig_rej_556_b28_10(self) -> ValidationResult:
        """B28-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se emissão normal (tpEmis = 1-Normal): - dhCont e xJust não
        devem ser informados
        Erro: 556: Rejeição: Justificativa de entrada em contingência não deve ser
        informada para tipo de emissão normal
        """
        if not self._ide:
            return None
        tpEmis = _v(getattr(self._ide, "tpEmis", None))
        if tpEmis == "1" and (
            getattr(self._ide, "dhCont", None) or getattr(self._ide, "xJust", None)
        ):
            return self._err(
                "B28-10",
                556,
                "Rej.",
                "Rejeição: Emissão normal com dhCont/xJust",
                "ide/dhCont",
            )
        return None

    def validation_obrig_rej_557_b28_20(self) -> ValidationResult:
        """B28-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se emissão em contingência utilizando DPEC, formulário de
        segurança ou contingência off-line (tpEmis = 2, 4, 5 ou 9): - dhCont e xJust
        devem ser informados
        Erro: 557: Rejeição: A Justificativa de entrada em contingência deve ser
        informada
        """
        if not self._ide:
            return None
        tpEmis = _v(getattr(self._ide, "tpEmis", None))
        if tpEmis in ("2", "4", "5", "9") and (
            not getattr(self._ide, "dhCont", None)
            or not getattr(self._ide, "xJust", None)
        ):
            return self._err(
                "B28-20",
                557,
                "Rej.",
                "Rejeição: Contingência sem dhCont/xJust",
                "ide/dhCont",
            )
        return None

    def validation_facul_rej_558_b28_30(self) -> ValidationResult:
        """B28-30.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Data de entrada em contingência não deve ser maior que a
        data de recepção da NF-e (NT 2010/004). Observação 1: Não considerar a Hora no
        caso da NF-e com versão inferior a versão 3.0. Observação 2: Aceita uma
        tolerância de até 5 minutos, devido ao sincronismo de horário do servidor da
        Empresa e o servidor da SEFAZ.
        Erro: 558: Rejeição: Data de entrada em contingência posterior a data de
        recebimento
        """
        # TODO: implement validation logic for B28-30
        return None

    def validation_facul_rej_569_b28_40(self) -> ValidationResult:
        """B28-40.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Data de entrada em contingência deve ser menor ou igual à
        data de emissão - 30 dias (NT 2010/004) Observação: Não considerar a Hora no
        caso da NF-e com versão inferior a versão 3.0
        Erro: 569: Rejeição: Data de entrada em contingência muito atrasada
        """
        # TODO: implement validation logic for B28-40
        return None

    # ============================================================
    # Group BA
    # ============================================================

    def validation_obrig_rej_708_ba01_10(self) -> ValidationResult:
        """BA01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e não pode referenciar outros documentos (tag:NFref)
        Erro: 708: Rejeição: NFC-e não pode referenciar documento fiscal
        """
        if not self._is_nfce():
            return None
        nfref = getattr(self._ide, "NFref", None) or []
        if nfref:
            return self._err(
                "BA01-10",
                708,
                "Rej.",
                "Rejeição: NFC-e não pode referenciar documentos fiscais",
                "ide/NFref",
            )
        return None

    def _get_nfref_list(self):
        """Return list of NFref items from ide."""
        if not self._ide:
            return []
        return getattr(self._ide, "NFref", None) or []

    def validation_facul_rej_547_ba02_10(self) -> ValidationResult:
        """BA02-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Dígito
        Verificador da Chave de Acesso inválido (NT 2015.002)
        Erro: 547: Rejeição: Chave de Acesso referenciada com Dígito Verificador
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44 and not validate_access_key_dv(key):
                errors.append(
                    self._err(
                        "BA02-10",
                        547,
                        "Rej.",
                        "Rejeição: Dígito Verificador da NF-e referenciada inválido",
                        "ide/NFref/refNFe",
                    )
                )
        return errors or None

    def validation_facul_rej_522_ba02_14(self) -> ValidationResult:
        """BA02-14.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Chave de
        Acesso referenciada com UF inválida (NT 2015.002)
        Erro: 522: Rejeição: Chave de Acesso referenciada com UF inválida[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44 and key[:2] not in VALID_UF_CODES:
                errors.append(
                    self._err(
                        "BA02-14",
                        522,
                        "Rej.",
                        "Rejeição: UF inválida na Chave de Acesso da NF-e referenciada",
                        "ide/NFref/refNFe",
                    )
                )
        return errors or None

    def validation_facul_rej_524_ba02_20(self) -> ValidationResult:
        """BA02-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Chave de
        Acesso referenciada com Ano Emissão < 06 ou > que o Ano corrente (NT 2015.002)
        Erro: 524: Rejeição: Chave de Acesso referenciada com Ano-Mês
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44:
                try:
                    ano = int(key[2:4])
                    if ano < 6:
                        errors.append(
                            self._err(
                                "BA02-20",
                                524,
                                "Rej.",
                                "Rejeição: Ano de emissão inválido na NF-e referenciada",
                                "ide/NFref/refNFe",
                            )
                        )
                except (ValueError, TypeError):
                    pass
        return errors or None

    def validation_facul_rej_524_ba02_24(self) -> ValidationResult:
        """BA02-24.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Chave de
        Acesso referenciada com Mês Emissão < 01 ou > 12 NT 2015.002)
        Erro: 524: Rejeição: Chave de Acesso referenciada com Ano-Mês
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44:
                try:
                    mes = int(key[4:6])
                    if not (1 <= mes <= 12):
                        errors.append(
                            self._err(
                                "BA02-24",
                                524,
                                "Rej.",
                                "Rejeição: Mês de emissão inválido na NF-e referenciada",
                                "ide/NFref/refNFe",
                            )
                        )
                except (ValueError, TypeError):
                    pass
        return errors or None

    def validation_facul_rej_552_ba02_30(self) -> ValidationResult:
        """BA02-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Série =
        [0-909] e CNPJ zerado ou dígito inválido, ou - Série = [910-969] e CPF zerado ou
        dígito inválido (NT 2018.001)
        Erro: 552: Rejeição: Chave de Acesso referenciada com CNPJ/CPF
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44:
                try:
                    serie = int(key[22:25])
                    cnpj = key[6:20]
                    if serie <= 909 and not validate_cnpj(cnpj):
                        errors.append(
                            self._err(
                                "BA02-30",
                                552,
                                "Rej.",
                                "Rejeição: CNPJ inválido na Chave de Acesso da NF-e referenciada",
                                "ide/NFref/refNFe",
                            )
                        )
                except (ValueError, TypeError):
                    pass
        return errors or None

    def validation_facul_rej_679_ba02_34(self) -> ValidationResult:
        """BA02-34.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Modelo da
        NF-e referenciada diferente de 55/65/59 (NT 2013/003) (NT 2015.002)
        Erro: 679: Rejeição: Chave de Acesso referenciada com Modelo inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44:
                mod = key[20:22]
                if mod not in ("55", "65", "59"):
                    errors.append(
                        self._err(
                            "BA02-34",
                            679,
                            "Rej.",
                            "Rejeição: Modelo inválido na Chave de Acesso da NF-e referenciada",
                            "ide/NFref/refNFe",
                        )
                    )
        return errors or None

    def validation_facul_rej_683_ba02_40(self) -> ValidationResult:
        """BA02-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Chave de
        Acesso referenciada com Número zerado (NT 2015.002)
        Erro: 683: Rejeição: Chave de Acesso referenciada com Número inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if len(key) == 44 and key[25:34] == "000000000":
                errors.append(
                    self._err(
                        "BA02-40",
                        683,
                        "Rej.",
                        "Rejeição: Número zerado na Chave de Acesso da NF-e referenciada",
                        "ide/NFref/refNFe",
                    )
                )
        return errors or None

    def validation_facul_rej_680_ba02_44(self) -> ValidationResult:
        """BA02-44.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Verificar
        duplicidade da NF-e referenciada (duplicidade da tag refNFe) (NT 2013/003) (NT
        2015.002)
        Erro: 680: Rejeição: Chave de Acesso referenciada em duplicidade na NF-e
        [nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        seen = set()
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if key:
                if key in seen:
                    return self._err(
                        "BA02-44",
                        680,
                        "Rej.",
                        "Rejeição: NF-e referenciada em duplicidade",
                        "ide/NFref/refNFe",
                    )
                seen.add(key)
        return None

    def validation_obrig_rej_316_ba02_50(self) -> ValidationResult:
        """BA02-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada uma NF-e referenciada (tag:refNFe): - Nota
        Fiscal referenciada com a mesma Chave de Acesso da Nota Fiscal atual (NT
        2015.002)
        Erro: 316: Rejeição: Chave de Acesso referenciada com a mesma Chave de Acesso da
        Nota Fiscal atual [nOcor:nnn]
        """
        if not self._is_nfe() or not self._inf:
            return None
        own_key = (_v(getattr(self._inf, "Id", None)) or "").replace("NFe", "")
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refNFe", None)) or ""
            if key and own_key and key == own_key:
                return self._err(
                    "BA02-50",
                    316,
                    "Rej.",
                    "Rejeição: NF-e referencia a si mesma",
                    "ide/NFref/refNFe",
                )
        return None

    def validation_facul_rej_681_ba03_10(self) -> ValidationResult:
        """BA03-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF Modelo 1 ou NF Modelo 2 referenciada
        (tag:refNF): - Verificar duplicidade de Nota Fiscal Modelo 1 ou 2 referenciada
        (mesmo CNPJ, Modelo, Série, Número) (NT 2016.002)
        Erro: 681: Rejeição: Duplicidade de NF Modelo 1 referenciada (CNPJ, Modelo,
        Série e Número) [nOcor: nnn]
        """
        if not self._is_nfe():
            return None
        seen = set()
        for ref in self._get_nfref_list():
            ref_nf = getattr(ref, "refNF", None)
            if ref_nf is None:
                continue
            key = (
                _v(getattr(ref_nf, "cUF", None)) or "",
                _v(getattr(ref_nf, "AAMM", None)) or "",
                _v(getattr(ref_nf, "CNPJ", None)) or "",
                _v(getattr(ref_nf, "mod", None)) or "",
                _v(getattr(ref_nf, "serie", None)) or "",
                _v(getattr(ref_nf, "nNF", None)) or "",
            )
            if key in seen:
                return self._err(
                    "BA03-10",
                    681,
                    "Rej.",
                    "Rejeição: NF Modelo 1/2 referenciada em duplicidade",
                    "ide/NFref/refNF",
                )
            seen.add(key)
        return None

    def validation_facul_rej_317_ba05_10(self) -> ValidationResult:
        """BA05-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF Modelo 1 referenciada (tag:refNF): - NF
        modelo 1 referenciada emitida há mais de 20 anos da data atual ou com data de
        emissão superior ao Ano-Mês atual (NT 2015.002)
        Erro: 317: Rejeição: NF modelo 1 referenciada com data de emissão inválida
        [nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        # Requires comparing AAMM with current date – deferred (would need current date)
        return None

    def validation_facul_rej_548_ba06_10(self) -> ValidationResult:
        """BA06-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF Modelo 1 referenciada (tag:refNF): - CNPJ
        com zeros, nulo ou DV inválido
        Erro: 548: Rejeição: NF modelo 1 referenciada com data de emissão inválida
        [nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            ref_nf = getattr(ref, "refNF", None)
            if ref_nf is None:
                continue
            cnpj = _v(getattr(ref_nf, "CNPJ", None)) or ""
            if cnpj and not validate_cnpj(cnpj):
                errors.append(
                    self._err(
                        "BA06-10",
                        548,
                        "Rej.",
                        "Rejeição: CNPJ inválido na NF Modelo 1 referenciada",
                        "ide/NFref/refNF/CNPJ",
                    )
                )
        return errors or None

    def validation_facul_rej_682_ba10_10(self) -> ValidationResult:
        """BA10-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF de Produtor referenciada (tag:refNFP): -
        Verificar duplicidade de Nota Fiscal de Produtor referenciada (mesma IE, Modelo,
        Série, Número) (NT 2013/003) (NT 2015.002)
        Erro: 682: Rejeição: Duplicidade de NF de Produtor referenciada (IE, Modelo,
        Série e Número) [nOcor: 999]
        """
        if not self._is_nfe():
            return None
        seen = set()
        for ref in self._get_nfref_list():
            ref_nfp = getattr(ref, "refNFP", None)
            if ref_nfp is None:
                continue
            key = (
                _v(getattr(ref_nfp, "cUF", None)) or "",
                _v(getattr(ref_nfp, "AAMM", None)) or "",
                _v(getattr(ref_nfp, "CNPJ", None)) or "",
                _v(getattr(ref_nfp, "CPF", None)) or "",
                _v(getattr(ref_nfp, "IE", None)) or "",
                _v(getattr(ref_nfp, "mod", None)) or "",
                _v(getattr(ref_nfp, "serie", None)) or "",
                _v(getattr(ref_nfp, "nNF", None)) or "",
            )
            if key in seen:
                return self._err(
                    "BA10-10",
                    682,
                    "Rej.",
                    "Rejeição: NF de Produtor referenciada em duplicidade",
                    "ide/NFref/refNFP",
                )
            seen.add(key)
        return None

    def validation_facul_rej_318_ba10_20(self) -> ValidationResult:
        """BA10-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Contranota de Produtor sem Nota Fiscal referenciada: - não
        informada NF de Produtor referenciada (tag:refNFP); - e não informada Nota
        Fiscal referenciada (tag:refNFe). Observação 1: A Contranota de Produtor é
        identificada como uma Nota Fiscal de entrada (tag:tpNF=0) e remetente da mesma
        UF com IE de Produtor Rural. Observação 2: A utilização e controle da Contranota
        de Produtor é opcional, a critério da UF.
        Erro: 318: Rejeição: Contranota de Produtor sem Nota Fiscal referenciada
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA10-20
        return None

    def validation_facul_rej_319_ba10_30(self) -> ValidationResult:
        """BA10-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Contranota de Produtor não pode referenciar somente Nota
        Fiscal de entrada: - não informada NF de Produtor referenciada (tag:refNFP); - e
        não informada Nota Fiscal referenciada (tag:refNFe) de saída (tag:tpNF=1).
        Observação 1: Identificação de Contranota de Produtor conforme observação da
        validação anterior. Observação 2: A utilização e controle da Contranota de
        Produtor é opcional, a critério da UF. (NT 2015.002)
        Erro: 319: Rejeição: Contranota de Produtor não pode referenciar somente Nota
        Fiscal de entrada
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA10-30
        return None

    def validation_facul_rej_320_ba10_40(self) -> ValidationResult:
        """BA10-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Contranota de Produtor referencia somente Nota Fiscal de
        outro emitente. Não existe nenhuma das ocorrências abaixo: - IE da NF de
        Produtor referenciada (tag: refNFP/IE) idêntica à IE do Emitente (tag: emit/IE)
        ou do Remetente (tag: dest/IE); - IE do emitente da NF referenciada (tag:
        emit/IE) idêntica à IE do Emitente (tag: emit/IE) ou do Remetente (tag:
        dest/IE). Observação 1: Identificação de Contranota de Produtor conforme
        Observação 1 da regra BA10-20. Observação 2: A utilização e controle da
        Contranota de Produtor é opcional, a critério da UF. Observação 3: A critério da
        UF, a validação da IE do emitente da NF referenciada (tag: emit/IE) pode ser
        substituída por: o CNPJ-8 do emitente da NF referenciada (tag:emit/CNPJ)
        idêntico ao CNPJ-8 do Emitente (tag: emit/CNPJ) ou do Remetente (tag: dest/CNPJ)
        (NT 2019.001 v1.00).
        Erro: 320: Rejeição: Contranota de Produtor referencia somente NF de outro
        emitente
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA10-40
        return None

    def validation_facul_rej_922_ba10_50(self) -> ValidationResult:
        """BA10-50.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Contranota de Produtor só pode referenciar NF-e (tag:
        refNFe) ou NF de Produtor Modelo 4 (tag: refNFP): Observação 1: Identificação de
        Contranota de Produtor conforme Observação 1 da regra BA10-20. Observação 2:
        Regra opcional, a critério da UF. (NT 2019.001 v1.00)
        Erro: 922: Rejeição: Contranota de Produtor só pode referenciar NF-e ou NF de
        Produtor Modelo 4
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA10-50
        return None

    def validation_facul_rej_322_ba12_10(self) -> ValidationResult:
        """BA12-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF de Produtor referenciada (tag:refNFP): - NF
        de produtor referenciada emitida a mais de 20 anos da data atual ou com data de
        emissão superior ao Ano-Mês atual (NT 2015.002)
        Erro: 322: Rejeição: NF de produtor referenciada com data de emissão inválida
        [nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        # Requires comparing AAMM with current date – deferred
        return None

    def validation_facul_rej_549_ba13_10(self) -> ValidationResult:
        """BA13-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF de Produtor referenciada (tag:refNFP): -
        CNPJ com zeros, nulo ou DV inválido
        Erro: 549: Rejeição: CNPJ da NF referenciada de produtor inválido [nOcor: 999]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            ref_nfp = getattr(ref, "refNFP", None)
            if ref_nfp is None:
                continue
            cnpj = _v(getattr(ref_nfp, "CNPJ", None)) or ""
            if cnpj and not validate_cnpj(cnpj):
                errors.append(
                    self._err(
                        "BA13-10",
                        549,
                        "Rej.",
                        "Rejeição: CNPJ inválido na NF de Produtor referenciada",
                        "ide/NFref/refNFP/CNPJ",
                    )
                )
        return errors or None

    def validation_facul_rej_550_ba14_10(self) -> ValidationResult:
        """BA14-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF de Produtor referenciada (tag:refNFP): - CPF
        com zeros, nulo, 111..., 222, ..., ou DV inválido (NT 2012/003)
        Erro: 550: Rejeição: CPF da NF referenciada de produtor inválido.
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            ref_nfp = getattr(ref, "refNFP", None)
            if ref_nfp is None:
                continue
            cpf = _v(getattr(ref_nfp, "CPF", None)) or ""
            if cpf and not validate_cpf(cpf):
                errors.append(
                    self._err(
                        "BA14-10",
                        550,
                        "Rej.",
                        "Rejeição: CPF inválido na NF de Produtor referenciada",
                        "ide/NFref/refNFP/CPF",
                    )
                )
        return errors or None

    def validation_facul_rej_551_ba15_10(self) -> ValidationResult:
        """BA15-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informada NF de Produtor referenciada (tag:refNFP): - IE
        com zeros, nulo ou DV inválido para a UF.
        Erro: 551: Rejeição: IE da NF referenciada de produtor inválido.
        """
        if not self._is_nfe():
            return None
        # TODO: IE validation per UF requires external table
        return None

    def validation_facul_rej_547_ba19_10(self) -> ValidationResult:
        """BA19-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com Dígito Verificador inválido (NT 2015.002)
        Erro: 547: Rejeição: Chave de Acesso referenciada com Dígito Verificador
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44 and not validate_access_key_dv(key):
                errors.append(
                    self._err(
                        "BA19-10",
                        547,
                        "Rej.",
                        "Rejeição: Dígito Verificador do CT-e referenciado inválido",
                        "ide/NFref/refCTe",
                    )
                )
        return errors or None

    def validation_facul_rej_522_ba19_14(self) -> ValidationResult:
        """BA19-14.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com UF inválida (NT 2015.002)
        Erro: 522: Rejeição: Chave de Acesso referenciada com UF inválida[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44 and key[:2] not in VALID_UF_CODES:
                errors.append(
                    self._err(
                        "BA19-14",
                        522,
                        "Rej.",
                        "Rejeição: UF inválida na Chave de Acesso do CT-e referenciado",
                        "ide/NFref/refCTe",
                    )
                )
        return errors or None

    def validation_facul_rej_524_ba19_20(self) -> ValidationResult:
        """BA19-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com Ano Emissão < 06 ou > que o Ano corrente (NT 2015.002)
        Erro: 524: Rejeição: Chave de Acesso referenciada com Ano-Mês
        inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44:
                try:
                    ano = int(key[2:4])
                    if ano < 6:
                        errors.append(
                            self._err(
                                "BA19-20",
                                524,
                                "Rej.",
                                "Rejeição: Ano de emissão inválido no CT-e referenciado",
                                "ide/NFref/refCTe",
                            )
                        )
                except (ValueError, TypeError):
                    pass
        return errors or None

    def validation_facul_rej_524_ba19_24(self) -> ValidationResult:
        """BA19-24.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com Mês Emissão < 01 ou > 12 (NT 2015.002)
        Erro: 524: Rejeição: Chave de Acesso referenciada com Ano-Mês inválido [nOcor:
        999]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44:
                try:
                    mes = int(key[4:6])
                    if not (1 <= mes <= 12):
                        errors.append(
                            self._err(
                                "BA19-24",
                                524,
                                "Rej.",
                                "Rejeição: Mês de emissão inválido no CT-e referenciado",
                                "ide/NFref/refCTe",
                            )
                        )
                except (ValueError, TypeError):
                    pass
        return errors or None

    def validation_facul_rej_552_ba19_30(self) -> ValidationResult:
        """BA19-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com CNPJ zerado ou CNPJ com DV inválido (NT 2015.002)
        Erro: 552: Rejeição: Chave de Acesso referenciada com CNPJ inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44:
                cnpj = key[6:20]
                if not validate_cnpj(cnpj):
                    errors.append(
                        self._err(
                            "BA19-30",
                            552,
                            "Rej.",
                            "Rejeição: CNPJ inválido na Chave de Acesso do CT-e referenciado",
                            "ide/NFref/refCTe",
                        )
                    )
        return errors or None

    def validation_facul_rej_679_ba19_34(self) -> ValidationResult:
        """BA19-34.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com Modelo diferente de 57 (NT 2013/003) (NT 2015.002)
        Erro: 679: Rejeição: Chave de Acesso referenciada com Modelo inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44 and key[20:22] != "57":
                errors.append(
                    self._err(
                        "BA19-34",
                        679,
                        "Rej.",
                        "Rejeição: Modelo inválido na Chave de Acesso do CT-e referenciado (deve ser 57)",
                        "ide/NFref/refCTe",
                    )
                )
        return errors or None

    def validation_facul_rej_683_ba19_40(self) -> ValidationResult:
        """BA19-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada com Número zerado (NT 2015.002)
        Erro: 683: Rejeição: Chave de Acesso referenciada com Número inválido[nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if len(key) == 44 and key[25:34] == "000000000":
                errors.append(
                    self._err(
                        "BA19-40",
                        683,
                        "Rej.",
                        "Rejeição: Número zerado na Chave de Acesso do CT-e referenciado",
                        "ide/NFref/refCTe",
                    )
                )
        return errors or None

    def validation_facul_rej_680_ba19_44(self) -> ValidationResult:
        """BA19-44.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CT-e Referenciado (tag:refCTe): - Chave de
        Acesso referenciada em duplicidade na NF-e (duplicidade da tag refCTe) (NT
        2013/003) (NT 2015.002)
        Erro: 680: Rejeição: Chave de Acesso referenciada em duplicidade na NF-e
        [nOcor:nnn]
        """
        if not self._is_nfe():
            return None
        seen = set()
        for ref in self._get_nfref_list():
            key = _v(getattr(ref, "refCTe", None)) or ""
            if key:
                if key in seen:
                    return self._err(
                        "BA19-44",
                        680,
                        "Rej.",
                        "Rejeição: CT-e referenciado em duplicidade",
                        "ide/NFref/refCTe",
                    )
                seen.add(key)
        return None

    def validation_facul_rej_684_ba20_10(self) -> ValidationResult:
        """BA20-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado Cupom Fiscal referenciado (tag:refECF): -
        Verificar duplicidade de Cupom Fiscal referenciado (mesmo Modelo, Número de
        Ordem e COO) (NT 2013/003)
        Erro: 684: Rejeição: Duplicidade de Cupom Fiscal referenciado (Modelo, Número de
        Ordem e COO) [nOcor: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA20-10
        return None

    def validation_facul_rej_923_ba20_20(self) -> ValidationResult:
        """BA20-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Informado Cupom Fiscal referenciado (tag: refECF) ou
        informado NF modelo 1 ou 2 referenciada (tag: refNF) em NF-e de operação
        interestadual ou com o exterior (tag: idDest<>1) (NT 2019.001 v1.00)
        Erro: 923: Rejeição: Referenciado documento de operação interna em operação
        interestadual ou com o exterior
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for BA20-20
        return None

    def validation_facul_rej_924_ba20_30(self) -> ValidationResult:
        """BA20-30.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado Cupom Fiscal referenciado (tag: refECF) em UF que
        não permite essa referência. Observação: Regra de validação opcional, a critério
        da UF. (NT 2019.001 v1.00, v.150)
        Erro: 924: Rejeição: Informado Cupom Fiscal referenciado
        """
        # TODO: implement validation logic for BA20-30
        return None

    # ============================================================
    # Group C
    # ============================================================

    def validation_obrig_rej_207_c02_10(self) -> ValidationResult:
        """C02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ do emitente: - CNPJ com zeros, nulo ou DV
        inválido
        Erro: 207: Rejeição: CNPJ do emitente inválido
        """
        if not self._emit:
            return None
        cnpj = getattr(self._emit, "CNPJ", None)
        if cnpj and not validate_cnpj(cnpj):
            return self._err(
                "C02-10",
                207,
                "Rej.",
                "Rejeição: CNPJ do emitente inválido",
                "emit/CNPJ",
            )
        return None

    def validation_facul_rej_560_c02_20(self) -> ValidationResult:
        """C02-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CNPJ do emitente: - CNPJ Base do Emitente
        difere do CNPJ Base da primeira NF-e do Lote recebido (NT 2018.001)
        Erro: 560: Rejeição: CNPJ base/CPF do emitente difere do CNPJ base/CPF da
        primeira NF-e do lote recebido
        """
        # TODO: implement validation logic for C02-20
        return None

    def validation_obrig_rej_503_c02_30(self) -> ValidationResult:
        """C02-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ do Emitente: - Série difere da faixa para
        emitente CNPJ: faixa 000-909 (NT 2018.001)
        Erro: 503: Rejeição: CNPJ do emitente com Série incompatível
        """
        if not self._emit or not self._ide:
            return None
        if not getattr(self._emit, "CNPJ", None):
            return None
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (0 <= serie <= 909):
            return self._err(
                "C02-30",
                503,
                "Rej.",
                "Rejeição: CNPJ do emitente com Série incompatível",
                "ide/serie",
            )
        return None

    def validation_obrig_rej_337_c02a_04(self) -> ValidationResult:
        """C02a-04.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do emitente: - Se NFC-e (modelo 65) (NT
        2015.002)
        Erro: 337: Rejeição: NFC-e para emitente pessoa física
        """
        if not self._is_nfce():
            return None
        if self._emit and getattr(self._emit, "CPF", None):
            return self._err(
                "C02a-04",
                337,
                "Rej.",
                "Rejeição: NFC-e para emitente pessoa física",
                "emit/CPF",
            )
        return None

    def validation_obrig_rej_652_c02a_08(self) -> ValidationResult:
        """C02a-08.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do emitente: - Se NF-e (modelo 55)
        Observação: Regra de validação opcional a critério da UF. (NT 2018.001)
        Erro: 652: Rejeição: NF-e para emitente pessoa física
        """
        if not self._is_nfe():
            return None
        if self._emit and getattr(self._emit, "CPF", None):
            return self._err(
                "C02a-08",
                652,
                "Rej.",
                "Rejeição: NF-e para emitente pessoa física",
                "emit/CPF",
            )
        return None

    def validation_obrig_rej_495_c02a_10(self) -> ValidationResult:
        """C02a-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do emitente: - Série difere da faixa para
        emitente CPF: 890-899 e 910-969 (NT 2018.001 / NT 2015.002)
        Erro: 495: Rejeição: CPF do Emitente com Série incompatível
        """
        if not self._is_nfe() or not self._emit or not self._ide:
            return None
        if not getattr(self._emit, "CPF", None):
            return None
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (890 <= serie <= 899 or 910 <= serie <= 969):
            return self._err(
                "C02a-10",
                495,
                "Rej.",
                "Rejeição: CPF do Emitente com Série incompatível",
                "ide/serie",
            )
        return None

    def validation_obrig_rej_407_c02a_14(self) -> ValidationResult:
        """C02a-14.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do Emitente: - Série difere da faixa para
        emitente CPF: 890-899 e 910-919 Observação: Regra de validação opcional a
        critério da UF. Permite a emissão de NF-e por pessoa física, somente no serviço
        de Nota Fiscal Avulsa no site da UF. (NT 2018.001)
        Erro: 407: Rejeição: CPF do Emitente somente no serviço de Nota Fiscal Avulsa no
        site do Fisco
        """
        if not self._is_nfe() or not self._emit or not self._ide:
            return None
        if not getattr(self._emit, "CPF", None):
            return None
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (890 <= serie <= 899 or 910 <= serie <= 919):
            return self._err(
                "C02a-14",
                407,
                "Rej.",
                "Rejeição: CPF do Emitente somente no serviço de Nota Fiscal Avulsa no site do Fisco",
                "ide/serie",
            )
        return None

    def validation_obrig_rej_401_c02a_20(self) -> ValidationResult:
        """C02a-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do emitente: - CPF com zeros, nulo, 111...,
        222..., ..., ou DV inválido (NT 2012/003) (NT 2015.002)
        Erro: 401: Rejeição: CPF do emitente inválido
        """
        if not self._is_nfe():
            return None
        if not self._emit:
            return None
        cpf = getattr(self._emit, "CPF", None)
        if cpf and not validate_cpf(cpf):
            return self._err(
                "C02a-20", 401, "Rej.", "Rejeição: CPF do emitente inválido", "emit/CPF"
            )
        return None

    def validation_facul_rej_560_c02a_30(self) -> ValidationResult:
        """C02a-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado CPF do emitente: - CPF do Emitente difere do
        CPF da primeira NF-e do Lote recebido (NT 2018.001)
        Erro: 560: Rejeição: CNPJ Base/CPF do emitente difere do CNPJ Base/CPF da
        primeira NF-e do lote recebido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for C02a-30
        return None

    def validation_obrig_rej_272_c10_10(self) -> ValidationResult:
        """C10-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código do Município do Emitente inexistente (Tabela
        Municípios IBGE) (NT 2015.002)
        Erro: 272: Rejeição: Código Município do Emitente inexistente
        """
        if not self._emit:
            return None
        ender = getattr(self._emit, "enderEmit", None)
        if ender:
            cmun = _v(getattr(ender, "cMun", None)) or ""
            if cmun and not validate_municipality_code(cmun):
                return self._err(
                    "C10-10",
                    272,
                    "Rej.",
                    "Rejeição: Código Município do Emitente inexistente",
                    "emit/enderEmit/cMun",
                )
        return None

    def validation_obrig_rej_273_c10_20(self) -> ValidationResult:
        """C10-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código do Município do Emitente (2 primeiras posições)
        difere do Código da UF do emitente
        Erro: 273: Rejeição: Código Município do Emitente: difere da UF do emitente
        """
        if not self._emit or not self._ide:
            return None
        ender = getattr(self._emit, "enderEmit", None)
        if ender:
            cmun = _v(getattr(ender, "cMun", None)) or ""
            cuf = _v(getattr(self._ide, "cUF", None)) or ""
            if cmun and cuf and cmun[:2] != cuf:
                return self._err(
                    "C10-20",
                    273,
                    "Rej.",
                    "Rejeição: Código Município do Emitente difere da UF",
                    "emit/enderEmit/cMun",
                )
        return None

    def validation_obrig_rej_247_c12_10(self) -> ValidationResult:
        """C12-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Sigla da UF do Emitente difere da UF do Web Service
        Erro: 247: Rejeição: Sigla da UF do Emitente diverge da UF autorizadora
        """
        # TODO: implement validation logic for C12-10
        return None

    def validation_obrig_rej_229_c17_10(self) -> ValidationResult:
        """C17-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: IE Emitente com zeros ou nulo
        Erro: 229: Rejeição: IE do emitente não informada
        """
        if not self._emit:
            return None
        ie = getattr(self._emit, "IE", None) or ""
        if not ie or ie == "0" * len(ie):
            return self._err(
                "C17-10",
                229,
                "Rej.",
                "Rejeição: IE do emitente com zeros ou nulo",
                "emit/IE",
            )
        return None

    def validation_obrig_rej_209_c17_20(self) -> ValidationResult:
        """C17-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se IE diferente de “ISENTO”, validar a Inscrição Estadual: -
        IE Emitente inválida para a UF: erro no tamanho, na composição da IE, ou no
        dígito verificador (*2) (NT 2018.001)
        Erro: 209: Rejeição: IE do emitente inválida
        """
        # TODO: implement validation logic for C17-20
        return None

    def validation_obrig_rej_554_c17_30(self) -> ValidationResult:
        """C17-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se IE informada com “ISENTO”: - Se modelo = 65 ou Série
        difere da faixa 890-919 (NT 2018.001)
        Erro: 554: Rejeição: IE do Emitente informada como ISENTO indevidamente
        """
        if not self._emit or not self._ide:
            return None
        ie = getattr(self._emit, "IE", None) or ""
        if ie != "ISENTO":
            return None
        if self._is_nfce():
            return self._err(
                "C17-30",
                554,
                "Rej.",
                "Rejeição: IE do Emitente informada como ISENTO indevidamente",
                "emit/IE",
            )
        serie_str = _v(getattr(self._ide, "serie", None)) or ""
        try:
            serie = int(serie_str)
        except (ValueError, TypeError):
            return None
        if not (890 <= serie <= 919):
            return self._err(
                "C17-30",
                554,
                "Rej.",
                "Rejeição: IE do Emitente informada como ISENTO indevidamente",
                "emit/IE",
            )
        return None

    def validation_obrig_rej_718_c18_10(self) -> ValidationResult:
        """C18-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e não deve informar IE de Substituto Tributário
        (tag:emit/IEST)
        Erro: 718: Rejeição: NFC-e não deve informar IE de Substituto Tributário
        """
        if not self._is_nfce():
            return None
        if self._emit and getattr(self._emit, "IEST", None):
            return self._err(
                "C18-10",
                718,
                "Rej.",
                "Rejeição: NFC-e com IE de Substituto Tributário",
                "emit/IEST",
            )
        return None

    def validation_obrig_rej_347_c18_14(self) -> ValidationResult:
        """C18-14.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Substituto Tributário para uma operação
        com Exterior ou Operação Interna (tag:idDest=1 ou 3) Exceção: A critério da UF,
        poderá ser aceita a informação da IE-ST em operação interna. (NT 2015.002)
        Erro: 347: Rejeição: Informada IE do substituto tributário em operação que não é
        interestadual
        """
        if not self._is_nfe() or not self._emit or not self._ide:
            return None
        iest = getattr(self._emit, "IEST", None)
        if not iest:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        if idDest in ("1", "3"):
            return self._err(
                "C18-14",
                347,
                "Rej.",
                "Rejeição: Informada IE do substituto tributário em operação que não é interestadual",
                "emit/IEST",
            )
        return None

    def validation_obrig_rej_478_c18_20(self) -> ValidationResult:
        """C18-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada operação de Faturamento Direto para veículos
        novos (id:J02, tag:tpOp = 2): - UF do Local de Entrega (id:G09) não informada
        Observação: A UF é necessária na validação da IEST nestas operações. Vide
        Convênio ICMS 51/00.
        Erro: 478: Rejeição: Local da entrega não informado para faturamento direto de
        veículos novos
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for C18-20
        return None

    def validation_obrig_rej_211_c18_30(self) -> ValidationResult:
        """C18-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Substituto Tributário: - IEST inválida
        para a UF: erro no tamanho, na composição da IE, ou no dígito verificador (*2)
        UF a ser utilizada na validação: - UF do Local de Entrega para operação de
        Faturamento Direto de veículos novos (id:G09, caso tpOP, id:J02 = 2); - UF do
        destinatário (UF, campo E12) nos demais casos. (NT 2015.002)
        Erro: 211: Rejeição: IE do substituto inválida
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for C18-30
        return None

    def validation_obrig_rej_363_c18_40(self) -> ValidationResult:
        """C18-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Substituto Tributário: - IEST idêntica
        à IE do emitente ou do destinatário (NT 2015.002)
        Erro: 363: Rejeição: IE do substituto tributário idêntica à IE do emitente ou do
        destinatário
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for C18-40
        return None

    def validation_facul_rej_812_c21_10(self) -> ValidationResult:
        """C21-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Regime Tributário SN, com excesso de sublimite não é
        permitido para Emitentes desta UF (id:CRT=2). Nota: Regra de validação opcional,
        a critério da UF. (NT 2015.002)
        Erro: 812: Rejeição: Regime Tributário SN, com excesso de sublimite não é
        permitido para Emitentes desta UF
        """
        # TODO: implement validation logic for C21-10
        return None

    # ============================================================
    # Group D
    # ============================================================

    def validation_obrig_rej_403_d01_10(self) -> ValidationResult:
        """D01-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado grupo “avulsa” pela empresa (tag:procEmi<>1 e 2).
        Erro: 403: Rejeição: O grupo de informações da NF-e avulsa é de uso exclusivo do
        Fisco
        """
        if not self._ide or not self._inf:
            return None
        procEmi = _v(getattr(self._ide, "procEmi", None))
        if procEmi not in ("1", "2") and getattr(self._inf, "avulsa", None):
            return self._err(
                "D01-10",
                403,
                "Rej.",
                "Rejeição: Informado grupo avulsa pela empresa",
                "avulsa",
            )
        return None

    def validation_obrig_rej_369_d01_20(self) -> ValidationResult:
        """D01-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Não informado grupo "avulsa" na emissão de Nota Fiscal pelo
        Fisco (tag:procEmi=1 ou 2)
        Erro: 369: Rejeição: Não informado o grupo avulsa na emissão pelo Fisco
        """
        if not self._ide or not self._inf:
            return None
        procEmi = _v(getattr(self._ide, "procEmi", None))
        if procEmi in ("1", "2") and not getattr(self._inf, "avulsa", None):
            return self._err(
                "D01-20",
                369,
                "Rej.",
                "Rejeição: Não informado o grupo avulsa na emissão pelo Fisco",
                "avulsa",
            )
        return None

    # ============================================================
    # Group E
    # ============================================================

    def validation_obrig_rej_719_e01_10(self) -> ValidationResult:
        """E01-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e sem a identificação do destinatário (tag:infNFe/dest)
        Erro: 719: Rejeição: NF-e sem a identificação do destinatário
        """
        if not self._is_nfe():
            return None
        if not self._dest:
            return self._err(
                "E01-10",
                719,
                "Rej.",
                "Rejeição: NF-e sem a identificação do destinatário",
                "dest",
            )
        return None

    def validation_obrig_rej_787_e01_20(self) -> ValidationResult:
        """E01-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com entrega a domicílio (indPres=4) sem identificação
        do destinatário (tag:infNFe/dest)
        Erro: 787: Rejeição: NFC-e de entrega a domicílio sem a identificação do
        destinatário
        """
        if not self._is_nfce():
            return None
        if (
            self._ide
            and _v(getattr(self._ide, "indPres", None)) == "4"
            and not self._dest
        ):
            return self._err(
                "E01-20",
                787,
                "Rej.",
                "Rejeição: NFC-e de entrega a domicílio sem a identificação do destinatário",
                "dest",
            )
        return None

    def validation_obrig_rej_208_e02_10(self) -> ValidationResult:
        """E02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ: - CNPJ com zeros ou dígito de controle
        inválido
        Erro: 208: Rejeição: CNPJ do destinatário inválido
        """
        if self._dest:
            cnpj = getattr(self._dest, "CNPJ", None)
            if cnpj and not validate_cnpj(cnpj):
                return self._err(
                    "E02-10",
                    208,
                    "Rej.",
                    "Rejeição: CNPJ do destinatário inválido",
                    "dest/CNPJ",
                )
        return None

    def validation_obrig_rej_220_e02_20(self) -> ValidationResult:
        """E02-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ: - CNPJ do destinatário = CNPJ do Emitente
        (NT 2015.002)
        Erro: 220: Rejeição: Destinatário com identificação igual à identificação do
        emitente
        """
        if not self._is_nfce():
            return None
        if self._dest and self._emit:
            cnpj_dest = getattr(self._dest, "CNPJ", None) or ""
            cnpj_emit = getattr(self._emit, "CNPJ", None) or ""
            if cnpj_dest and cnpj_emit and cnpj_dest == cnpj_emit:
                return self._err(
                    "E02-20",
                    220,
                    "Rej.",
                    "Rejeição: Destinatário com identificação igual à identificação do emitente",
                    "dest/CNPJ",
                )
        return None

    def validation_obrig_rej_237_e03_10(self) -> ValidationResult:
        """E03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF: - CPF com zeros, nulo, 111..., 222..., ...
        ou dígito de controle inválido (NT 2013/003)
        Erro: 237: Rejeição: CPF do destinatário inválido
        """
        if self._dest:
            cpf = getattr(self._dest, "CPF", None)
            if cpf and not validate_cpf(cpf):
                return self._err(
                    "E03-10",
                    237,
                    "Rej.",
                    "Rejeição: CPF do destinatário inválido",
                    "dest/CPF",
                )
        return None

    def validation_obrig_rej_720_e03a_10(self) -> ValidationResult:
        """E03a-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Operação com Exterior (tag:idDest = 3): - Deve ser
        informada tag idEstrangeiro (conteúdo da tag pode ser nulo)
        Erro: 720: Rejeição: Na operação com Exterior deve ser informada tag
        idEstrangeiro
        """
        if not self._is_nfe() or not self._ide:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        if idDest == "3" and (
            not self._dest or getattr(self._dest, "idEstrangeiro", None) is None
        ):
            return self._err(
                "E03a-10",
                720,
                "Rej.",
                "Rejeição: Na operação com Exterior deve ser informada tag idEstrangeiro",
                "dest/idEstrangeiro",
            )
        return None

    def validation_obrig_rej_721_e03a_20(self) -> ValidationResult:
        """E03a-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se não é operação com Exterior (tag:idDest<>3): - Informado
        “idEstrangeiro”, e operação não é com consumidor final(tag:indFinal<> 1) (NT
        2015.002)
        Erro: 721: Rejeição: Informado idEstrangeiro e Operação não é com consumidor
        final.
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        indFinal = _v(getattr(self._ide, "indFinal", None))
        idEst = getattr(self._dest, "idEstrangeiro", None)
        if idDest != "3" and idEst is not None and indFinal != "1":
            return self._err(
                "E03a-20",
                721,
                "Rej.",
                "Rejeição: Informado idEstrangeiro e Operação não é com consumidor final",
                "dest/idEstrangeiro",
            )
        return None

    def validation_obrig_rej_925_e03a_30(self) -> ValidationResult:
        """E03a-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado “idEstrangeiro” não pode ser informada “IE” do
        destinatário (tag: dest/IE). (NT 2019.001 v1.00)
        Erro: 925: Rejeição: NF-e com identificação de estrangeiro e inscrição estadual
        informada para destinatário
        """
        if not self._dest:
            return None
        idEst = getattr(self._dest, "idEstrangeiro", None)
        ie = getattr(self._dest, "IE", None)
        if idEst is not None and ie:
            return self._err(
                "E03a-30",
                925,
                "Rej.",
                "Rejeição: NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário",
                "dest/IE",
            )
        return None

    def validation_obrig_rej_372_e03a_60(self) -> ValidationResult:
        """E03a-60.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado “idEstrangeiro”, campo deve conter somente
        algarismos, letras (maiúsculas e minúsculas) e/ou os caracteres do conjunto que
        segue: [:.+- /()](NT 2015.002)
        Erro: 372: Rejeição: Destinatário com identificação de estrangeiro com
        caracteres inválidos
        """
        if not self._dest:
            return None
        idEst = getattr(self._dest, "idEstrangeiro", None)
        if idEst is None:
            return None
        import re

        if idEst and not re.match(r"^[0-9A-Za-z:.+\-/ ()]*$", str(idEst)):
            return self._err(
                "E03a-60",
                372,
                "Rej.",
                "Rejeição: Destinatário com identificação de estrangeiro com caracteres inválidos",
                "dest/idEstrangeiro",
            )
        return None

    def validation_obrig_rej_724_e04_10(self) -> ValidationResult:
        """E04-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e sem o nome do destinatário (tag:dest/xNome)
        Erro: 724: Rejeição: NF-e sem o nome do destinatário
        """
        if not self._is_nfe():
            return None
        if self._dest and not getattr(self._dest, "xNome", None):
            return self._err(
                "E04-10",
                724,
                "Rej.",
                "Rejeição: NF-e sem o nome do destinatário",
                "dest/xNome",
            )
        return None

    def validation_obrig_rej_598_e04_20(self) -> ValidationResult:
        """E04-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se tag:tpAmb (id:B24) = 2: o xNome (E04) deve ser informado
        com a literal “NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL” (NT
        2011/002)
        Erro: 598: Rejeição: NF-e emitida em ambiente de homologação com Razão Social do
        destinatário diferente de NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR
        FISCAL
        """
        if not self._ide or not self._dest:
            return None
        tpAmb = _v(getattr(self._ide, "tpAmb", None))
        if tpAmb == "2":
            xNome = getattr(self._dest, "xNome", None) or ""
            expected = "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
            if xNome != expected:
                return self._err(
                    "E04-20",
                    598,
                    "Rej.",
                    "Rejeição: Ambiente de homologação com Razão Social do destinatário incorreta",
                    "dest/xNome",
                )
        return None

    def validation_obrig_rej_726_e05_10(self) -> ValidationResult:
        """E05-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e sem a informação de endereço do destinatário
        (tag:dest/enderDest)
        Erro: 726: Rejeição: NF-e sem a informação de endereço do destinatário
        """
        if not self._is_nfe():
            return None
        if self._dest and not getattr(self._dest, "enderDest", None):
            return self._err(
                "E05-10",
                726,
                "Rej.",
                "Rejeição: NF-e sem a informação de endereço do destinatário",
                "dest/enderDest",
            )
        return None

    def validation_obrig_rej_788_e05_20(self) -> ValidationResult:
        """E05-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com entrega a domicílio (indPres=4) sem o endereço do
        destinatário (tag:dest/enderDest)
        Erro: 788: Rejeição: NFC-e de entrega a domicílio sem o endereço do destinatário
        """
        if not self._is_nfce():
            return None
        if (
            self._ide
            and _v(getattr(self._ide, "indPres", None)) == "4"
            and self._dest
            and not getattr(self._dest, "enderDest", None)
        ):
            return self._err(
                "E05-20",
                788,
                "Rej.",
                "Rejeição: NFC-e de entrega a domicílio sem o endereço do destinatário",
                "dest/enderDest",
            )
        return None

    def validation_obrig_rej_274_e10_10(self) -> ValidationResult:
        """E10-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se endereço destinatário não é no Exterior (dest/UF <>
        “EX"): - Código Município do destinatário inexistente (Tabela Municípios IBGE)
        (NT 2015.002)
        Erro: 274: Rejeição: Código Município do Destinatário inexistente
        """
        if not self._dest:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if ender:
            cmun = _v(getattr(ender, "cMun", None)) or ""
            if cmun and cmun != "9999999" and not validate_municipality_code(cmun):
                return self._err(
                    "E10-10",
                    274,
                    "Rej.",
                    "Rejeição: Código Município do Destinatário inexistente",
                    "dest/enderDest/cMun",
                )
        return None

    def validation_obrig_rej_275_e10_20(self) -> ValidationResult:
        """E10-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se endereço destinatário não é no Exterior (dest/UF <>
        “EX"): - Código Município do destinatário (2 primeiras posições) difere do
        Código da UF do destinatário
        Erro: 275: Rejeição: Código Município do Destinatário: difere da UF do
        Destinatário
        """
        if not self._dest:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if ender:
            cmun = _v(getattr(ender, "cMun", None)) or ""
            uf = _v(getattr(ender, "UF", None)) or ""
            if cmun and uf and uf != "EX" and not municipality_matches_uf(cmun, uf):
                return self._err(
                    "E10-20",
                    275,
                    "Rej.",
                    "Rejeição: UF do destinatário difere da UF do cMun",
                    "dest/enderDest/UF",
                )
        return None

    def validation_obrig_rej_509_e10_30(self) -> ValidationResult:
        """E10-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se endereço destinatário é no Exterior (dest/UF = “EX"): -
        Código Município do destinatário difere de “9999999”
        Erro: 509: Rejeição: Informado código de município diferente de “9999999” para
        operação com o exterior
        """
        if not self._is_nfe():
            return None
        if not self._dest:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if ender:
            uf = _v(getattr(ender, "UF", None)) or ""
            if uf == "EX":
                cmun = _v(getattr(ender, "cMun", None)) or ""
                if cmun and cmun != "9999999":
                    return self._err(
                        "E10-30",
                        509,
                        "Rej.",
                        "Rejeição: Informado código de município diferente de 9999999 para operação com o exterior",
                        "dest/enderDest/cMun",
                    )
        return None

    def validation_obrig_rej_727_e12_10(self) -> ValidationResult:
        """E12-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se endereço destinatário é no Exterior (dest/UF = “EX"): -
        UF de destino diferente de “EX”
        Erro: 727: Rejeição: Operação com Exterior e UF diferente de EX
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        if idDest == "3":
            ender = getattr(self._dest, "enderDest", None)
            if ender and _v(getattr(ender, "UF", None)) != "EX":
                return self._err(
                    "E12-10",
                    727,
                    "Rej.",
                    "Rejeição: Operação com Exterior e UF diferente de EX",
                    "dest/enderDest/UF",
                )
        return None

    def validation_obrig_rej_772_e12_30(self) -> ValidationResult:
        """E12-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Nota Fiscal é de Saída (tpNF=1) e operação é
        Interestadual (tag:idDest = 2): - UF do destinatário (tag: enderDest/UF) igual à
        UF do emitente (tag: enderEmit/UF) e CNPJ emissor diferente do CNPJ destinatário
        (NT 2013/005). Observação: Não rejeitar se existir algum item com a tag UFCons
        (id:L120) diversa da UF do emitente. Exceção 1: A regra de validação não se
        aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do
        emitente (tag: enderEmit/UF) e não informada UF do local de retirada (tag:
        retirada/UF); Exceção 2: A regra de validação não se aplica se informada UF do
        local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag:
        enderDest/UF) e não informada UF do local de entrega (tag: entrega/UF); Exceção
        3: A regra de validação não se aplica se informadas UF do local de entrega (tag:
        entrega/UF) e UF do local de retirada (tag: retirada/UF) diferentes entre si;
        (NT 2015.003)
        Erro: 772: Rejeição: Operação Interestadual e UF de destino igual à UF de origem
        """
        if not self._is_nfe() or not self._ide or not self._dest or not self._emit:
            return None
        tpNF = _v(getattr(self._ide, "tpNF", None))
        idDest = _v(getattr(self._ide, "idDest", None))
        if tpNF != "1" or idDest != "2":
            return None
        ender_dest = getattr(self._dest, "enderDest", None)
        ender_emit = getattr(self._emit, "enderEmit", None)
        if not ender_dest or not ender_emit:
            return None
        uf_dest = _v(getattr(ender_dest, "UF", None)) or ""
        uf_emit = _v(getattr(ender_emit, "UF", None)) or ""
        cnpj_dest = getattr(self._dest, "CNPJ", None) or ""
        cnpj_emit = getattr(self._emit, "CNPJ", None) or ""
        if uf_dest and uf_emit and uf_dest == uf_emit and cnpj_dest != cnpj_emit:
            return self._err(
                "E12-30",
                772,
                "Rej.",
                "Rejeição: Operação Interestadual e UF de destino igual à UF de origem",
                "dest/enderDest/UF",
            )
        return None

    def validation_obrig_rej_773_e12_40(self) -> ValidationResult:
        """E12-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Nota Fiscal é de Saída (tpNF=1), operação é Interna no
        Estado (tag:idDest = 1) e operação não é com Consumidor final: - UF do
        destinatário (tag: enderDest/UF) difere da UF do emitente (tag: enderEmit/UF).
        (NT 2015.003) Exceção 1: Se a tag UFCons (id:LA06) foi informada com a mesma UF
        do emitente não se aplica esta regra (NT 2013/005) Exceção 2: A regra de
        validação não se aplica se informada UF do local de entrega (tag: entrega/UF)
        igual à UF do emitente (tag: enderEmit/UF) e não informada UF do local de
        retirada (tag: retirada/UF); Exceção 3: A regra de validação não se aplica se
        informada UF do local de retirada (tag: retirada/UF) igual à UF do destinatário
        (tag: enderDest/UF) e não informada UF do local de entrega (tag: entrega/UF);
        Exceção 4: A regra de validação não se aplica se informadas UF do local de
        entrega (tag: entrega/UF) e UF do local de retirada (tag: retirada/UF) iguais
        entre si;
        Erro: 773: Rejeição: Operação Interna e UF de destino difere da UF de origem
        """
        if not self._is_nfe() or not self._ide or not self._dest or not self._emit:
            return None
        tpNF = _v(getattr(self._ide, "tpNF", None))
        idDest = _v(getattr(self._ide, "idDest", None))
        indFinal = _v(getattr(self._ide, "indFinal", None))
        if tpNF != "1" or idDest != "1" or indFinal == "1":
            return None
        ender_dest = getattr(self._dest, "enderDest", None)
        ender_emit = getattr(self._emit, "enderEmit", None)
        if not ender_dest or not ender_emit:
            return None
        uf_dest = _v(getattr(ender_dest, "UF", None)) or ""
        uf_emit = _v(getattr(ender_emit, "UF", None)) or ""
        if uf_dest and uf_emit and uf_dest != uf_emit:
            return self._err(
                "E12-40",
                773,
                "Rej.",
                "Rejeição: Operação Interna e UF de destino difere da UF de origem",
                "dest/enderDest/UF",
            )
        return None

    def validation_obrig_rej_772_e12_50(self) -> ValidationResult:
        """E12-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Nota Fiscal é de Entrada (tpNF=0) e operação é
        Interestadual (tag:idDest = 2): - UF do destinatário (tag: enderDest/UF) igual à
        UF do emitente (tag: enderEmit/UF) e CNPJ emissor diferente do CNPJ
        destinatário. Observação: Não rejeitar se existir algum item com a tag UFCons
        (id:L120) diversa da UF do emitente. Exceção 1: A regra de validação não se
        aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do
        destinatário (tag: enderDest/UF) e não informada UF do local de retirada (tag:
        retirada/UF); Exceção 2: A regra de validação não se aplica se informada UF do
        local de retirada (tag: retirada/UF) diferente da UF do emitente (tag:
        enderEmit/UF) e não informada UF do local de entrega (tag: entrega/UF); Exceção
        3: A regra de validação não se aplica se informadas UF do local de entrega (tag:
        entrega/UF) e UF do local de retirada (tag: retirada/UF) diferentes entre si;
        (NT 2015.003)
        Erro: 772: Rejeição: Operação Interestadual e UF de destino igual à UF de origem
        """
        if not self._is_nfe() or not self._ide or not self._dest or not self._emit:
            return None
        tpNF = _v(getattr(self._ide, "tpNF", None))
        idDest = _v(getattr(self._ide, "idDest", None))
        if tpNF != "0" or idDest != "2":
            return None
        ender_dest = getattr(self._dest, "enderDest", None)
        ender_emit = getattr(self._emit, "enderEmit", None)
        if not ender_dest or not ender_emit:
            return None
        uf_dest = _v(getattr(ender_dest, "UF", None)) or ""
        uf_emit = _v(getattr(ender_emit, "UF", None)) or ""
        cnpj_dest = getattr(self._dest, "CNPJ", None) or ""
        cnpj_emit = getattr(self._emit, "CNPJ", None) or ""
        if uf_dest and uf_emit and uf_dest == uf_emit and cnpj_dest != cnpj_emit:
            return self._err(
                "E12-50",
                772,
                "Rej.",
                "Rejeição: Operação Interestadual e UF de destino igual à UF de origem",
                "dest/enderDest/UF",
            )
        return None

    def validation_obrig_rej_773_e12_60(self) -> ValidationResult:
        """E12-60.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Nota Fiscal é de Entrada (tpNF=0), operação é Interna no
        Estado (tag:idDest = 1) e operação não é com Consumidor final: - UF do
        destinatário (tag: enderDest/UF) difere da UF do emitente (tag: enderEmit/UF).
        Exceção 1: Se a tag UFCons (id:LA06) foi informada com a mesma UF do emitente
        não se aplica esta regra; Exceção 2: A regra de validação não se aplica se
        informada UF do local de entrega (tag: entrega/UF) igual à UF do destinatário
        (tag: enderDest/UF) e não informada UF do local de retirada (tag: retirada/UF);
        Exceção 3: A regra de validação não se aplica se informada UF do local de
        retirada (tag: retirada/UF) igual à UF do emitente (tag: enderEmit/UF) e não
        informada UF do local de entrega (tag: entrega/UF); Exceção 4: A regra de
        validação não se aplica se informadas UF do local de entrega (tag: entrega/UF) e
        UF do local de retirada (tag: retirada/UF) iguais entre si; (NT 2015.003)
        Erro: 773: Rejeição: Operação Interna e UF de destino difere da UF de origem
        """
        if not self._is_nfe() or not self._ide or not self._dest or not self._emit:
            return None
        tpNF = _v(getattr(self._ide, "tpNF", None))
        idDest = _v(getattr(self._ide, "idDest", None))
        indFinal = _v(getattr(self._ide, "indFinal", None))
        if tpNF != "0" or idDest != "1" or indFinal == "1":
            return None
        ender_dest = getattr(self._dest, "enderDest", None)
        ender_emit = getattr(self._emit, "enderEmit", None)
        if not ender_dest or not ender_emit:
            return None
        uf_dest = _v(getattr(ender_dest, "UF", None)) or ""
        uf_emit = _v(getattr(ender_emit, "UF", None)) or ""
        if uf_dest and uf_emit and uf_dest != uf_emit:
            return self._err(
                "E12-60",
                773,
                "Rej.",
                "Rejeição: Operação Interna e UF de destino difere da UF de origem",
                "dest/enderDest/UF",
            )
        return None

    def validation_obrig_rej_377_e14_04(self) -> ValidationResult:
        """E14-04.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Código País do destinatário (tag:
        enderDest/cPais): - Código do País inexistente (Tabela do BACEN, vide tabela de
        apoio publicada no Portal da NF-e). Observação: O Código do País informado na
        NF-e pode conter ou não zeros não significativos. (NT 2015.002)
        Erro: 377: Rejeição: Código de País do destinatário inexistente
        """
        if not self._dest:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if not ender:
            return None
        cpais = _v(getattr(ender, "cPais", None)) or ""
        if cpais and not validate_country_code(cpais):
            return self._err(
                "E14-04",
                377,
                "Rej.",
                "Rejeição: Código do País do destinatário inexistente",
                "dest/enderDest/cPais",
            )
        return None

    def validation_facul_rej_510_e14_10(self) -> ValidationResult:
        """E14-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se operação com Exterior (tag:idDest=3): - Código País do
        destinatário = 1058 (Brasil), ou não informado
        Erro: 510: Rejeição: Operação com Exterior e Código País destinatário é 1058
        (Brasil) ou não informado
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        if _v(getattr(self._ide, "idDest", None)) != "3":
            return None
        ender = getattr(self._dest, "enderDest", None)
        cpais = _v(getattr(ender, "cPais", None)) if ender else None
        if not cpais or str(int(cpais)).zfill(4) == BRAZIL_COUNTRY_CODE:
            return self._err(
                "E14-10",
                510,
                "Rej.",
                "Rejeição: Operação com Exterior com código de país inválido (Brasil ou não informado)",
                "dest/enderDest/cPais",
            )
        return None

    def validation_facul_rej_511_e14_20(self) -> ValidationResult:
        """E14-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se não é operação com Exterior (tag:idDest<>3) e informado
        Código País do destinatário: - Código País do destinatário difere de 1058
        (Brasil) Exceção: Se idEstrangeiro <> nulo é permitido cPais <> 1058. (NT
        2015.002)
        Erro: 511: Rejeição: Não é de Operação com Exterior e Código País destinatário
        difere de 1058 (Brasil)
        """
        if not self._ide or not self._dest:
            return None
        if _v(getattr(self._ide, "idDest", None)) == "3":
            return None
        ender = getattr(self._dest, "enderDest", None)
        if not ender:
            return None
        cpais = _v(getattr(ender, "cPais", None)) or ""
        if cpais:
            try:
                if str(int(cpais)).zfill(4) != BRAZIL_COUNTRY_CODE:
                    return self._err(
                        "E14-20",
                        511,
                        "Rej.",
                        "Rejeição: Operação interna/interestadual com código de país diferente do Brasil",
                        "dest/enderDest/cPais",
                    )
            except (ValueError, TypeError):
                pass
        return None

    def validation_obrig_rej_926_e14_30(self) -> ValidationResult:
        """E14-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se endereço do destinatário é no Exterior (dest/UF = “EX"):
        - Código do país “cPais” (id: E14) não pode ser 1058 (Brasil). (NT 2019.001
        v1.00)
        Erro: 926: Rejeição: Operação com Exterior e país de destino igual a Brasil.
        """
        if not self._dest:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if not ender:
            return None
        uf = _v(getattr(ender, "UF", None)) or ""
        if uf != "EX":
            return None
        cpais = _v(getattr(ender, "cPais", None)) or ""
        if not cpais or not validate_country_code(cpais):
            return self._err(
                "E14-30",
                926,
                "Rej.",
                "Rejeição: Destinatário no Exterior sem código de país válido",
                "dest/enderDest/cPais",
            )
        return None

    def validation_obrig_rej_789_e16a_10(self) -> ValidationResult:
        """E16a-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com indicação de IE do destinatário diferente de "Não
        Contribuinte" (tag:indIEDest <> 9)
        Erro: 789: Rejeição: NFC-e para destinatário contribuinte de ICMS
        """
        if not self._is_nfce():
            return None
        if self._dest:
            indIEDest = _v(getattr(self._dest, "indIEDest", None))
            if indIEDest and indIEDest != "9":
                return self._err(
                    "E16a-10",
                    789,
                    "Rej.",
                    "Rejeição: NFC-e para destinatário contribuinte de ICMS",
                    "dest/indIEDest",
                )
        return None

    def validation_obrig_rej_790_e16a_20(self) -> ValidationResult:
        """E16a-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se operação com Exterior (tag:idDest=3): - Indicação de IE
        Destinatário diferente "Não Contribuinte" (tag:indIEDest <> 9) (NT 2015.003)
        Erro: 790: Rejeição: Operação com Exterior para destinatário Contribuinte de
        ICMS
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        if idDest == "3":
            indIEDest = _v(getattr(self._dest, "indIEDest", None))
            if indIEDest and indIEDest != "9":
                return self._err(
                    "E16a-20",
                    790,
                    "Rej.",
                    "Rejeição: Operação com Exterior para destinatário Contribuinte de ICMS",
                    "dest/indIEDest",
                )
        return None

    def validation_obrig_rej_805_e16a_30(self) -> ValidationResult:
        """E16a-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado destinatário como Contribuinte Isento de Inscrição
        Estadual (indIEDest=2-ISENTO) em UF que não permite esta situação nas operações
        interestaduais (idDest=2), conforme abaixo: - AM, BA, CE, GO, MG, MS, MT, PA,
        PE, RN, SE, SP Exceção 1: Esta regra de validação não se aplica quando houver
        destaque do ICMS-ST (campo vICMSST) em pelo menos um item da NF-e Exceção 2:
        Esta regra de validação não se aplica quando houver informação do ICMS-ST retido
        anteriormente (campo vICMSSTRet) em pelo menos um item da NF-e Exceção 3: A
        regra de validação não se aplica, em produção, para Nota Fiscal com data de
        emissão anterior a 01/07/2016 Exceção 4: Esta regra de validação não se aplica
        nas operações isentas (CST=40-Isenta ou CSOSN=103-Isento), imunes ou não
        tributadas (CST=41- Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não
        tributada pelo Simples Nacional)
        Erro: 805: Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de
        Inscrição Estadual
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        idDest = _v(getattr(self._ide, "idDest", None))
        if idDest != "2":
            return None
        indIEDest = _v(getattr(self._dest, "indIEDest", None))
        if indIEDest != "2":
            return None
        ender_dest = getattr(self._dest, "enderDest", None)
        uf_dest = _v(getattr(ender_dest, "UF", None)) or "" if ender_dest else ""
        from nfelib.nfe.nfe_validation_helpers import UF_NO_IE_ISENTO_INTERESTADUAL

        if uf_dest in UF_NO_IE_ISENTO_INTERESTADUAL:
            return self._err(
                "E16a-30",
                805,
                "Rej.",
                "Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual",
                "dest/indIEDest",
            )
        return None

    def validation_facul_rej_805_e16a_35(self) -> ValidationResult:
        """E16a-35.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Informado destinatário como Contribuinte Isento de Inscrição
        Estadual (indIEDest=2-ISENTO) em UF que não permite esta situação nas operações
        internas (idDest=1) Exceção 1: Esta regra de validação não se aplica quando
        houver destaque do ICMS-ST (campo vICMSST) em pelo menos um item da NF-e.
        Exceção 2: Esta regra de validação não se aplica quando houver informação do
        ICMS-ST retido anteriormente (campo vICMSSTRet) em pelo menos um item da NF-e.
        Exceção 3: A regra de validação não se aplica, em produção, para Nota Fiscal com
        data de emissão anterior a 01/07/2016. Exceção 4: Esta regra de validação não se
        aplica nas operações isentas (CST=40-Isenta ou CSOSN=103-Isento), imunes ou não
        tributadas (CST=41- Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não
        tributada pelo Simples Nacional) (NT 2015.003)
        Erro: 805: Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de
        Inscrição Estadual
        """
        if not self._is_nfe():
            return None
        # TODO: UF-specific tables needed (internal operations)
        return None

    def validation_obrig_rej_696_e16a_40(self) -> ValidationResult:
        """E16a-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado indicador de IE do Destinatário não-contribuinte
        (tag: indIEDest=9) e não é operação com consumidor final (tag: indFinal<>1) em
        operação de saída (tag: tpNF=1) que não é com exterior (tag:idDest<>3). (NT
        2019.001 v1.00)
        Erro: 696: Rejeição: Operação com não contribuinte deve indicar operação com
        consumidor final
        """
        if not self._is_nfe() or not self._ide or not self._dest:
            return None
        tpNF = _v(getattr(self._ide, "tpNF", None))
        idDest = _v(getattr(self._ide, "idDest", None))
        indFinal = _v(getattr(self._ide, "indFinal", None))
        if tpNF != "1" or idDest == "3":
            return None
        indIEDest = _v(getattr(self._dest, "indIEDest", None))
        if indIEDest == "9" and indFinal != "1":
            return self._err(
                "E16a-40",
                696,
                "Rej.",
                "Rejeição: Operação com não contribuinte deve indicar operação com consumidor final",
                "dest/indIEDest",
            )
        return None

    def validation_obrig_rej_729_e17_10(self) -> ValidationResult:
        """E17-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Se operação com Exterior (tag:idDest=3): NFC-e com tag IE do
        Destinatário (tag:dest/IE)
        Erro: 729: Rejeição: NFC-e com informação da IE do destinatário
        """
        if not self._is_nfce():
            return None
        if self._dest and getattr(self._dest, "IE", None):
            return self._err(
                "E17-10",
                729,
                "Rej.",
                "Rejeição: NFC-e com informação da IE do destinatário",
                "dest/IE",
            )
        return None

    def validation_obrig_rej_728_e17_20(self) -> ValidationResult:
        """E17-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com indicação de Destinatário Contribuinte do ICMS
        (tag:dest/indIEDest=1), sem informar a IE (tag:dest/IE)
        Erro: 728: Rejeição: NF-e sem informação da IE do destinatário
        """
        if not self._is_nfe():
            return None
        if self._dest:
            indIEDest = _v(getattr(self._dest, "indIEDest", None))
            ie = getattr(self._dest, "IE", None)
            if indIEDest == "1" and not ie:
                return self._err(
                    "E17-20",
                    728,
                    "Rej.",
                    "Rejeição: NF-e sem informação da IE do destinatário",
                    "dest/IE",
                )
        return None

    def validation_obrig_rej_791_e17_30(self) -> ValidationResult:
        """E17-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e com indicação de Destinatário Contribuinte Isento de IE
        (tag:dest/indIEDest=2), mas com informação da IE (tag:dest/IE)
        Erro: 791: Rejeição: NF-e com indicação de destinatário isento de IE, com a
        informação da IE do destinatário
        """
        if not self._is_nfe():
            return None
        if self._dest:
            indIEDest = _v(getattr(self._dest, "indIEDest", None))
            ie = getattr(self._dest, "IE", None)
            if indIEDest == "2" and ie:
                return self._err(
                    "E17-30",
                    791,
                    "Rej.",
                    "Rejeição: NF-e com indicação de destinatário isento de IE, com a informação da IE do destinatário",
                    "dest/IE",
                )
        return None

    def validation_obrig_rej_792_e17_40(self) -> ValidationResult:
        """E17-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Destinatário: - Não informar a IE do
        Destinatário se endereço do Destinatário no Exterior
        (tag:dest/enderDest/UF=”EX”)
        Erro: 792: Rejeição: Informada a IE do destinatário para operação com
        destinatário no Exterior
        """
        if not self._is_nfe():
            return None
        if not self._dest:
            return None
        ie = getattr(self._dest, "IE", None)
        if not ie:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if ender and _v(getattr(ender, "UF", None)) == "EX":
            return self._err(
                "E17-40",
                792,
                "Rej.",
                "Rejeição: Informada a IE do destinatário para operação com destinatário no Exterior",
                "dest/IE",
            )
        return None

    def validation_obrig_rej_210_e17_50(self) -> ValidationResult:
        """E17-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Destinatário: - IE inválida para a UF:
        erro no tamanho, na composição da IE, ou no dígito verificador (*2)
        Erro: 210: Rejeição: IE do destinatário inválida
        """
        if not self._is_nfe():
            return None
        # Stub: requires IE validation per UF (external table)
        return None

    def validation_obrig_rej_730_e18_10(self) -> ValidationResult:
        """E18-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Inscrição da Suframa (tag:dest/ISUF)
        Erro: 730: Rejeição: NFC-e com Inscrição Suframa
        """
        if not self._is_nfce():
            return None
        if self._dest and getattr(self._dest, "ISUF", None):
            return self._err(
                "E18-10",
                730,
                "Rej.",
                "Rejeição: NFC-e com Inscrição Suframa",
                "dest/ISUF",
            )
        return None

    def validation_obrig_rej_235_e18_20(self) -> ValidationResult:
        """E18-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Inscrição SUFRAMA informada: - Inscrição com dígito
        verificador inválido
        Erro: 235: Rejeição: Inscrição SUFRAMA inválida
        """
        if not self._dest:
            return None
        isuf = getattr(self._dest, "ISUF", None)
        if isuf and not validate_suframa(isuf):
            return self._err(
                "E18-20",
                235,
                "Rej.",
                "Rejeição: Inscrição SUFRAMA inválida",
                "dest/ISUF",
            )
        return None

    def validation_obrig_rej_251_e18_30(self) -> ValidationResult:
        """E18-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Inscrição SUFRAMA informada: - UF destinatário difere de
        AC-Acre, ou AM-Amazonas, ou RO-Rondônia, ou RR-Roraima, ou AP-Amapá (só para
        municípios 1600303-Macapá e 1600600- Santana)
        Erro: 251: Rejeição: UF/Município destinatário não pertence a SUFRAMA
        """
        if not self._dest:
            return None
        isuf = getattr(self._dest, "ISUF", None)
        if not isuf:
            return None
        ender = getattr(self._dest, "enderDest", None)
        if ender:
            uf = _v(getattr(ender, "UF", None)) or ""
            cmun = _v(getattr(ender, "cMun", None)) or ""
            if not validate_suframa_uf(uf, cmun):
                return self._err(
                    "E18-30",
                    251,
                    "Rej.",
                    "Rejeição: UF/Município destinatário não pertence a SUFRAMA",
                    "dest/ISUF",
                )
        return None

    # ============================================================
    # Group F
    # ============================================================

    def validation_facul_rej_512_f02_10(self) -> ValidationResult:
        """F02-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado Local de Retirada com CNPJ: - CNPJ com zeros ou
        dígito inválido
        Erro: 512: Rejeição: CNPJ do Local de Retirada inválido
        """
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        cnpj = getattr(retirada, "CNPJ", None)
        if cnpj and not validate_cnpj(cnpj):
            return self._err(
                "F02-10",
                512,
                "Rej.",
                "Rejeição: CNPJ do Local de Retirada inválido",
                "retirada/CNPJ",
            )
        return None

    def validation_facul_rej_540_f02a_10(self) -> ValidationResult:
        """F02a-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado Local de Retirada com CPF: - CPF com zeros,
        nulo, 111..., 222..., ..., ou dígito de controle inválido (NT 2012/003)
        Erro: 540: Rejeição: CPF do Local de Retirada inválido
        """
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        cpf = getattr(retirada, "CPF", None)
        if cpf and not validate_cpf(cpf):
            return self._err(
                "F02a-10",
                540,
                "Rej.",
                "Rejeição: CPF do Local de Retirada inválido",
                "retirada/CPF",
            )
        return None

    def validation_obrig_rej_513_f07_10(self) -> ValidationResult:
        """F07-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Local de Retirada com UF Retirada = “EX”: -
        Código do Município do Local de Retirada difere de “9999999”
        Erro: 513: Rejeição: Código Município do Local de Retirada deve ser 9999999 para
        UF retirada = “EX”.
        """
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        uf = _v(getattr(retirada, "UF", None))
        cmun = _v(getattr(retirada, "cMun", None)) or ""
        if uf == "EX" and cmun != "9999999":
            return self._err(
                "F07-10",
                513,
                "Rej.",
                "Rejeição: cMun do Local de Retirada no exterior inválido",
                "retirada/cMun",
            )
        return None

    def validation_obrig_rej_276_f07_20(self) -> ValidationResult:
        """F07-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Local de Retirada com UF Retirada <> “EX”: -
        Código do Município do Local de Retirada inexistente (Tabela Municípios IBGE)
        (NT 2015.002)
        Erro: 276: Rejeição: Código Município do Local de Retirada inexistente
        """
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        uf = _v(getattr(retirada, "UF", None))
        cmun = _v(getattr(retirada, "cMun", None)) or ""
        if uf and uf != "EX" and not validate_municipality_code(cmun):
            return self._err(
                "F07-20",
                276,
                "Rej.",
                "Rejeição: cMun do Local de Retirada inexistente",
                "retirada/cMun",
            )
        return None

    def validation_obrig_rej_277_f07_30(self) -> ValidationResult:
        """F07-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Local de Retirada com UF Retirada <> “EX”: -
        Código Município do Local de Retirada (2 primeiras posições) difere do Código da
        UF do Local de Retirada
        Erro: 277: Rejeição: Código Município do Local de Retirada: difere da UF do
        Local de Retirada
        """
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        uf = _v(getattr(retirada, "UF", None))
        cmun = _v(getattr(retirada, "cMun", None)) or ""
        if uf and uf != "EX" and cmun and not municipality_matches_uf(cmun, uf):
            return self._err(
                "F07-30",
                277,
                "Rej.",
                "Rejeição: cMun do Local de Retirada incompatível com UF",
                "retirada/cMun",
            )
        return None

    def validation_obrig_rej_970_f11_10(self) -> ValidationResult:
        """F11-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Código País do local de retirada (tag:
        retirada/cPais): - Código do País inexistente (Tabela do BACEN, vide tabela de
        apoio publicada no Portal da NF-e). Observação: O Código do País pode conter
        zeros não significativos. (NT2018.005)
        Erro: 970: Rejeição: Código de País inexistente [local de retirada/entrega]
        """
        if not self._is_nfe():
            return None
        retirada = getattr(self._inf, "retirada", None) if self._inf else None
        if not retirada:
            return None
        cpais = _v(getattr(retirada, "cPais", None)) or ""
        if cpais and not validate_country_code(cpais):
            return self._err(
                "F11-10",
                970,
                "Rej.",
                "Rejeição: Código do País do local de retirada inexistente",
                "retirada/cPais",
            )
        return None

    def validation_obrig_rej_971_f15_10(self) -> ValidationResult:
        """F15-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Expedidor: - IE inválida para a UF do
        Expedidor (id: F09): erro no tamanho, na composição da IE, ou no dígito
        verificador (NT2018.005)
        Erro: 971: Rejeição: IE inválida [local de retirada/entrega]
        """
        if not self._is_nfe():
            return None
        # TODO: IE validation per UF requires external table
        return None

    # ============================================================
    # Group G
    # ============================================================

    def validation_facul_rej_514_g02_10(self) -> ValidationResult:
        """G02-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado o Local de Entrega com CNPJ: - CNPJ com zeros
        ou dígito inválido
        Erro: 514: Rejeição: CNPJ do Local de Entrega inválido
        """
        entrega = getattr(self._inf, "entrega", None) if self._inf else None
        if not entrega:
            return None
        cnpj = getattr(entrega, "CNPJ", None)
        if cnpj and not validate_cnpj(cnpj):
            return self._err(
                "G02-10",
                514,
                "Rej.",
                "Rejeição: CNPJ do Local de Entrega inválido",
                "entrega/CNPJ",
            )
        return None

    def validation_facul_rej_541_g02a_10(self) -> ValidationResult:
        """G02a-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado o Local de Entrega com CPF: - CPF com zeros,
        nulo, 111..., 222..., ..., ou dígito de controle inválido (NT 2012/003)
        Erro: 541: Rejeição: CPF do Local de Entrega inválido
        """
        entrega = getattr(self._inf, "entrega", None) if self._inf else None
        if not entrega:
            return None
        cpf = getattr(entrega, "CPF", None)
        if cpf and not validate_cpf(cpf):
            return self._err(
                "G02a-10",
                541,
                "Rej.",
                "Rejeição: CPF do Local de Entrega inválido",
                "entrega/CPF",
            )
        return None

    def validation_obrig_rej_278_g07_20(self) -> ValidationResult:
        """G07-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Local de Entrega com UF Entrega <> “EX”: -
        Código Município do Local de Entrega inexistente (Tabela Municípios IBGE) (NT
        2015.002)
        Erro: 278: Rejeição: Código Município do Local de Entrega inexistente
        """
        entrega = getattr(self._inf, "entrega", None) if self._inf else None
        if not entrega:
            return None
        uf = _v(getattr(entrega, "UF", None))
        cmun = _v(getattr(entrega, "cMun", None)) or ""
        if uf and uf != "EX" and not validate_municipality_code(cmun):
            return self._err(
                "G07-20",
                278,
                "Rej.",
                "Rejeição: cMun do Local de Entrega inexistente",
                "entrega/cMun",
            )
        return None

    def validation_obrig_rej_279_g07_30(self) -> ValidationResult:
        """G07-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Local de Entrega com UF Entrega <> “EX”: -
        Código Município do Local de Entrega (2 primeiras posições) difere do Código da
        UF do Local de Entrega
        Erro: 279: Rejeição: Código Município do Local de Entrega: difere da UF do Local
        de Entrega
        """
        entrega = getattr(self._inf, "entrega", None) if self._inf else None
        if not entrega:
            return None
        uf = _v(getattr(entrega, "UF", None))
        cmun = _v(getattr(entrega, "cMun", None)) or ""
        if uf and uf != "EX" and cmun and not municipality_matches_uf(cmun, uf):
            return self._err(
                "G07-30",
                279,
                "Rej.",
                "Rejeição: cMun do Local de Entrega incompatível com UF",
                "entrega/cMun",
            )
        return None

    def validation_obrig_rej_970_g11_10(self) -> ValidationResult:
        """G11-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Código País do local de retirada (tag:
        entrega/cPais): - Código do País inexistente (Tabela do BACEN, vide tabela de
        apoio publicada no Portal da NF-e). Observação: O Código do País pode conter
        zeros não significativos. (NT 2018.005)
        Erro: 970: Rejeição: Código de País inexistente [local de retirada/entrega]
        """
        if not self._is_nfe():
            return None
        entrega = getattr(self._inf, "entrega", None) if self._inf else None
        if not entrega:
            return None
        cpais = _v(getattr(entrega, "cPais", None)) or ""
        if cpais and not validate_country_code(cpais):
            return self._err(
                "G11-10",
                970,
                "Rej.",
                "Rejeição: Código do País do local de entrega inexistente",
                "entrega/cPais",
            )
        return None

    def validation_obrig_rej_971_g15_10(self) -> ValidationResult:
        """G15-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Recebedor: - IE inválida para a UF do
        Recebedor (id: G09): erro no tamanho, na composição da IE, ou no dígito
        verificador (NT 2018.005)
        Erro: 971: Rejeição: IE inválida [local de retirada/entrega]
        """
        if not self._is_nfe():
            return None
        # TODO: IE validation per UF requires external table
        return None

    # ============================================================
    # Group GA
    # ============================================================

    def validation_obrig_rej_323_ga02_10(self) -> ValidationResult:
        """GA02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada autorização download XML com CNPJ: - CNPJ com
        zeros ou dígito inválido
        Erro: 323: Rejeição: CNPJ autorizado para download inválido
        """
        aut_list = getattr(self._inf, "autXML", None) or []
        for aut in aut_list:
            cnpj = getattr(aut, "CNPJ", None)
            if cnpj and not validate_cnpj(cnpj):
                return self._err(
                    "GA02-10",
                    323,
                    "Rej.",
                    "Rejeição: CNPJ de Autorização de Download inválido",
                    "autXML/CNPJ",
                )
        return None

    def validation_obrig_rej_324_ga02_20(self) -> ValidationResult:
        """GA02-20.

        Modelo: 55/65
        Aplicação: Obirg.
        Regra de Validação: Se informada autorização download XML com CNPJ: - Informado
        CNPJ do destinatário
        Erro: 324: Rejeição: CNPJ do destinatário já autorizado para download
        """
        if not self._dest:
            return None
        dest_cnpj = getattr(self._dest, "CNPJ", None)
        if not dest_cnpj:
            return None
        aut_list = getattr(self._inf, "autXML", None) or []
        for aut in aut_list:
            cnpj = getattr(aut, "CNPJ", None)
            if cnpj and cnpj == dest_cnpj:
                return self._err(
                    "GA02-20",
                    324,
                    "Rej.",
                    "Rejeição: CNPJ de Autorização igual ao do Destinatário",
                    "autXML/CNPJ",
                )
        return None

    def validation_obrig_rej_325_ga03_10(self) -> ValidationResult:
        """GA03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada autorização download do XML com CPF: - CPF com
        zeros, nulo, 111..., 222..., ..., ou dígito de controle inválido
        Erro: 325: Rejeição: CPF autorizado para download inválido
        """
        aut_list = getattr(self._inf, "autXML", None) or []
        for aut in aut_list:
            cpf = getattr(aut, "CPF", None)
            if cpf and not validate_cpf(cpf):
                return self._err(
                    "GA03-10",
                    325,
                    "Rej.",
                    "Rejeição: CPF de Autorização de Download inválido",
                    "autXML/CPF",
                )
        return None

    def validation_obrig_rej_326_ga03_20(self) -> ValidationResult:
        """GA03-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada autorização download do XML com CPF: -
        Informado CPF do destinatário
        Erro: 326: Rejeição: CPF do destinatário já autorizado para download
        """
        if not self._dest:
            return None
        dest_cpf = getattr(self._dest, "CPF", None)
        if not dest_cpf:
            return None
        aut_list = getattr(self._inf, "autXML", None) or []
        for aut in aut_list:
            cpf = getattr(aut, "CPF", None)
            if cpf and cpf == dest_cpf:
                return self._err(
                    "GA03-20",
                    326,
                    "Rej.",
                    "Rejeição: CPF de Autorização igual ao do Destinatário",
                    "autXML/CPF",
                )
        return None

    # ============================================================
    # Group H
    # ============================================================

    def validation_obrig_rej_927_h02_10(self) -> ValidationResult:
        """H02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Número sequencial do item no arquivo XML “nItem” fora de
        ordem incremental, consecutiva, a partir de 1. Observação: Regra de validação
        opcional, a critério da UF (NT 2019.001)
        Erro: 927: Rejeição: Número do item fora da ordem sequencial.
        """
        for i, item in enumerate(self._det, start=1):
            nitem = getattr(item, "nItem", None)
            if nitem is not None and str(nitem) != str(i):
                return self._err(
                    "H02-10",
                    927,
                    "Rej.",
                    "Rejeição: nItem fora de ordem sequencial",
                    "det/nItem",
                    i,
                )
        return None

    # ============================================================
    # Group I
    # ============================================================

    def validation_obrig_rej_611_i03_10(self) -> ValidationResult:
        """I03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN (tag: cEAN) <> “SEM GTIN” ou Nulo): - cEAN
        com dígito de controle inválido Observação: Cálculo do dígito verificador em
        www.gs1.org/check-digit- calculator. (NT 2017.001)
        Erro: 611: Rejeição: GTIN (cEAN) inválido [nItem:999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean = getattr(prod, "cEAN", None)
            if cean and cean not in ("SEM GTIN",) and not validate_gtin(str(cean)):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I03-10",
                        611,
                        "Rej.",
                        "Rejeição: cEAN com dígito de controle inválido",
                        "det/prod/cEAN",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_882_i03_20(self) -> ValidationResult:
        """I03-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN (tag: cEAN) <> “SEM GTIN” ou Nulo): -
        Prefixo GS1 inválido, conforme tabela de prefixos publicada no Portal da NF- e
        Observação: Validação efetuada conforme prefixos e orientações constantes na
        “Tabela Prefixo GS1” publicada no Portal Nacional da NF-e. (NT 2017.001)
        Erro: 882: Rejeição: GTIN (cEAN) com prefixo inválido [nItem:999]
        """
        # Stub: full GS1 prefix validation requires the official NF-e portal prefix table
        return None

    def validation_obrig_rej_883_i03_30(self) -> ValidationResult:
        """I03-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: GTIN (tag: cEAN) em branco, campo sem informação. Observação
        1: Para produtos que não possuem GTIN, utilizar a informação de "SEM GTIN" (NT
        2017.001)
        Erro: 883: Rejeição: GTIN (cEAN) sem informação [nItem: 999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean = getattr(prod, "cEAN", None)
            if cean == "":
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I03-30",
                        883,
                        "Rej.",
                        "Rejeição: cEAN em branco; usar 'SEM GTIN' quando não há GTIN",
                        "det/prod/cEAN",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_373_i04_10(self) -> ValidationResult:
        """I04-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Para a NFC-e, se ambiente de homologação (tag:tpAmb=2,
        id:B24): - Descrição do primeiro item da Nota Fiscal (tag:xProd) deve ser
        informada como “NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR
        FISCAL” (NT 2015.002)
        Erro: 373: Rejeição: Descrição do primeiro item diferente de NOTA FISCAL EMITIDA
        EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL [nItem:nnn]
        """
        if not self._is_nfce() or not self._ide:
            return None
        tpAmb = _v(getattr(self._ide, "tpAmb", None))
        if tpAmb != "2":
            return None
        if not self._det:
            return None
        first_item = self._det[0]
        prod = getattr(first_item, "prod", None)
        if not prod:
            return None
        xprod = _v(getattr(prod, "xProd", None)) or ""
        expected = "NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
        if xprod != expected:
            nitem = int(getattr(first_item, "nItem", 0))
            return self._err(
                "I04-10",
                373,
                "Rej.",
                "Rejeição: NFC-e em homologação com descrição do 1º item incorreta",
                "det/prod/xProd",
                nitem,
            )
        return None

    def validation_obrig_rej_777_i05_10(self) -> ValidationResult:
        """I05-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informar o NCM completo (8 posições) Exceção: no caso de
        item de Serviço ou item que não tenha produto (ex. transferência de crédito,
        crédito do ativo imobilizado, etc.), informar o valor “00” (zeros). (NT 2013/005
        v 1.10) Observação 1: o início de aplicabilidade desta regra obedece a
        cronograma disposto no Ajuste Sinief 07/05. (NT 2013/005 v 1.10) Observação 2:
        no caso de mercadorias que não possuem uma classificação exatamente igual à
        descrita na tabela do MDIC, deve ser seguida a orientação daquele Ministério:
        “As mercadorias que não possam ser classificadas por aplicação das [...]
        classificam-se na posição correspondente aos artigos mais semelhantes.” (NT
        2013/005 v 1.10) Observação 3: em caso de não ser possível aplicar o disposto na
        observação 2, pelo fato de o item da nota se referir a operação impossível de
        ser classificada segundo a tabela do MDIC, deve ser Informado o código
        “00000000” (NT 2014/004)
        Erro: 777: Rejeição: Obrigatória a informação do NCM completo (redação dada pela
        NT 2013/005 v 1.20) [nItem: 999]
        """
        # TODO: implement validation logic for I05-10
        return None

    def validation_obrig_rej_778_i05_20(self) -> ValidationResult:
        """I05-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado NCM completo (8 pos.) e valor difere de
        “00000000”: - NCM inexistente na tabela de NCM publicada pelo Ministério do
        Desenvolvimento, Indústria e Comércio Exterior - MDIC Exceção 1: A regra de
        validação não se aplica, em produção, para Nota Fiscal com Data de Emissão
        anterior a 01/01/2016. Exceção 2: Para a NF-e, considerar nesta validação os
        códigos de NCM especiais definidos pela RFB para permitir o uso no Registro de
        Exportação (Erro! Fonte de referência não encontrada.). (NT 2015.002)
        Erro: 778: Rejeição: Informado NCM inexistente[nItem:nnn]
        """
        # TODO: implement validation logic for I05-20
        return None

    def validation_obrig_rej_471_i05_24(self) -> ValidationResult:
        """I05-24.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado NCM = “00”: - Não é uma NF-e de Ajuste
        (tag:finfe <> 3) e não é um item de serviço (item não possui a tag:ISSQN)
        Observação: A UF autorizadora que aceitar o uso da NF-e modelo 55 para
        documentar prestações de serviços ocorridas dentro do campo de incidência do
        ICMS poderá definir outras exceções a esta regra. (NT 2014/004)
        Erro: 471: Rejeição: Informado NCM=00 indevidamente (NT 2014/004) [nItem: 999]
        """
        # TODO: implement validation logic for I05-24
        return None

    def validation_obrig_rej_779_i05_30(self) -> ValidationResult:
        """I05-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado NCM incompatível com a NFC-e
        Erro: 779: Rejeição: NFC-e com NCM incompatível [nItem: 999]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for I05-30
        return None

    def validation_obrig_rej_879_i05e_10(self) -> ValidationResult:
        """I05e-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado indEscala=”N- não relevante” (id: I05d), deve
        ser informado CNPJ do Fabricante da Mercadoria (id: I05e) (NT 2016.002)
        Erro: 879: Rejeição: Informado item “Produzido em Escala NÃO Relevante” e não
        informado CNPJ do Fabricante [nItem: 999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            ind_escala = _v(getattr(prod, "indEscala", None))
            if ind_escala == "N":
                cnpj_fab = getattr(prod, "CNPJFab", None)
                if not cnpj_fab:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "I05e-10",
                            879,
                            "Rej.",
                            "Rejeição: CNPJFab obrigatório para indEscala=N",
                            "det/prod/CNPJFab",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_489_i05e_20(self) -> ValidationResult:
        """I05e-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJFab (id: I05e) - CNPJ inválido (DV, zeros)
        (NT 2016.002)
        Erro: 489: Rejeição: CNPJ informado inválido (DV ou zeros) [nItem: 999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cnpj_fab = getattr(prod, "CNPJFab", None)
            if cnpj_fab and not validate_cnpj(str(cnpj_fab)):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I05e-20",
                        489,
                        "Rej.",
                        "Rejeição: CNPJ do Fabricante inválido",
                        "det/prod/CNPJFab",
                        nitem,
                    )
                )
        return errors or None

    def validation_facul_rej_928_i05f_10(self) -> ValidationResult:
        """I05f-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado código de benefício fiscal (tag: cBenef) para CST
        sem benefício fiscal (CST = 00, 10, 60), conforme Tabela de apoio publicada no
        Portal Nacional da NF-e Observação: Implementação a critério da UF, por CST e
        por modelo de DF-e. (NT 2019.001 v1.00, v1.50)
        Erro: 928: Rejeição: Informado código de benefício fiscal para CST sem benefício
        fiscal [nItem: nnn]
        """
        # TODO: implement validation logic for I05f-10
        return None

    def validation_facul_rej_931_i05f_20(self) -> ValidationResult:
        """I05f-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado código de benefício fiscal (tag: cBenef): -
        verificar se tipo de código do benefício corresponde ao CST com benefício
        fiscal. Exemplo: Código de benefício fiscal de isenção deve ser utilizado com
        CST de isenção. Observação 1: Implementação a critério da UF, por modelo de
        DF-e. Observação 2: Tabela de código de benefício fiscal por UF publicada no
        Portal Nacional da NF-e (NT 2019.001 v1.00, v1.50)
        Erro: 931: Rejeição: CST não corresponde ao tipo de código de benefício fiscal
        [nItem: nnn]
        """
        # TODO: implement validation logic for I05f-20
        return None

    def validation_facul_rej_934_i05f_30(self) -> ValidationResult:
        """I05f-30.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado código de benefício fiscal (tag: cBenef),
        Obrig.atório informar valor do ICMS desonerado (tag: vICMSDeson) e o motivo de
        desoneração (tag: motDesICMS) Observações: Implementação a critério da UF (NT
        2019.001 v1.00, v1.50)
        Erro: 934: Rejeição: Não informado valor do ICMS desonerado ou o Motivo de
        desoneração [nItem: nnn]
        """
        # TODO: implement validation logic for I05f-30
        return None

    def validation_obrig_rej_770_i08_04(self) -> ValidationResult:
        """I08-04.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: CFOP inexistente ou não pode ser usado na NF-e, conforme
        tabela de apoio publicada no Portal da NF-e (Tabela CFOP, indNFe=0) (NT
        2015.002)
        Erro: 770: Rejeição: CFOP Inexistente [nItem:nnn]
        """
        # TODO: implement validation logic for I08-04
        return None

    def validation_facul_rej_518_i08_10(self) -> ValidationResult:
        """I08-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Entrada (inicia por 1, 2, 3) para NF-e de Saída
        (tpNF=1)
        Erro: 518: Rejeição: CFOP de entrada para NF-e de saída
        """
        if not self._is_nfe():
            return None
        tp_nf = _v(getattr(self._ide, "tpNF", None))
        if tp_nf != "1":
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and is_cfop_entrada(cfop):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-10",
                        518,
                        "Rej.",
                        "Rejeição: CFOP de Entrada em NF-e de Saída",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_facul_rej_519_i08_20(self) -> ValidationResult:
        """I08-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Saída (inicia por 5, 6, 7) para NF-e de Entrada
        (tpNF=0)
        Erro: 519: Rejeição: CFOP de saída para NF-e de entrada
        """
        if not self._is_nfe():
            return None
        tp_nf = _v(getattr(self._ide, "tpNF", None))
        if tp_nf != "0":
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and is_cfop_saida(cfop):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-20",
                        519,
                        "Rej.",
                        "Rejeição: CFOP de Saída em NF-e de Entrada",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_731_i08_30(self) -> ValidationResult:
        """I08-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: CFOP de operação com Exterior (inicia por 3 ou 7) e idDest
        <> 3 Exceção: Se a tag UFCons (id:LA06) foi informada com ”EX” é válido CFOP
        iniciado por 7 e idDest <> 3 (NT 2013/005 v 1.10)
        Erro: 731: Rejeição: CFOP de operação com Exterior e idDest <> 3
        """
        if not self._is_nfe():
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and is_cfop_exterior(cfop) and id_dest != "3":
                # Exception: if UFCons is present (combustível), skip
                comb = (
                    getattr(getattr(item, "imposto", None), "comb", None)
                    if getattr(item, "imposto", None)
                    else None
                )
                if not comb or not getattr(comb, "UFCons", None):
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "I08-30",
                            731,
                            "Rej.",
                            "Rejeição: CFOP de Exterior com idDest diferente de 3",
                            "det/prod/CFOP",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_732_i08_40(self) -> ValidationResult:
        """I08-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: CFOP de operação interestadual (inicia por 2 ou 6) e idDest
        <> 2
        Erro: 732: Rejeição: CFOP de operação interestadual e idDest <> 2
        """
        if not self._is_nfe():
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and is_cfop_interestadual(cfop) and id_dest != "2":
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-40",
                        732,
                        "Rej.",
                        "Rejeição: CFOP Interestadual com idDest diferente de 2",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_733_i08_50(self) -> ValidationResult:
        """I08-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: CFOP de operação interna (inicia por 1 ou 5) e idDest <> 1
        Erro: 733: Rejeição: CFOP de operação interna e idDest <> 1
        """
        if not self._is_nfe():
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and is_cfop_interna(cfop) and id_dest != "1":
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-50",
                        733,
                        "Rej.",
                        "Rejeição: CFOP Interna com idDest diferente de 1",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_facul_rej_520_i08_60(self) -> ValidationResult:
        """I08-60.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de operação com Exterior (inicia por 3 ou 7) e UF
        Destinatário <> “EX” Exceção: Se a tag UFCons (id:LA06) foi informada com ”EX”:
        CFOP iniciado com 3 ou 7 é válido (NT 2010/007)
        Erro: 520: Rejeição: CFOP de Operação com Exterior e UF destinatário difere de
        “EX”
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-60
        return None

    def validation_facul_rej_521_i08_70(self) -> ValidationResult:
        """I08-70.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Operação Interna (idDest=1) e UF emitente diferente da UF do
        destinatário/remetente e destinatário/remetente contribuinte do ICMS
        (indIEDest=1) Exceção 1: A regra de validação não se aplica se a tag UFCons
        (id:LA06) foi informada com a mesma UF do emitente. (NT 2010/007) Exceção 2: A
        regra de validação não se aplica se a operação é presencial (tag: indPres=1
        -Operação presencial) e não possui frete (tag: modFrete=9 - Sem frete).(NT
        2011/004) Observação: No caso da NFC-e, a informação do endereço do destinatário
        é opcional. Considerar a UF do destinatário como sendo a mesma UF do emitente
        (operação interna). (NT 2015.002)
        Erro: 521: Rejeição: Operação Interna e UF do emitente difere da UF do
        destinatário/remetente contribuinte do ICMS
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-70
        return None

    def validation_facul_rej_523_i08_90(self) -> ValidationResult:
        """I08-90.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP é de operação interestadual (inicia por 2 ou 6) e UF
        emitente = UF destinatário e CNPJ/CPF emissor diferente do CNPJ/CPF destinatário
        (NT 2010/004) Exceção: Se a tag UFCons (id:LA06) foi informada com UF diversa do
        emitente: CFOP iniciado com 2 ou 6 é válido. (NT 2010/010)
        Erro: 523: Rejeição: CFOP não é de Operação Estadual e UF emitente igual à UF
        destinatário [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-90
        return None

    def validation_facul_rej_771_i08_94(self) -> ValidationResult:
        """I08-94.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Operação Interestadual (idDest=2) e informado idEstrangeiro
        Exceção: A regra acima não se aplica para o CFOP=”6.667- Venda de combustível ou
        lubrificante a consumidor ou usuário final estabelecido em outra UF diferente da
        que ocorrer o consumo” (NT 2015.002)
        Erro: 771: Rejeição: Informado idEstrangeiro em operação interestadual
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-94
        return None

    def validation_facul_rej_525_i08_110(self) -> ValidationResult:
        """I08-110.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Importação (inicia por 3) e não informado a tag DI
        Exceção: a regra não se aplica para os seguintes CFOP: 3.201; 3.202; 3.503;
        3.553 (NT 2010/007)
        Erro: 525: Rejeição: CFOP de Importação e não informado dados da DI [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-110
        return None

    def validation_facul_rej_597_i08_120(self) -> ValidationResult:
        """I08-120.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Importação (inicia por 3) e não informado o grupo de
        IPI Exceção: a regra não se aplica para os seguintes CFOP: 3.201; 3.202; 3.211;
        3.503; 3.553 (NT 2011/004, NT 2020.002 v1.00)
        Erro: 597: Rejeição: CFOP de Importação e não informado dados de IPI
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-120
        return None

    def validation_facul_rej_599_i08_130(self) -> ValidationResult:
        """I08-130.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Importação (inicia por 3) e não informado o grupo de
        II Exceção: a regra não se aplica para os seguintes CFOP: 3.201; 3.202; 3.211;
        3.503; 3.553 (NT 2011/004)
        Erro: 599: Rejeição: CFOP de Importação e não informado dados de II [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-130
        return None

    def validation_obrig_rej_327_i08_140(self) -> ValidationResult:
        """I08-140.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Para as NF-e com finalidade de devolução de mercadoria
        (tag:finNFe=4), somente serão aceitos CFOP de devolução de mercadoria.
        Observação: Vide relação de CFOP de devolução de mercadoria natabela de apoio
        publicada no Portal da NF-e (Tabela CFOP, indDevol=1). Exceção: Aceitar os CFOP
        1.949 e 2.949 na devolução de venda para não Contribuinte. Para estes CFOP
        verificar a condição: - tag:finNFe = 4 (devolução) e tag:indIEDest = 9 (não
        Contribuinte) (NT 2015.002)
        Erro: 327: Rejeição: CFOP inválido para Nota Fiscal com finalidade de devolução
        de mercadoria[nItem:nnn]
        """
        if not self._is_nfe():
            return None
        fin_nfe = _v(getattr(self._ide, "finNFe", None))
        if fin_nfe != "4":
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in CFOP_DEVOLUTION:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-140",
                        327,
                        "Rej.",
                        "Rejeição: CFOP inválido para NF-e de devolução",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_328_i08_144(self) -> ValidationResult:
        """I08-144.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Para as NF-e que não tem a finalidade de devolução de
        mercadoria (tag:finNFe não é “2” nem “4”), não serão aceitos CFOP de devolução
        de mercadoria. (NT 2013/005) Observação: Vide relação de CFOP de devolução de
        mercadoria natabela de apoio publicada no Portal da NF-e (Tabela CFOP,
        indDevol=1). (NT 2015.002)
        Erro: 328: Rejeição: CFOP de devolução de mercadoria para NF-e que não tem
        finalidade de devolução de mercadoria [nItem:nnn]
        """
        if not self._is_nfe():
            return None
        fin_nfe = _v(getattr(self._ide, "finNFe", None))
        if fin_nfe in ("2", "4"):
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop in CFOP_DEVOLUTION:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-144",
                        328,
                        "Rej.",
                        "Rejeição: CFOP de devolução em NF-e sem finalidade de devolução",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_725_i08_150(self) -> ValidationResult:
        """I08-150.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e (mod=65) com CFOP inválido. Aceitar unicamente os
        CFOP: - 5.101: Venda de produção do estabelecimento; - 5.102: Venda de
        mercadoria de terceiros; - 5.103: Venda de produção do estabelecimento efetuada
        fora do estabelecimento; - 5.104: Venda de mercadoria adquirida ou recebida de
        terceiros, efetuada fora do estabelecimento; - 5.115: Venda de mercadoria de
        terceiros, recebida anteriormente em consignação mercantil; - 5.405: Venda de
        mercadoria de terceiros, sujeita a ST, como contribuinte substituído; - 5.656:
        Venda de combustível ou lubrificante de terceiros, destinados a consumidor
        final; - 5.667: Venda de combustível ou lubrificante a consumidor ou usuário
        final estabelecido em outra Unidade da Federação; - 5.933: Prestação de serviço
        tributado pelo ISSQN (Nota Fiscal conjugada); (NT 2013/005 v 1.20) (NT 2015.002)
        Erro: 725: Rejeição: NFC-e com CFOP inválido[nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in NFCE_VALID_CFOPS:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I08-150",
                        725,
                        "Rej.",
                        "Rejeição: CFOP inválido para NFC-e",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_374_i08_160(self) -> ValidationResult:
        """I08-160.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e (mod=65) com CFOP=5.933 (Prestação de serviço), sem o
        grupo de tributação pelo ISSQN (tag:imposto/ISSQN) (NT 2015.002)
        Erro: 374: Rejeição: CFOP incompatível com o grupo de tributação [nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop == "5933":
                imposto = getattr(item, "imposto", None)
                issqn = getattr(imposto, "ISSQN", None) if imposto else None
                if not issqn:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "I08-160",
                            374,
                            "Rej.",
                            "Rejeição: NFC-e CFOP=5933 sem grupo ISSQN",
                            "det/imposto/ISSQN",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_374_i08_170(self) -> ValidationResult:
        """I08-170.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e (mod=65) com CFOP diferente de 5.933 (Prestação de
        serviço), com o grupo de tributação pelo ISSQN (tag:imposto/ISSQN) (NT 2015.002)
        Erro: 374: Rejeição: CFOP incompatível com o grupo de tributação [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop != "5933":
                imposto = getattr(item, "imposto", None)
                issqn = getattr(imposto, "ISSQN", None) if imposto else None
                if issqn:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "I08-170",
                            374,
                            "Rej.",
                            "Rejeição: NFC-e com grupo ISSQN para CFOP diferente de 5933",
                            "det/imposto/ISSQN",
                            nitem,
                        )
                    )
        return errors or None

    def validation_facul_rej_375_i08_180(self) -> ValidationResult:
        """I08-180.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: NF-e (mod=55) com lançamento relativo a Cupom Fiscal
        (CFOP=5.929) e existe NFC-e referenciada (tag:refNFe com modelo 65) Observação:
        Regra de Validação opcional, a critério da UF poderá ser aceito o CFOP 5.929.
        (NT 2015.002)
        Erro: 375: Rejeição: NF-e com lançamento relativo a Cupom Fiscal referencia uma
        NFC-e [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-180
        return None

    def validation_obrig_rej_701_i08_184(self) -> ValidationResult:
        """I08-184.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e (mod=55) com lançamento relativo a Cupom Fiscal
        (CFOP=5.929ou CFOP6.929) sem Documento Fiscal referenciado (tag:NFref, idBA01)
        (NT 2015.002)
        Erro: 701: Rejeição: Não informado Nota Fiscal referenciada (Lançamento relativo
        a Cupom Fiscal) [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-184
        return None

    def validation_obrig_rej_701_i08_190(self) -> ValidationResult:
        """I08-190.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e (mod=55) com CFOP de exportação indireta (3503, 7501)
        sem Nota Fiscal referenciada (tag:NFref, id:BA01) (NT 2015.002)
        Erro: 701: Rejeição: Não informado Nota Fiscal referenciada (CFOP de Exportação
        Indireta) [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I08-190
        return None

    def validation_obrig_rej_734_i09_10(self) -> ValidationResult:
        """I09-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Unidade de Comercialização inválida (tag:uCom não
        consta de tabela específica)
        Erro: 734: Rejeição: NFC-e com Unidade de Comercialização inválida [nItem: 999]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for I09-10
        return None

    def validation_facul_rej_629_i11_10(self) -> ValidationResult:
        """I11-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se NF-e Normal (tag:finNFe=1): - vProd (id:I11) difere de
        vUnCom (id:I10a) * qCom (id:I10) (*4) (NT 2011/005)
        Erro: 629: Rejeição: Valor do Produto difere do produto Valor Unitário de
        Comercialização e Quantidade Comercial [nItem: 999]
        """
        # TODO: implement validation logic for I11-10
        return None

    def validation_facul_rej_630_i11_20(self) -> ValidationResult:
        """I11-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se NF-e Normal (tag:finNFe=1): - vProd (id:I11) difere de
        vUnTrib (id:I14a) * qTrib (id:I14) (*4) (NT 2011/005)
        Erro: 630: Rejeição: Valor do Produto difere do produto Valor Unitário de
        Tributação e Quantidade Tributável [nItem: 999]
        """
        # TODO: implement validation logic for I11-20
        return None

    def validation_obrig_rej_612_i12_10(self) -> ValidationResult:
        """I12-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN da unidade tributável (tag: cEANTrib) <>
        “SEM GTIN” ou Nulo): - cEANTrib com dígito de controle inválido Observação:
        Cálculo do dígito verificador em www.gs1.org/check-digit- calculator (NT
        2017.001)
        Erro: 612: Rejeição: GTIN da unidade tributável (cEANTrib) inválido [nItem:999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean_trib = getattr(prod, "cEANTrib", None)
            if (
                cean_trib
                and cean_trib not in ("SEM GTIN",)
                and not validate_gtin(str(cean_trib))
            ):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I12-10",
                        612,
                        "Rej.",
                        "Rejeição: cEANTrib com dígito de controle inválido",
                        "det/prod/cEANTrib",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_884_i12_20(self) -> ValidationResult:
        """I12-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN da unidade tributável (tag: cEANTrib) <>
        “SEM GTIN” ou Nulo): - Prefixo GS1 inválido, conforme tabela de prefixos
        publicada no Portal da NF- e Observação: Validação efetuada conforme prefixos e
        orientações constantes na “Tabela Prefixo GS1” publicada no Portal Nacional da
        NF-e. (NT 2017.001)
        Erro: 884: Rejeição: GTIN da unidade tributável (cEANTrib) com prefixo inválido
        [nItem:999]
        """
        # Stub: full GS1 prefix validation requires the official NF-e portal prefix table
        return None

    def validation_obrig_rej_885_i12_30(self) -> ValidationResult:
        """I12-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado GTIN específico (cEAN<>“SEM GTIN” ou Nulo) e
        informado GTIN da unidade tributável igual a "SEM GTIN" ou Nulo (cEANTrib=“SEM
        GTIN” ou Nulo) (NT 2017.001)
        Erro: 885: Rejeição: GTIN informado, mas não informado o GTIN da unidade
        tributável [nItem:999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean = getattr(prod, "cEAN", None)
            cean_trib = getattr(prod, "cEANTrib", None)
            if (
                cean
                and cean not in ("SEM GTIN",)
                and cean_trib
                and cean_trib not in ("SEM GTIN",)
                and cean == cean_trib
            ):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I12-30",
                        885,
                        "Rej.",
                        "Rejeição: cEAN e cEANTrib não podem ser iguais quando específicos",
                        "det/prod/cEANTrib",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_886_i12_40(self) -> ValidationResult:
        """I12-40.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado GTIN da unidade tributável específico
        (cEANTrib<>“SEM GTIN” ou Nulo) e informado GTIN igual a "SEM GTIN" ou Nulo
        (cEAN=“SEM GTIN” ou Nulo) (NT 2017.001)
        Erro: 886: Rejeição: GTIN da unidade tributável informado, mas não informado o
        GTIN [nItem:999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean = getattr(prod, "cEAN", None)
            cean_trib = getattr(prod, "cEANTrib", None)
            if (
                cean_trib
                and cean_trib not in ("SEM GTIN",)
                and (not cean or cean == "SEM GTIN")
            ):
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I12-40",
                        886,
                        "Rej.",
                        "Rejeição: cEANTrib específico mas cEAN é SEM GTIN",
                        "det/prod/cEANTrib",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_888_i12_60(self) -> ValidationResult:
        """I12-60.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: GTIN da unidade tributável (tag: cEANTrib) em branco, campo
        sem informação. Observação Para produtos que não possuem GTIN da unidade
        tributável, utilizar a informação de "SEM GTIN". (NT 2017.001)
        Erro: 888: Rejeição: GTIN da unidade tributável (cEANTrib) sem informação
        [nItem:999]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cean_trib = getattr(prod, "cEANTrib", None)
            if cean_trib == "":
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I12-60",
                        888,
                        "Rej.",
                        "Rejeição: cEANTrib em branco; usar 'SEM GTIN' quando não há GTIN",
                        "det/prod/cEANTrib",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_735_i13_10(self) -> ValidationResult:
        """I13-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Unidade de Tributação inválida (tag:uTrib não
        consta da tabela específica) Observação: Implementação Futura
        Erro: 735: Rejeição: NFC-e com Unidade de Tributação inválida [nItem: 999]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for I13-10
        return None

    def validation_obrig_rej_854_i13_20(self) -> ValidationResult:
        """I13-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado campo cProdANP (id: LA02) = 210203001 (GLP) e
        campo uTrib (id: I13) <> “kg” (ignorar a diferenciação entre maiúsculas e
        minúsculas) (NT 2016.002)
        Erro: 854: Rejeição: Unidade Tributável (tag:uTrib) incompatível com produto
        informado [nItem: 999]
        """
        # TODO: implement validation logic for I13-20
        return None

    def validation_obrig_rej_817_i14_10(self) -> ValidationResult:
        """I14-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Validar a correspondência entre o código NCM e a unidade
        tributável (tag: uTrib) nas operações com o Comércio Exterior, conforme segue: -
        Operação de Exportação (tpNF=1-Saída e idDest=3); ou - Operações vinculadas a
        exportação, CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505
        Observação: Tabela de Unidades Tributáveis no Comércio Exterior publicada na aba
        “Documentos”, opção “Diversos” do Portal Nacional da NF-e
        (www.nfe.fazenda.gov.br) Nota: O uso diferenciado de maiúsculas ou minúsculas
        não deve ser considerado na validação. (NT 2016.001)
        Erro: 817: Rejeição: Unidade Tributável incompatível com o NCM informado na
        operação com Comércio Exterior [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I14-10
        return None

    def validation_obrig_rej_483_i17_10(self) -> ValidationResult:
        """I17-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Valor do Desconto (tag:vDesc, id:I17) maior que o valor do
        Produto (tag:vProd, id:I11) (NT 2015.002)
        Erro: 483: Rejeição: Valor do desconto maior que valor do produto [nItem: nnn]
        """
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            v_prod = safe_decimal(getattr(prod, "vProd", None))
            v_desc = safe_decimal(getattr(prod, "vDesc", None))
            if v_desc > v_prod:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I17-10",
                        483,
                        "Rej.",
                        "Rejeição: Desconto maior que valor do Produto",
                        "det/prod/vDesc",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_774_i17b_10(self) -> ValidationResult:
        """I17b-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com indicador de item não participante do total
        (tag:indTot=0)
        Erro: 774: R Rejeição: NFC-e com indicador de item não participante do total
        [nItem: 999]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            ind_tot = _v(getattr(prod, "indTot", None))
            if ind_tot == "0":
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "I17b-10",
                        774,
                        "Rej.",
                        "Rejeição: NFC-e com item não participante do total",
                        "det/prod/indTot",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_329_i19_10(self) -> ValidationResult:
        """I19-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Número da DI / DSI inválido
        Erro: 329: Rejeição: Número da DI /DSI inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I19-10
        return None

    def validation_obrig_rej_376_i23_10(self) -> ValidationResult:
        """I23-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Data do Desembaraço Aduaneiro inferior a 5 anos da data
        atual ou superior a data atual (NT 2015.002)
        Erro: 376: Rejeição: Data do Desembaraço Aduaneiro inválida [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I23-10
        return None

    def validation_obrig_rej_330_i23b_10(self) -> ValidationResult:
        """I23b-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informar o Valor da AFRMM na importação por via marítima
        (tag:tpViaTransp=1 e não existe tag:vAFRMM)
        Erro: 330: Rejeição: Informar o Valor da AFRMM na importação por via marítima
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I23b-10
        return None

    def validation_obrig_rej_331_i23d_10(self) -> ValidationResult:
        """I23d-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informar o CNPJ do adquirente ou do encomendante na
        importação por conta e ordem ou encomenda (tag:DI/tpIntermedio=2 ou 3)
        Erro: 331: Rejeição: Informar o CNPJ do adquirente ou do encomendante nesta
        forma de importação
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I23d-10
        return None

    def validation_obrig_rej_332_i23d_20(self) -> ValidationResult:
        """I23d-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: CNPJ do adquirente ou do encomendante inválido (zeros, nulo
        ou DV inválido)
        Erro: 332: Rejeição: CNPJ do adquirente ou do encomendante da importação
        inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I23d-20
        return None

    def validation_obrig_rej_333_i23e_10(self) -> ValidationResult:
        """I23e-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informar a UF do adquirente ou do encomendante na importação
        por conta e ordem ou encomenda (tag:DI/tpIntermedio=2 ou 3)
        Erro: 333: Rejeição: Informar a UF do adquirente ou do encomendante nesta forma
        de importação
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I23e-10
        return None

    def validation_obrig_rej_334_i29a_10(self) -> ValidationResult:
        """I29a-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Obrigatória a informação do número do processo de drawback
        na Adição (Declaração de Importação) para os CFOP: 3127, 3211
        Erro: 334: Rejeição: Número do processo de drawback não informado na importação
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I29a-10
        return None

    def validation_obrig_rej_335_i29a_20(self) -> ValidationResult:
        """I29a-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Número do processo de drawback inválido na Adição
        (Declaração de Importação)
        Erro: 335: Rejeição: Número do processo de drawback na importação inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I29a-20
        return None

    def validation_obrig_rej_336_i50_10(self) -> ValidationResult:
        """I50-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado o grupo de Exportação (tag:detExport) no Item em
        operação que não é com exterior (tag: idDest <> 3). (NT 2015.002)
        Erro: 336: Rejeição: Informado o grupo de exportação no item em operação que não
        é com exterior [nItem: nnn]
        """
        # TODO: implement validation logic for I50-10
        return None

    def validation_obrig_rej_338_i51_10(self) -> ValidationResult:
        """I51-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Obrigatória informação do número do processo de drawback
        para CFOP: - 7127: Venda de produção do estabelecimento sob o regime de drawback
        - 7211: Devolução de compras p/ industrialização sob o regime de drawback
        Erro: 338: Rejeição: Número do processo de drawback não informado na exportação
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I51-10
        return None

    def validation_obrig_rej_339_i51_20(self) -> ValidationResult:
        """I51-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Número do processo de drawback inválido
        Erro: 339: Rejeição: Número do processo de drawback na exportação inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I51-20
        return None

    def validation_facul_rej_340_i52_10(self) -> ValidationResult:
        """I52-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Grupo de controle para a Exportação Indireta
        (tag:detExport/exportInd) não informado para os CFOP: 3503, 7501 Observação 1:
        Implementação opcional por UF (NT 2013/005 v 1.10) Observação 2: Esta regra não
        se aplica para NF-e complementar (NT 2013/005 v 1.10)
        Erro: 340: Rejeição: Não informado o grupo de exportação indireta no item
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I52-10
        return None

    def validation_obrig_rej_341_i53_10(self) -> ValidationResult:
        """I53-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Número do registro de exportação inválido
        (tag:detExport/exportInd/nRE)
        Erro: 341: Rejeição: Número do registro de exportação inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I53-10
        return None

    def validation_facul_rej_342_i54_10(self) -> ValidationResult:
        """I54-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Chave de Acesso na exportação indireta
        (tag:exportInd/chNFe): - Dígito Verificador da Chave de Acesso inválido
        Erro: 342: Rejeição: Chave de Acesso informada na Exportação Indireta com DV
        inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I54-10
        return None

    def validation_facul_rej_343_i54_20(self) -> ValidationResult:
        """I54-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Chave de Acesso na exportação indireta
        (tag:exportInd/chNFe): - Modelo da Chave de Acesso diferente de 55
        Erro: 343: Rejeição: Modelo da NF-e informada na Exportação Indireta diferente
        de 55
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I54-20
        return None

    def validation_facul_rej_344_i54_30(self) -> ValidationResult:
        """I54-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Chave de Acesso na exportação indireta
        (tag:exportInd/chNFe): - Verificar duplicidade da Chave de Acesso informada
        (duplicidade de informação da tag exportInd/chNFe), para o item da NF-e
        Erro: 344: Rejeição: Duplicidade de NF-e informada na Exportação Indireta (Chave
        de Acesso informada mais de uma vez)
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I54-30
        return None

    def validation_facul_rej_345_i54_40(self) -> ValidationResult:
        """I54-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Chave de Acesso na exportação indireta
        (tag:exportInd/chNFe): - Verificar se Chave de Acesso na exportação indireta
        consta como NF-e referenciada
        Erro: 345: Rejeição: Chave de Acesso informada na Exportação Indireta não consta
        como NF-e referenciada
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I54-40
        return None

    def validation_facul_rej_346_i55_10(self) -> ValidationResult:
        """I55-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado o grupo de Exportação Indireta, o somatório das
        quantidades informada (tag:qExport) deve corresponder a quantidade comercial
        informada para o item (tag:qCom) Observação: Implementação opcional por UF (NT
        2013/005 v 1.10)
        Erro: 346: Rejeição: Somatório das quantidades informadas na Exportação Indireta
        não corresponde a quantidade total do item
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for I55-10
        return None

    def validation_facul_rej_465_i70_10(self) -> ValidationResult:
        """I70-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado o Número de Controle da FCI (tag:nFCI, id:I70):
        - Acessar Cadastro de FCI (Chave: nFCI) Observação: esta regra possui previsão
        de implementação futura, não tendo sido posta em produção até a publicação deste
        Manual.
        Erro: 465: Rejeição: Número de Controle da FCI inexistente
        """
        # TODO: implement validation logic for I70-10
        return None

    def validation_obrig_rej_877_i83_10(self) -> ValidationResult:
        """I83-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Data de Fabricação dFab (id:I83) maior que a data de
        processamento (NT 2016.002)
        Erro: 877: Rejeição: Data de fabricação maior que a data de processamento
        [nItem: 999]
        """
        import datetime

        today = datetime.date.today()
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            rastro_list = getattr(prod, "rastro", None) or []
            for rastro in rastro_list:
                dfab_str = _v(getattr(rastro, "dFab", None)) or ""
                if dfab_str:
                    try:
                        dfab = datetime.date.fromisoformat(dfab_str[:10])
                        if dfab > today:
                            nitem = int(getattr(item, "nItem", 0))
                            errors.append(
                                self._err(
                                    "I83-10",
                                    877,
                                    "Rej.",
                                    "Rejeição: Data de Fabricação posterior à data atual",
                                    "det/prod/rastro/dFab",
                                    nitem,
                                )
                            )
                            break
                    except (ValueError, TypeError):
                        pass
        return errors or None

    def validation_obrig_rej_870_i84_10(self) -> ValidationResult:
        """I84-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informada data de validade dVal(id: I84) menor que Data de
        Fabricação dFab (id: I83) (NT 2016.002)
        Erro: 870: Rejeição: Data de validade incompatível com data de fabricação
        [nItem: 999]
        """
        import datetime

        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            rastro_list = getattr(prod, "rastro", None) or []
            for rastro in rastro_list:
                dfab_str = _v(getattr(rastro, "dFab", None)) or ""
                dval_str = _v(getattr(rastro, "dVal", None)) or ""
                if dfab_str and dval_str:
                    try:
                        dfab = datetime.date.fromisoformat(dfab_str[:10])
                        dval = datetime.date.fromisoformat(dval_str[:10])
                        if dval < dfab:
                            nitem = int(getattr(item, "nItem", 0))
                            errors.append(
                                self._err(
                                    "I84-10",
                                    870,
                                    "Rej.",
                                    "Rejeição: Data de Validade anterior à Data de Fabricação",
                                    "det/prod/rastro/dVal",
                                    nitem,
                                )
                            )
                            break
                    except (ValueError, TypeError):
                        pass
        return errors or None

    # ============================================================
    # Group J
    # ============================================================

    def validation_obrig_rej_736_j01_10(self) -> ValidationResult:
        """J01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com grupo de Veículos novos (tag:veicProd)
        Erro: 736: Rejeição: NFC-e com grupo de Veículos novos
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            prod = getattr(item, "prod", None)
            if prod and getattr(prod, "veicProd", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "J01-10",
                    736,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de Veículos Novos",
                    "det/prod/veicProd",
                    nitem,
                )
        return None

    # ============================================================
    # Group K
    # ============================================================

    def validation_obrig_rej_873_k01_20(self) -> ValidationResult:
        """K01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Grupo de Medicamentos (tag :med) Obrig.atório
        preenchimento do grupo rastro (id: I80) (NT 2016.002)
        Erro: 873: Rejeição: Operação com medicamentos e não informado os campos de
        rastreabilidade [nItem: 999]
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            med = getattr(prod, "med", None)
            if med is None:
                continue
            rastro_list = getattr(prod, "rastro", None) or []
            if not rastro_list:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "K01-20",
                        873,
                        "Rej.",
                        "Rejeição: Grupo de Medicamentos informado sem grupo rastro",
                        "det/prod/rastro",
                        nitem,
                    )
                )
        return errors or None

    # ============================================================
    # Group L
    # ============================================================

    def validation_obrig_rej_738_l01_10(self) -> ValidationResult:
        """L01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com grupo de Armamentos (tag:arma)
        Erro: 738: Rejeição: NFC-e com grupo de Armamentos
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            prod = getattr(item, "prod", None)
            if prod and getattr(prod, "arma", None):
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "L01-10",
                    738,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de Armamentos",
                    "det/prod/arma",
                    nitem,
                )
        return None

    # ============================================================
    # Group LA
    # ============================================================

    def validation_facul_rej_660_la01_20(self) -> ValidationResult:
        """LA01-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Obrigatória a informação do grupo de combustível para os
        CFOP constantes na Tabela CFOP, indComb=1 ou 2. Observação: Para a NFC-e, a
        regra de validação é opcional, a critério da UF. Exceção: Para a NFC-e, a regra
        de validação não se aplica, em produção, para Nota Fiscal com Data de Emissão
        anterior a 01/01/2016. (NT 2016.002/ NT 2015.002)
        Erro: 660: Rejeição: CFOP de Combustível e não informado grupo de combustível da
        NF- e [nItem: nnn]
        """
        # TODO: implement validation logic for LA01-20
        return None

    def validation_obrig_rej_761_la02_10(self) -> ValidationResult:
        """LA02-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Código do Produto da ANP (tag: cProdANP) inexistente na
        tabela de codificação de produtos do Sistema de Informações de Movimentação de
        Produtos (SIMP), disponibilizada pela ANP, para uso na NF-e. (NT 2015.003)
        Erro: 761: Rejeição: Código de Produto ANP inexistente [nItem: 999]
        """
        # TODO: implement validation logic for LA02-10
        return None

    def validation_obrig_rej_461_la03c_10(self) -> ValidationResult:
        """LA03c-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado percentual do GLP (id: LA03a) ou percentual de Gás
        Natural Nacional (id: LA03b) ou percentual de Gás Natural Importado (id: LA03c)
        para produto diferente de "210203001 - GLP" (tag:cProdANP) (NT 2016.002)
        Erro: 461: Rejeição: Informado campos de percentual de GLP e/ou GLGNn e/ou GLGNi
        para produto diferente de GLP [nItem: 999]
        """
        # TODO: implement validation logic for LA03c-10
        return None

    def validation_obrig_rej_855_la03c_20(self) -> ValidationResult:
        """LA03c-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GLP (cProdANP=210203001) o somatório dos
        percentuais pGLP(id:LA03a) e pGNn(id:LA03b) e pGNi(id:LA03c) deve ser igual a
        100. (NT 2016.002)
        Erro: 855: Rejeição: Somatório percentuais de GLP derivado do petróleo, GLGNn e
        GLGNi diferente de 100 [nItem: 999].
        """
        # TODO: implement validation logic for LA03c-20
        return None

    def validation_obrig_rej_856_la03d_10(self) -> ValidationResult:
        """LA03d-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Obrigatória a informação do campo vPart (id: LA03d) para
        produto "210203001 - GLP" (tag:cProdANP) (NT 2016.002)
        Erro: 856: Rejeição: Campo valor de partida não preenchido para produto GLP
        [nItem: 999].
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for LA03d-10
        return None

    def validation_facul_rej_378_la11_10(self) -> ValidationResult:
        """LA11-10.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: NFC-e sem a informação do grupo de Encerrante na venda de
        combustível para consumidor final Observação: Regra de validação opcional a
        critério da UF. Exceção 1: A regra de validação se aplica somente para os
        códigos de produtos ANP (cProdANP) abaixo: - 810101002 - ETANOL HIDRATADO
        ADITIVADO - 810101001 - ETANOL HIDRATADO COMUM - 220101005 - GÁS NATURAL
        VEICULAR - 220101006 - GÁS NATURAL VEICULAR PADRÃO - 320103001 - GASOLINA
        AUTOMOTIVA PADRÃO - 320102002 - GASOLINA C ADITIVADA - 320102001 - GASOLINA C
        COMUM - 320102003 - GASOLINA C PREMIUM - 820101033 - ÓLEO DIESEL B S10 -
        ADITIVADO - 820101034 - ÓLEO DIESEL B S10 - COMUM - 420106001 - ÓLEO DIESEL B
        S10 AMD 10 - 820101011 - ÓLEO DIESEL B S1800 Não Rodoviário- Aditivado -
        820101003 - ÓLEO DIESEL B S1800 Não Rodoviário - Comum - 820101013 - ÓLEO DIESEL
        B S500 - ADITIVADO - 820101012 - ÓLEO DIESEL B S500 - COMUM - 420106002 - ÓLEO
        DIESEL B S500 AMD 10 - 420301004 - OLEO DIESEL DE REFERÊNCIA S300 Exceção 2: A
        regra de validação não se aplica, em produção, para Nota Fiscal com Data de
        Emissão anterior a 01/01/2016. (NT 2015.002)
        Erro: 378: Rejeição: Grupo de Combustível sem a informação de Encerrante [nItem:
        nnn]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for LA11-10
        return None

    def validation_obrig_rej_379_la11_20(self) -> ValidationResult:
        """LA11-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado o grupo de “Encerrante” na NF-e (modelo 55) para
        CFOP diferente de venda de combustível para consumidor final (CFOP= 5.656,
        5.667). (NT 2015.002)
        Erro: 379: Rejeição: Grupo de Encerrante na NF-e (modelo 55) para CFOP diferente
        de venda de combustível para consumidor final [nItem:nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for LA11-20
        return None

    def validation_obrig_rej_380_la16_10(self) -> ValidationResult:
        """LA16-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Valor do Encerrante final não é superior ao Encerrante
        inicial Observação: No caso do valor do encerrante chegar ao final (zerar) o
        item correspondente deverá ser informado com encerrante final 999... e deverá
        ser incluído um novo item na NF a partir do encerrante com valor inicial zero.
        (NT 2015.002)
        Erro: 380: Rejeição: Valor do Encerrante final não é superior ao Encerrante
        inicial [nItem: nnn]
        """
        # TODO: implement validation logic for LA16-10
        return None

    # ============================================================
    # Group LB
    # ============================================================

    def validation_obrig_rej_348_lb01_10(self) -> ValidationResult:
        """LB01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com grupo RECOPI - Papel Imune (tag:nRECOPI)
        Erro: 348: Rejeição: NFC-e com grupo RECOPI
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            prod = getattr(item, "prod", None)
            if prod and getattr(prod, "nRECOPI", None):
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "LB01-10",
                    348,
                    "Rej.",
                    "Rejeição: NFC-e com grupo RECOPI - Papel Imune",
                    "det/prod/nRECOPI",
                    nitem,
                )
        return None

    def validation_facul_rej_349_lb01_20(self) -> ValidationResult:
        """LB01-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se não informado o número do RECOPI (tag:nRECOPI, id:LB01) -
        Se Papel Imune (CST=41 ou CSOSN=300) e - NCM papel (ver relação NCM na seção
        8.12 do MOC - Visão Geral) Observação: implementação futura (NT 2013/005 v 1.10)
        Erro: 349: Rejeição: Número RECOPI não informado
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for LB01-20
        return None

    def validation_facul_rej_350_lb01_30(self) -> ValidationResult:
        """LB01-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Informado número do RECOPI: - Número do RECOPI inválido (Ver
        Seção 8.5 do MOC - Visão Geral,, Identificador RECOPI)
        Erro: 350: Rejeição: Número RECOPI inválido
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for LB01-30
        return None

    # ============================================================
    # Group N
    # ============================================================

    def validation_facul_rej_929_n07_10(self) -> ValidationResult:
        """N07-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Não informados campos de valores do CST 51 (Diferimento): -
        modBC (id: N13), pRedBC (id: N14), vBC (id: N15), pICMS (id: N16), vICMSOp (id:
        N16a), pDif (id: N16b), vICMSDif (id: N16c), vICMS (id: N17) Observações:
        Implementação a critério da UF (NT 2019.001 v1.10, v1.50)
        Erro: 929: Rejeição: Informado CST de diferimento sem as informações de
        diferimento [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N07-10
        return None

    def validation_obrig_rej_858_n08_10(self) -> ValidationResult:
        """N08-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Grupo ICMS60 (id:N08) informado indevidamente nas operações
        com os produtos combustíveis sujeitos a repasse interestadual (tag:cProdANP)
        igual a 210203001, 320101001, 320101002, 320102002, 320102001, 320102003,
        320102005, 320201001, 320103001, 220102001, 320301001, 320103002, 820101032,
        820101026, 820101027, 820101004, 820101005, 820101022, 820101031, 820101030,
        820101014, 820101006, 820101016, 820101015, 820101025, 820101017, 820101018,
        820101019, 820101020, 820101021, 420105001, 420101005, 420101004, 420102005,
        420102004, 420104001, 820101033, 820101034, 420106001, 820101011, 820101003,
        820101013, 820101012, 420106002, 830101001, 420301004, 420202001, 420301001,
        420301002, 410103001, 410101001, 410102001, 430101004, 510101001, 510101002,
        510102001, 510102002, 510201001, 510201003, 510301003, 510103001, 510301001
        Obs.: Para CST 60 Obrig.atório o preenchimento do Grupo Repasse de ICMS ST
        (id:N10b) com o Campo Tributação do ICMS (id:N12) igual a 60 (NT 2016.002)
        Erro: 858: Rejeição: Grupo de Tributação informado indevidamente [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N08-10
        return None

    def validation_facul_rej_527_n12_10(self) -> ValidationResult:
        """N12-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CFOP de Exportação (inicia por 7): - Informado CST de ICMS
        diferente de 41 ou CSOSN diferente de 300 (NT 2010/010) Exceção: A regra acima
        não se aplica para a NF-e de devolução (finNFe=4).
        Erro: 527: Rejeição: Operação de Exportação com informação de ICMS incompatível
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N12-10
        return None

    def validation_facul_rej_590_n12_20(self) -> ValidationResult:
        """N12-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado CST (id:N12) para CRT (id:C21) igual a 1 (NT
        2010/010)
        Erro: 590: Rejeição: Informado CST para emissor do Simples Nacional (CRT=1)
        """
        if not self._emit:
            return None
        crt = _v(getattr(self._emit, "CRT", None))
        if crt != "1":
            return None
        errors = []
        for item in self._det:
            cst, csosn, _ = self._get_item_icms_info(item)
            if cst is not None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-20",
                        590,
                        "Rej.",
                        "Rejeição: Informado CST para emissor do Simples Nacional (CRT=1)",
                        "det/imposto/ICMS",
                        nitem,
                    )
                )
        return errors or None

    _NFCE_VALID_CST = {"00", "20", "40", "41", "60", "90"}
    _NFCE_CST_NON_ST = {"00", "20", "40", "41", "90"}
    _NFCE_CFOP_NON_ST = {"5101", "5102", "5103", "5104", "5115"}
    _NFCE_CFOP_ST = {"5405", "5656", "5667"}

    def _get_item_icms_info(self, item):
        """Return (cst, csosn, icms_grp) from a det item, or (None, None, None)."""
        imposto = getattr(item, "imposto", None)
        if not imposto:
            return None, None, None
        icms_cont = getattr(imposto, "ICMS", None)
        if not icms_cont:
            return None, None, None
        for attr in (
            "ICMS00",
            "ICMS10",
            "ICMS20",
            "ICMS30",
            "ICMS40",
            "ICMS41",
            "ICMS50",
            "ICMS51",
            "ICMS60",
            "ICMS70",
            "ICMS90",
        ):
            grp = getattr(icms_cont, attr, None)
            if grp is not None:
                return _v(getattr(grp, "CST", None)), None, grp
        for attr in (
            "ICMSSN101",
            "ICMSSN102",
            "ICMSSN201",
            "ICMSSN202",
            "ICMSSN500",
            "ICMSSN900",
        ):
            grp = getattr(icms_cont, attr, None)
            if grp is not None:
                return None, _v(getattr(grp, "CSOSN", None)), grp
        return None, None, None

    def _get_all_icms_groups(self, item):
        """Return list of all ICMS sub-group objects present in a det item."""
        imposto = getattr(item, "imposto", None)
        if not imposto:
            return []
        icms_cont = getattr(imposto, "ICMS", None)
        if not icms_cont:
            return []
        groups = []
        for attr in (
            "ICMS00",
            "ICMS10",
            "ICMS20",
            "ICMS30",
            "ICMS40",
            "ICMS41",
            "ICMS50",
            "ICMS51",
            "ICMS60",
            "ICMS70",
            "ICMS90",
            "ICMSSN101",
            "ICMSSN102",
            "ICMSSN201",
            "ICMSSN202",
            "ICMSSN500",
            "ICMSSN900",
        ):
            grp = getattr(icms_cont, attr, None)
            if grp is not None:
                groups.append(grp)
        return groups

    def validation_obrig_rej_766_n12_30(self) -> ValidationResult:
        """N12-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CST diferente da relação abaixo: - 00-Tributada
        integralmente; - 20-Com redução da Base de Cálculo; - 40-Isenta; - 41-Não
        tributada; - 60-ICMS cobrado anteriormente por substituição tributária; Exceção
        1: Aceitar CST=90-Outros, a critério da UF. Exceção 2: A regra de validação não
        se aplica, em produção, para Nota Fiscal com Data de Emissão anterior a
        01/04/2016. (NT 2015.002)
        Erro: 766: Rejeição: Item com CST indevido [nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            cst, csosn, _ = self._get_item_icms_info(item)
            if cst is not None and cst not in self._NFCE_VALID_CST:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-30",
                        766,
                        "Rej.",
                        "Rejeição: CST inválido para NFC-e",
                        "det/imposto/ICMS",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_381_n12_34(self) -> ValidationResult:
        """N12-34.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CST=90, informando dados do ICMS-ST (tag:
        ICMS90/modBCST) (NT 2015.002)
        Erro: 381: Rejeição: Grupo de tributação ICMS90, informando dados do ICMS-ST
        [nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            cst, _, grp = self._get_item_icms_info(item)
            if cst == "90" and grp is not None:
                mod_bc_st = getattr(grp, "modBCST", None)
                if mod_bc_st is not None:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N12-34",
                            381,
                            "Rej.",
                            "Rejeição: NFC-e com CST=90 e dados de ICMS-ST",
                            "det/imposto/ICMS/ICMS90",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_382_n12_40(self) -> ValidationResult:
        """N12-40.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CST=00, 20, 40, 41 ou 90 e - CFOP diferente de
        5.101, 5.102, 5.103, 5.104, 5.115 (NT 2015.002)
        Erro: 382: Rejeição: CFOP não permitido para o CST informado [nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            cst, _, _ = self._get_item_icms_info(item)
            if cst not in self._NFCE_CST_NON_ST:
                continue
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in self._NFCE_CFOP_NON_ST:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-40",
                        382,
                        "Rej.",
                        "Rejeição: CFOP inválido para CST de NFC-e sem ST",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_382_n12_44(self) -> ValidationResult:
        """N12-44.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CST=60 (ICMS cobrado anteriormente por ST) e CFOP
        diferente de 5.405, 5.656, 5.667 (NT 2015.002)
        Erro: 382: Rejeição: CFOP não permitido para o CST informado [nItem:nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            cst, _, _ = self._get_item_icms_info(item)
            if cst != "60":
                continue
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in self._NFCE_CFOP_ST:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-44",
                        382,
                        "Rej.",
                        "Rejeição: CFOP inválido para CST=60 na NFC-e",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_741_n12_50(self) -> ValidationResult:
        """N12-50.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Partilha de ICMS entre UF (tag:ICMS/ICMSPart)
        Erro: 741: Rejeição: NFC-e com Partilha de ICMS entre UF
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if not imposto:
                continue
            icms_cont = getattr(imposto, "ICMS", None)
            if not icms_cont:
                continue
            if getattr(icms_cont, "ICMSPart", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-50",
                        741,
                        "Rej.",
                        "Rejeição: NFC-e com Partilha de ICMS entre UF",
                        "det/imposto/ICMS/ICMSPart",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_740_n12_60(self) -> ValidationResult:
        """N12-60.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com repasse de ICMS-ST retido anteriormente em
        operação interestadual com repasse pelo SubstitutoTributário (tag: ICMS/ICMSST)
        (NT 2015.002)
        Erro: 740: Rejeição: Item com Repasse de ICMS retido por Substituto Tributário
        [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if not imposto:
                continue
            icms_cont = getattr(imposto, "ICMS", None)
            if not icms_cont:
                continue
            if getattr(icms_cont, "ICMSST", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12-60",
                        740,
                        "Rej.",
                        "Rejeição: NFC-e com repasse de ICMS-ST interestadual",
                        "det/imposto/ICMS/ICMSST",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_508_n12_70(self) -> ValidationResult:
        """N12-70.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Operação com Não Contribuinte (indIEDest=9) e CST difere da
        relação abaixo: - 00-Tributada integralmente; - 20-Com redução da Base de
        Cálculo; - 40-Isenta; - 41-Não tributada; - 60-ICMS cobrado anteriormente por
        substituição tributária; Exceção 1: A regra de validação acima não se aplica
        para NF-e de entrada (tpNF=0-Entrada). Exceção 2: A regra de validação acima não
        se aplica, para o CST=50 (Suspensão), nas operações com CFOP de Retorno de
        Mercadorias (Tabela CFOP, indRetor=1), nem nas operações com CFOP de Remessa de
        Mercadorias (Tabela CFOP, indRemes=1), e nem nas operações com CFOP 5.949 ou
        6.949. Exceção 3: A regra de validação acima não se aplica quando houver ao
        menos um item de venda de veículos novos (grupo “veicProd”). Exceção 4: A regra
        de validação não se aplica, em produção, para Nota Fiscal com data de emissão
        anterior a 01/07/2016. Exceção 5: A regra de validação não se aplica para o
        CST=30 (Isenta ou não tributada e com cobrança do ICMS por substituição
        tributária), em operação interestadual (idDest=2) com combustíveis (tag: comb)
        derivados de petróleo (código ANP diferente de: 820101001, 820101010, 810102001,
        810102004, 810102002, 810102003, 810101002, 810101001, 810101003, 220101003,
        220101004, 220101002, 220101001, 220101005, 220101006, 560101001). Exceção 6: A
        regra de validação acima não se aplica, para os CST=50 (Suspensão) e 51
        (Diferimento), nas operações de devolução (finNFe=4). Exceção 7: A regra de
        validação acima não se aplica, para o CST=51 (Diferimento), nas operações com
        CFOP 5.123, 5.922, 6.123 e 6.922, nem nas operações internas (idDest=1).de
        retorno de Mercadoria depositada em depósito fechado ou armazém geral (CFOP
        5.906 ou 5.907). Exceção 8: A critério da UF a regra de validação não se aplica
        para o CST=10 (Tributada e com cobrança do ICMS por substituição tributária) em
        operação interna (idDest=1). (NT 2017.002 / NT 2015.003)
        Erro: 508: Rejeição: CST incompatível na operação com Não Contribuinte [nItem:
        999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N12-70
        return None

    def validation_obrig_rej_529_n12_80(self) -> ValidationResult:
        """N12-80.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Operação com Contribuinte Isento de Inscrição Estadual
        (indIEDest=2) e CST constante na relação abaixo: - 50-Suspensão na cobrança do
        ICMS; - 51-Diferimento na cobrança do ICMS. Exceção 1: A regra de validação
        acima não se aplica para o CST=50- Suspensão, nas operações com CFOP de conserto
        ou reparo (CFOP 1915, 1916, 2915, 2916, 5915, 5916, 6915 e 6916) ou de remessa
        para demonstração dentro do Estado (CFOP 1912, 1913, 5912 e 5913). Exceção 2: A
        regra de validação acima não se aplica, em produção, para Nota Fiscal com data
        de emissão anterior a 01/07/2016. Exceção 3: A critério da UF, a regra de
        validação acima não se aplica para CST=51-Diferimento em operações internas
        (idDest=1) quando o destinatário for Pessoa Jurídica (tag:dest/CNPJ). Exceção 4:
        Esta regra não se aplica na emissão da NFA-e nas operações internas, a critério
        da UF. (NT 2017.002 / NT 2015.003)
        Erro: 529: Rejeição: CST incompatível na operação com Contribuinte Isento de
        Inscrição Estadual [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N12-80
        return None

    def validation_facul_rej_938_n12_81(self) -> ValidationResult:
        """N12-81.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CST 60 em operações que não sejam para
        consumidor final (tag: indFinal=0, “Normal”): - Não informada Base de Cálculo
        ICMS Retido na operação anterior (tag: vBCSTRet), Alíquota suportada pelo
        Consumidor Final (tag: pST) e Valor do ICMS ST Retido na operação anterior (tag:
        vICMSSTRet). Observação: Implementação opcional a critério da UF. (Atualizado NT
        2018.005 v1.30)
        Erro: 938: Rejeição: Não informada BCST, pST e ICMSST retido na operação
        anterior [nItem: 999]
        """
        # TODO: implement validation logic for N12-81
        return None

    def validation_facul_rej_906_n12_82(self) -> ValidationResult:
        """N12-82.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se Informado CST = 60 em operações a consumidor final (tag:
        indFinal=1, “Consumidor final”), preenchimento Obrig.atório dos campos do grupo
        opcional para informações do ICMS Efetivo (N33) Observação: Implementação
        opcional a critério da UF. (NT 2018.005)
        Erro: 906: Rejeição: Não informados os campos para informações do ICMS Efetivo.
        [nItem: nnn]
        """
        # TODO: implement validation logic for N12-82
        return None

    def validation_facul_rej_930_n12_84(self) -> ValidationResult:
        """N12-84.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CST com benefício fiscal (CST = 20, 30, 40, 41,
        50, 51, 60, 70 ou 90): - Obrig.atório informar o código de benefício fiscal
        (tag: cBenef) Observação 1: Implementação a critério da UF, por modelo de DF-e e
        por CST. Observação 2: Tabela de código de benefício fiscal por UF publicada no
        Portal Nacional da NF-e Exceção: Não se aplica esta regra de validação no caso
        de CST=90 e: - Percentual de Redução de Base de Cálculo (tag: pRedBC) igual a
        zero; - e (Percentual de Redução de Base de Cálculo do ICMS-ST (tag: pRedBCST)
        igual a zero e operação interna (idDest=1). (NT 2019.001 v1.10, v1.50)
        Erro: 930: Rejeição: CST com benefício fiscal e não informado o código de
        benefício fiscal [nItem: nnn]
        """
        # TODO: implement validation logic for N12-84
        return None

    def validation_facul_rej_930_n12_85(self) -> ValidationResult:
        """N12-85.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CST e não informado código de benefício fiscal:
        - Verificar se CST exige código de benefício fiscal (tag: cBenef), conforme
        tabela de código de benefício fiscal por UF publicada no Portal da Secretaria de
        Fazenda da respectiva UF. Observação 1: Implementação a critério da UF, por
        modelo de DF-e e por CST. Observação 2: Para o CST informado, o sistema
        autorizador apenas verifica se existe qualquer cBenef na tabela publicada no
        Portal da Secretaria de Fazenda da respectiva UF, sem verificar a
        compatibilidade. Exceção 1: a RV não se aplica quando Finalidade de emissão da
        NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de
        destino da operação (tag: idDest) igual a Operação interestadual ou com o
        Exterior; Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de
        emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a
        critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag:
        finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se se
        aplica quando Tipo de Operação (tag: tpNF) igual à Entrada. (NT 2019.001 v1.50)
        Erro: 930: Rejeição: CST com benefício fiscal e não informado o código de
        benefício fiscal [nItem: nnn]
        """
        # TODO: implement validation logic for N12-85
        return None

    def validation_facul_rej_928_n12_86(self) -> ValidationResult:
        """N12-86.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CST e informado código de benefício fiscal: -
        Verificar se CST não possui código de benefício fiscal, conforme tabela de
        código de benefício fiscal por UF publicada no Portal da Secretaria de Fazenda
        da respectiva UF. Observação 1: Implementação a critério da UF, por modelo de
        DF-e e CST. Observação 2: Para o CST informado, o sistema apenas verifica se não
        existe qualquer cBenef na tabela publicada no Portal da Secretaria de Fazenda da
        respectiva UF, sem verificar a compatibilidade. Exceção 1: a RV não se aplica
        quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de
        Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a
        Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não
        se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução
        de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade
        de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério
        da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.
        (NT 2019.001 v1.50)
        Erro: 928: Rejeição: Informado código de benefício fiscal para CST sem benefício
        fiscal [nItem: nnn]
        """
        # TODO: implement validation logic for N12-86
        return None

    def validation_facul_rej_931_n12_88(self) -> ValidationResult:
        """N12-88.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado código de benefício fiscal (tag: cBenef): -
        verificar se tipo de código do benefício corresponde ao CST com benefício
        fiscal. Exemplo: Código de benefício fiscal de isenção deve ser utilizado com
        CST de isenção. Observação 1: Implementação a critério da UF, por modelo de DF-e
        e por CST. Observação 2: Tabela de código de benefício fiscal por UF publicada
        no Portal Nacional da NF-e (NT 2019.001 v1.10, v1.50)
        Erro: 931: Rejeição: CST não corresponde ao tipo de código de benefício fiscal
        [nItem: nnn]
        """
        # TODO: implement validation logic for N12-88
        return None

    def validation_facul_rej_934_n12_90(self) -> ValidationResult:
        """N12-90.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se CST de ICMS = (20, 30, 40, 41, 50, 70 ou 90): - Verificar
        se informado o valor do ICMS desonerado (tag:vICMSDeson) e o Motivo da
        Desoneração (tag: motDesICMS). Observação: Implementação a critério da UF, por
        modelo de DF-e e por CST. Exceção 1: a RV não se aplica quando Finalidade de
        emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de
        local de destino da operação (tag: idDest) igual a Operação interestadual ou com
        o Exterior; Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de
        emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a
        critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag:
        finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica
        quando Tipo de Operação (tag: tpNF) igual à Entrada. Exceção 5: Não se aplica
        esta regra de validação no caso de CST=90 e: - Percentual de Redução de Base de
        Cálculo (tag: pRedBC) igual a zero; - e (Percentual de Redução de Base de
        Cálculo do ICMS-ST (tag: pRedBCST) igual a zero (NT 2019.001 v1.10, v1.50)
        Erro: 934: Rejeição: Não informado valor do ICMS desonerado ou o Motivo de
        desoneração [nItem: nnn]
        """
        # TODO: implement validation logic for N12-90
        return None

    def validation_facul_rej_931_n12_94(self) -> ValidationResult:
        """N12-94.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CST e informado código de benefício fiscal: -
        Verificar se código de benefício fiscal corresponde ao CST informado, conforme
        tabela de código de benefício fiscal por UF publicada no Portal da Secretaria de
        Fazenda da respectiva UF. Observação: Implementação a critério da UF, por modelo
        de DF-e e por CST. Exceção 1: a RV não se aplica quando Finalidade de emissão da
        NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de
        destino da operação (tag: idDest) igual a Operação interestadual ou com o
        Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de
        emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a
        critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag:
        finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica
        quando Tipo de Operação (tag: tpNF) igual à Entrada. Nota: Para itens sem
        benefício fiscal, a UF poderá exigir a informação da literal “SEM CBENEF” para
        alguns CST, vide tabela publicada no Portal da Secretaria de Fazenda da
        respectiva UF. Nota: Para itens sem benefício fiscal, a UF poderá exigir a
        informação da literal “SEM CBENEF” para alguns CST, vide tabela publicada no
        Portal Nacional Fazenda da respectiva UF.
        Erro: 931: Rejeição: Informado código de benefício fiscal incompatível com CST e
        UF [nItem: nnn]
        """
        # TODO: implement validation logic for N12-94
        return None

    def validation_facul_rej_929_n12_97(self) -> ValidationResult:
        """N12-97.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Não informados campos de valores do CST 51 (Diferimento): -
        modBC (id: N13), pRedBC (id: N14), vBC (id: N15), pICMS (id: N16), vICMSOp (id:
        N16a), pDif (id: N16b), vICMSDif (id: N16c), vICMS (id: N17) Observações: Regra
        de Validação opcional a critério da UF. Exceção 1: a RV não se aplica quando
        Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e
        Identificador de local de destino da operação (tag: idDest) igual a Operação
        interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica
        quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de
        Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de
        emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da
        UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.
        (NT2019.001)
        Erro: 929: Rejeição: Informado CST de diferimento sem as informações de
        diferimento [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N12-97
        return None

    def validation_facul_rej_946_n12_98(self) -> ValidationResult:
        """N12-98.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado código de benefício fiscal: - Verificar se
        código de benefício fiscal existe e está vigente, conforme tabela de código de
        benefício fiscal por UF publicada no Portal da Secretaria de Fazenda da
        respectiva UF. Observação: Implementação a critério da UF e por modelo de DF-e.
        Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe)
        igual a Devolução de Mercadoria e Identificador de local de destino da operação
        (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a
        critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag:
        finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não
        se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de
        Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação
        (tag: tpNF) igual à Entrada. Exceção 5: essa RV não se aplica quando informado
        CSOSN (operação realizada por optante pelo Simples Nacional). (NT2019.001 v1.50)
        Erro: 946: Rejeição: Informado código de benefício fiscal incorreto ou
        inexistente na UF [nItem: nnn]
        """
        # TODO: implement validation logic for N12-98
        return None

    def validation_facul_rej_591_n12a_10(self) -> ValidationResult:
        """N12a-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado CSOSN (id:N12a) para CRT (id:C21) diferente de 1
        (NT 2010/010)
        Erro: 591: Rejeição: Informado CSOSN para emissor que não é do Simples Nacional
        (CRT diferente de 1)
        """
        if not self._emit:
            return None
        crt = _v(getattr(self._emit, "CRT", None))
        if crt == "1":
            return None
        errors = []
        for item in self._det:
            cst, csosn, _ = self._get_item_icms_info(item)
            if csosn is not None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12a-10",
                        591,
                        "Rej.",
                        "Rejeição: Informado CSOSN para emissor que não é do Simples Nacional (CRT diferente de 1)",
                        "det/imposto/ICMS",
                        nitem,
                    )
                )
        return errors or None

    _NFCE_VALID_CSOSN = {"102", "103", "300", "400", "500", "900"}
    _NFCE_CSOSN_NON_ST = {"102", "103", "300", "400", "900"}

    def validation_obrig_rej_383_n12a_20(self) -> ValidationResult:
        """N12a-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CSOSN diferente da relação abaixo: -
        102-Tributação SN sem permissão de crédito; - 103-Tributação SN, com isenção
        para faixa de receita bruta; - 300-Imune; - 400-Não tributada pelo Simples
        Nacional; - 500-ICMS cobrado anteriormente por substituição tributária ou por
        antecipação; Exceção 1: Aceitar CSOSN=900-Outros, a critério da UF. Exceção 2: A
        regra de validação não se aplica, em produção, para Nota Fiscal com Data de
        Emissão anterior a 01/04/2016. (NT 2015.002)
        Erro: 383: Rejeição: Item com CSOSN indevido [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            _, csosn, _ = self._get_item_icms_info(item)
            if csosn is not None and csosn not in self._NFCE_VALID_CSOSN:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12a-20",
                        383,
                        "Rej.",
                        "Rejeição: CSOSN inválido para NFC-e",
                        "det/imposto/ICMS",
                        nitem,
                    )
                )
        return errors or None

    def validation_facul_rej_938_n12a_50(self) -> ValidationResult:
        """N12a-50.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado CSOSN = 500 em operações que não sejam para
        consumidor final (tag: indFinal=0, “Normal”): - Não informada Base de Cálculo
        ICMS Retido na operação anterior (tag: vBCSTRet), Alíquota suportada pelo
        Consumidor Final (tag: pST) e Valor do ICMS ST Retido na operação anterior (tag:
        vICMSSTRet). Observação: Implementação opcional a critério da UF. (Atualizado na
        NT 2018.005 v1.30)
        Erro: 938: Rejeição: Não informada BCST, pST e ICMSST retido na operação
        anterior [nItem: 999]
        """
        # TODO: implement validation logic for N12a-50
        return None

    def validation_facul_rej_906_n12a_60(self) -> ValidationResult:
        """N12a-60.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se Informado CSOSN=500 em operações a consumidor final (tag:
        indFinal=1, “Consumidor final”), preenchimento Obrig.atório dos campos do grupo
        opcional para informações do ICMS Efetivo (N33) Observação: Implementação
        opcional a critério da UF. (NT 2018.005)
        Erro: 906: Rejeição: Não informados os campos para informações do ICMS Efetivo.
        [nItem: nnn]
        """
        # TODO: implement validation logic for N12a-60
        return None

    def validation_obrig_rej_384_n12a_30(self) -> ValidationResult:
        """N12a-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CSOSN 103 ou 400 não permitidos para a UF.
        Observação: Regra de validação opcional a critério da UF. Exceção: A regra de
        validação não se aplica, em produção, para Nota Fiscal com Data de Emissão
        anterior a 01/04/2016. (NT 2015.002)
        Erro: 384: Rejeição: CSOSN não permitido para a UF [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for N12a-30
        return None

    def validation_obrig_rej_385_n12a_34(self) -> ValidationResult:
        """N12a-34.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CSOSN=900, informando dados do ICMS-ST (tag:
        ICMSSN900/modBCST) (NT 2015.002)
        Erro: 385: Rejeição: Grupo de tributação ICMSSN900, informando dados do ICMS-ST
        [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            _, csosn, grp = self._get_item_icms_info(item)
            if csosn == "900" and grp is not None:
                mod_bc_st = getattr(grp, "modBCST", None)
                if mod_bc_st is not None:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N12a-34",
                            385,
                            "Rej.",
                            "Rejeição: NFC-e com CSOSN=900 e dados de ICMS-ST",
                            "det/imposto/ICMS/ICMSSN900",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_386_n12a_40(self) -> ValidationResult:
        """N12a-40.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CSOSN=102, 103, 300, 400 ou 900 CFOP diferente de
        5.101, 5.102, 5.103, 5.104, 5.115 (NT 2015.002)
        Erro: 386: Rejeição: CFOP não permitido para o CSOSN informado [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            _, csosn, _ = self._get_item_icms_info(item)
            if csosn not in self._NFCE_CSOSN_NON_ST:
                continue
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in self._NFCE_CFOP_NON_ST:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12a-40",
                        386,
                        "Rej.",
                        "Rejeição: CFOP inválido para CSOSN de NFC-e sem ST",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_386_n12a_44(self) -> ValidationResult:
        """N12a-44.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com CSOSN=500 (ICMS cobrado anteriormente) CFOP
        diferente de 5.405, 5.656, 5.667 (NT 2015.002)
        Erro: 386: Rejeição: CFOP não permitido para o CSOSN informado [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        errors = []
        for item in self._det:
            _, csosn, _ = self._get_item_icms_info(item)
            if csosn != "500":
                continue
            prod = getattr(item, "prod", None)
            if not prod:
                continue
            cfop = str(getattr(prod, "CFOP", "") or "")
            if cfop and cfop not in self._NFCE_CFOP_ST:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "N12a-44",
                        386,
                        "Rej.",
                        "Rejeição: CFOP inválido para CSOSN=500 na NFC-e",
                        "det/prod/CFOP",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_600_n12a_70(self) -> ValidationResult:
        """N12a-70.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Operação com Não Contribuinte (indIEDest=9) e CSOSN difere
        da relação abaixo: - 102-Tributação SN sem permissão de crédito; -
        103-Tributação SN, com isenção para faixa de receita bruta; - 300-Imune; -
        400-Não tributada pelo Simples Nacional; - 500-ICMS cobrado anteriormente por
        substituição tributária ou por antecipação; Exceção 1: A regra de validação
        acima não se aplica para NF-e de entrada (tpNF=0-Entrada). Exceção 2: A regra de
        validação acima não se aplica nas operações com CFOP de conserto ou reparo (CFOP
        5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP
        5912 e 5913). Exceção 3: A regra de validação não se aplica, em produção, para
        Nota Fiscal com data de emissão anterior a 01/07/2016. (NT 2015.003)
        Erro: 600: Rejeição: CSOSN incompatível na operação com Não Contribuinte [nItem:
        999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N12a-70
        return None

    def validation_facul_rej_663_n16_04(self) -> ValidationResult:
        """N16-04.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Validação alíquota do ICMS na operação interestadual de
        produtos importados (NT 2012/005 e NT2013/006): - Operação Interestadual de
        Saída (idDest=2 e tpNF=1); - Origem da mercadoria = 1, 2, 3 ou 8; - CST de ICMS
        = 00, 10, 20, 70 ou 90; - Data de Emissão igual ou superior a 01/01/2013; -
        Valor alíquota do ICMS maior do que “4.00” (4 por cento). Exceção 0: Para as
        NF-e com Data de Emissão anterior a 01/07/2016, a regra de validação acima não
        se aplica para destinatário Não Contribuinte (tag:dest/indIEDest=9). Exceção 1:
        A regra acima não se aplica para as operações de Devolução (finNFe=4). Exceção
        2: A regra de validação acima não se aplica para as operações com CFOP de
        Retorno de Mercadorias (Tabela CFOP, indRetor=1). Exceção 3: A regra de
        validação acima não se aplica na venda de veículos novos (grupo “veicProd”) se
        existir ao menos um item de Venda direta para grandes consumidores (tpOp=3), ou
        de Faturamento direto para consumidor final (tpOp=2). Exceção 4: : Para as NF-e
        com Data de Emissão anterior a 01/07/2016, mesmo que informada a IE do
        destinatário, a regra de validação acima não se aplica para as operações com os
        CFOP 6107, 6108 (Não Contribuinte).Exceção 5: A regra de validação acima não se
        aplica para a NF Complementar (finNFe=2) quando: - Se referenciada uma NF-e, a
        NF-e referenciada tem a Data de Emissão anterior a 01/01/13; - Se referenciada
        uma NF modelo 1, a Data de Emissão é anterior a 1301 (tag refNF/AAMM). Exceção
        6: Para as NF-e com Data de Emissão anterior a 01/07/2016, mesmo que informada a
        IE do destinatário, a regra de validação acima não se aplica para as operações
        com o CFOP 6.929 - Lançamento relativo a operação registrada em Cupom Fiscal (NT
        2013/004) Exceção 7: A regra de validação acima não se aplica para as operações
        de venda à ordem (CFOP 6.118, 6.119, 6.122 e 6.123). (NT 2017.002 / NT 2015.003)
        Erro: 663: Rejeição: Alíquota do ICMS com valor superior a 4 por cento na
        operação de saída interestadual com produtos importados [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N16-04
        return None

    def validation_obrig_rej_693_n16_20(self) -> ValidationResult:
        """N16-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Validação alíquota do ICMS na operação interestadual de
        Saída Normal: - Operação Interestadual de Saída Normal (idDest=2, tpNF=1 e
        finNFe=1); - Origem da mercadoria difere de 1, 2, 3 ou 8; - Valor alíquota do
        ICMS (tag:pICMS) maior do que “7.00” (7 por cento) para os Estados de origem
        (enderEmit/UF) do Sul e Sudeste, exceto ES, destinado (enderDest/UF) para os
        Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo. - Valor alíquota do
        ICMS (tag:pICMS) maior do que “12.00” (12 por cento) para os demais casos.
        Exceção 1: Para as NF-e com Data de Emissão anterior a 01/07/2016, a regra de
        validação acima não se aplica para destinatário Não Contribuinte
        (tag:dest/indIEDest=9). Exceção 2: A regra de validação acima não se aplica na
        venda de veículos novos (grupo “veicProd”) se existir ao menos um item de Venda
        direta para grandes consumidores (tpOp=3), ou de Faturamento direto para
        consumidor final (tpOp=2). Exceção 3: A regra de validação acima não se aplica
        para as operações com CFOP de Retorno de Mercadorias ou Anulação de Valor
        (Tabela CFOP, indRetor=1 ou indAnula=1). Exceção 4: A regra de validação acima
        não se aplica para as operações de venda à ordem (CFOP 6.118, 6.119, 6.122 e
        6.123) Exceção 5: A regra de validação não se aplica se informada UF do local de
        entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF);
        Exceção 6: A regra de validação não se aplica se informada UF do local de
        retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF);
        (NT 2017.002 / NT 2015.003)
        Erro: 693: Rejeição: Alíquota de ICMS superior à definida para a operação
        interestadual [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N16-20
        return None

    def validation_facul_rej_351_n16a_10(self) -> ValidationResult:
        """N16a-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se CST de ICMS = 51 (diferimento): - Valor ICMS da Operação
        (id:N16a) difere de Base de Cálculo (id:N15) * Alíquota (id:N16) (*4)
        Observação: Campos opcionais não informados serão considerados como se tiverem
        sido informados com valor = zero.
        Erro: 351: Rejeição: Valor do ICMS da Operação no CST=51 difere do produto BC e
        Alíquota [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N16a-10
        return None

    def validation_facul_rej_352_n16c_10(self) -> ValidationResult:
        """N16c-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se CST de ICMS = 51 (diferimento): - Valor do ICMS diferido
        (id:N16c) difere do produto do Valor do ICMS da Operação (id:N16a) e percentual
        do diferimento (id:N16b) (*4) Observação: Campos opcionais não informados serão
        considerados como se tiverem sido informados com valor = zero.
        Erro: 352: Rejeição: Valor do ICMS Diferido no CST=51 difere do produto Valor
        ICMS Operação e percentual diferimento [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N16c-10
        return None

    def validation_facul_rej_353_n17_10(self) -> ValidationResult:
        """N17-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se CST de ICMS = 51 (diferimento): - Valor do ICMS (id:N17)
        não corresponde a diferença do Valor do ICMS da Operação (id:N16a) e Valor do
        ICMS diferido (id:N16c) Exceção: A regra de validação acima não se aplica caso
        não forem informados os dois campos: vICMSDif e vICMS. Observação: Campos
        opcionais não informados serão considerados como se tiverem sido informados com
        valor = zero.
        Erro: 353: Rejeição: Valor do ICMS no CST=51 não corresponde a diferença do ICMS
        operação e ICMS diferido [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N17-10
        return None

    def validation_facul_rej_528_n17_20(self) -> ValidationResult:
        """N17-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se CST de ICMS = 00, 10, 20, 70 e tag:finNFe = 1 (id:B25) -
        Valor ICMS (id:N17) difere de Base de Cálculo (id:N15) * Alíquota (id:N16) (*4)
        (NT 2010/010):
        Erro: 528: Rejeição: Valor do ICMS difere do produto BC e Alíquota [nItem: 999]
        """
        # TODO: implement validation logic for N17-20
        return None

    def validation_obrig_rej_880_n17b_10(self) -> ValidationResult:
        """N17b-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado percentual de FCP (id:N17b) igual a zero. Nota:
        Não informar os campos relativos a FCP para os produtos não sujeitos à sua
        incidência. (NT 2016.002)
        Erro: 880: Rejeição: Percentual de FCP igual a zero [nItem: 999]
        """
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                pfcp = getattr(grp, "pFCP", None)
                if pfcp is not None and safe_decimal(pfcp) == 0:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N17b-10",
                            880,
                            "Rej.",
                            "Rejeição: Percentual de FCP igual a zero",
                            "det/imposto/ICMS/pFCP",
                            nitem,
                        )
                    )
                    break
        return errors or None

    def validation_obrig_rej_874_n17b_20(self) -> ValidationResult:
        """N17b-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado percentual de FCP (id:N17b), percentual de FCP
        validado conforme tabela de alíquota definida por UF do emitente
        (tag:enderEmit/UF, id:C12). (NT 2016.002)
        Erro: 874: Rejeição: Percentual de FCP inválido [nItem: 999]
        """
        # TODO: implement validation logic for N17b-20
        return None

    def validation_obrig_rej_860_n17c_10(self) -> ValidationResult:
        """N17c-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado a tag vFCP (id:N17c) e finNFe=1 (id:B25),
        verificar: - Se CST=00 e vFCP (id:N17c) difere da vBC (id:N15)* pFCP (id:N17b)
        (*4) ou - Se CST=10, 20,70, 90 ou 51 e vFCP (id:N17c) difere da vBCFCP
        (id:N17a)* pFCP (id:N17b) (*4) (NT 2016.002)
        Erro: 860: Rejeição: Valor do FCP informado difere de base de cálculo*alíquota
        [nItem: 999]
        """
        # TODO: implement validation logic for N17c-10
        return None

    def validation_obrig_rej_876_n17c_20(self) -> ValidationResult:
        """N17c-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se Operação interestadual (tag:idDest=2) para Consumidor
        Final (tag: indFinal=1), não contribuinte (tag: indIEDest=9) e informado o valor
        do FCP (tag: vFCP) Observação: Em operações interestaduais para consumidor final
        não contribuinte, o valor do FCP, quando existir, deve ser informado no campo
        vFCPUFDest (id:NA13). (NT 2016.002)
        Erro: 876: Rejeição: Operação interestadual para Consumidor Final e valor do FCP
        informado em campo diferente de vFCPUFDest (id:NA13) [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N17c-20
        return None

    def validation_facul_rej_932_n18_10(self) -> ValidationResult:
        """N18-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se o campo modBCST = “4” Margem Valor Agregado, Obrigatório
        o preenchimento do campo pMVAST Nota: Regra de Validação opcional a critério da
        UF (NT 2019.001 v1.10, v1.50)
        Erro: 932: Rejeição: Informada modalidade de determinação da BC da ST como MVA e
        não informado o campo pMVAST [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                mod_bc_st = _v(getattr(grp, "modBCST", None))
                if mod_bc_st == "4" and getattr(grp, "pMVAST", None) is None:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N18-10",
                            932,
                            "Rej.",
                            "Rejeição: Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST",
                            "det/imposto/ICMS/pMVAST",
                            nitem,
                        )
                    )
                    break
        return errors or None

    def validation_facul_rej_933_n18_20(self) -> ValidationResult:
        """N18-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se o campo modBCST <> “4” Margem Valor Agregado, não deverá
        ser preenchido o campo pMVAST Nota: Regra de Validação opcional a critério da UF
        (NT 2019.001 v1.10, v1.50)
        Erro: 933: Rejeição: Informada modalidade de determinação da BC da ST diferente
        de MVA e informado o campo pMVAST [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                mod_bc_st = _v(getattr(grp, "modBCST", None))
                if (
                    mod_bc_st is not None
                    and mod_bc_st != "4"
                    and getattr(grp, "pMVAST", None) is not None
                ):
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N18-20",
                            933,
                            "Rej.",
                            "Rejeição: Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST",
                            "det/imposto/ICMS/pMVAST",
                            nitem,
                        )
                    )
                    break
        return errors or None

    def validation_obrig_rej_806_n23_10(self) -> ValidationResult:
        """N23-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Operação sem informação do campo CEST, e CST ou CSOSN da
        relação abaixo: -10-tributada com cobrança de ICMS por substituição tributária
        -30-isenta ou não tributada com cobrança de ICMS por substituição tributária
        -60-ICMS cobrado anteriormente por substituição tributária -70-com redução de
        base de cálculo e cobrança de ICMS por substituição tributária -90-outros, desde
        que com valor de ICMS retido por substituição tributária (tag: vICMSST diferente
        de zero) -201-tributada pelo Simples Nacional com permissão de crédito e com
        cobrança do ICMS por substituição tributária -202-tributada pelo Simples
        Nacional sem permissão de crédito e com cobrança do ICMS por substituição
        tributária -203-isenção de ICMS do Simples Nacional para a faixa de receita, com
        cobrança do ICMS por substituição tributária -500-ICMS cobrado anteriormente por
        substituição tributária ou por antecipação; -900-outros, desde que com valor de
        ICMS retido por substituição tributária (tag: vICMSST diferente de zero).
        Exceção 1: A regra de validação não se aplica se informado o Grupo de Partilha
        do ICMS (campo ICMSPart). (NT 2015.003)
        Erro: 806: Rejeição: Operação com ICMS-ST sem informação do CEST [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N23-10
        return None

    def validation_obrig_rej_881_n23b_10(self) -> ValidationResult:
        """N23b-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado percentual de FCP ST (tag:N23b) igual a zero.
        Nota: não informar os campos relativos a FCP ST para os produtos não sujeitos à
        sua incidência. (NT 2016.002)
        Erro: 881: Rejeição: Percentual de FCPST igual a zero [nItem: 999]
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                pfcpst = getattr(grp, "pFCPST", None)
                if pfcpst is not None and safe_decimal(pfcpst) == 0:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N23b-10",
                            881,
                            "Rej.",
                            "Rejeição: Percentual de FCPST igual a zero",
                            "det/imposto/ICMS/pFCPST",
                            nitem,
                        )
                    )
                    break
        return errors or None

    def validation_obrig_rej_875_n23b_20(self) -> ValidationResult:
        """N23b-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se UF do destinatário diferente de “EX” e se informado
        percentual de FCP ST (tag:N23b), percentual de FCP validado conforme tabela de
        alíquota definida por UF. Obs.1: Utilizar a UF do destinatário na validação
        (tag: enderDest/UF, id:E12); Obs.2: Quando informada a UF do local de entrega
        (tag: entrega/UF) diferente de “EX”, aceitar como válidas tanto a alíquota da UF
        do destinatário (tag: enderDest/UF; id:E12) quanto a alíquota da UF de entrega
        (tag: entrega/UF). Obs.: Implementação Futura (NT 2016.002)
        Erro: 875: Rejeição: Percentual de FCPST inválido [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N23b-20
        return None

    def validation_obrig_rej_860_n23d_10(self) -> ValidationResult:
        """N23d-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado a tag vFCPST (id:N23d) e finNFe=1 (id:B25),
        verificar: - Se informado CST= 10 ou 30 ou 70 ou 90 ou CSOSN=201 ou 202 ou 203
        ou 900 e vFCPST (id:N23d) difere da vBCFCPST (id:N23a)* pFCPST (id:N23b) - vFCP
        (id:N17c) (*4) Obs.1: Campos não informados devem ser considerados como “0"
        Obs.2: Regra de validação aplicável a critério da UF (NT 2016.002)
        Erro: 860: Rejeição: Valor do FCP informado difere de base de cálculo*alíquota
        [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N23d-10
        return None

    def validation_obrig_rej_881_n27b_10(self) -> ValidationResult:
        """N27b-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado percentual de FCP ST retido (id:N27b) igual a
        zero. Nota: não informar os campos relativos a FCP ST para os produtos não
        sujeitos à sua incidência. (NT 2016.002)
        Erro: 881: Rejeição: Percentual de FCPST igual a zero [nItem: 999]
        """
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                pfcpstret = getattr(grp, "pFCPSTRet", None)
                if pfcpstret is not None and safe_decimal(pfcpstret) == 0:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "N27b-10",
                            881,
                            "Rej.",
                            "Rejeição: Percentual de FCPST igual a zero",
                            "det/imposto/ICMS/pFCPSTRet",
                            nitem,
                        )
                    )
                    break
        return errors or None

    def validation_obrig_rej_875_n27b_20(self) -> ValidationResult:
        """N27b-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se UF do destinatário diferente de “EX” e se informado
        percentual de FCP ST retido (id:N27b), percentual de FCP validado conforme
        tabela de alíquota definida por UF. Obs.1: Utilizar a UF do destinatário na
        validação (tag: enderDest/UF; id:E12); Obs.2: Quando informada a UF do local de
        entrega (tag: entrega/UF) diferente de “EX, aceitar como válidas tanto a
        alíquota da UF de destinatário (tag: enderDest/UF; id:E12) quanto a alíquota da
        UF de entrega (tag: entrega/UF). (NT 2016.002)
        Erro: 875: Rejeição: Percentual de FCPST inválido [nItem: 999]
        """
        # TODO: implement validation logic for N27b-20
        return None

    def validation_obrig_rej_860_n27d_10(self) -> ValidationResult:
        """N27d-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Informado a tag vFCPSTRet (id:N27d) e finNFe=1 (id:B25),
        verificar: - Se CST=60 ou CSOSN=500 e vFCPSTRet (id:N27d) difere da vBCFCPSTRet
        (id:N27a)* pFCPSTRet (id:N27b) (*4) Obs.: regra de validação para implementação
        futura (NT 2016.002)
        Erro: 860: Rejeição: Valor do FCP informado difere de base de cálculo*alíquota
        [nItem: 999]
        """
        # TODO: implement validation logic for N27d-10
        return None

    def validation_facul_rej_625_n28_10(self) -> ValidationResult:
        """N28-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado motDesICMS = 7 (desoneração Suframa): -
        tag:ISUF (id:E18) deve ser informado (NT 2011/004) Exceção: Não exigir a
        Inscrição Suframa se informado CFOP de entrada (inicia por 1 ou 2) (NT 2012/003)
        Erro: 625: Rejeição: Inscrição SUFRAMA deve ser informada na venda com isenção
        para ZFM [nItem: 999]
        """
        # TODO: implement validation logic for N28-10
        return None

    def validation_facul_rej_626_n28_20(self) -> ValidationResult:
        """N28-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Se informado tag:motDesICMS = 7 (desoneração Suframa): -
        deve ser informado um dos CFOP abaixo: 1203, 1204, 1208, 1209, 2203, 2204, 2208,
        2209, 5109, 5110, 5120, 5151, 5152, 5651, 5652, 5654, 5655, 5658, 5659, 5910,
        6905, 6109, 6110, 6120, 6122, 6123, 6151, 6152, 6651, 6652, 6654, 6655, 6658,
        6659, 6910, 6923 (NT 2012/003) (NT 2013/005 v1.10)
        Erro: 626: Rejeição: CFOP de operação isenta para ZFM diferente do previsto
        [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for N28-20
        return None

    def validation_facul_rej_627_n28_30(self) -> ValidationResult:
        """N28-30.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado tag:motDesICMS, o vICMSDeson (id:N28a) deve ser
        maior que zero (NT 2011/004). Observação: O motivo da desoneração pode ocorre
        nos grupos de tributação do ICMS 20, 30, 40, 70 e 90. (NT 2016.002)
        Erro: 627: Rejeição: O valor do ICMS desonerado deve ser informado [nItem: 999]
        """
        errors = []
        for item in self._det:
            for grp in self._get_all_icms_groups(item):
                mot_des = getattr(grp, "motDesICMS", None)
                if mot_des is not None:
                    v_icms_deson = safe_decimal(getattr(grp, "vICMSDeson", None))
                    if v_icms_deson <= 0:
                        nitem = int(getattr(item, "nItem", 0))
                        errors.append(
                            self._err(
                                "N28-30",
                                627,
                                "Rej.",
                                "Rejeição: O valor do ICMS desonerado deve ser informado",
                                "det/imposto/ICMS/vICMSDeson",
                                nitem,
                            )
                        )
                        break
        return errors or None

    def validation_facul_rej_906_n33_10(self) -> ValidationResult:
        """N33-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se Informado CST = 60 ou CSOSN=500 e indFinal=1 (id:B25a),
        preenchimento Obrig.atório dos campos do grupo opcional para informações do ICMS
        Efetivo (N33) Observação: Implementação opcional a critério da UF. (NT 2016.002)
        (REMOVIDA NA NT 2018.005)
        Erro: 906: Rejeição: Não informados os campos do grupo opcional para informações
        do ICMS Efetivo, Obrig.atório quando CST = 60 ou CSOSN=500 e operação com
        consumidor final [nItem: nnn]
        """
        # TODO: implement validation logic for N33-10
        return None

    # ============================================================
    # Group NA
    # ============================================================

    def validation_obrig_rej_807_na01_10(self) -> ValidationResult:
        """NA01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado grupo “ICMSUFDest” para a NFC-e (NT 2015.003)
        Erro: 807: Rejeição: NFC-e com grupo de ICMS para a UF do destinatário
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "ICMSUFDest", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "NA01-10",
                    807,
                    "Rej.",
                    "Rejeição: NFC-e com grupo ICMSUFDest",
                    "det/imposto/ICMSUFDest",
                    nitem,
                )
        return None

    def validation_obrig_rej_694_na01_20(self) -> ValidationResult:
        """NA01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Não informado grupo de ICMS para a UF de Destino
        (tag:ICMSUFDest): - Operação Interestadual (idDest=2) e - Operação com
        Consumidor Final (indFinal=1) e - Operação com Não Contribuinte (indIEDest=9) e
        - Não é operação de prestação de serviços (não existe tag “ISSQN”). Exceção 1:
        Esse grupo não deve ser exigido se o Grupo de Partilha do ICMS (campo ICMSPart)
        estiver preenchido. Exceção 2: A regra de validação não se aplica, em produção,
        para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 3: A regra
        de validação não se aplica para Devolução de Mercadoria (finNFe=4) que
        referencie Nota Fiscal com chave de acesso anterior a 2016. Exceção 4: A regra
        de validação acima não se aplica para as operações com CFOP de Retorno de
        Mercadorias (Tabela CFOP, indRetor=1). Exceção 5: A regra de validação acima não
        se aplica nas NF-e de entrada (tpNF=0). Exceção 6: A regra de validação acima
        não se aplica nas operações com combustíveis (tag:comb) derivados de petróleo
        com código ANP diferente de: 820101001, 820101010, 810102001, 810102004,
        810102002, 810102003, 810101002, 810101001, 810101003, 220101003, 220101004,
        220101002, 220101001, 220101005, 220101006, 560101001. Exceção 7: A regra de
        validação acima não se aplica se informada UF do local de entrega (tag:
        entrega/UF) igual à UF do emitente (tag: emit/enderEmit/UF). Exceção 8: A regra
        de validação acima não se aplica para as operações com CFOP de Remessa de
        Mercadoria (Tabela CFOP, indRemes=1). Exceção 9: A regra de validação acima não
        se aplica para os CFOP: - 6.552 - Transferência de bem do ativo imobilizado; -
        6.922 - Lançamento efetuado a título de simples faturamento decorrente de venda
        p/ entrega futura; - 6.929 - Lançamento relativo a Cupom Fiscal. Exceção 10:
        Esta regra de validação não se aplica nas operações isentas (CST=40-Isenta ou
        CSOSN=103-Isento), imunes ou não tributadas (CST=41-
        Erro: 694: Rejeição: Não informado o grupo de ICMS para a UF de destino [nItem:
        999]
        """
        if not self._is_nfe():
            return None
        if not self._ide:
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        ind_final = _v(getattr(self._ide, "indFinal", None))
        if id_dest != "2" or ind_final != "1":
            return None
        ind_ie_dest = _v(getattr(self._dest, "indIEDest", None)) if self._dest else None
        if ind_ie_dest != "9":
            return None
        tp_nf = _v(getattr(self._ide, "tpNF", None))
        if tp_nf == "0":
            return None
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if not imposto:
                continue
            if getattr(imposto, "ICMSUFDest", None) is None:
                icms_part = None
                icms_cont = getattr(imposto, "ICMS", None)
                if icms_cont:
                    icms_part = getattr(icms_cont, "ICMSPart", None)
                if icms_part is None:
                    nitem = int(getattr(item, "nItem", 0))
                    errors.append(
                        self._err(
                            "NA01-20",
                            694,
                            "Rej.",
                            "Rejeição: Não informado o grupo de ICMS para a UF de destino",
                            "det/imposto/ICMSUFDest",
                            nitem,
                        )
                    )
        return errors or None

    def validation_obrig_rej_695_na01_30(self) -> ValidationResult:
        """NA01-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado indevidamente o grupo de ICMS para a UF de Destino
        (tag:ICMSUFDest): - Não é operação Interestadual (idDest<>2) ou - Não é operação
        com Consumidor Final (indFinal<>1) ou - Não é operação com Não Contribuinte
        (indIEDest<>9) ou - Operação de prestação de serviços (existe tag “ISSQN”) ou -
        Operação com combustível (tag:comb) derivado de petróleo: código ANP diferente
        de: 820101001, 820101010, 810102001, 810102004, 810102002, 810102003, 810101002,
        810101001, 810101003, 220101003, 220101004, 220101002, 220101001, 220101005,
        220101006, 560101001, ou - Data de Emissão anterior a 01/01/2016. Exceção 1: A
        critério da UF a regra de validação acima não se aplica na devolução (finNFe=4)
        por NFe Avulsa com IE do Emitente=ISENTO. Exceção 2: A regra de validação acima
        não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da
        UF do emitente (tag: emit/enderEmit/UF). Exceção 3: A regra de validação não se
        aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016.
        (NT 2015.003)
        Erro: 695: Rejeição: Informado indevidamente o grupo de ICMS para a UF de
        destino [nItem:999]
        """
        if not self._is_nfe():
            return None
        if not self._ide:
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        ind_final = _v(getattr(self._ide, "indFinal", None))
        ind_ie_dest = _v(getattr(self._dest, "indIEDest", None)) if self._dest else None
        is_qualifying = id_dest == "2" and ind_final == "1" and ind_ie_dest == "9"
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if not imposto:
                continue
            if getattr(imposto, "ICMSUFDest", None) is not None and not is_qualifying:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "NA01-30",
                        695,
                        "Rej.",
                        "Rejeição: Informado indevidamente o grupo de ICMS para a UF de destino",
                        "det/imposto/ICMSUFDest",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_697_na09_10(self) -> ValidationResult:
        """NA09-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada alíquota interestadual (tag:pICMSInter) de 4% e
        - Origem da mercadoria difere de produto importado (tag:orig<>1,2,3,8) Exceção:
        A regra de validação não se aplica, em produção, para Nota Fiscal com data de
        emissão anterior a 01/07/2016. (NT 2015.003)
        Erro: 697: Rejeição: Alíquota interestadual do ICMS com origem diferente do
        previsto [nItem:999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA09-10
        return None

    def validation_obrig_rej_697_na09_20(self) -> ValidationResult:
        """NA09-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada alíquota interestadual (tag:pICMSInter) de 7%
        ou 12% e - Origem da mercadoria de produto importado (tag:orig=1,2,3,8) Exceção:
        A regra de validação não se aplica, em produção, para Nota Fiscal com data de
        emissão anterior a 01/07/2016. (NT 2015.003)
        Erro: 697: Rejeição: Alíquota interestadual do ICMS com origem diferente do
        previsto [nItem:999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA09-20
        return None

    def validation_obrig_rej_698_na09_30(self) -> ValidationResult:
        """NA09-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada alíquota interestadual (tag:pICMSInter) de 7%
        ou 12% em NF de Saída Normal (tpNF=1 e finNFe=1) e alíquota interestadual
        incompatível com as UF envolvidas: - 7% para os Estados de origem do Sul e
        Sudeste, exceto ES, destinado para os Estados do Norte, Nordeste, Centro-Oeste e
        Espírito Santo; - 12% para os demais casos. Exceção 1: A regra de validação
        acima não se aplica para as operações com CFOP de Retorno de Mercadorias (Tabela
        CFOP, indRetor=1) Exceção 2: A regra de validação não se aplica, em produção,
        para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 3: A regra
        de validação não se aplica se informada UF do local de entrega (tag: entrega/UF)
        diferente da UF do emitente (tag: enderEmit/UF); Exceção 4: A regra de validação
        não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente
        da UF do destinatário (tag: enderDest/UF); (NT 2017.002 / NT 2015.003)
        Erro: 698: Rejeição: Alíquota interestadual do ICMS incompatível com as UF
        envolvidas na operação [nItem:999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA09-30
        return None

    def validation_obrig_rej_699_na11_10(self) -> ValidationResult:
        """NA11-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Percentual do ICMS Interestadual para a UF de destino
        (tag:pICMSInterPart) difere do previsto para o ano da Data de Emissão.
        Observação: Nas operações que não sejam de finalidade de emissão normal
        (finNFe<>1) ou nas operações com CFOP de Retorno de Mercadorias (Tabela CFOP,
        indRetor=1) considerar o ano da NF referenciada em substituição ao ano da Data
        de Emissão. Exceção: A regra de validação não se aplica, em produção, para Nota
        Fiscal com data de emissão anterior a 01/01/2016. (NT 2017.002 / NT 2015.003)
        Erro: 699: Rejeição: Percentual do ICMS Interestadual para a UF de destino
        difere do previsto para o ano da Data de Emissão [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA11-10
        return None

    def validation_obrig_rej_793_na13_10(self) -> ValidationResult:
        """NA13-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF
        de destino tag: vFCPUFDest (id:NA11) difere de vBCFCPUFDest (id:NA04) *
        pFCPUFDest (id:NA05) (*4) Exceção: A regra de validação não se aplica, em
        produção, para Nota Fiscal com data de emissão anterior a 01/01/2016. (NT
        2016.002/ NT 2015.003)
        Erro: 793: Rejeição: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF
        de destino difere do calculado [nItem: 999]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA13-10
        return None

    def validation_obrig_rej_815_na15_10(self) -> ValidationResult:
        """NA15-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Valor do ICMS Interestadual para UF de Destino (tag:
        vICMSUFDest) difere de vBCUFDest _ (pICMSUFDest - pICMSInter) _ pICMSInterPart
        (*4)1 Observação: implementação futura (NT 2015.003)
        Erro: 815: Rejeição: Valor do ICMS Interestadual para UF de Destino difere do
        calculado [nItem: 999] (Valor Informado: XXX, Valor Calculado:XXX)
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA15-10
        return None

    def validation_obrig_rej_816_na17_10(self) -> ValidationResult:
        """NA17-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Valor do ICMS Interestadual para a UF do Remetente (tag:
        vICMSUFRemet) difere de (vBCUFDest * (pICMSUFDest - pICMSInter)) - vICMSUFDest
        (*4)2Observação: implementação futura (NT 2015.003)
        Erro: 816: Rejeição: Valor do ICMS Interestadual para UF do Remetente difere do
        calculado [nItem: 999] (Valor Informado: XXX, Valor Calculado:XXX)
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for NA17-10
        return None

    # ============================================================
    # Group O
    # ============================================================

    def validation_obrig_rej_742_o01_10(self) -> ValidationResult:
        """O01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com o grupo de tributação pelo IPI (id:O01)
        Erro: 742: Rejeição: NFC-e com grupo do IPI
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "IPI", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "O01-10",
                    742,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de tributação pelo IPI",
                    "det/imposto/IPI",
                    nitem,
                )
        return None

    def validation_obrig_rej_387_o06_10(self) -> ValidationResult:
        """O06-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Código de Enquadramento Legal do IPI inválido (tag:cEnq,
        id:O06). Preenchimento conforme seção 8.9 do MOC - Visão Geral (Tabela do Código
        de Enquadramento do IPI)
        Erro: 387: Rejeição: Código de Enquadramento Legal do IPI inválido [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for O06-10
        return None

    def validation_obrig_rej_388_o09_10(self) -> ValidationResult:
        """O09-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Verificar compatibilidade entre o CST do IPI e o Código de
        Enquadramento Legal (cEnq), conforme as regras abaixo: - CST de Isenção e Código
        de Enquadramento incompatível (IPINT/CST=02, 52 e cEnq fora da faixa [301, 399])
        - CST de Imunidade e Código de Enquadramento incompatível (IPINT/CST=04, 54 e
        cEnq fora da faixa [001, 099]) - CST de Suspensão e Código de Enquadramento
        incompatível (IPINT/CST=05, 55 e cEnq fora da faixa [101, 199]) Exceção: A regra
        de validação não se aplica, em produção, para Nota Fiscal com data de emissão
        anterior a 01/04/2016. (NT 2015.002)
        Erro: 388: Rejeição: Código de Situação Tributária do IPI incompatível com o
        Código de Enquadramento Legal do IPI [nItem: nnn]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for O09-10
        return None

    # ============================================================
    # Group P
    # ============================================================

    def validation_obrig_rej_743_p01_10(self) -> ValidationResult:
        """P01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com o grupo de tributação pelo II (id:P01)
        Erro: 743: Rejeição: NFC-e com grupo do II
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "II", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "P01-10",
                    743,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de tributação pelo II",
                    "det/imposto/II",
                    nitem,
                )
        return None

    # ============================================================
    # Group Q
    # ============================================================

    def validation_obrig_rej_745_q01_20(self) -> ValidationResult:
        """Q01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e sem o grupo de tributação pelo PIS (id:Q01)
        Erro: 745: Rejeição: NF-e sem grupo do PIS
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "PIS", None) is None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "Q01-20",
                        745,
                        "Rej.",
                        "Rejeição: NF-e sem grupo do PIS",
                        "det/imposto/PIS",
                        nitem,
                    )
                )
        return errors or None

    # ============================================================
    # Group R
    # ============================================================

    def validation_obrig_rej_746_r01_10(self) -> ValidationResult:
        """R01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com o grupo de tributação pelo PIS-ST (id:R01)
        Erro: 746: Rejeição: NFC-e com grupo do PIS-ST
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "PISST", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "R01-10",
                    746,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de tributação pelo PIS-ST",
                    "det/imposto/PISST",
                    nitem,
                )
        return None

    # ============================================================
    # Group S
    # ============================================================

    def validation_obrig_rej_748_s01_20(self) -> ValidationResult:
        """S01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: NF-e sem o grupo de tributação pela COFINS (id:S01)
        Erro: 748: Rejeição: NF-e sem grupo da COFINS
        """
        if not self._is_nfe():
            return None
        errors = []
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "COFINS", None) is None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "S01-20",
                        748,
                        "Rej.",
                        "Rejeição: NF-e sem grupo da COFINS",
                        "det/imposto/COFINS",
                        nitem,
                    )
                )
        return errors or None

    # ============================================================
    # Group T
    # ============================================================

    def validation_obrig_rej_749_t01_10(self) -> ValidationResult:
        """T01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com o grupo de tributação pela COFINS-ST (id:T01)
        Erro: 749: Rejeição: NFC-e com grupo da COFINS-ST
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            imposto = getattr(item, "imposto", None)
            if imposto and getattr(imposto, "COFINSST", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "T01-10",
                    749,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de tributação pela COFINS-ST",
                    "det/imposto/COFINSST",
                    nitem,
                )
        return None

    # ============================================================
    # Group U
    # ============================================================

    def validation_facul_rej_530_u01_10(self) -> ValidationResult:
        """U01-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado grupo de tributação do ISSQN (id:U01) sem informar
        a Inscrição Municipal (id:C19)
        Erro: 530: Rejeição: Operação com tributação de ISSQN sem informar a Inscrição
        Municipal
        """
        # TODO: implement validation logic for U01-10
        return None

    def validation_facul_rej_592_u01_20(self) -> ValidationResult:
        """U01-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado grupo de tributação do ISSQN (id:U01) sem informar
        nenhum grupo de ICMS (id:N01) Exceção: A critério da UF poderá ser autorizada a
        emissão de NF-e que só tenham itens sujeitos ao ISSQN. (NT 2010/010)
        Erro: 592: Rejeição: A NF-e deve ter pelo menos um item de produto sujeito ao
        ICMS.
        """
        # TODO: implement validation logic for U01-20
        return None

    def validation_obrig_rej_287_u05_10(self) -> ValidationResult:
        """U05-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Código Município do FG - ISSQN: - Código
        Município do FG - ISSQN inexistente (Tabela Municípios IBGE) Exceção: Aceitar
        ISSQN/cMunFG=”9999999” no caso de prestação de serviço no exterior
        (dest/cUF=”EX”). (NT 2013/005 v1.20) (NT 2015.002)
        Erro: 287: Rejeição: Código Município do Fato Gerador de ISSQN inexistente
        [nItem:nnn]
        """
        # TODO: implement validation logic for U05-10
        return None

    def validation_obrig_rej_389_u14_10(self) -> ValidationResult:
        """U14-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Código Município de incidência do ISSQN: -
        Código Município ISSQN inexistente (Tabela Municípios IBGE) (NT 2015.002)
        Erro: 389: Rejeição: Código Município ISSQN inexistente [nItem:nnn]
        """
        # TODO: implement validation logic for U14-10
        return None

    def validation_obrig_rej_739_u15_10(self) -> ValidationResult:
        """U15-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado Código País onde o serviço foi prestado
        (tag:ISSQN/cPais) - Código País inexistente (Tabela do BACEN, vide tabela de
        apoio publicada no Portal da NF-e). Observação: O Código do País informado na
        NF-e pode conter ou não zeros não significativos. (NT 2015.002)
        Erro: 739: Rejeição: Código de País do ISSQN Inexistente
        """
        # TODO: implement validation logic for U15-10
        return None

    # ============================================================
    # Group UA
    # ============================================================

    def validation_obrig_rej_354_ua01_10(self) -> ValidationResult:
        """UA01-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado grupo de devolução de tributos (tag:impostoDevol):
        - NF-e não é de devolução de tributos (NT 2013/005 v 1.20)
        Erro: 354: Rejeição: Informado grupo de devolução de tributos para NF-e que não
        tem finalidade de devolução de mercadoria
        """
        if not self._is_nfe():
            return None
        fin_nfe = _v(getattr(self._ide, "finNFe", None)) if self._ide else None
        if fin_nfe == "4":
            return None
        errors = []
        for item in self._det:
            if getattr(item, "impostoDevol", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                errors.append(
                    self._err(
                        "UA01-10",
                        354,
                        "Rej.",
                        "Rejeição: Informado grupo de devolução de tributos para NF-e que não tem finalidade de devolução de mercadoria",
                        "det/impostoDevol",
                        nitem,
                    )
                )
        return errors or None

    def validation_obrig_rej_390_ua01_20(self) -> ValidationResult:
        """UA01-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado grupo de devolução de tributos (tag:
        impostoDevol): - NFC-e com grupo de devolução de tributos (NT 2015.002)
        Erro: 390: Rejeição: Nota Fiscal com grupo de devolução de Tributos [nItem: nnn]
        """
        if not self._is_nfce():
            return None
        for item in self._det:
            if getattr(item, "impostoDevol", None) is not None:
                nitem = int(getattr(item, "nItem", 0))
                return self._err(
                    "UA01-20",
                    390,
                    "Rej.",
                    "Rejeição: NFC-e com grupo de devolução de tributos",
                    "det/impostoDevol",
                    nitem,
                )
        return None

    # ============================================================
    # Group W
    # ============================================================

    def validation_facul_rej_531_w03_10(self) -> ValidationResult:
        """W03-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total da BC ICMS (id:W03) difere do somatório do valor dos
        itens (id:N15).
        Erro: 531: Rejeição: Total da BC ICMS difere do somatório dos itens
        """
        # TODO: implement validation logic for W03-10
        return None

    def validation_facul_rej_935_w03_20(self) -> ValidationResult:
        """W03-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Valor total da base de cálculo tag “vBC” (id:W03) superior
        ao valor limite estabelecido pela SEFAZ por modelo de DF-e. Observação: o valor
        total máximo da base de cálculo é de R$ 200.000,00 (Duzentos mil reais). (NT
        2019.001 v1.10, v1.50)
        Erro: 935: Rejeição: Valor total da Base de Cálculo superior ao valor limite
        estabelecido [Valor Limite: R$ XXX.XXX,XX] (valor definido pela UF)
        """
        # TODO: implement validation logic for W03-20
        return None

    def validation_facul_rej_532_w04_10(self) -> ValidationResult:
        """W04-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do ICMS (id:W04) difere do somatório do valor dos
        itens (id:N17). O Total não deve considerar o valor informado para os CST 40,
        41, 50. (NT 2010/007)
        Erro: 532: Rejeição: Total do ICMS difere do somatório dos itens
        """
        # TODO: implement validation logic for W04-10
        return None

    def validation_facul_rej_417_w04_20(self) -> ValidationResult:
        """W04-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Valor total do ICMS superior ao valor limite estabelecido
        pela SEFAZ (valor parametrizável por UF)
        Erro: 417: Rejeição: Total do ICMS superior ao valor limite estabelecido
        """
        # TODO: implement validation logic for W04-20
        return None

    def validation_facul_rej_795_w04a_10(self) -> ValidationResult:
        """W04a-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do ICMS desonerado (id:W04a) difere do somatório do
        valor dos itens (id:N28a). (NT 2016.002)
        Erro: 795: Rejeição: Total do ICMS desonerado difere do somatório dos itens
        """
        # TODO: implement validation logic for W04a-10
        return None

    def validation_obrig_rej_861_w04b_10(self) -> ValidationResult:
        """W04b-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total do FCP (id: W04b) difere do somatório do valor dos
        itens (id:N17c). (NT 2016.002)
        Erro: 861: Rejeição: Total do FCP difere do somatório dos itens
        """
        # TODO: implement validation logic for W04b-10
        return None

    def validation_obrig_rej_798_w04c_10(self) -> ValidationResult:
        """W04c-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Total do ICMS relativo Fundo de Combate à Pobreza (FCP) da
        UF de destino (tag:vFCPUFDest, id:W04c) difere do somatório do valor dos itens
        (id:NA13) (NT 2015.003)
        Erro: 798: Rejeição: Valor total do ICMS relativo Fundo de Combate à Pobreza
        (FCP) da UF de destino difere do somatório do valor dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W04c-10
        return None

    def validation_obrig_rej_799_w04e_10(self) -> ValidationResult:
        """W04e-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Total do ICMS Interestadual para a UF de destino
        (tag:vICMSUFDest, id:W04e) difere do somatório do valor dos itens (id:NA15).
        Nota: Considerar o valor Null como sendo zero. (NT 2015.003)
        Erro: 799: Rejeição: Valor total do ICMS Interestadual da UF de destino difere
        do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W04e-10
        return None

    def validation_obrig_rej_800_w04g_10(self) -> ValidationResult:
        """W04g-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Total do ICMS Interestadual para a UF do remetente
        (tag:vICMSUFRemet, id:W04g) difere do somatório do valor dos itens (id:NA17).
        Nota: Considerar o valor Null como sendo zero. (NT 2015.003)
        Erro: 800: Rejeição: Valor total do ICMS Interestadual da UF do remetente difere
        do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W04g-10
        return None

    def validation_facul_rej_533_w05_10(self) -> ValidationResult:
        """W05-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total da BC ICMS-ST (id:W05) difere do somatório do valor
        dos itens (id:N21)
        Erro: 533: Rejeição: Total da BC ICMS-ST difere do somatório dos itens
        """
        # TODO: implement validation logic for W05-10
        return None

    def validation_facul_rej_534_w06_10(self) -> ValidationResult:
        """W06-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do ICMS-ST (id:W06) difere do somatório do valor dos
        itens (id:N23)
        Erro: 534: Rejeição: Total do ICMS-ST difere do somatório dos itens
        """
        # TODO: implement validation logic for W06-10
        return None

    def validation_facul_rej_418_w06_20(self) -> ValidationResult:
        """W06-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Valor total do ICMS-ST superior ao valor limite estabelecido
        pela SEFAZ (valor parametrizável por UF)
        Erro: 418: Rejeição: Total do ICMS ST superior ao valor limite estabelecido
        """
        # TODO: implement validation logic for W06-20
        return None

    def validation_obrig_rej_862_w06a_10(self) -> ValidationResult:
        """W06a-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Total do FCP ST (id: W06a) difere do somatório do valor dos
        itens (id:N23d) (NT 2016.002)
        Erro: 862: Rejeição: Total do FCP ST difere do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W06a-10
        return None

    def validation_obrig_rej_859_w06b_10(self) -> ValidationResult:
        """W06b-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Total do FCP ST retido anteriormente (id: W06b) difere do
        somatório do valor dos itens (id:N27d) (NT 2016.002)
        Erro: 859: Rejeição: Total do FCP retido anteriormente por Substituição
        Tributária difere do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W06b-10
        return None

    def validation_facul_rej_564_w07_10(self) -> ValidationResult:
        """W07-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total dos Produtos e Serviços (id:W07) difere do somatório
        do valor dos itens (id:I11) sujeitos ao ICMS. Considerar somente os valores dos
        itens com a TAG indTot (id:I17b) = 1 (NT 2011.004)
        Erro: 564: Rejeição: Total do Produto / Serviço difere do somatório dos itens
        """
        # TODO: implement validation logic for W07-10
        return None

    def validation_facul_rej_535_w08_10(self) -> ValidationResult:
        """W08-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do Frete (id:W08) difere do somatório do valor dos
        itens (id:I15)
        Erro: 535: Rejeição: Total do Frete difere do somatório dos itens
        """
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_total = safe_decimal(getattr(icms_tot, "vFrete", None))
        v_items = sum(
            safe_decimal(getattr(getattr(i, "prod", None), "vFrete", None))
            for i in self._det
            if getattr(i, "prod", None) is not None
        )
        if not values_match(v_total, v_items):
            return self._err(
                "W08-10",
                535,
                "Rej.",
                "Rejeição: Total do Frete difere do somatório dos itens",
                "total/ICMSTot/vFrete",
            )
        return None

    def validation_facul_rej_536_w09_10(self) -> ValidationResult:
        """W09-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do Seguro (id:W09) difere do somatório do valor dos
        itens (id:I16)
        Erro: 536: Rejeição: Total do Seguro difere do somatório dos itens
        """
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_total = safe_decimal(getattr(icms_tot, "vSeg", None))
        v_items = sum(
            safe_decimal(getattr(getattr(i, "prod", None), "vSeg", None))
            for i in self._det
            if getattr(i, "prod", None) is not None
        )
        if not values_match(v_total, v_items):
            return self._err(
                "W09-10",
                536,
                "Rej.",
                "Rejeição: Total do Seguro difere do somatório dos itens",
                "total/ICMSTot/vSeg",
            )
        return None

    def validation_facul_rej_537_w10_10(self) -> ValidationResult:
        """W10-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do Desconto (id:W10) difere do somatório do valor dos
        itens (id:I17)
        Erro: 537: Rejeição: Total do Desconto difere do somatório dos itens
        """
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_total = safe_decimal(getattr(icms_tot, "vDesc", None))
        v_items = sum(
            safe_decimal(getattr(getattr(i, "prod", None), "vDesc", None))
            for i in self._det
            if getattr(i, "prod", None) is not None
        )
        if not values_match(v_total, v_items):
            return self._err(
                "W10-10",
                537,
                "Rej.",
                "Rejeição: Total do Desconto difere do somatório dos itens",
                "total/ICMSTot/vDesc",
            )
        return None

    def validation_facul_rej_601_w11_10(self) -> ValidationResult:
        """W11-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Total do vII (id:W11) difere do somatório do valor dos itens
        (id:P04) (NT 2011/004)
        Erro: 601: Rejeição: Total do II difere do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W11-10
        return None

    def validation_facul_rej_538_w12_10(self) -> ValidationResult:
        """W12-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Total do IPI (id:W12) difere do somatório do valor dos itens
        (id:O14)
        Erro: 538: Rejeição: Total do IPI difere do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W12-10
        return None

    def validation_facul_rej_863_w12a_10(self) -> ValidationResult:
        """W12a-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Total do IPI devolvido (id: W12a) difere do somatório do
        valor dos itens (id:UA04) ) (NT 2016.002)
        Erro: 863: Rejeição: Total do IPI devolvido difere do somatório dos itens
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W12a-10
        return None

    def validation_facul_rej_602_w13_10(self) -> ValidationResult:
        """W13-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do vPIS (id:W13) difere do somatório do valor dos
        itens (id:Q09) de item sujeito ao ICMS (existe grupo ICMS). (NT 2011.004)
        Erro: 602: Rejeição: Total do PIS difere do somatório dos itens sujeitos ao ICMS
        """
        # TODO: implement validation logic for W13-10
        return None

    def validation_facul_rej_603_w14_10(self) -> ValidationResult:
        """W14-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do vCOFINS (id:W14) difere do somatório do valor dos
        itens (id:S11) de item sujeito ao ICMS (existe grupo ICMS). (NT 2011.004)
        Erro: 603: Rejeição: Total da COFINS difere do somatório dos itens sujeitos ao
        ICMS
        """
        # TODO: implement validation logic for W14-10
        return None

    def validation_facul_rej_604_w15_10(self) -> ValidationResult:
        """W15-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do vOutro (id:W15) difere do somatório do valor dos
        itens (id:I17a) (NT 2011/004)
        Erro: 604: Rejeição: Total do vOutro difere do somatório dos itens
        """
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_total = safe_decimal(getattr(icms_tot, "vOutro", None))
        v_items = sum(
            safe_decimal(getattr(getattr(i, "prod", None), "vOutro", None))
            for i in self._det
            if getattr(i, "prod", None) is not None
        )
        if not values_match(v_total, v_items):
            return self._err(
                "W15-10",
                604,
                "Rej.",
                "Rejeição: Total do vOutro difere do somatório dos itens",
                "total/ICMSTot/vOutro",
            )
        return None

    def validation_facul_rej_610_w16_10(self) -> ValidationResult:
        """W16-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: -Total do vNF (id:W16) difere do somatório de: (+) vProd
        (id:W07) (-) vDesc (id:W10) (-) vICMSDeson (id:W04a) (+) vST (id:W06) (+) vFCPST
        (id:W06a) (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII
        (id:W11) (+) vIPI (id:W12) (+) vIPIDevol (id: W12a) (+) vServ (id:W18) (*3) (NT
        2011/005) Exceção 1: Faturamento direto de veículos novos: Se informada operação
        de Faturamento Direto para veículos novos (tpOp = 2, id:J02): - Total do vNF
        (id:W16) difere do somatório de: (+) vProd (id:W07) (-) vDesc (id:W10) (-)
        vICMSDeson (id:W04a) (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15)
        (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (*3) (NT 2011/005) Exceção
        2: Esta regra não se aplica nas operações de importação (CFOP inicia com “3”).
        Exceção 3 (NT 2013/005 v 1.22): Esta regra de validação não deverá causar
        rejeição caso não tenha sido subtraído o valor do ICMS Desonerado (vICMSDeson)
        do valor total da NF-e. ) (NT 2016.002)
        Erro: 610: Rejeição: Total da NF difere do somatório dos Valores compõe o valor
        Total da NF.
        """
        # TODO: implement validation logic for W16-10
        return None

    def validation_facul_rej_628_w16_20(self) -> ValidationResult:
        """W16-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Valor total da NF-e superior ao valor limite estabelecido
        pela SEFAZ (valor limite parametrizável por UF) (NT 2011/004)
        Erro: 628: Rejeição: Total da NF superior ao valor limite estabelecido pela
        SEFAZ [Limite]
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for W16-20
        return None

    def validation_obrig_rej_780_w16_30(self) -> ValidationResult:
        """W16-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Valor total da NFC-e é superior ao valor limite estabelecido
        pela SEFAZ (valor parametrizável por UF) Observação: O valor máximo default para
        a NFC-e é de R$200.000,00
        Erro: 780: Rejeição: Total da NFC-e superior ao valor limite estabelecido pela
        SEFAZ [Limite]
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for W16-30
        return None

    def validation_obrig_rej_750_w16_40(self) -> ValidationResult:
        """W16-40.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com valor total superior a R$ 10.000,00: - Código do
        Destinatário não informado (tag:dest/CNPJ, dest/CPF ou dest/idEstrang). (NT
        2015.002)
        Erro: 750: Rejeição: NFC-e com valor total superior ao permitido para
        destinatário não identificado (Código) [Limite]
        """
        if not self._is_nfce():
            return None
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_nf = safe_decimal(getattr(icms_tot, "vNF", None))
        if v_nf <= 10000.0:
            return None
        if not self._dest:
            return self._err(
                "W16-40",
                750,
                "Rej.",
                "Rejeição: NFC-e > R$10.000 sem identificação do Destinatário",
                "dest",
            )
        cnpj = getattr(self._dest, "CNPJ", None)
        cpf = getattr(self._dest, "CPF", None)
        id_estrangeiro = getattr(self._dest, "idEstrangeiro", None)
        if not cnpj and not cpf and not id_estrangeiro:
            return self._err(
                "W16-40",
                750,
                "Rej.",
                "Rejeição: NFC-e > R$10.000 sem CNPJ/CPF do Destinatário",
                "dest/CNPJ",
            )
        return None

    def validation_facul_rej_751_w16_50(self) -> ValidationResult:
        """W16-50.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: NFC-e com valor total superior a R$ 10.000,00: - Nome do
        Destinatário não informado (tag:dest/xNome) Observação: Regra de Validação
        opcional, a critério da UF. (NT 2015.002)
        Erro: 751: Rejeição: NFC-e com valor total superior ao permitido para
        destinatário não identificado (Nome) [Limite]
        """
        if not self._is_nfce():
            return None
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_nf = safe_decimal(getattr(icms_tot, "vNF", None))
        if v_nf <= 10000.0:
            return None
        if not self._dest or not getattr(self._dest, "xNome", None):
            return self._err(
                "W16-50",
                751,
                "Rej.",
                "Rejeição: NFC-e > R$10.000 sem Nome do Destinatário",
                "dest/xNome",
            )
        return None

    def validation_obrig_rej_752_w16_60(self) -> ValidationResult:
        """W16-60.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com valor total superior a R$ 10.000,00: - Endereço do
        Destinatário não informado (tag:dest/enderDest) Observação: Regra de Validação
        opcional, a critério da UF. (NT 2015.002)
        Erro: 752: Rejeição: NFC-e com valor total superior ao permitido para
        destinatário não identificado (Endereço) [Limite]
        """
        if not self._is_nfce():
            return None
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_nf = safe_decimal(getattr(icms_tot, "vNF", None))
        if v_nf <= 10000.0:
            return None
        if not self._dest or not getattr(self._dest, "enderDest", None):
            return self._err(
                "W16-60",
                752,
                "Rej.",
                "Rejeição: NFC-e > R$10.000 sem Endereço do Destinatário",
                "dest/enderDest",
            )
        return None

    def validation_facul_rej_685_w16a_10(self) -> ValidationResult:
        """W16a-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total do valor aproximado dos tributos (id:W16a) difere do
        somatório dos itens (id:M02) (NT 2013/003) Observação: O campo “vTotTrib” é
        opcional para o Item e para o grupo de Totais. Considerar valor=0, se não
        informado.
        Erro: 685: Rejeição: Total do Valor Aproximado dos Tributos difere do somatório
        dos itens
        """
        # TODO: implement validation logic for W16a-10
        return None

    def validation_facul_rej_605_w18_10(self) -> ValidationResult:
        """W18-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total vServ (id:W18) difere do somatório do valor dos itens
        do vProd (id:I11) de item sujeito ao ISSQN (NT 2011/004)
        Erro: 605: Rejeição: Total do vServ difere do somatório do vProd dos itens
        sujeitos ao ISSQN
        """
        # TODO: implement validation logic for W18-10
        return None

    def validation_facul_rej_606_w19_10(self) -> ValidationResult:
        """W19-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total vBC (id:W19) difere do somatório do valor dos itens
        (id:U02) de item sujeito ao ISSQN (NT 2011/004)
        Erro: 606: Rejeição: Total do vBC do ISS difere do somatório dos itens
        """
        # TODO: implement validation logic for W19-10
        return None

    def validation_facul_rej_607_w20_10(self) -> ValidationResult:
        """W20-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total vISS (id:W20) difere do somatório do valor dos itens
        (id:U04) de item sujeito ao ISSQN (NT 2011/004)
        Erro: 607: Rejeição: Total do ISS difere do somatório dos itens
        """
        # TODO: implement validation logic for W20-10
        return None

    def validation_facul_rej_608_w21_10(self) -> ValidationResult:
        """W21-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total vPIS (id:W21) difere do somatório do valor dos itens
        (id:Q09) de item sujeito ao ISSQN (NT 2011/004)
        Erro: 608: Rejeição: Total do PIS difere do somatório dos itens sujeitos ao
        ISSQN
        """
        # TODO: implement validation logic for W21-10
        return None

    def validation_facul_rej_609_w22_10(self) -> ValidationResult:
        """W22-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Total vCOFINS (id:W22) difere do somatório do valor dos
        itens (id:S11) de item sujeito ao ISSQN (NT 2011/004)
        Erro: 609: Rejeição: Total da COFINS difere do somatório dos itens sujeitos ao
        ISSQN
        """
        # TODO: implement validation logic for W22-10
        return None

    def validation_obrig_rej_364_w22b_10(self) -> ValidationResult:
        """W22b-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total do valor da dedução (id:W22b) difere do somatório dos
        itens (id:U07)
        Erro: 364: Rejeição: Total do valor da dedução do ISS difere do somatório dos
        itens
        """
        # TODO: implement validation logic for W22b-10
        return None

    def validation_obrig_rej_365_w22c_10(self) -> ValidationResult:
        """W22c-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total de outras retenções (id:W22c) difere do somatório dos
        itens (id:U08)
        Erro: 365: Rejeição: Total de outras retenções difere do somatório dos itens
        """
        # TODO: implement validation logic for W22c-10
        return None

    def validation_obrig_rej_366_w22d_10(self) -> ValidationResult:
        """W22d-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total do desconto incondicionado ISS (id:W22d) difere do
        somatório dos itens (id:U09)
        Erro: 366: Rejeição: Total do desconto incondicionado ISS difere do somatório
        dos itens
        """
        # TODO: implement validation logic for W22d-10
        return None

    def validation_obrig_rej_367_w22e_10(self) -> ValidationResult:
        """W22e-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total do desconto condicionado ISS (id:W22e) difere do
        somatório dos itens (id:U10)
        Erro: 367: Rejeição: Total do desconto condicionado ISS difere do somatório dos
        itens
        """
        # TODO: implement validation logic for W22e-10
        return None

    def validation_obrig_rej_368_w22f_10(self) -> ValidationResult:
        """W22f-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Total de ISS retido (id:W22f) difere do somatório dos itens
        (id:U11)
        Erro: 368: Rejeição: Total de ISS retido difere do somatório dos itens
        """
        # TODO: implement validation logic for W22f-10
        return None

    # ============================================================
    # Group X
    # ============================================================

    def validation_obrig_rej_753_x02_10(self) -> ValidationResult:
        """X02-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com Frete e não é entrega a domicílio (tag:modFrete<>9
        e indPres<>4)
        Erro: 753: Rejeição: NFC-e com Frete
        """
        if not self._is_nfce():
            return None
        if self._transp:
            modFrete = _v(getattr(self._transp, "modFrete", None))
            indPres = _v(getattr(self._ide, "indPres", None))
            if modFrete and modFrete != "9" and indPres != "4":
                return self._err(
                    "X02-10",
                    753,
                    "Rej.",
                    "Rejeição: NFC-e com Frete",
                    "transp/modFrete",
                )
        return None

    def validation_obrig_rej_868_x02_20(self) -> ValidationResult:
        """X02-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se operação interestadual (idDest=2), não informar os Grupos
        Veiculo Transporte (id:X18; veicTransp) e Grupo Reboque (id: X22). Obs1: a
        critério de cada UF, a regra de validação acima também pode ser aplicada nas
        operações internas (idDest=1) se cMun (id:C10) do Emitente <> cMun (id: E10) do
        Destinatário Obs.2: Esta regra nãose aplica a emissão da NFA-e. ) (NT 2016.002)
        Erro: 868: Rejeição: Grupos Veiculo Transporte e Reboque não devem ser
        informados
        """
        if not self._is_nfe():
            return None
        if not self._ide:
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        if id_dest != "2":
            return None
        if not self._transp:
            return None
        if getattr(self._transp, "veicTransp", None) is not None:
            return self._err(
                "X02-20",
                868,
                "Rej.",
                "Rejeição: Grupos Veiculo Transporte e Reboque não devem ser informados",
                "transp/veicTransp",
            )
        reboque = getattr(self._transp, "reboque", None)
        if reboque and (
            (isinstance(reboque, list) and len(reboque) > 0)
            or not isinstance(reboque, list)
        ):
            return self._err(
                "X02-20",
                868,
                "Rej.",
                "Rejeição: Grupos Veiculo Transporte e Reboque não devem ser informados",
                "transp/reboque",
            )
        return None

    def validation_obrig_rej_754_x03_10(self) -> ValidationResult:
        """X03-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados do Transportador e não é entrega a domicílio
        (tag:transporta e indPres<>4)
        Erro: 754: Rejeição: NFC-e com dados do Transportador
        """
        if not self._is_nfce():
            return None
        transporta = getattr(self._transp, "transporta", None) if self._transp else None
        if not transporta:
            return None
        ind_pres = _v(getattr(self._ide, "indPres", None))
        if ind_pres != "4":
            return self._err(
                "X03-10",
                754,
                "Rej.",
                "Rejeição: NFC-e com dados de Transportador sem ser entrega a domicílio",
                "transp/transporta",
            )
        return None

    def validation_obrig_rej_786_x03_20(self) -> ValidationResult:
        """X03-20.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e sem dados do Transportador (tag:transporta) e é
        entrega a domicílio (indPres=4)
        Erro: 786: Rejeição: NFC-e de entrega a domicílio sem dados do Transportador
        """
        if not self._is_nfce():
            return None
        ind_pres = _v(getattr(self._ide, "indPres", None))
        if ind_pres != "4":
            return None
        transporta = getattr(self._transp, "transporta", None) if self._transp else None
        if not transporta:
            return self._err(
                "X03-20",
                786,
                "Rej.",
                "Rejeição: NFC-e entrega a domicílio sem dados de Transportador",
                "transp/transporta",
            )
        return None

    def validation_facul_rej_362_x04_10(self) -> ValidationResult:
        """X04-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Obrigatória a informação de identificação do Transportador
        para os CFOP de venda de combustível (tag: CNPJ/CPF, id:X04/X05) com esta
        Obrig.atoriedade na Tabela CFOP, indComb=2. Exceção 1: A regra de validação
        acima se aplica somente para as NF-e com Finalidade de Emissão normal
        (tag:finNFe=1); Exceção 2: A regra de validação acima se aplica somente para os
        Códigos de Produto ANP relacionados na seção 8.11 do MOC - Visão Geral, Exceção
        3: A regra de validação acima não se aplica se for informada a UF do
        Transportador no exterior (tag:transporta/UF=”EX”, id:X10); Observação: Nos
        casos em que não houver circulação física de mercadoria ou em que o
        transportador seja estrangeiro, os dados do transportador poderão ser
        preenchidos com o CNPJ do próprio emitente do documento fiscal. (NT 2015.002)
        Erro: 362: Rejeição: Venda de combustível sem informação do Transportador
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for X04-10
        return None

    def validation_obrig_rej_542_x04_20(self) -> ValidationResult:
        """X04-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ do Transportador: - CNPJ com zeros ou
        dígito de controle inválido
        Erro: 542: Rejeição: CNPJ do Transportador inválido
        """
        if not self._transp:
            return None
        transporta = getattr(self._transp, "transporta", None)
        if not transporta:
            return None
        cnpj = getattr(transporta, "CNPJ", None)
        if cnpj and not validate_cnpj(str(cnpj)):
            return self._err(
                "X04-20",
                542,
                "Rej.",
                "Rejeição: CNPJ do Transportador inválido",
                "transp/transporta/CNPJ",
            )
        return None

    def validation_obrig_rej_543_x05_10(self) -> ValidationResult:
        """X05-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do transportador: - CPF com zeros, nulo,
        111..., 222..., ..., ou DV inválido (NT 2012/003)
        Erro: 543: Rejeição: CPF do Transportador inválido
        """
        if not self._transp:
            return None
        transporta = getattr(self._transp, "transporta", None)
        if not transporta:
            return None
        cpf = getattr(transporta, "CPF", None)
        if cpf and not validate_cpf(str(cpf)):
            return self._err(
                "X05-10",
                543,
                "Rej.",
                "Rejeição: CPF do Transportador inválido",
                "transp/transporta/CPF",
            )
        return None

    def validation_obrig_rej_559_x07_10(self) -> ValidationResult:
        """X07-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada a IE do Transportador: - UF do Transportador
        (id:X10) não informada
        Erro: 559: Rejeição: UF do Transportador não informada
        """
        if not self._transp:
            return None
        transporta = getattr(self._transp, "transporta", None)
        if not transporta:
            return None
        ie = getattr(transporta, "IE", None)
        if ie and ie != "ISENTO":
            uf_transp = getattr(transporta, "UF", None)
            if not uf_transp:
                return self._err(
                    "X07-10",
                    559,
                    "Rej.",
                    "Rejeição: IE do Transportador informada sem UF",
                    "transp/transporta/IE",
                )
        return None

    def validation_obrig_rej_544_x07_20(self) -> ValidationResult:
        """X07-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: IE do Transportador informada e diferente de “ISENTO”: -
        Validar IE, conforme a UF do transportador informada
        Erro: 544: Rejeição: IE do Transportador inválida
        """
        # TODO: implement validation logic for X07-20
        return None

    def validation_obrig_rej_755_x11_10(self) -> ValidationResult:
        """X11-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados de Retenção do ICMS no Transporte
        (tag:retTransp)
        Erro: 755: Rejeição: NFC-e com dados de Retenção do ICMS no Transporte
        """
        if not self._is_nfce():
            return None
        if self._transp and getattr(self._transp, "retTransp", None):
            return self._err(
                "X11-10",
                755,
                "Rej.",
                "Rejeição: NFC-e com dados de Retenção do ICMS no Transporte",
                "transp/retTransp",
            )
        return None

    def validation_obrig_rej_722_x16_10(self) -> ValidationResult:
        """X16-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: CFOP de Transporte inexistente ou não pode ser usado no
        grupo de retenção do ICMS de transporte, conforme tabela de apoio publicada no
        Portal da NF-e (Tabela CFOP, indTransp=0) (NT 2015.002)
        Erro: 722: Rejeição: CFOP de Transporte Inexistente
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for X16-10
        return None

    def validation_obrig_rej_288_x17_10(self) -> ValidationResult:
        """X17-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Código Município do FG - Transporte (id:X17): -
        Código do Município do FG - Transporte inexistente (Tabela Municípios IBGE) (NT
        2015.002)
        Erro: 288: Rejeição: Código Município do Fato Gerador do Transporte inexistente
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for X17-10
        return None

    def validation_obrig_rej_756_x18_10(self) -> ValidationResult:
        """X18-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados do veículo de Transporte (tag:veicTransp)
        Erro: 756: Rejeição: NFC-e com dados do veículo de Transporte
        """
        if not self._is_nfce():
            return None
        if self._transp and getattr(self._transp, "veicTransp", None):
            return self._err(
                "X18-10",
                756,
                "Rej.",
                "Rejeição: NFC-e com dados do veículo de Transporte",
                "transp/veicTransp",
            )
        return None

    def validation_obrig_rej_757_x22_10(self) -> ValidationResult:
        """X22-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados de Reboque do veículo de Transporte
        (tag:reboque)
        Erro: 757: Rejeição: NFC-e com dados de Reboque do veículo de Transporte
        """
        if not self._is_nfce():
            return None
        reboque = getattr(self._transp, "reboque", None) if self._transp else None
        if reboque and (
            (isinstance(reboque, list) and len(reboque) > 0)
            or not isinstance(reboque, list)
        ):
            return self._err(
                "X22-10",
                757,
                "Rej.",
                "Rejeição: NFC-e com dados de Reboque",
                "transp/reboque",
            )
        return None

    def validation_obrig_rej_758_x25a_10(self) -> ValidationResult:
        """X25a-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados do Vagão de Transporte (tag:vagao)
        Erro: 758: Rejeição: NFC-e com dados do Vagão de Transporte
        """
        if not self._is_nfce():
            return None
        if self._transp and getattr(self._transp, "vagao", None):
            return self._err(
                "X25a-10",
                758,
                "Rej.",
                "Rejeição: NFC-e com dados do Vagão de Transporte",
                "transp/vagao",
            )
        return None

    def validation_obrig_rej_759_x25b_10(self) -> ValidationResult:
        """X25b-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados da Balsa de Transporte (tag:balsa)
        Erro: 759: Rejeição: NFC-e com dados da Balsa de Transporte
        """
        if not self._is_nfce():
            return None
        if self._transp and getattr(self._transp, "balsa", None):
            return self._err(
                "X25b-10",
                759,
                "Rej.",
                "Rejeição: NFC-e com dados da Balsa de Transporte",
                "transp/balsa",
            )
        return None

    # ============================================================
    # Group Y
    # ============================================================

    def validation_obrig_rej_760_y01_10(self) -> ValidationResult:
        """Y01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados de cobrança (Fatura, Duplicata) (tag:cobr)
        Erro: 760: Rejeição: NFC-e com dados de cobrança (Fatura, Duplicata)
        """
        if not self._is_nfce():
            return None
        if self._cobr:
            return self._err(
                "Y01-10", 760, "Rej.", "Rejeição: NFC-e com dados de cobrança", "cobr"
            )
        return None

    def validation_obrig_rej_905_y01_20(self) -> ValidationResult:
        """Y01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o Grupo Cobrança (Y01, tag: cobr) os campos
        nFat, vOrig e vLiq devem ser informados. Observação: Implementação futura em
        ambiente de produção a partir de 03/09/2018 ) (NT 2016.002)
        Erro: 905: Rejeição: Campos do grupo Fatura não informados
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        fat = getattr(self._cobr, "fat", None)
        if not fat:
            return None
        n_fat = getattr(fat, "nFat", None)
        v_orig = getattr(fat, "vOrig", None)
        v_liq = getattr(fat, "vLiq", None)
        if not n_fat or v_orig is None or v_liq is None:
            return self._err(
                "Y01-20",
                905,
                "Rej.",
                "Rejeição: Grupo Cobrança sem nFat, vOrig ou vLiq",
                "cobr/fat",
            )
        return None

    def validation_obrig_rej_901_y05_10(self) -> ValidationResult:
        """Y05-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Valor do Desconto (vDesc, id:Y05) maior que o Valor Original
        da Fatura (vOrig, id:Y04) Obs.: Considerar como zero os valores opcionais não
        informados. ) (NT 2016.002)
        Erro: 901: Rejeição: Valor do Desconto da Fatura maior que Valor Original da
        Fatura
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        fat = getattr(self._cobr, "fat", None)
        if not fat:
            return None
        v_orig = safe_decimal(getattr(fat, "vOrig", None))
        v_desc = safe_decimal(getattr(fat, "vDesc", None))
        if v_desc > 0 and v_desc > v_orig:
            return self._err(
                "Y05-10",
                901,
                "Rej.",
                "Rejeição: Desconto da Fatura maior que Valor Original",
                "cobr/fat/vDesc",
            )
        return None

    def validation_obrig_rej_902_y06_10(self) -> ValidationResult:
        """Y06-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Valor Líquido da Fatura (vLiq, id:Y06) e o
        Valor Original da Fatura (vOrig; id:Y04): - Valor Líquido da Fatura (vLiq,
        id:Y06) difere do Valor Original da Fatura (vOrig; id:Y04) - Valor do Desconto
        (vDesc, id:Y05) Obs.: Considerar como zero os valores opcionais não informados )
        (NT 2016.002)
        Erro: 902: Rejeição: Valor Liquido da Fatura difere do Valor Original menos o
        Valor do Desconto
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        fat = getattr(self._cobr, "fat", None)
        if not fat:
            return None
        v_orig = safe_decimal(getattr(fat, "vOrig", None))
        v_desc = safe_decimal(getattr(fat, "vDesc", None))
        v_liq = safe_decimal(getattr(fat, "vLiq", None))
        if getattr(fat, "vLiq", None) is not None and not values_match(
            v_liq, v_orig - v_desc
        ):
            return self._err(
                "Y06-10",
                902,
                "Rej.",
                "Rejeição: vLiq difere de vOrig - vDesc na Fatura",
                "cobr/fat/vLiq",
            )
        return None

    def validation_obrig_rej_852_y08_10(self) -> ValidationResult:
        """Y08-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o Grupo Parcelas de cobrança (tag:dup, Id:Y07),
        Número da parcela (nDup, id:Y08) não informado ou inválido. Obs1: O número de
        parcelas deve ser informado com 3 algarismos, sequenciais e consecutivos. Ex.:
        “001”,”002”,”003”,...(NT 2016.002)
        Erro: 852: Rejeição: Número da parcela inválido ou não informado [nOcor: 999]
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        dups = getattr(self._cobr, "dup", None) or []
        for dup in dups:
            n_dup = getattr(dup, "nDup", None)
            if not n_dup:
                return self._err(
                    "Y08-10",
                    852,
                    "Rej.",
                    "Rejeição: nDup não informado em Parcela de Cobrança",
                    "cobr/dup/nDup",
                )
        return None

    def validation_obrig_rej_900_y09_20(self) -> ValidationResult:
        """Y09-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o grupo de Parcelas de cobrança (tag:dup,
        Id:Y07) e Data de vencimento (dVenc, id:Y09) não informada ou menor que a Data
        de Emissão (id:B09) (NT 2016.002)
        Erro: 900: Rejeição: Data de vencimento da parcela não informada ou menor que
        Data de Emissão [nOcor: 999]
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        dups = getattr(self._cobr, "dup", None) or []
        d_emi = getattr(self._ide, "dhEmi", None) or ""
        if not d_emi or not dups:
            return None
        emi_date = str(d_emi)[:10]
        for dup in dups:
            d_venc = getattr(dup, "dVenc", None)
            if d_venc and str(d_venc)[:10] < emi_date:
                return self._err(
                    "Y09-20",
                    900,
                    "Rej.",
                    "Rejeição: Data de vencimento anterior à emissão da NF-e",
                    "cobr/dup/dVenc",
                )
        return None

    def validation_obrig_rej_850_y09_30(self) -> ValidationResult:
        """Y09-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o grupo de Parcelas de cobrança (tag:dup,
        Id:Y07) e Data de vencimento (dVenc, id:Y09) não informada ou menor que a Data
        de vencimento da parcela anterior (dVenc, id:Y09) ) (NT 2016.002)
        Erro: 850: Rejeição: Data de vencimento da parcela não informada ou menor que a
        Data de vencimento da parcela anterior [nOcor: 999]
        """
        # Stub: requires validation of date format beyond scope of format-only checks
        return None

    def validation_obrig_rej_851_y10_10(self) -> ValidationResult:
        """Y10-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o grupo de Parcelas de cobrança (tag:dup,
        Id:Y07) e a soma do valor das parcelas (vDup, id: Y10) difere do Valor Líquido
        da Fatura (vLiq, id:Y06). (NT 2016.002)
        Erro: 851: Rejeição: Soma do valor das parcelas difere do Valor Líquido da
        Fatura
        """
        if not self._is_nfe():
            return None
        if not self._cobr:
            return None
        fat = getattr(self._cobr, "fat", None)
        dups = getattr(self._cobr, "dup", None) or []
        if not fat or not dups:
            return None
        v_liq = safe_decimal(getattr(fat, "vLiq", None))
        total_dup = sum(safe_decimal(getattr(d, "vDup", None)) for d in dups)
        if not values_match(total_dup, v_liq):
            return self._err(
                "Y10-10",
                851,
                "Rej.",
                "Rejeição: Soma das Parcelas difere do Valor Líquido da Fatura",
                "cobr/dup/vDup",
            )
        return None

    # ============================================================
    # Group YA
    # ============================================================

    def validation_obrig_rej_871_ya02_04(self) -> ValidationResult:
        """YA02-04.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se campo finNFe = 3 ou 4 e campo Meio de Pagamento (tag:
        tPag, id:YA02) <> 90 (Sem Pagamento). ) (NT 2016.002)
        Erro: 871: Rejeição: O campo Meio de Pagamento deve ser preenchido com a opção
        Sem Pagamento
        """
        if not self._is_nfe():
            return None
        fin_nfe = _v(getattr(self._ide, "finNFe", None))
        if fin_nfe not in ("3", "4"):
            return None
        if not self._pag:
            return None
        det_pag = getattr(self._pag, "detPag", None) or []
        for pag in det_pag:
            t_pag = _v(getattr(pag, "tPag", None))
            if t_pag and t_pag != "90":
                return self._err(
                    "YA02-04",
                    871,
                    "Rej.",
                    "Rejeição: NF-e de ajuste/devolução deve ter tPag=90",
                    "pag/detPag/tPag",
                )
        return None

    def validation_obrig_rej_857_ya02_10(self) -> ValidationResult:
        """YA02-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Se informado Campo Forma de Pagamento (tag:tPag, id:YA02)
        =14 ) (NT 2016.002)
        Erro: 857: Rejeição: Informado Duplicata Mercantil como Forma de Pagamento
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for YA02-10
        return None

    def validation_obrig_rej_899_ya02_40(self) -> ValidationResult:
        """YA02-40.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado tpag (id=YA02)= 90 “Sem Pagamento” ) (NT 2016.002)
        Erro: 899: Rejeição: Informado incorretamente o campo meio de pagamento
        """
        if not self._is_nfce():
            return None
        if not self._pag:
            return None
        det_pag = getattr(self._pag, "detPag", None) or []
        for pag in det_pag:
            t_pag = _v(getattr(pag, "tPag", None))
            if t_pag == "90":
                return self._err(
                    "YA02-40",
                    899,
                    "Rej.",
                    "Rejeição: Informado incorretamente o campo meio de pagamento",
                    "pag/detPag/tPag",
                )
        return None

    def validation_obrig_rej_436_ya02_50(self) -> ValidationResult:
        """YA02-50.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado meio de pagamento tPag= 99 “Outros” Observação:
        Regra de validação valida a partir de 01/02/2021 para homologação e 01/09/2021
        para produção (Incluída na NT 2020.006)
        Erro: 436: Rejeição: Informado 99-Outros como meio de pagamento
        """
        if not self._is_nfce():
            return None
        if not self._pag:
            return None
        det_pag = getattr(self._pag, "detPag", None) or []
        for pag in det_pag:
            t_pag = _v(getattr(pag, "tPag", None))
            if t_pag == "99":
                return self._err(
                    "YA02-50",
                    436,
                    "Rej.",
                    "Rejeição: Informado 99-Outros como meio de pagamento",
                    "pag/detPag/tPag",
                )
        return None

    def validation_facul_rej_865_ya03_10(self) -> ValidationResult:
        """YA03-10.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: Somatório do valor dos pagamentos (id:YA03, tag:vPag) menor
        que o total da nota (id:W16, tag: vNF) Exceção 1: Esta regra não se aplica para
        nota fiscal de Ajuste, campo finNFe=3 (id:B25) e para nota fiscal de Devolução
        finNFe=4 (id:B25) Exceção 2: Esta regra não se aplica quando o campo Meio de
        Pagamento (id:YA02, tag:tPag) for igual a 90 (sem pagamento). ) (NT 2016.002)
        Erro: 865: Rejeição: Total dos pagamentos menor que o total da nota
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for YA03-10
        return None

    def validation_facul_rej_866_ya03_20(self) -> ValidationResult:
        """YA03-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Somatório do valor dos pagamentos (id:YA03, tag:vPag) maior
        que o total da nota (id:W16, tag: vNF) e sem informação no campo vTroco
        (id:YA09) ) (NT 2016.002)
        Erro: 866: Rejeição: Ausência de troco quando o valor dos pagamentos informados
        for maior que o total da nota
        """
        # TODO: implement validation logic for YA03-20
        return None

    def validation_facul_rej_904_ya03_30(self) -> ValidationResult:
        """YA03-30.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado o campo Meio de Pagamento igual a sem pagamentoo
        (tag:tPag=90, id:YA02) e informado campo Valor do Pagamento diferente de zero
        (tag:vPag<>0, id:YA03). ) (NT 2016.002)
        Erro: 904: Rejeição: Informado indevidamente campo valor de pagamento
        """
        # TODO: implement validation logic for YA03-30
        return None

    def validation_facul_rej_391_ya04_10(self) -> ValidationResult:
        """YA04-10.

        Modelo: 65
        Aplicação: Facul.
        Regra de Validação: Se informado o grupo de pagamentos (tag:pag): - Se o
        Pagamento for por cartão (tag:tPag=03, 04), deve ser informado o grupo de
        cartões (tag:card) Observação: Implementação por padrão, opcional a critério da
        UF. Exceção: A regra de validação não se aplica, em produção, para Nota Fiscal
        com Data de Emissão anterior a 01/04/2016. (NT 2015.002)
        Erro: 391: Rejeição: Não informados os dados do cartão de crédito / débito nas
        Formas de Pagamento da Nota Fiscal
        """
        if not self._is_nfce():
            return None
        # TODO: implement validation logic for YA04-10
        return None

    def validation_facul_rej_737_ya04a_20(self) -> ValidationResult:
        """YA04a-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado o tipo de integração como pagamento não
        integrado com o sistema de automação da empresa (tag: tpIntegra=2) para UF que
        não aceita esse tipo de integração. Observação 1: Regra de Validação opcional a
        critério da UF. ) (NT 2016.002 / NT 2015.002)
        Erro: 737: Rejeição: Pagamento com cartão de crédito em sistema de automação não
        integrado
        """
        # TODO: implement validation logic for YA04a-20
        return None

    def validation_facul_rej_392_ya05_10(self) -> ValidationResult:
        """YA05-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Se informado o grupo de Cartão de Crédito / Débito
        (tag:card): - Se o pagamento com cartão for integrado ao sistema de automação da
        empresa (tag:tpIntegra=1) devem ser informado os campos de CNPJ da Credenciadora
        e o código de autenticação da operação (tag:card/CNPJ e card/cAut) Observação:
        Implementação por padrão, opcional a critério da UF. Exceção: A regra de
        validação não se aplica, em produção, para Nota Fiscal com Data de Emissão
        anterior a 01/04/2016. ) (NT 2016.002/ NT 2015.002)
        Erro: 392: Rejeição: Não informados os dados da operação de pagamento por cartão
        de crédito / débito
        """
        # TODO: implement validation logic for YA05-10
        return None

    def validation_obrig_rej_437_ya05_20(self) -> ValidationResult:
        """YA05-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado o CNPJ da instituição de pagamento - Verificar
        CNPJ com zeros, nulo ou DV inválido (Incluída na NT 2020.006
        Erro: 437: Rejeição: CNPJ da instituição de pagamento inválido)
        """
        if not self._pag:
            return None
        det_pag = getattr(self._pag, "detPag", None) or []
        for pag in det_pag:
            card = getattr(pag, "card", None)
            if not card:
                continue
            cnpj = getattr(card, "CNPJ", None)
            if cnpj and not validate_cnpj(str(cnpj)):
                return self._err(
                    "YA05-20",
                    437,
                    "Rej.",
                    "Rejeição: CNPJ da Instituição de Pagamento inválido",
                    "pag/detPag/card/CNPJ",
                )
        return None

    def validation_obrig_rej_869_ya09_10(self) -> ValidationResult:
        """YA09-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado campo Valor do troco (id:YA09, tag:vTroco) com
        valor difere de: (+) vPag (id:YA03) (-) vNF (id:W16) ) (NT 2016.002)
        Erro: 869: Rejeição: Valor do troco incorreto
        """
        if not self._pag:
            return None
        v_troco = safe_decimal(getattr(self._pag, "vTroco", None))
        if v_troco == 0.0:
            return None
        det_pag = getattr(self._pag, "detPag", None) or []
        total_pag = sum(safe_decimal(getattr(p, "vPag", None)) for p in det_pag)
        if not self._total:
            return None
        icms_tot = getattr(self._total, "ICMSTot", None)
        if not icms_tot:
            return None
        v_nf = safe_decimal(getattr(icms_tot, "vNF", None))
        expected_troco = total_pag - v_nf
        if not values_match(v_troco, expected_troco):
            return self._err(
                "YA09-10",
                869,
                "Rej.",
                "Rejeição: Valor do Troco difere de vPag - vNF",
                "pag/vTroco",
            )
        return None

    # ============================================================
    # Group YB
    # ============================================================

    def validation_obrig_rej_438_yb01_10(self) -> ValidationResult:
        """YB01-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Indicador do Intermediador IGUAL “1=Operação em
        site ou plataforma de terceiros (intermediadores/marketplace)” (indIntermed=1) -
        Obrigatório o preenchimento das Informações do Intermediador da Transação (tag:
        infIntermed) (Incluída na NT 2020.006
        Erro: 438: Rejeição: Obrigatória as informações do intermediador da transação
        para operação por site de terceiros
        """
        if not self._is_nfe():
            return None
        ind_intermed = _v(getattr(self._ide, "indIntermed", None))
        if ind_intermed != "1":
            return None
        inf_intermed = getattr(self._inf, "infIntermed", None) if self._inf else None
        if not inf_intermed:
            return self._err(
                "YB01-10",
                438,
                "Rej.",
                "Rejeição: Grupo infIntermed obrigatório para indIntermed=1",
                "infIntermed",
            )
        return None

    def validation_obrig_rej_439_yb01_20(self) -> ValidationResult:
        """YB01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado Indicador de presença do comprador no
        estabelecimento comercial no momento da operação DIFERENTE de “1=Operação em
        site ou plataforma de terceiros (intermediadores/marketplace)” (indIntermed<>1)
        - Não é permitido o preenchimento das Informações do Intermediador da Transação
        (tag: infIntermed) (Incluída na NT 2020.006
        Erro: 439: Rejeição: Informações do intermediador da transação para operação por
        site de terceiros preenchido indevidamente
        """
        if not self._is_nfe():
            return None
        inf_intermed = getattr(self._inf, "infIntermed", None) if self._inf else None
        if not inf_intermed:
            return None
        ind_pres = _v(getattr(self._ide, "indPres", None))
        if ind_pres not in ("2", "3", "4", "9"):
            return self._err(
                "YB01-20",
                439,
                "Rej.",
                "Rejeição: indPres incompatível com operação intermediada",
                "ide/indPres",
            )
        return None

    def validation_obrig_rej_440_yb02_10(self) -> ValidationResult:
        """YB02-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado o CNPJ do intermediador da transação -
        Verificar CNPJ com zeros, nulo ou DV inválido (Incluída na NT 2020.006
        Erro: 440: Rejeição: CNPJ do intermediador da transação inválido
        """
        if not self._is_nfe():
            return None
        inf_intermed = getattr(self._inf, "infIntermed", None) if self._inf else None
        if not inf_intermed:
            return None
        cnpj = getattr(inf_intermed, "CNPJ", None)
        if cnpj and not validate_cnpj(str(cnpj)):
            return self._err(
                "YB02-10",
                440,
                "Rej.",
                "Rejeição: CNPJ do Intermediador inválido",
                "infIntermed/CNPJ",
            )
        return None

    # ============================================================
    # Group ZA
    # ============================================================

    def validation_obrig_rej_355_za01_10(self) -> ValidationResult:
        """ZA01-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Não informado o local embarque ou de transposição de
        fronteira (tag:exporta) na operação de exportação (tpNF=1 e idDest=3)
        Erro: 355: Rejeição: Informar o local de saída do Pais no caso da exportação
        """
        if not self._is_nfe():
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        if id_dest != "3":
            return None
        if not self._inf or not getattr(self._inf, "exporta", None):
            return self._err(
                "ZA01-10",
                355,
                "Rej.",
                "Rejeição: Grupo exporta obrigatório para operação com Exterior",
                "exporta",
            )
        return None

    def validation_obrig_rej_356_za01_20(self) -> ValidationResult:
        """ZA01-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Informado o local embarque ou de transposição de fronteira
        (tag:exporta) em operação que não é de exportação (tpNF=0 ou idDest<>3)
        Erro: 356: Rejeição: Informar o local de saída do Pais somente no caso da
        exportação
        """
        if not self._is_nfe():
            return None
        if not self._inf or not getattr(self._inf, "exporta", None):
            return None
        id_dest = _v(getattr(self._ide, "idDest", None))
        if id_dest != "3":
            has_export_cfop = any(
                is_cfop_exterior(
                    str(getattr(getattr(i, "prod", None), "CFOP", "") or "")
                )
                for i in self._det
                if getattr(i, "prod", None)
            )
            if not has_export_cfop:
                return self._err(
                    "ZA01-20",
                    356,
                    "Rej.",
                    "Rejeição: Grupo exporta informado em operação não destinada ao Exterior",
                    "exporta",
                )
        return None

    def validation_obrig_rej_814_za01_30(self) -> ValidationResult:
        """ZA01-30.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Informado grupo de comércio exterior (tag: exporta): - NFC-e
        com grupo de exportação (NT 2015.002)
        Erro: 814: Rejeição: Nota Fiscal com grupo de comércio exterior
        """
        if not self._is_nfce():
            return None
        if self._inf and getattr(self._inf, "exporta", None):
            return self._err(
                "ZA01-30",
                814,
                "Rej.",
                "Rejeição: NFC-e com grupo de comércio exterior",
                "exporta",
            )
        return None

    # ============================================================
    # Group ZB
    # ============================================================

    def validation_obrig_rej_762_zb01_10(self) -> ValidationResult:
        """ZB01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados de compras (Empenho, Pedido, Contrato)
        (tag:compra)
        Erro: 762: Rejeição: NFC-e com dados de compras (Empenho, Pedido, Contrato)
        """
        if not self._is_nfce():
            return None
        if self._inf and getattr(self._inf, "compra", None):
            return self._err(
                "ZB01-10", 762, "Rej.", "Rejeição: NFC-e com dados de compras", "compra"
            )
        return None

    def validation_facul_rej_359_zb02_10(self) -> ValidationResult:
        """ZB02-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: NF-e com desoneração de ICMS motivada por venda a Órgão
        Públlico (tag:ICMSxx/motDesICMS=8; id:N28), sem informar Nota de Empenho.
        Observação: Implementação opcional, a critério da UF.
        Erro: 359: Rejeição: NF-e de venda a Órgão Público sem informar a Nota de
        Empenho
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for ZB02-10
        return None

    def validation_facul_rej_360_zb02_20(self) -> ValidationResult:
        """ZB02-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: NF-e com Nota de Empenho inválida para a UF. Observação:
        Implementação opcional, a critério da UF.
        Erro: 360: Rejeição: NF-e com Nota de Empenho inválida para a UF.
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for ZB02-20
        return None

    def validation_facul_rej_361_zb02_30(self) -> ValidationResult:
        """ZB02-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: NF-e com Nota de Empenho inexistente para a UF. Observação:
        Implementação opcional, a critério da UF.
        Erro: 361: Rejeição: NF-e com Nota de Empenho inexistente na UF.
        """
        if not self._is_nfe():
            return None
        # TODO: implement validation logic for ZB02-30
        return None

    # ============================================================
    # Group ZC
    # ============================================================

    def validation_obrig_rej_763_zc01_10(self) -> ValidationResult:
        """ZC01-10.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: NFC-e com dados de aquisição de Cana (tag:cana)
        Erro: 763: Rejeição: NFC-e com dados de aquisição de Cana
        """
        if not self._is_nfce():
            return None
        if self._inf and getattr(self._inf, "cana", None):
            return self._err(
                "ZC01-10",
                763,
                "Rej.",
                "Rejeição: NFC-e com dados de aquisição de Cana",
                "cana",
            )
        return None

    # ============================================================
    # Group ZD
    # ============================================================

    def validation_facul_rej_972_zd01_10(self) -> ValidationResult:
        """ZD01-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Não informado o grupo de informações do responsável técnico
        Observação: Implementação futura, exceto as UF de AM, MS, PE, PR, SC e TO, nas
        quais estas regras já estão em vigor em ambiente de teste e entrarão em vigor em
        ambiente de produção no dia 03 de junho de 2019 (NT 2018.005 v 1.30)
        Erro: 972: Rejeição: Obrigatória as informações do responsável técnico
        """
        # TODO: implement validation logic for ZD01-10
        return None

    def validation_facul_rej_973_zd02_10(self) -> ValidationResult:
        """ZD02-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Informado CNPJ do responsável técnico inválido - CNPJ com
        zeros, nulo ou DV inválido Observação: Implementação futura, exceto as UF de AM,
        MS, PE, PR, SC e TO, nas quais estas regras já estão em vigor em ambiente de
        teste e entrarão em vigor em ambiente de produção no dia 03 de junho de 2019 (NT
        2018.005 v 1.30)
        Erro: 973: Rejeição: CNPJ do responsável técnico inválido
        """
        inf_resp_tec = getattr(self._inf, "infRespTec", None) if self._inf else None
        if not inf_resp_tec:
            return None
        cnpj = getattr(inf_resp_tec, "CNPJ", None)
        if cnpj and not validate_cnpj(str(cnpj)):
            return self._err(
                "ZD02-10",
                973,
                "Rej.",
                "Rejeição: CNPJ do Responsável Técnico inválido",
                "infRespTec/CNPJ",
            )
        return None

    def validation_facul_rej_975_zd07_10(self) -> ValidationResult:
        """ZD07-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Obrigatória a informação do identificador do CSRT (tag:
        idCSRT) e Hash do CSRT (tag: hashCSRT) Observação: Implementação futura, todas
        as UFs (NT 2018.005 v1.30)
        Erro: 975: Rejeição: Obrigatória a informação do identificador do CSRT e do Hash
        do CSRT
        """
        # TODO: implement validation logic for ZD07-10
        return None

    # ============================================================
    # Group 1C
    # ============================================================

    def validation_facul_rej_935_1c03_10(self) -> ValidationResult:
        """1C03-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Razão Social (tag: emitxNome) do emitente diverge do
        informado no cadastro da SEFAZ. Observação: Regra de validação opcional, a
        critério da UF. (NT 2019.001 v1.50)
        Erro: 935: Rejeição: Razão Social do emitente diverge do informado no cadastro
        da SEFAZ
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_230_1c17_10(self) -> ValidationResult:
        """1C17-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - Acessar Cadastro de
        Contribuinte da UF (Chave: IE Emitente) - IE Emitente não cadastrada
        Erro: 230: Rejeição: IE do emitente não cadastrada
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_231_1c17_20(self) -> ValidationResult:
        """1C17-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - IE Emitente não vinculada ao
        CNPJ (se informado CNPJ emitente, tratar Regime Especial de IE Única)
        Erro: 231: Rejeição: IE do emitente não vinculada ao CNPJ
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_622_1c17_30(self) -> ValidationResult:
        """1C17-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - IE emitente não vinculada ao
        CPF (se informado CPF emitente)
        Erro: 622: Rejeição: IE emitente não vinculada ao CPF
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_203_1c17_34(self) -> ValidationResult:
        """1C17-34.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - Emitente não autorizado para
        emissão de NF-e
        Erro: 203: Rejeição: Emissor não habilitado para emissão da NF-e
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_781_1c17_38(self) -> ValidationResult:
        """1C17-38.

        Modelo: 65
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - Emitente não autorizado para
        emissão de NFC-e
        Erro: 781: Rejeição: Emissor não habilitado para emissão da NFC-e
        """
        if not self._is_nfce():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_den_301_1c17_40(self) -> ValidationResult:
        """1C17-40.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Emitente: - Emitente em situação
        irregular perante o Fisco
        Erro: 301: Uso Denegado: Irregularidade fiscal do emitente
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_230_1c17_50(self) -> ValidationResult:
        """1C17-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se IE do Emitente = "ISENTO" (unicamente para Nota Fiscal
        Avulsa): - Se não for NF-e Avulsa (excluída na NT 2018.001)
        Erro: 230: Rejeição: IE do emitente não cadastrada
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_245_1c17_60(self) -> ValidationResult:
        """1C17-60.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Mensagens opcionais no caso de IE não vinculada ao CNPJ/CPF.
        - Acessar Cadastro de Pessoa Jurídica ou Pessoa Física: - CNPJ emitente não
        cadastrado
        Erro: 245: Rejeição: CNPJ Emitente não cadastrado
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_621_1c17_70(self) -> ValidationResult:
        """1C17-70.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Mensagens opcionais no caso de IE não vinculada ao CNPJ/CPF.
        - Acessar Cadastro de Pessoa Jurídica ou Pessoa Física: - CPF Emitente não
        cadastrado (NT 2011/004)
        Erro: 621: Rejeição: CPF Emitente não cadastrado
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 2AB
    # ============================================================

    def validation_obrig_rej_692_2ab08_10(self) -> ValidationResult:
        """2AB08-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Acesso ao BD Evento EPEC (Chave: Modelo, UF, CNPJ ou CPF
        Emitente, Série, Nro): - Se existe EPEC: - Se Tipo Emissão da NF-e <> 4
        Erro: 692: Rejeição: Existe EPEC registrado para esta Série e Número [Chave
        EPEC: xxxxxxxxxxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_691_2ab08_20(self) -> ValidationResult:
        """2AB08-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: - Chave de Acesso da NF-e diverge da Chave de Acesso do EPEC
        Erro: 691: Rejeição: Chave de Acesso da NF-e diverge da Chave de Acesso do EPEC
        [Chave EPEC: xxxxxxxxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_467_2ab08_30(self) -> ValidationResult:
        """2AB08-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: - Verificar divergência entre os dados da NF-e e os dados do
        EPEC (*1)
        Erro: 467: Rejeição: Dados da NF-e divergentes do EPEC [tag: xxxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_468_2ab08_40(self) -> ValidationResult:
        """2AB08-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: - Se não existe EPEC: - Se Tipo Emissão da NF-e=4-EPEC e
        Data Emissão NF-e > Data da desativação do DPEC (01/04/2015) (NT 2018.001/NT
        2014.001 v1.20)
        Erro: 468: Rejeição: NF-e com Tipo Emissão = 4, sem EPEC correspondente.
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 2B
    # ============================================================

    def validation_facul_rej_539_2b08_10(self) -> ValidationResult:
        """2B08-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Modelo 55: Acesso BD NFE (Chave: Modelo, UF, CNPJ/CPF
        Emitente, Série, Número): - NF-e já cadastrada, com diferença na Chave de Acesso
        (Código Numérico ou outras posições da Chave de Acesso). (NT 2011/004) Modelo
        65: Acesso BD NFE (Chave: Modelo, UF, CNPJ Emitente, Série, Número, Tipo de
        Emissão): - NF-e já cadastrada, com diferença na Chave de Acesso (Código
        Numérico ou outras posições da Chave de Acesso). (NT 2011/004) (NT 2018.001
        v1.10)
        Erro: 539: Rejeição: Duplicidade de NF-e com diferença na Chave de Acesso
        [chNFe: 99999999999999999999999999999999999999999999][nRec:9999999999999 99]
        Observação: Na resposta assíncrona, a SEFAZ pode devolver o nREC - Número do
        Recibo do Lote caso tenha condições.
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_204_2b08_20(self) -> ValidationResult:
        """2B08-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Acesso BD NFE (Chave: Modelo, UF, CNPJ/CPF Emitente, Série,
        Número): - NF-e já cadastrada e não Cancelada/Denegada Observação 1: Na resposta
        assíncrona, a SEFAZ pode devolver o nREC - Número do Recibo do Lote caso tenha
        condições. Observação 2: A critério da UF, no caso do DigestValue ser igual a
        NF-e autorizada, poderá retornar o protocolo de Autorização. (NT 2018.005 v1.30
        / NT 2018.001 v1.10)
        Erro: 204: Rejeição: Duplicidade de NF-e [nRec:999999999999999] Observação: Na
        resposta assíncrona, concatenar na mensagem de erro o Número do Recibo do Lote
        (opcional).
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_218_2b08_30(self) -> ValidationResult:
        """2B08-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Acesso BD NFE (Chave: Modelo, UF, CNPJ/CPF Emitente, Série,
        Número): - NF-e já cadastrada e está Cancelada (NT 2018.001)
        Erro: 218: Rejeição: NF-e já está cancelada na base de dados da SEFAZ
        [nRec:999999999999999] Observação: Na resposta assíncrona, a SEFAZ pode devolver
        o nREC - Número do Recibo do Lote caso tenha condições.
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_205_2b08_40(self) -> ValidationResult:
        """2B08-40.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Acesso BD NFE (Chave: Modelo, UF, CNPJ/CPF Emitente, Série,
        Número): - NF-e já cadastrada e está Denegada (NT 2018.001)
        Erro: 205: Rejeição: NF-e está denegada na base de dados da SEFAZ
        [nRec:999999999999999] Observação: Na resposta assíncrona, a SEFAZ pode devolver
        o nREC - Número do Recibo do Lote caso tenha condições.
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_635_2b08_50(self) -> ValidationResult:
        """2B08-50.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Acesso BD NFE (Chave: Modelo, UF, CNPJ/CPF Emitente, Série,
        Número): NF-e com mesmo número e série já transmitida e aguardando processamento
        (NT 2011/004) Observação: Verificação necessária para algumas UF. (NT 2018.001)
        Erro: 635: Rejeição: NF-e com mesmo número e série já transmitida e aguardando
        processamento
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 3B
    # ============================================================

    def validation_obrig_rej_206_3b08_100(self) -> ValidationResult:
        """3B08-100.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Acesso BD de Inutilização (Chave: Modelo, UF, CNPJ/CPF,
        Série, Número): - Numeração da NF-e está inutilizada (NT 2011/004) (NT 2018.001)
        Erro: 206: Rejeição: NF-e já está inutilizada na Base de Dados da SEFAZ
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 3BA
    # ============================================================

    def validation_facul_rej_267_3ba02_10(self) -> ValidationResult:
        """3BA02-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF-e referenciada (tag:refNFe), se a UF da Chave
        de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de
        Acesso referenciada (se mod=55) - NF-e referenciada inexistente Exceção: A NF-e
        referenciada pode não existir no caso de Emissão em Contingência (tpEmis = 2, 4
        ou 5) (NT 2013/003) Observação: A exceção acima não se aplica para “finNFe=2"
        (NF-e Complementar).
        Erro: 267: Rejeição: Chave de Acesso referenciada inexistente [nRef: xxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_268_3ba02_20(self) -> ValidationResult:
        """3BA02-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF-e referenciada (tag:refNFe), se a UF da Chave
        de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de
        Acesso referenciada (se mod=55) - NF-e Complementar (finNFe=2) referencia uma
        outra NF-e Complementar (finNFe=2)
        Erro: 268: Rejeição: NF Complementar referencia uma outra NF-e Complementar
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_686_3ba02_30(self) -> ValidationResult:
        """3BA02-30.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF-e referenciada (tag:refNFe), se a UF da Chave
        de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de
        Acesso referenciada (se mod=55) - NF-e Complementar (finNFe=2) referencia uma
        NF-e cancelada (NT 2013/003)
        Erro: 686: Rejeição: NF Complementar referencia uma NF-e cancelada
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_687_3ba02_40(self) -> ValidationResult:
        """3BA02-40.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF-e referenciada (tag:refNFe), se a UF da Chave
        de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de
        Acesso referenciada (se mod=55) - NF-e Complementar (finNFe=2) referencia uma
        NF-e denegada (NT 2013/003)
        Erro: 687: Rejeição: NF Complementar referencia uma NF-e denegada
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_688_3ba15_10(self) -> ValidationResult:
        """3BA15-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF de Produtor referenciada (tag:refNFP), se a
        Nota Fiscal referenciada for da própria UF (tag:refNFP/cUF): - Acessar Cadastro
        da SEFAZ: - IE de Produtor inexistente (NT 2013/003)
        Erro: 688: Rejeição: NF referenciada de Produtor com IE inexistente [nRef: xxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_689_3ba15_20(self) -> ValidationResult:
        """3BA15-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada NF de Produtor referenciada (tag:refNFP), se a
        Nota Fiscal referenciada for da própria UF (tag:refNFP/cUF): - Acessar Cadastro
        da SEFAZ: - IE de Produtor não vinculada ao CNPJ / CPF (NT 2013/003)
        Erro: 689: Rejeição: NF referenciada de Produtor com IE não vinculada ao
        CNPJ/CPF informado [nRef: xxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 4I
    # ============================================================

    def validation_facul_rej_357_4i54_10(self) -> ValidationResult:
        """4I54-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada Chave de Acesso citada na Exportação Indireta
        (tag:detExport/exportInd/chNFe), se a UF da Chave de Acesso citada for igual a
        UF do Emitente: - Acessar BD NFE com Chave de Acesso (mod=55) - NF-e inexistente
        Erro: 357: Rejeição: Chave de Acesso do grupo de Exportação Indireta inexistente
        [nRef: xxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_358_4i54_20(self) -> ValidationResult:
        """4I54-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Para cada Chave de Acesso citada na Exportação Indireta
        (tag:detExport/exportInd/chNFe), se a UF da Chave de Acesso citada for igual a
        UF do Emitente: - Acessar BD NFE com Chave de Acesso (mod=55) - NF-e cancelada /
        denegada
        Erro: 358: Rejeição: Chave de Acesso do grupo de Exportação Indireta cancelada
        ou denegada [nRef: xxx]
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 5E
    # ============================================================

    def validation_obrig_rej_233_5e17_10(self) -> ValidationResult:
        """5E17-10.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informada IE do Destinatário: - Acessar Cadastro de
        Contribuinte da UF (Chave: UF Dest, IE Dest.) (*5) - IE destinatário não
        cadastrada (*7) (NT 2019.001 v1.00)
        Erro: 233: Rejeição: IE do destinatário não cadastrada
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_234_5e17_20(self) -> ValidationResult:
        """5E17-20.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CNPJ do destinatário e IE destinatário não
        vinculada ao CNPJ (tratar Regime Especial de IE Única) (NT 2019.001 v1.00)
        Erro: 234: Rejeição: IE do destinatário não vinculada ao CNPJ
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_624_5e17_30(self) -> ValidationResult:
        """5E17-30.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se informado CPF do destinatário e IE destinatário não
        vinculada ao CPF (*7) (NT 2019.001 v1.00)
        Erro: 624: Rejeição: IE Destinatário não vinculada ao CPF
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_den_302_5e17_40(self) -> ValidationResult:
        """5E17-40.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Destinatário em situação irregular perante o Fisco, vedada
        operação na UF (CCC.cSitCNPJ=3-Vedado) (NT 2019.001 v1.00)
        Erro: 302: Uso Denegado: Irregularidade fiscal do destinatário
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_305_5e17_43(self) -> ValidationResult:
        """5E17-43.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado) (NT
        2019.001 v1.00)
        Erro: 305: Rejeição: Destinatário bloqueado na UF
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_306_5e17_46(self) -> ValidationResult:
        """5E17-46.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: IE do Destinatário não está ativa na UF (CCC.cSitIE=0-Não
        habilitado) (*7) (NT 2019.001 v1.00)
        Erro: 306: Rejeição: IE do destinatário não está ativa na UF
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_232_5e17_50(self) -> ValidationResult:
        """5E17-50.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: Se IE Destinatário não informada e informado CNPJ do
        destinatário: - Acessar Cadastro Contribuinte da UF (Chave: UF-Dest, CNPJ-Dest)
        (*6) - Destinatário possui IE ativa na UF (CCC.cSitIE=1-Habilitado) e
        CCC.IndIEDestOpc = 0 - Obrig.atório (NT 2019.001 v1.00)
        Erro: 232: Rejeição: IE do destinatário não informada
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_den_303_5e17_60(self) -> ValidationResult:
        """5E17-60.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: - Destinatário com CNPJ vedado na UF (CCC.cSitCNPJ=3-Vedado)
        (NT 2019.001 v1.00)
        Erro: 303: Uso Denegado: Destinatário não habilitado a operar na UF
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_305_5e17_63(self) -> ValidationResult:
        """5E17-63.

        Modelo: 55
        Aplicação: Obrig.
        Regra de Validação: - Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado)
        (NT 2019.001 v1.00)
        Erro: 305: Rejeição: Destinatário bloqueado na UF
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_246_5e17_70(self) -> ValidationResult:
        """5E17-70.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Mensagens opcionais se informada IE do destinatário e IE não
        vinculada ao CNPJ/CPF. - Acessar Cadastro de Pessoa Jurídica ou Pessoa Física: -
        CNPJ destinatário não cadastrado (NT 2019.001 v1.00)
        Erro: 246: Rejeição: CNPJ Destinatário não cadastrado
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_623_5e17_80(self) -> ValidationResult:
        """5E17-80.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: CPF destinatário não cadastrado (*7) (NT 2019.001 v1.00)
        Erro: 623: Rejeição: CPF Destinatário não cadastrado
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7B
    # ============================================================

    def validation_facul_rej_479_7b09_10(self) -> ValidationResult:
        """7B09-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Data de Emissão anterior a data de credenciamento do
        Contribuinte para a emissão de Nota Fiscal na UF, ou anterior a Data de Abertura
        do estabelecimento na UF. (NT 2015.002)
        Erro: 479: Rejeição: Data de Emissão anterior a data de credenciamento ou
        anterior a Data de Abertura do estabelecimento
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7C
    # ============================================================

    def validation_facul_rej_480_7c10_10(self) -> ValidationResult:
        """7C10-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Código do Município do Emitente diverge do cadastrado na UF
        (NT 2015.002)
        Erro: 480: Rejeição: Código Município do Emitente diverge do cadastrado na UF
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_481_7c21_10(self) -> ValidationResult:
        """7C21-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Código de Regime Tributário do emitente divergente do
        cadastrado na SEFAZ (tag:emit/CRT): - CRT=”1-Simples Nacional” para Contribuinte
        cadastrado como Regime Normal na UF; - CRT=”3-Regime Normal” para Contribuinte
        cadastrado como Simples Nacional na UF; Observação: Implementação futura. (NT
        2015.002)
        Erro: 481: Rejeição: Código Regime Tributário do emitente diverge do cadastro na
        SEFAZ
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7E
    # ============================================================

    def validation_facul_rej_482_7e10_10(self) -> ValidationResult:
        """7E10-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Código do Município do Destinatário diverge do cadastrado na
        UF (NT 2015.002)
        Erro: 482: Rejeição: Código do Município do Destinatário diverge do cadastrado
        na UF
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7GA
    # ============================================================

    def validation_facul_rej_486_7ga01_10(self) -> ValidationResult:
        """7GA01-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Não informado o Grupo de Autorização para obter o XML, para
        a UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal,
        conforme legislação estadual. Observação: Regra de Validação opcional, a
        critério da UF. (NT 2015.002)
        Erro: 486: Rejeição: Não informado o Grupo de Autorização para UF que exige a
        identificação do Escritório de Contabilidade na Nota Fiscal
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_487_7ga01_20(self) -> ValidationResult:
        """7GA01-20.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Verificar se o CNPJ/CPF informado na primeira ocorrência do
        Grupo de Autorização corresponde a um Escritório de Contabilidade cadastrado na
        SEFAZ, conforme legislação estadual. Observação: Regra de Validação opcional a
        critério da UF. (NT 2015.002)
        Erro: 487: Rejeição: Escritório de Contabilidade não cadastrado na SEFAZ
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7I
    # ============================================================

    def validation_obrig_rej_889_7i03_10(self) -> ValidationResult:
        """7I03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se não informado GTIN (cEAN=Nulo). Observação: Para produtos
        que não possuem GTIN, utilizar a informação de "SEM GTIN" (NT 2017.001)
        Erro: 889: Rejeição: Obrigatória a informação do GTIN para o produto [nItem:
        999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 7ZD
    # ============================================================

    def validation_facul_rej_974_7zd02_10(self) -> ValidationResult:
        """7ZD02-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: CNPJ do responsável técnico diverge do cadastrado para o
        emitente (UF/CNPJ). Observação: Implementação futura (NT 2018.005 v1.30)
        Erro: 974: Rejeição: CNPJ do responsável técnico diverge do cadastrado
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_976_7zd08_10(self) -> ValidationResult:
        """7ZD08-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Identificador do CSRT (tag: idCSRT) não cadastrado na SEFAZ.
        Observação: Implementação futura (NT 2018.005 v1.30)
        Erro: 976: Rejeição: Identificador do CSRT não cadastrado na SEFAZ
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_977_7zd08_20(self) -> ValidationResult:
        """7ZD08-20.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Identificador do CSRT (tag: idCSRT) revogado. Observação:
        Implementação futura (NT 2018.005 v1.30)
        Erro: 977: Rejeição: Identificador do CSRT revogado
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_facul_rej_978_7zd09_10(self) -> ValidationResult:
        """7ZD09-10.

        Modelo: 55/65
        Aplicação: Facul.
        Regra de Validação: Hash do CSRT (tag: hashCSRT) diverge do calculado.
        Observação: Implementação futura (NT 2018.005 v1.30)
        Erro: 978: Rejeição: Hash do CSRT diverge do calculado
        """
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 8C
    # ============================================================

    def validation_facul_rej_488_8c02_10(self) -> ValidationResult:
        """8C02-10.

        Modelo: 55
        Aplicação: Facul.
        Regra de Validação: Na Nota Fiscal de Saída, verificar se a soma das demais
        Notas Fiscais de Saída (vendas) do Emitente no período ultrapassa o limite anual
        de faturamento, conforme o Porte da Empresa. Observação 1: Regra de validação
        opcional a critério da UF. Observação 2: Considerar tolerância, conforme a
        legislação estadual. (NT 2015.002)
        Erro: 488: Rejeição: Vendas do Emitente incompatíveis com o Porte da Empresa
        """
        if not self._is_nfe():
            return None
        # Stub: requires external database (SEFAZ)
        return None

    # ============================================================
    # Group 9I
    # ============================================================

    def validation_obrig_rej_890_9i03_10(self) -> ValidationResult:
        """9I03-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN (tag: cEAN) com prefixo do Brasil
        (iniciado em 789 ou 790) e GTIN informado na NF-e inexistente no CCG. (NT
        2017.001)
        Erro: 890: Rejeição: GTIN inexistente no Cadastro Centralizado de GTIN (CCG)
        [nItem:999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_891_9i03_20(self) -> ValidationResult:
        """9I03-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN (tag: cEAN) com prefixo do Brasil
        (iniciado em 789 ou 790) e NCM informada na NF-e diferente da cadastrada no CCG
        (NT 2017.001)
        Erro: 891: Rejeição: GTIN incompatível com a NCM [nItem:999; NCM esperada:
        99999999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_892_9i03_30(self) -> ValidationResult:
        """9I03-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado o GTIN (tag: cEAN) com prefixo do Brasil
        (iniciado em 789 ou 790) e CEST informado na NF-e diferente do cadastrado no CCG
        (NT 2017.001)
        Erro: 892: Rejeição: GTIN incompatível com CEST [nItem:999; CEST esperado:
        9999999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_893_9i03_40(self) -> ValidationResult:
        """9I03-40.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN-14 (tag: cEAN>09999999999999) com prefixo
        do Brasil (iniciado em 789 ou 790) e informado GTIN da unidade tributável (tag:
        cEANTrib) diferente do GTIN Contido cadastrado no CCG Exceção: a RV não se
        aplica em operações com exterior (idDest=3) Nota: o GTIN pode possuir GTIN de
        nível inferior (GTIN Contido), agrupando diversas unidades do mesmo produto. O
        GTIN da unidade tributável deve corresponder àquele da menor unidade
        comercializável identificada por código GTIN, ou seja, deve corresponder ao GTIN
        do menor nível inferior (GTIN Contido). (NT 2017.001)
        Erro: 893: Rejeição: GTIN da unidade tributável diverge do GTIN Contido
        cadastrado no CCG [nItem:999; GTIN Contido esperado: 99999999999999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_894_9i12_10(self) -> ValidationResult:
        """9I12-10.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN da unidade tributável (tag: cEANTrib) com
        prefixo do Brasil (iniciado em 789 ou 790) e GTIN da unidade tributável
        informado na NF-e (tag: cEANTrib) inexistente no CCG. (NT 2017.001)
        Erro: 894: Rejeição: GTIN da unidade tributável inexistente no Cadastro
        Centralizado de GTIN (CCG) [nItem:999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_895_9i12_20(self) -> ValidationResult:
        """9I12-20.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN da unidade tributável (tag: cEANTrib) com
        prefixo do Brasil (iniciado em 789 ou 790) e NCM informada na NF-e diferente da
        cadastrada no CCG (NT 2017.001)
        Erro: 895: Rejeição: GTIN da unidade tributável incompatível com a NCM
        [nItem:999; NCM esperada: 99999999]
        """
        # Stub: requires external database (SEFAZ)
        return None

    def validation_obrig_rej_896_9i12_30(self) -> ValidationResult:
        """9I12-30.

        Modelo: 55/65
        Aplicação: Obrig.
        Regra de Validação: Se informado GTIN da unidade tributável (tag: cEANTrib) com
        prefixo do Brasil (iniciado em 789 ou 790) e CEST informado na NF-e diferente do
        cadastrado no CCG (NT 2017.001)
        Erro: 896: Rejeição: GTIN da unidade tributável incompatível com CEST
        [nItem:999; CEST esperado: 9999999]
        """
        # Stub: requires external database (SEFAZ)
        return None
