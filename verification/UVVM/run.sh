#!/usr/bin/env sh

git submodule update --init --recursive verification/UVVM/uvvm
$GHDL_PREFIX/vendors/compile-uvvm.sh --uvvm --source $(dirname $0)/uvvm --output precompiled
