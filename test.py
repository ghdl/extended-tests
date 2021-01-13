"""
Verify that all extended tests work
"""

import sys
from sys import executable, platform
from os import environ
from pathlib import Path
from subprocess import check_call, STDOUT
from shutil import which
import unittest
import pytest


isWin = platform == 'win32'


class TestExtended(unittest.TestCase):
    """
    Verify that all extended tests work
    """

    def setUp(self):
        self.shell = [which('bash')] if platform == 'win32' else []
        self.root = Path(__file__).parent
        print('\n::group::Log')
        sys.stdout.flush()

    def tearDown(self):
        print('\n::endgroup::')
        sys.stdout.flush()


    def _sh(self, args):
        check_call(self.shell + args, stderr=STDOUT)

    def _py(self, args):
        check_call([executable] + args, stderr=STDOUT)


    def test_verification_OSVVM(self):
        self._sh([str(self.root / 'verification' / 'OSVVM' / 'run.sh')])


    def test_verification_UVVM(self):
        self._sh([str(self.root / 'verification' / 'UVVM' / 'run.sh')])
