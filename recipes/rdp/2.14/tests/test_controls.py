import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)


    def test_rdp16S(self):
        with open("16S_checksum.txt") as f:
            rdp_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            rdp_checksum,
            "a38342a9ba63946ffb4324c7858f5cc43b873673cb08080437f7500dda351f65",
        )

    def test_rdp18S(self):
        with open("18S_checksum.txt") as f:
            rdp_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            rdp_checksum,
            "44bf9c60750ff3b804b3e3a56969dab982307a16faee63f0928b2f54e70b02f7",
        )


if __name__ == "__main__":
    unittest.main()