git submodule update --init --recursive verification\UVVM\uvvm
& $env:GHDL_LIBS\vendors\compile-uvvm.ps1 -UVVM -UVVM_VIP_UART -Source verification\UVVM\uvvm -Output precompiled
