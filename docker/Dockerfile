FROM opensciencegrid/software-base:3.6-el9-release

RUN yum -y install vim iproute xrootd xrootd-server xrootd-libs xrootd-server-libs xrootd-client \
    xrootd-client-libs xrootd-scitokens python3-scitokens gfal2-plugin-xrootd \
    xrootd-multiuser xrootd-voms voms-clients xrootd-fuse && yum clean all

RUN curl -OL https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz && \
    tar -xzvf node_exporter-1.7.0.linux-amd64.tar.gz && \
    mv node_exporter-1.7.0.linux-amd64/node_exporter /usr/bin/

COPY grid-mapfile /etc/grid-security/grid-mapfile
COPY auth-file /etc/xrootd/auth-file

RUN mkdir -p /etc/grid-security/vomsdir/cms/
COPY voms/voms-cms-auth.app.cern.ch.lsc /etc/grid-security/vomsdir/cms/voms-cms-auth.app.cern.ch.lsc
COPY voms/voms-mapfile /etc/grid-security/voms-mapfile

COPY supervisord.conf /etc/supervisord.d/10-xrootd.conf
COPY xrootd.cfg /etc/xrootd/xrootd.cfg

COPY image-config.d/* /etc/osg/image-config.d/
