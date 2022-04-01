import unittest
import subprocess
from subprocess import PIPE


class TestVersions(unittest.TestCase):

    def test_version_trimmomatic(self):
        bash_cmd = "trimmomatic -version"
        result = subprocess.run(bash_cmd, shell=True, stdout=PIPE)
        self.assertEqual(b"0.39\n", result.stdout)


if __name__ == '__main__':
    unittest.main()
