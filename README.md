# Python-SSL-checker-Zabbix

Python 3.7 dependencies:
```
#Python3.7
#pip3.7 install pyopenssl
#pip3.7 install cryptography
#pip3.7 install idna
```

###### Params expected for the script
```
Params:
-s --site Example: ssl_checker.py -s consultoronline.cloud
Retuurn: CloudFlare Inc ECC CA-2
-e --expiration Example: ssl_checker.py -e consultoronline.cloud
Return: 354
```
Will return de CN issuer and days left to expire the certificate.

###### This script is a modification from  gdamjan/ssl-check.py - https://gist.github.com/gdamjan/55a8b9eec6cf7b771f92021d93b87b2c
###### Configuration for Zabbix.
###### It works specially for SNI certificates like cloudflare, other type of certs should work too

Place the script at /usr/lib/zabbix/externalscripts/

Grant ownage to zabbix user and group and chmod 755 the script.

Import the template Python-SSL-checker-Zabbix.xml

###### This script was tested on zabbix 4.x.x version
