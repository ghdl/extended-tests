git submodule update --init --recursive verification\UVVM\uvvm
& $env:GHDL_PREFIX\vendors\compile-uvvm.ps1 `
  -All `
  -Source verification\UVVM\uvvm -Output precompiled
