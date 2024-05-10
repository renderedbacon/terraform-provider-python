#!/usr/bin/env zsh
MIRROR_DIR=$(realpath terraform/mirror)
MIRROR_PROVIDER_DIR=terraform/mirror/registry.terraform.io/renderedbacon/python/0.1.0/darwin_arm64
PROVIDER_EXE=terraform-provider-python_darwin_arm64

# This script is used to build the Darwin version of the project.
pyinstaller terraform_provider_python.py --onefile --name $PROVIDER_EXE

# copy the output to the provider mirror directory
mkdir -p $MIRROR_PROVIDER_DIR || true
cp dist/$PROVIDER_EXE $MIRROR_PROVIDER_DIR/$PROVIDER_EXE

# build .terraformrc using heredoc
cat > "terraform/.terraformrc" <<EOF
provider_installation {
  filesystem_mirror {
    path    = "${MIRROR_DIR}"
    include = ["*/*"]
  }
}
EOF
