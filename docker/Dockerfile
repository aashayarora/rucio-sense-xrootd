FROM opensciencegrid/software-base:3.6-el7-release

RUN yum -y install vim && \
    yum -y install osg-xrootd-standalone && \
    yum -y install osg-ca-certs && \
    yum -y install iproute 

RUN curl -OL https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz && \
    tar -xzvf node_exporter-1.7.0.linux-amd64.tar.gz && \
    mv node_exporter-1.7.0.linux-amd64/node_exporter /usr/bin/

COPY grid-mapfile /etc/grid-security/grid-mapfile
COPY auth-file /etc/xrootd/auth-file

COPY supervisord.conf /etc/supervisord.d/10-xrootd.conf
COPY xrootd.cfg /etc/xrootd/xrootd.cfg

COPY image-config.d/* /etc/osg/image-config.d/
