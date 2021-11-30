# livstreame-recon
Let's recon the Walmart

## Companies
List of the companies:
- 1

## Domains
List of the domains:
- walmartchile.cl
- walmartgamecenter.com
- walmartlivebetter.ca
- wal-mart.com
- walmart.com
- walmartpr.com
- amigo.com
- wmt.co
- samsclub.com
- walmartimages.ca
- walmartimages.com
- sams.com.mx
- walmart.com.mx
- asda.com
- samsclubpr.com
- walmart.com.br
- wmfs.ca
- walmart.ca
- walmartapis.com
- walmartshoplive.com
- walmartgift.com
- walmarthealth.com
- wmstorechat-1.custhelp.com
- dxfairmall.com
- hayneedle.com
- jet.com
- wal-mart.com

## Shodan
List of the shodan searches:
- walmart org:"Wal-Mart Stores Inc."

## ASN
List of the AS numbers:
- 46313
- 46312


## method

here are the moethods we used:

1. domain -> ASN -> CIDR -> Reverse IP lookup
2. domain -> certificate -> information -> reverse look up in certificates
3. domain -> ASN -> CIDR -> certificate search
4. Text parsing, Google dorks
5. Reverse image search 

## Censys searcher

Approach 1:
1. Search and get the pages
2. Request to all pages and parse `parsed.subject_dn` field
3. Save the results
```
curl -s https://censys.io/api/v1/search/certificates -u "KEY:SECRET" -H "content-type: application/json" --data '{"query":"parsed.subject.organization: walmart"}' | tee walmart-censys.json | jq -r ".results[].\"parsed.subject_dn\"" | tee walmart-censys-parsed.txt
```

Approach 2:
1. Search and get the pages
2. Request to all pages
3. Request to certificates (By SHA256)
4. Parse the JSON response to extract the information
```
curl -s https://censys.io/api/v1/view/certificates/d53579e8fab81588193d26d91d029ff0fc76521c4c18f60e125066ca8426e8b9 -u "KEY:SECRET" | tee 1 | jq -r ".parsed | [.__expanded_names, .extensions.subject_alt_name.dns_names, .names][][]" | sort -u
```
Host seaches:
```
services.banner: walmart
services.tls.certificates.leaf_data.issuer.common_name: Walmart Inc.
services.tls.certificates.leaf_data.issuer.email_address: walmart.com
services.tls.certificates.leaf_data.subject.organization: walmart and services.port:25

gathering ip address and then can check by reverse ip search
and with ports or banner
services.tls.certificates.leaf_data.subject.organization: (Walmart Inc.) and autonomous_system.asn: 46312
```

## Text Parsing
```
"Walmart. All Rights Reserved."
"© 2021 Walmart. All Rights Reserved."
"Walmart. All Rights Reserved."  -inurl:walmart.com"
© 2021 Walmart. All Rights Reserved."
```

## Image reverse Search
Search for logo or photo

## Unverified domains
List:
```
walmartmuseum.com
walmartprepaid.com
walmartmobile.com.mx
walmartimages.ca
walmartbrandcenter.com
walmartethics.com
walmartmmxcam.com
walmartlogistics.ca
walmartmexico.com
walmartbr.org
walmartspouseswithamission.com
walmartimages.com
walmartfoodsafetychina.com
walmartmedia.com
walmart.com.ar
walmartone.com
walmartstores.net
walmartcommunityvotes.com
walmartrecovery.com
walmartbrasil.com.br
walmartcareerswithamission.com
walmartrealty.com
walmartmobile.cn
walmartstores.com
walmartplus.com
walmartcanadafinancialservices.ca
pso2walmart.com
walmartlabs.com
walmartphotocentre.ca
walmartgreatforyou.com
walmarthealth.com
walmartsustainabilityhub.com
walmart.com
walmartfoodsafetychina.cn
walmartmexico.com.mx
walmartrussia.biz
bhartiwalmart-careers.in
walmartcontacts.com
walmartclaimsservices.com
walmartjapanseiyu.com
walmartcentroamerica.com
walmartcanada.ca
walmartstationery.com
campuscrecerwalmartchile.cl
walmartmoneycard.com
walmart-jump.com
walmart.org
walmartchile.cl
walmart.ca
walmartmexicoycam.com
walmartapis.com
walmart.com.mx
walmartretail.cl
asda.jobs
tellasda.com
cellstores.com
presto.cl
jet.com
americasbest.com
liderdomicilio.cl
asdabusiness.com
asda.jobs
novedadeslider.cl
sparkshop.com
wmlakshya.com
asda.com
asdasupplier.com
novedadesacuenta.cl
mundolider.com
w-mt.co
seyco.cl
superbodegaacuenta.cl
seiyu-survey.com
vudu.com
Wal-mart.com
bestprice.in
samsclubsng.com
changomas.com.ar
071dapp.com
marquee.net
miclublider.cl
ssff.cl
Wal-Mart.com
cmiw.com
centralmayorista.cl
prestoviajes.cl
recetaslider.cl
kanetix.ca
samsclub.cn
lider.cl
wal-mart.com
member-ally.com
inphonic.com
beneficioslidermastercard.cl
simplexity.com
samsclub.com
wal.co
jetcdn.net
librodigitalchile.cl
Hayneedle.com
notjet.net
onmicrosoft.com
superama.com.mx
thedealdepot.com
liderseguro.cl
ecmwi.com
eloquii.com
lidermovil.cl
servifacil.cl
liderserviciosfinancieros.cl
viathonbicycles.com
prestopagoenlinea.cl
prestored.cl
ekono.cl
lidermastercard.cl
expressdelider.cl
accenture.com
dys.cl
```

## Verified Domains

List:

```

```