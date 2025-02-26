import unittest
import subprocess
from subprocess import PIPE
import os

class TestPositiveControl(unittest.TestCase):
    # Run this once to have the outputs for all tests
    @classmethod
    def setUpClass(cls):
        bash_cmd = "bash /tests/scripts/run_positive_control.sh"
        subprocess.run(bash_cmd, shell=True, stdout=PIPE)

    def test_alignments_equal(self):
        with open("/data/pos_control/outdir_parsnp_fasttree/parsnp.xmfa.checksum", 'r') as f:
            fasttree_aln_test_hash = f.readlines()[0].split(" ")[0]
        with open("/data/pos_control/outdir_parsnp_raxml/parsnp.xmfa.checksum", 'r') as f:
            raxml_aln_test_hash = f.readlines()[0].split(" ")[0]
        self.assertEqual(fasttree_aln_test_hash, raxml_aln_test_hash)

    def test_fasttree_tree_dist_to_ref(self):
        bash_cmd = "rf /data/pos_control/outdir_parsnp_fasttree/parsnp.tree /tests/files/ref.tre"
        rf_dist = subprocess.run(bash_cmd, shell=True, stdout=PIPE, universal_newlines=True).stdout
        print("Robinson-Foulds distance between FastTree tree and reference tree is: " + rf_dist)
        self.assertLessEqual(float(rf_dist), 0.5)

    def test_raxml_tree_dist_to_ref(self):
        bash_cmd = "rf /data/pos_control/outdir_parsnp_raxml/parsnp_quoted.tree /tests/files/ref.tre"
        rf_dist = subprocess.run(bash_cmd, shell=True, stdout=PIPE, universal_newlines=True).stdout
        print("Robinson-Foulds distance between RAxML tree and reference tree is: " + rf_dist)
        self.assertLessEqual(float(rf_dist), 0.5)

    def test_fasttree_tree_dist_to_raxml_tree(self):
        bash_cmd = "rf /data/pos_control/outdir_parsnp_fasttree/parsnp.tree /data/pos_control/outdir_parsnp_raxml/parsnp_quoted.tree"
        rf_dist = subprocess.run(bash_cmd, shell=True, stdout=PIPE, universal_newlines=True).stdout
        print("Robinson-Foulds distance between FastTree tree and RAxML tree is: " + rf_dist)
        self.assertLessEqual(float(rf_dist), 0.5)


class TestNegativeControl(unittest.TestCase):
    # Run this once to have the outputs for all tests
    @classmethod
    def setUpClass(cls):
        bash_cmd = "bash /tests/scripts/run_negative_control.sh"
        subprocess.run(bash_cmd, shell=True, stdout=PIPE)

    def test_filter(self):
        with open("/data/neg_control/outdir_parsnp_filter/parsnp.tree", 'r') as f:
            filter_tree = f.read()
        self.assertEqual('GCA_000748565.2_ASM74856v2_genomic.fna' in filter_tree, False)


if __name__ == '__main__':
    unittest.main()
