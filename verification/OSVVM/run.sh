#!/usr/bin/env sh

git submodule update --init --recursive verification/OSVVM/OsvvmLibraries
$GHDL_PREFIX/vendors/compile-osvvm.sh \
  --osvvm \
  --source $(dirname $0)/OsvvmLibraries/osvvm --output precompiled
