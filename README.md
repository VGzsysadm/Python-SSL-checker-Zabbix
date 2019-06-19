# Python-SSL-checker-Zabbix

Tested on python 3.5 - 3.6 - 3.7

###### Params expected for the script
```
Params:
-s --site Example: ssl_checker.py -s consultoronline.cloud
Return: /C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=CloudFlare Inc ECC CA-2
-e --expiration Example: ssl_checker.py -e consultoronline.cloud
Return: 354
```

###### This script is a modification from  gdamjan/ssl-check.py - https://gist.github.com/gdamjan/55a8b9eec6cf7b771f92021d93b87b2c
###### Ready for Zabbix.
###### It works specially for SNI certificates like cloudflare, other type of certs should work too

Drop the script at /usr/lib/zabbix/externalscripts

Grant ownage to zabbix user and chmod 755

Create a host

With the following macro:

{$HOSTNAME} = dns_domain_to_check

Add an item with the following key:
```
ssl_checker.py["-s","{HOSTNAME}"] -> will return CN
ssl_checker.py["-e","{HOSTNAME}"] -> will return days left to expire
```

Type text for CN checker
Type integer for expiration check
