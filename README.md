nfelib — the Python library for Brazilian electronic invoicing
==============================================================

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


nfelib covers the full life-cycle of the Brazilian electronic fiscal documents
(DF-e): parse, build, sign, validate, transmit to the SEFAZ webservices and
print:

| Document | Parse / build / sign / validate | Transmission | PDF |
|----------|---------------------------------|--------------|-----|
| **NF-e / NFC-e** (invoices) | yes | SOAP: authorize, cancel, CC-e, inutilização, consultation, MD-e events, DistDFe | DANFE |
| **CT-e** (freight) | yes | SOAP: authorize (synchronous) | DACTE |
| **MDF-e** (manifest) | yes | SOAP: authorize (synchronous), cancel, encerramento, consultation | DAMDFE |
| **NFS-e** (national standard) | yes | REST: DPS submission, NFS-e and event consultation, cancelling | DANFSE |
| **NF3e / NFCom** (energy / telecom) | yes | — | — |
| **BP-e** (passenger transport) | yes | — | — |

Our goal is to make nfelib the default Python library for electronic
invoicing in Brazil. The library is used extensively by the
[OCA/l10n-brazil](https://github.com/OCA/l10n-brazil) localization for Odoo
(ERP). nfelib delegates the PDF rendering to the free
[BrazilFiscalReport](https://github.com/Engenere/BrazilFiscalReport) project,
maintained by friends of nfelib, which draws DANFE, DACTE, DACTE-OS and DAMDFE.


## Why nfelib?

* **Simple and reliable.** Other libraries maintain tens of thousands of
  lines of hand-written code to do what nfelib does with a few lines: it
  generates its databindings from the official Fazenda XSD packages with
  [xsdata](https://xsdata.readthedocs.io/), an extremely well written and
  tested data binding library. nfelib itself round-trip tests every document
  type it supports.
* **Complete and current.** Because regenerating bindings is trivial, nfelib
  tracks every Fazenda release package for NF-e, NFS-e, CT-e, MDF-e and BP-e —
  documents *and* their events — and its test suite detects when a new schema
  package is published.
* **Everything in one place.** Bindings, XML signing (A1 certificates),
  schema validation, SOAP transmission clients and PDF printing compose into a
  single pipeline; you no longer need to glue several libraries together.

nfelib focuses on electronic invoicing. Its generator can technically bind any
official XSD package, but we deliberately scope support to the DF-e schemas
for now so they stay complete and battle-tested.


## Installation

```bash
pip install nfelib
```

Optional features (install only what you need):

```bash
pip install nfelib[sign]   # XML signing with A1 certificates
pip install nfelib[pdf]    # PDF printing (BrazilFiscalReport)
pip install nfelib[soap]   # SOAP transmission clients (NF-e, CT-e, MDF-e)
pip install nfelib[nfse]   # REST client for the national NFS-e (ADN)
```


## Usage

**NF-e**

```python
>>> # Parse an NF-e:
>>> from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc
>>> nfe_proc = NfeProc.from_path("nfelib/nfe/samples/v4_0/leiauteNFe/NFe35200159594315000157550010000000012062777161.xml")
>>> # (from_xml(xml) also works)
>>>
>>> nfe_proc.NFe.infNFe.emit.CNPJ
'59594315000157'
>>> nfe_proc.NFe.infNFe.emit.enderEmit.UF.value
'SP'
>>>
>>> # Serialize an NF-e:
>>> nfe_proc.to_xml()
'<?xml version="1.0" encoding="UTF-8"?>\n<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"> [...]'
>>>
>>> # Build an NF-e from scratch:
>>> from nfelib.nfe.bindings.v4_0.nfe_v4_00 import Nfe
>>> nfe = Nfe(infNFe=Nfe.InfNfe(emit=Nfe.InfNfe.Emit(xNome="My Company", CNPJ="59594315000157")))
>>>
>>> # Validate the XML against the official schemas:
>>> nfe.validate_xml()
["Element '{http://www.portalfiscal.inf.br/nfe}infNFe': The attribute 'versao' is required but missing.", ...]
```

Sign the XML of a document with an A1 certificate
([erpbrasil.assinatura](https://github.com/erpbrasil/erpbrasil.assinatura),
works with every document type):

```python
>>> with open(path_to_your_pkcs12_certificate, "rb") as pkcs12_buffer:
...     pkcs12_data = pkcs12_buffer.read()
>>> signed_xml = nfe.sign_xml(xml, pkcs12_data, cert_password, nfe.NFe.infNFe.Id)
```

Print the DANFE PDF with
[BrazilFiscalReport](https://github.com/Engenere/BrazilFiscalReport) — which
also prints the CT-e (DACTE/DACTE-OS) and the MDF-e (DAMDFE):

```python
>>> pdf_bytes = nfe.to_pdf()
>>> # Or sign and print at once:
>>> pdf_bytes = nfe.to_pdf(
...     pkcs12_data=cert_data,
...     pkcs12_password=cert_password,
...     doc_id=nfe.NFe.infNFe.Id,
... )
```

**NFS-e (national standard)**

```python
>>> # Parse an NFS-e:
>>> from nfelib.nfse.bindings.v1_0.nfse_v1_00 import Nfse
>>> nfse = Nfse.from_path("alguma_nfse.xml")
>>>
>>> # Serialize an NFS-e:
>>> nfse.to_xml()
>>> # Parse a DPS:
>>> from nfelib.nfse.bindings.v1_0.dps_v1_00 import Dps
>>> dps = Dps.from_path("nfelib/nfse/samples/v1_0/GerarNFSeEnvio-env-loterps.xml")
```

**MDF-e**

```python
>>> # Parse an MDF-e:
>>> from nfelib.mdfe.bindings.v3_0.mdfe_v3_00 import Mdfe
>>> mdfe = Mdfe.from_path("nfelib/mdfe/samples/v3_0/ComPagtoPIX_41210780568835000181580010402005751006005791-procMDFe.xml")
>>>
>>> # Serialize an MDF-e:
>>> mdfe.to_xml()
```

**CT-e**

```python
>>> # Parse a CT-e:
>>> from nfelib.cte.bindings.v4_0.cte_v4_00 import Cte
>>> cte = Cte.from_path("nfelib/cte/samples/v4_0/43120178408960000182570010000000041000000047-cte.xml")
>>>
>>> # Serialize a CT-e:
>>> cte.to_xml()
```

**BP-e**

```python
>>> # Parse a BP-e:
>>> from nfelib.bpe.bindings.v1_0.bpe_v1_00 import Bpe
>>> bpe = Bpe.from_path("algum_bpe.xml")
>>>
>>> # Serialize a BP-e:
>>> bpe.to_xml()
```


## NFS-e transmission (REST)

The national NFS-e system exposes a REST API (ADN) instead of SOAP. The client
signs, GZip+Base64 packs the DPS and posts it over mutual TLS; install it with
`pip install nfelib[nfse]`.

```python
from nfelib.nfse.client.v1_0.nfse import NfseClient

client = NfseClient(
    ambiente="2",              # 1=production, 2=production restrita (homologation)
    pkcs12_data=pkcs12_bytes,  # decoded content of the A1 certificate (.pfx)
    pkcs12_password="password",
)

ret = client.envia_dps(dps)                    # POST /nfse -> generates the NFS-e
ret.body["chaveAcesso"]
ret = client.consulta_nfse(chave)              # GET /nfse/{chaveAcesso}
ret = client.consulta_dps(dps_id)              # GET /dps/{id}
ret = client.cancela_documento(chave, evento)  # POST /nfse/{chaveAcesso}/eventos
ret = client.consulta_evento(chave, tipo_evento, num_seq)
```

The certificate may be given as raw PFX bytes, base64 text (like an Odoo
Binary field) or a path to a `.pfx` file.


## SOAP transmission (BETA)

nfelib ships transmission clients that sign and transmit documents directly to
the SEFAZ webservices, over
[brazil-fiscal-client](https://github.com/akretion/brazil-fiscal-client) (mTLS
with your A1 certificate). Install with `pip install nfelib[soap]`.

```python
from nfelib.nfe.client.v4_0.nfe import NfeClient
from nfelib.nfe.client.v4_0.nfce import NfceClient
from nfelib.nfe.client.v4_0.mde import MdeClient
from nfelib.cte.client.v4_0.cte import CteClient
from nfelib.mdfe.client.v3_0.mdfe import MdfeClient

client = NfeClient(
    ambiente="2",                # 1=production, 2=homologation
    uf="35",                     # IBGE code of the UF (for the SOAP header)
    pkcs12_data=pkcs12_bytes,    # decoded content of the A1 certificate (.pfx)
    pkcs12_password="password",
    wrap_response=True,          # returns a WrappedResponse (envio_xml, resposta, retorno)
)

processo = client.processar_lote([nfe])             # NF-e / NFC-e (async, with receipt polling)
processo = client.envia_documento(cte)              # CT-e  (CTeRecepcaoSincV4, synchronous)
processo = client.envia_documento(mdfe)             # MDF-e (MDFeRecepcaoSinc, synchronous)
processo = client.cancela_documento(...)            # MDF-e / NF-e cancellation event
processo = client.enviar_cce(chave, correcao)       # NF-e carta de correcao event
ret = client.consulta_documento(chave)              # NF-e/CT-e/MDF-e consultation

# Manifestacao do Destinatario (MD-e) events go to the Ambiente Nacional:
mde = MdeClient(ambiente="2", uf="35", pkcs12_data=pkcs12_bytes,
                pkcs12_password="password", wrap_response=True)
ret = mde.ciencia_da_operacao(chave, cnpj_cpf)
ret = mde.confirmacao_da_operacao(chave, cnpj_cpf)
ret = mde.desconhecimento_da_operacao(chave, cnpj_cpf)
ret = mde.operacao_nao_realizada(chave, cnpj_cpf, justificativa)
```

Support status (**BETA**, API may change):

| Document | Authorization | Cancellation / events |
|----------|---------------|-----------------------|
| NF-e / NFC-e | yes | cancel, CC-e, inutilizacao |
| CT-e | yes (synchronous) | not yet |
| MDF-e | yes (synchronous) | cancel, encerramento |

The same clients power the DF-e distribution service (`NFeDistribuicaoDFe`,
polling the documents sent to your CNPJ) and the Manifestacao do Destinatario
events used by the [OCA/l10n-brazil](https://github.com/OCA/l10n-brazil)
localization for Odoo.

Because the bindings, signing and transmission are all pure Python and
serializable, nfelib can also be embedded behind a REST API (FastAPI, Odoo...)
to offer electronic invoicing as a service.


## Development / tests

Run the tests:

```bash
pytest
```

Update the bindings:

1. download the new schema package zip and update
   `nfelib/<nfe|nfse|cte|mdfe|bpe>/schemas/<version>/`
2. regenerate the bindings of one schema package, e.g. the NF-e:

    ```bash
    xsdata generate nfelib/nfe/schemas/v4_0 --package nfelib.nfe.bindings.v4_0
    # or ./generate_bindings.py nfe
    ```

Regenerate all bindings with xsdata:

```bash
./generate_bindings.py all
```

The exact source package of every binding directory is documented in
[CHANGELOG_SCHEMAS.md](CHANGELOG_SCHEMAS.md) and injected into the generated
files.


## Schema versions and folders

nfelib uses only 2 digits to characterize a version. This was decided after
observing that the Fazenda never uses the third digit, and that changing the
second digit is already a major change. So any schema change that does not
change the first nor the second digit of the schema version goes into the same
folder and supersedes the previous version, assuming that it is possible to
use the newer schema instead of the old one (for example, an NF-e 4.00 package
9j (NT 2022.003 v.1.00b) can be read with the bindings of the NF-e 4.00
package 9k (NT 2023.001 v.1.20)).

On the contrary, if there is a major change affecting the first 2 digits, as
with NF-e 3.0 and NF-e 3.1 or NF-e 3.1 and NF-e 4.0, it will also be possible
to support the various versions at the same time using different folders. It
would be possible, for example, to issue the future NF-e 5.0 and still import
an NF-e 4.0.


## Credits

nfelib builds on the work of other open source projects of the Brazilian
community:

* [erpbrasil.assinatura](https://github.com/erpbrasil/erpbrasil.assinatura) —
  used behind the façade to sign the XML documents with A1 certificates.
* [BrazilFiscalReport](https://github.com/Engenere/BrazilFiscalReport) — used
  behind the façade to print the DANFE, DACTE, DACTE-OS and DAMDFE PDFs.
* [erpbrasil.edoc](https://github.com/erpbrasil/erpbrasil.edoc) — the
  historical transmission library; it was the source of inspiration for the
  SOAP transmission clients.

Thanks to all the contributors:

<a href="https://github.com/akretion/nfelib/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=akretion/nfelib" alt="Contributors" />
</a>

