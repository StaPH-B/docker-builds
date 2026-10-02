# IQ-TREE3 container

Main tool : [iqtree3](https://github.com/iqtree/iqtree3)

Full documentation: [https://iqtree.github.io/doc/](http://www.iqtree.org/doc/)

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
iqtree3 -s example.phy -redo
```

Helpful parameters include:
- `-m MFP`: Uses ModelFinder Plus to perform ModelFinder and use the selected model for remaining analysis.
- `-st`: Used to swap from a DNA model to another sequence type model.
- `-mem`: Restricts memory usage
- `-nt AUTO`: Automatically determine the best number of cores given the current data and computer.
