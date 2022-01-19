import unittest

class TestPositiveControl(unittest.TestCase):

    def test_kraken_output(self):
        with open("/test_data/trim_reads/kraken2_checksums.txt", 'r') as f:
            kraken_output_hash = f.readlines()[0].split(" ")[0]
        self.assertEqual(kraken_output_hash, "2978537085462109e279ececa2a196c1a9101fecabe30e2f4f60a16b57d5b5ed")

    def test_kraken_tab_output(self):
        with open("/test_data/trim_reads/kraken2_checksums.txt", 'r') as f:
            kraken_tab_hash = f.readlines()[1].split(" ")[0]
        self.assertEqual(kraken_tab_hash, "c417eeb911c7cef3cd73485123e2978465b0329eeaf0cc0886034f57d2219cc6")

if __name__ == '__main__':
    unittest.main()
