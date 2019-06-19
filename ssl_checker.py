#######
# Author: VGzsysadm - sysadm.es - consultoronline.cloud
# repository: https://github.com/VGzsysadm/Python-SSL-checker-Zabbix
#######
#Python3.7
#pip install pyopenssl
#pip install cryptography
#pip install idna
from OpenSSL import SSL
import argparse
from datetime import datetime
import re
import idna
from socket import socket
from collections import namedtuple

HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')

def verify_sn(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()

    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.get_issuer()
    dirty = str(crypto_cert)
    regex = re.search("\'(.*.)'", dirty) 
    sock_ssl.close()
    sock.close()
    return regex.group(1)

def verify_cert(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()

    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()
    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)

def get_expiration(hostinfo):
    datenow = datetime.now()
    result = notafter=hostinfo.cert.not_valid_after
    delta = result - datenow
    dirty = str(delta)
    regex = re.search("^.{0,3}\s?\d+", dirty) 
    return regex.group(0)

def main():
    """
    Params expected for the script
    Params:
        -s --site Example: cert.py -s consultoronline.cloud
        Return: /C=US/ST=CA/L=San Francisco/O=CloudFlare, Inc./CN=CloudFlare Inc ECC CA-2
        -e --expiration Example: cert.py -s consultoronline.cloud
        Return: 354
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--site', action="store", dest="site")
    parser.add_argument('-e','--expiration', action="store", dest="expiration")
    args = parser.parse_args()

    if args.site:
        port = 443
        cn = verify_sn(args.site, port)
        print(cn)

    if args.expiration:
        hostinfo = verify_cert(args.expiration, 443)
        expiration = get_expiration(hostinfo)
        print(expiration)

if __name__ == "__main__":
    main()
