if [ -n $NUM_FILES ]; then
  ## CREATE TEST FILES AND LINKS ##
  data_dir="/rucio/store/data/Run2018A/EGamma/MINIAOD/UL2018_MiniAODv2-v1/50000"
  num_files=$NUM_FILES
  start_point=$START_POINT

  mkdir -p "$data_dir"

  for ((i=start_point; i<=num_files+start_point; i++)); do
    dd if=/dev/zero of="/rucio/testSourceFile$i" bs=1G count=1
    for ((j=0; j<=4; j++)); do
      ln "/rucio/testSourceFile$i" "${data_dir}/testSourceFile$((j * num_files + i)).root"
    done
  done

  # Set ownership to xrootd user and group
  chown -R xrootd:xrootd /rucio/*
fi
