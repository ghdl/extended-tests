
<p align="center">
  <a title="Documentation" href="https://ghdl.github.io/extended-tests"><img src="https://img.shields.io/website.svg?label=ghdl.github.io%2Fextended-tests&longCache=true&style=flat-square&url=http%3A%2F%2Fghdl.github.io%2Fextended-tests%2Findex.html&logo=GitHub"></a><!--
  -->
  <a title="Join the chat at https://gitter.im/ghdl1/Lobby" href="https://gitter.im/ghdl1/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img src="https://img.shields.io/badge/Chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef"></a><!--
  -->
  <a title="'Test' workflow Status" href="https://github.com/ghdl/extended-tests/actions/workflows/Test.yml"><img alt="'Test' workflow Status" src="https://img.shields.io/github/actions/workflow/status/ghdl/extended-tests/Test.yml?branch=main&longCache=true&style=flat-square&label=Test&logo=GitHubActions&logoColor=fff"></a><!--
  -->
</p>

# Extended tests for GHDL

This repository contains tests, examples and third-party projects to be tested on GitHub Actions workflows, using bleeding-edge realeases of [GHDL](https://github.com/ghdl/ghdl) ([nightly](https://github.com/ghdl/ghdl/releases/tag/nightly) assets through Action [setup-ghdl-ci](https://github.com/ghdl/setup-ghdl-ci), and/or [containers](https://github.com/ghdl/docker)).

- `ghdl-dom`: GHDL, PoC, OSVVM, UVVM, VUnit.
- Simulation
- Verification
  - [OSVVM](https://osvvm.org/)
  - [UVVM](https://uvvm.org/)
- Synthesis
- Formal verification

References:

- [ghdl/ghdl-yosys-plugin: examples](https://github.com/ghdl/ghdl-yosys-plugin/tree/master/examples)
- *Target projects for synthesis* ([ghdl/ghdl#974](https://github.com/ghdl/ghdl/issues/974))
- *Learning VHDL with GHDL* ([ghdl/ghdl#1291](https://github.com/ghdl/ghdl/issues/1291))
