if [ -z $NUM_FILES ]; then
  ## CREATE TEST FILES AND LINKS ##
  data_dir="/rucio/store/data/Run2018A/EGamma/MINIAOD/UL2018_MiniAODv2-v1/50000"
  num_files=$NUM_FILES

  mkdir -p "$data_dir"

  for i in $(seq 0 "$num_files"); do
    file_name="testSourceFile$i"
    dd if=/dev/zero of="/rucio/$file_name" bs=1G count=1
    ln "/rucio/$file_name" "$data_dir/$file_name.root"
  done
  
  # Set ownership to xrootd user and group
  chown -R xrootd:xrootd /rucio/*
fi
