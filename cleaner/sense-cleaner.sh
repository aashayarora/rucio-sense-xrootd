#!/bin/bash
# It will execute deletion of all files under /rucio/temp/store/data/*
# if SENSE_CLEANUP variable is set
while :
do
    if test "${SENSE_CLEANUP+x}"; then
        echo "[Cleaner] Cleaning UP /rucio/temp/store/data/* files older than 1 minute files"
        find /rucio/temp/store/data/* -type f -mmin +1 -exec rm -f {} \;
    else
        echo "[Cleaner] No SENSE_CLEANUP Flag set. Exit and will not do anything"
        exit 0
    fi
    echo "[Cleaner] Sleep 5 seconds before next loop"
    sleep 5
done