import unittest
import subprocess
from subprocess import PIPE
import re


class TestVersions(unittest.TestCase):

    def test_kraken_version(self):
        bash_cmd = "kraken --version"
        result = subprocess.run(bash_cmd, shell=True, stdout=PIPE)
        self.assertEqual(b"Kraken version 1.0\nCopyright 2013-2015, Derrick Wood (dwood@cs.jhu.edu)\n", result.stdout)


if __name__ == '__main__':
    unittest.main()
