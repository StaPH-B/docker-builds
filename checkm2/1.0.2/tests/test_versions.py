import unittest
import subprocess
import sys
import re


class TestVersion(unittest.TestCase):
    def test_python(self):
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.assertEqual(version, "3.8") 


if __name__ == "__main__":
    unittest.main()