#!/bin/bash

if [ -v REDIRECTOR ]; then
  echo 2001:48d0:3001:111::400 xrootd-sense-ucsd-01-111.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:111::500 xrootd-sense-ucsd-02-111.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:111::600 xrootd-sense-ucsd-03-111.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:111::700 xrootd-sense-ucsd-04-111.sdsc.optiputer.net > /etc/hosts
  
  echo 2001:48d0:3001:112::400 xrootd-sense-ucsd-01-112.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:112::500 xrootd-sense-ucsd-02-112.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:112::600 xrootd-sense-ucsd-03-112.sdsc.optiputer.net > /etc/hosts
  echo 2001:48d0:3001:112::700 xrootd-sense-ucsd-04-112.sdsc.optiputer.net > /etc/hosts
fi
