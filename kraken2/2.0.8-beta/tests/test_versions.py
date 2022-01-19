import unittest
import subprocess
from subprocess import PIPE
import re


class TestVersions(unittest.TestCase):

    def test_kraken_version(self):
        bash_cmd = "kraken2 --version"
        result = subprocess.run(bash_cmd, shell=True, stdout=PIPE)
        self.assertEqual(b"Kraken version 2.0.8-beta\nCopyright 2013-2019, Derrick Wood (dwood@cs.jhu.edu)\n", result.stdout)


if __name__ == '__main__':
    unittest.main()
