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
"acq. Walmart"
"a Walmart company"
"Acquired By Walmart"
```

## Image reverse Search
Search for logo or photo
