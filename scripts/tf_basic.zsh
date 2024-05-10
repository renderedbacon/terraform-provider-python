#!/usr/bin/env zsh

pushd terraform/basic
TF_CLI_CONFIG_FILE=$(realpath "../.terraformrc") terraform $@
popd
