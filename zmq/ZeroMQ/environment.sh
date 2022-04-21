export PYTHONPATH=$(pwd)
export PROJ_PATH=$(pwd)
export DEVICE_CONFIG=$(pwd)/Configs/$1_config.toml
echo $DEVICE_CONFIG
export COMMON_CONFIG=$(pwd)/Configs/common_config.toml
export CONFIG_PATH=$(pwd)/Configs/
export PROTOBUF_PATH=$PROJ_PATH/Third_Party/protobuf-3.17.3/
export PATH=$PATH:$(pwd)/Third_Party/
