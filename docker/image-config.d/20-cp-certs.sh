#!/bin/bash

curl http://uaf-2.t2.ucsd.edu/~aaarora/packages/560061af.0 -o /etc/grid-security/certificates/560061af.0
chmod 644 /etc/grid-security/certificates/560061af.0
chown root: /etc/grid-security/certificates/560061af.0

# chmod u+rx /etc/xrootd/xrdcp-tpc.sh
# chown xrootd:xrootd /etc/xrootd/xrdcp-tpc.sh

CERT_DIR=/etc/grid-security/
mkdir -p $CERT_DIR/xrd
if [ -f $CERT_DIR/hostcert.pem ]; then
    cp -f $CERT_DIR/hostcert.pem /etc/grid-security/xrd/xrdcert.pem
    cp -f $CERT_DIR/hostkey.pem /etc/grid-security/xrd/xrdkey.pem
    chmod 644  /etc/grid-security/xrd/xrdcert.pem
    chmod 600 /etc/grid-security/xrd/xrdkey.pem
    chown -R xrootd:xrootd /etc/grid-security/xrd
fi
