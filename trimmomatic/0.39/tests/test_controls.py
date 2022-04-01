import unittest


class TestPositiveControl(unittest.TestCase):

    def test_output_trimmed_r1_paired(self):
        with open("/test_result/R1.paired.fq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "a401ef04fb1d0dc8903aada4831fc3544212d7373f53ef000faaa5a1640cbe5e")

    def test_output_trimmed_r1_unpaired(self):
        with open("/test_result/R1.unpaired.fq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "7ad99ed6b8b9b03ef8de3a5152f5e0083ec21fce9c56c1c3171ec26328c860eb")

    def test_output_trimmed_r2_paired(self):
        with open("/test_result/R2.paired.fq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "3511ee4e96180b0c62b1dfb3f403967268703908b165945dec84022b0a971e27")

    def test_output_trimmed_r2_unpaired(self):
        with open("/test_result/R2.unpaired.fq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "6971c6b2f948a1d3c8dced7f6ec32b2d4fbebde374ce2f76e8ad5f02b94ff2be")


if __name__ == '__main__':
    unittest.main()
