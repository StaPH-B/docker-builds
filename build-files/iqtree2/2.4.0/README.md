# IQ-TREE2 container

Main tool : [iqtree2](https://github.com/iqtree/iqtree2)

Full documentation: [https://github.com/rrwick/Polypolish/wiki](http://www.iqtree.org/doc/)

| Efficient and versatile phylogenomic software by maximum likelihood

## Example Usage

An example phylip file (IQ-TREE2 also supports other file formats such as FASTA, NEXUS, CLUSTALW)

```
7 28
Frog       AAATTTGGTCCTGTGATTCAGCAGTGAT
Turtle     CTTCCACACCCCAGGACTCAGCAGTGAT
Bird       CTACCACACCCCAGGACTCAGCAGTAAT
Human      CTACCACACCCCAGGAAACAGCAGTGAT
Cow        CTACCACACCCCAGGAAACAGCAGTGAC
Whale      CTACCACGCCCCAGGACACAGCAGTGAT
Mouse      CTACCACACCCCAGGACTCAGCAGTGAT
```

Can be aligned with the following command:

```bash
iqtree2 -s example.phy --redo
```
