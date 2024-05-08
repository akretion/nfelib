nfelib - bindings Python para e ler e gerir XML de NF-e, NFS-e nacional, CT-e, MDF-e, BP-e
===
<p align="center">
<a href="https://akretion.com/pt-BR" > 
 <img src="https://raw.githubusercontent.com/akretion/nfelib/master/ext/nfelib.jpg"/>
</a>
</p>

<p align="center">
<a href="https://codecov.io/gh/akretion/nfelib" > 
 <img src="https://codecov.io/gh/akretion/nfelib/branch/master/graph/badge.svg?token=IqcCHJzhuw"/>
</a>
<a href="https://pypi.org/project/nfelib/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nfelib"></a>
<a href="https://pepy.tech/project/nfelib"><img alt="Downloads" src="https://pepy.tech/badge/nfelib"></a>
</p>


## Porque escolher a nfelib

* **Simples e confiável**. As outras bibliotecas costumam ter dezenas de milhares de linhas de código feito tudo manualmente para fazer o que o nfelib faz tudo automaticamente com algumas linhas para gerir código com o [xsdata](https://xsdata.readthedocs.io/) a partir dos últimos pacotes xsd da Fazenda. O xsdata é uma biblioteca de databinding extremamente bem escrita e bem testada. A própria nfelib tem testes para ler e gerir todos documentos fiscais.
* **Completa**: já que gerir os bindings ficou trivial, a nfelib mantém atualizada todos os bindings para interagir com todos os serviços e eventos de NF-e, NFS-e nacional, CT-e, MDF-e, BP-e. Os testes detetam também quando sai uma nova versão de algum esquema.


## Instalação

```bash
pip install nfelib
```

## Como usar

**NF-e**
```python
>>> # Ler o XML de uma NF-e:
>>> from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc
>>> nfe_proc = NfeProc.from_path("nfelib/nfe/samples/v4_0/leiauteNFe/NFe35200159594315000157550010000000012062777161.xml")
>>> # (pode ser usado também o metodo from_xml(xml) )
>>>
>>> nfe_proc.NFe.infNFe.emit.CNPJ
'59594315000157'
>>> nfe_proc.NFe.infNFe.emit
Tnfe.InfNfe.Emit(CNPJ='59594315000157', CPF=None, xNome='Akretion LTDA', xFant='Akretion', enderEmit=TenderEmi(xLgr='Rua Paulo Dias', nro='586', xCpl=None, xBairro=None, cMun='3501152', xMun='Alumínio', UF=<TufEmi.SP: 'SP'>, CEP='18125000', cPais=<TenderEmiCPais.VALUE_1058: '1058'>, xPais=<TenderEmiXPais.BRASIL: 'Brasil'>, fone='2130109965'), IE='755338250133', IEST=None, IM=None, CNAE=None, CRT=<EmitCrt.VALUE_1: '1'>)
>>> nfe_proc.NFe.infNFe.emit.enderEmit.UF.value
'SP'
>>>
>>> # Serializar uma NF-e:
>>> nfe_proc.to_xml()
'<?xml version="1.0" encoding="UTF-8"?>\n<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">\n  <NFe>\n    <infNFe versao="4.00" Id="35200159594315000157550010000000012062777161">\n      <ide>\n        <cUF>35</cUF>\n        <cNF>06277716</cNF>\n        <natOp>Venda</natOp>\n        <mod>55</mod>\n        <serie>1</serie>\n        <nNF>1</nNF>\n        <dhEmi>2020-01-01T12:00:00+01:00</dhEmi>\n        <dhSaiEnt>2020-01-01T12:00:00+01:00</dhSaiEnt>\n        <tpNF>1</tpNF>\n        <idDest>1</idDest>\n [...]
>>>
>>> # Montar uma NFe do zero:
>>> from nfelib.nfe.bindings.v4_0.nfe_v4_00 import Nfe
>>> nfe=Nfe(infNFe=Nfe.InfNfe(emit=Nfe.InfNfe.Emit(xNome="Minha Empresa", CNPJ='59594315000157')))
>>> nfe
Nfe(infNFe=Tnfe.InfNfe(ide=None, emit=Tnfe.InfNfe.Emit(CNPJ='59594315000157', CPF=None, xNome='Minha Empresa', xFant=None, enderEmit=None, IE=None, IEST=None, IM=None, CNAE=None, CRT=None), avulsa=None, dest=None, retirada=None, entrega=None, autXML=[], det=[], total=None, transp=None, cobr=None, pag=None, infIntermed=None, infAdic=None, exporta=None, compra=None, cana=None, infRespTec=None, infSolicNFF=None, versao=None, Id=None), infNFeSupl=None, signature=None)
>>> 
>>> # Validar o XML de uma nota:
>>> nfe.validate_xml()
["Element '{http://www.portalfiscal.inf.br/nfe}infNFe': The attribute 'versao' is required but missing.", "Element '{http://www.portalfiscal.inf.br/nfe}infNFe': The attribute 'Id' is required but missing." [...]
```

Assinar o XML de uma nota usando a lib [erpbrasil.assinatura](https://github.com/erpbrasil/erpbrasil.assinatura) (funciona com os outros documentos eletrônicos também)
```
>>> # Assinar o XML de uma nota:
>>> with open(path_to_your_pkcs12_certificate, "rb") as pkcs12_buffer:
    pkcs12_data = pkcs12_buffer.read()
>>> signed_xml = nfe.sign_xml(xml, pkcs12_data, cert_password, nfe.NFe.infNFe.Id)
```

Imprimir o DANFE usando a lib [BrazilFiscalReport](https://github.com/Engenere/BrazilFiscalReport) ou a lib [erpbrasil.edoc.pdf](https://github.com/erpbrasil/erpbrasil.edoc.pdf) (futuramente BrazilFiscalReport deve imprimir o pdf de outros documentos eletrônicos também; erpbrasil.edoc.pdf é uma lib mais 'legacy')
```
>>> # Imprimir o pdf de uma nota usando BrazilFiscalReport:
>>> pdf_bytes = nfe.to_pdf()
>>> # Imprimir o pdf de uma nota usando erpbrasil.edoc.pdf:
>>> pdf_bytes = nfe.to_pdf(engine="erpbrasil.edoc.pdf")
>>> # Ou então para imprimir e assinar junto:
>>> pdf_bytes = nfe.to_pdf(
    pkcs12_data=cert_data,
    pkcs12_password=cert_password,
    doc_id=nfe.NFe.infNFe.Id,
    )
```

**NFS-e padrão nacional**
```python
>>> # Ler uma NFS-e:
>>>> from nfelib.nfse.bindings.v1_0.nfse_v1_00 import Nfse
>>> nfse = Nfse.from_path("alguma_nfse.xml")
>>>
>>> # Serializar uma NFS-e:
>>> nfse.to_xml()
>>> # Ler uma DPS:
>>>> from nfelib.nfse.bindings.v1_0.dps_v1_00 import Dps
>>> dps = Nfse.from_path("nfelib/nfse/samples/v1_0/GerarNFSeEnvio-env-loterps.xml")
>>>
>>> # Serializar uma DPS:
>>> dps.to_xml()
```

**MDF-e**
```python
>>> # Ler um MDF-e:
>>>> from nfelib.mdfe.bindings.v3_0.mdfe_v3_00 import Mdfe
>>> mdfe = Mdfe.from_path("nfelib/mdfe/samples/v3_0/ComPagtoPIX_41210780568835000181580010402005751006005791-procMDFe.xml")
>>>
>>> # Serializar um MDF-e:
>>> mdfe.to_xml()
```

**CT-e**
```python
>>> # Ler um CT-e:
>>>> from nfelib.cte.bindings.v4_0.cte_v4_00 import Cte
>>> cte = Cte.from_path("nfelib/cte/samples/v4_0/43120178408960000182570010000000041000000047-cte.xml")
>>>
>>> # Serializar um CT-e:
>>> cte.to_xml()
```

**BP-e**
```python
>>> # Ler um BP-e:
>>>> from nfelib.bpe.bindings.v1_0.bpe_v1_00 import Bpe
>>> bpe = Bpe.from_path("algum_bpe.xml")
>>>
>>> # Serializar um BP-e:
>>> bpe.to_xml()
```


## Desenvolvimento / testes

Para rodar os testes:

```bash
pytest
```

Para atualizar os bindings:

1. baixar o novo zip dos esquemas e atualizar a pasta ```nfelib/<nfe|nfse|cte|mdfe|bpe>/schemas/<versao>/```
2. gerir os bindings de um pacote de esquemas xsd, por examplo da NF-e:

    ```bash
    xsdata generate nfelib/nfe/schemas/v4_0 --package nfelib.nfe.bindings.v4_0
    ```

Para gerir todos bindings com xsdata:

```bash
./script.sh
```

## Versões dos esquemas e pastas

A nfelib usa apenas 2 dígitos para caracterizar a versão. Isso foi decidido observando que a Fazenda nunca usa o terceiro dígito da versão e que a mudança do segundo dígito já caracteriza uma mudança maior. Nisso qualquer alteração de esquema que não mudar o primeiro nem o segundo dígito da versão do esquema vai na mesma pasta e se sobreponha a antiga versão, assumindo que é possível usar o mais novo esquema no lugar do antigo (por exemplo é possível ler uma NFe 4.00 pacote nº 9j (NT 2022.003 v.1.00b) com os bindings da versão nfe pacote nº 9k (NT 2023.001 v.1.20).

Pelo contrário, caso houver uma mudança maior afetando os 2 primeiros dígitos como NFe 3.0 e NFe 3.1 ou NFe 3.1 e NFe 4.0, será possível também suportar as várias versões ao mesmo tempo usando pastas diferentes. Assim seria possível por exemplo emitir a futura NFe 5.0 e ainda importar uma NFe 4.0.
