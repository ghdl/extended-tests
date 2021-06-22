from subprocess import check_call, STDOUT
from pathlib import Path
from pytest import mark

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)

def getVHDLSources():
	_srcs = []
	for extension in ['vhd', 'vhdl']:
		_items = Path(__file__).resolve().parent.glob('**/*.{}'.format(extension))
		if _items is not None:
			_srcs += [str(item) for item in _items]
	return _srcs


@mark.parametrize(
	"file",
	getVHDLSources()
)
@mark.xfail
def test_AllVHDLSources(file):
	check_call(['ghdl-dom', str(file)], stderr=STDOUT)
