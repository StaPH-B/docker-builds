import unittest

class TestPositiveControl(unittest.TestCase):

    def test_kraken_output(self):
        with open("/test_data/trim_reads/kraken_checksums.txt", 'r') as f:
            kraken_output_hash = f.readlines()[0].split(" ")[0]
        self.assertEqual(kraken_output_hash, "237c3be9e927866f3c9a9c7e031088d283c6de3684260602f1e0a3af6b6bc0fa")

    def test_kraken_tab_output(self):
        with open("/test_data/trim_reads/kraken_checksums.txt", 'r') as f:
            kraken_tab_hash = f.readlines()[1].split(" ")[0]
        self.assertEqual(kraken_tab_hash, "55b9bb27d5795acdfcdc9e3d9131aa7c358f3e8f44f9285e0c0df991ae854e2b")

if __name__ == '__main__':
    unittest.main()
