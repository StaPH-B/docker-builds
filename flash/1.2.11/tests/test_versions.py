import unittest
import subprocess
from subprocess import PIPE
import re


class TestVersions(unittest.TestCase):

    def test_flash_version(self):
        bash_cmd = "flash -v"
        result = subprocess.run(bash_cmd, shell=True, stdout=PIPE)
        assert re.search(b"FLASH v1.2.11\n", result.stdout)


if __name__ == '__main__':
    unittest.main()
