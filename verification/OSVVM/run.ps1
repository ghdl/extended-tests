git submodule update --init --recursive verification\OSVVM\OsvvmLibraries
& $env:GHDL_PREFIX\vendors\compile-osvvm.ps1 `
  -All `
  -Source verification\OSVVM\OsvvmLibraries -Output precompiled
