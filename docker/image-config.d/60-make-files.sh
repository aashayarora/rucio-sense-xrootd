#!/bin/bash

# num_files="${NUM_FILES:-10}"
# num_datasets="${NUM_DATASETS:-10}"
# num_symlinks="${NUM_SYMLINKS:-10}"

# if [ -z "$REDIRECTOR" ]; then
#   data_dir="/rucio/store/data/Run2018A/EGamma/MINIAOD/UL2018_MiniAODv2-v1/"
#   mkdir -p "$data_dir"

#   for ((i=0; i<=num_files; i++)); do
#     dd if=/dev/zero of="/rucio/testSourceFile$i" bs=1G count=4
#     for ((d=65000; d<=65000+1000*num_datasets; d+=1000)); do
#       for ((j=0; j<=num_symlinks; j++)); do
#         mkdir "${data_dir}/$d"
#         ln "/rucio/testSourceFile$i" "${data_dir}/$d/testSourceFile$((j * num_files + i)).root"
#       done
#     done
#   done
# fi

# # Set ownership to xrootd user and group
# chown -R xrootd:xrootd /rucio/*
