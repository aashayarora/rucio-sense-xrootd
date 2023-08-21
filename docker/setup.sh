#!/bin/bash

# Fix IPv6 Routing
current_gateway=$(ip -6 route show default | awk '/default/{print $3}')
new_gateway=$(NET_GATEWAY)

if [ "$current_gateway" == "$new_gateway" ]; then
else
    ip -6 route delete default
    ip -6 route add default via "$new_gateway"
fi

## CREATE TEST FILES AND LINKS ##
data_dir="/rucio/store/data/Run2018A/EGamma/MINIAOD/UL2018_MiniAODv2-v1/50000"
num_files="$1"

mkdir -p "$data_dir"

for i in $(seq 0 "$num_files"); do
  file_name="testSourceFile$i"
  dd if=/dev/zero of="/rucio/$file_name" bs=1G count=1
  ln "/rucio/$file_name" "$data_dir/$file_name.root"
done

# Set ownership to xrootd user and group
chown -R xrootd:xrootd /rucio/*
