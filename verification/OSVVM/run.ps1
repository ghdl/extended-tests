git submodule update --init --recursive verification\OSVVM\OsvvmLibraries
& $env:GHDL_PREFIX\vendors\compile-osvvm.ps1 `
  -OSVVM `
  -OSVVM_VIP_UART `
  -Source verification\OSVVM\OsvvmLibraries -Output precompiled
