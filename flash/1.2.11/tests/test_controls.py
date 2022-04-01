import unittest


class TestPositiveControl(unittest.TestCase):

    def test_output_merged(self):
        with open("/test_result/test.extendedFrags.fastq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "4ceab7268db4bb7e6c0bd15f49409d6bcec4fac97126804024a44cdfca5a3590")

    def test_output_unmerged_r1(self):
        with open("/test_result/test.notCombined_1.fastq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "c9d95a47c29735007deb81f1768022e355caeb07e41c1cc2ff2471a9c385866f")

    def test_output_unmerged_r2(self):
        with open("/test_result/test.notCombined_2.fastq.sha256sum", 'r') as f:
            checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(checksum, "59f0cd8c8526511716c44e71563f61d6cbf8ebea9521a8fedb21256f042e3842")


if __name__ == '__main__':
    unittest.main()
