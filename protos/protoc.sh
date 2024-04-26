#!/usr/bin/env bash
SRC_DIR=../src/terraform_provider_python/tfplugin
SRC_PROTO_FILE=./tfplugin6_5.proto
TMP_PROTO_FILE=./tfplugin.proto

cp -f $SRC_PROTO_FILE $TMP_PROTO_FILE
python -m grpc_tools.protoc -I. --python_out=$SRC_DIR --pyi_out=$SRC_DIR --grpc_python_out=$SRC_DIR $TMP_PROTO_FILE
python ./post_gen.py --python_out=$SRC_DIR --pyi_out=$SRC_DIR --grpc_python_out=$SRC_DIR --proto_file=$TMP_PROTO_FILE
black $SRC_DIR/*.py $SRC_DIR/*.pyi
rm -f $TMP_PROTO_FILE
