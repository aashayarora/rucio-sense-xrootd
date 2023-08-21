FROM opensciencegrid/software-base:fresh

RUN yum -y install vim && \
    yum -y install osg-xrootd-standalone && \
    yum -y install osg-ca-certs && \
    yum -y install iproute 

COPY grid-mapfile /etc/grid-security/grid-mapfile
COPY auth-file /etc/xrootd/auth-file

COPY supervisord.conf /etc/supervisord.d/10-xrootd.conf
COPY xrootd.cfg /etc/xrootd/xrootd.cfg

COPY setup.sh /setup.sh
COPY setup-redi.sh /setup-redi.sh

COPY image-config.d/* /etc/osg/image-config.d/
