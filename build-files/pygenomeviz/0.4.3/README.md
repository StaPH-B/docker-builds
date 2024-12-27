# pyGenomeViz container

Main tool : [pyGenomeViz](https://moshi4.github.io/pyGenomeViz/)

Additional tools:
- MMseqs2 v14-7e284+ds-1+b2
- MUMmer v3.23+dfsg-8
- progressiveMauve v1.2.0+4713+dfsg-5+b1

Full documentation: https://moshi4.github.io/pyGenomeViz/

> pyGenomeViz is a genome visualization python package for comparative genomics implemented based on matplotlib. This package is developed for the purpose of easily and beautifully plotting genomic features and sequence similarity comparison links between multiple genomes.

## Example Usage

Using the CLI

```bash
# Download four Erwinia phage genbank files
pgv-download-dataset -n erwinia_phage

# run pyGenomeViz to visualize MUMmer alignment
pgv-mummer --gbk_resources MT939486.gbk MT939487.gbk MT939488.gbk LT960552.gbk -o mummer_example1 --tick_style axis --align_type left --feature_plotstyle arrow

# run pyGenomeViz to visualize MMseqs2 alignment
pgv-mmseqs --gbk_resources MT939486.gbk:250000-358115 MT939487.gbk:250000-355376 MT939488.gbk:250000-356948 LT960552.gbk:270000-340000 -o mmseqs_example2 --tick_style bar --feature_plotstyle arrow

# Download four E.coli genbank files
pgv-download-dataset -n escherichia_coli

# run pyGenomeViz to visualize progressiveMauve alignment
pgv-pmauve --seq_files NC_000913.gbk NC_002695.gbk NC_011751.gbk NC_011750.gbk -o pmauve_example1 --tick_style bar
```

This container contains the pygenomeviz python package, so custom scripts can import pygenomeviz

```python
from pygenomeviz import GenomeViz

name, genome_size = "Tutorial 01", 5000
cds_list = ((100, 900, -1), (1100, 1300, 1), (1350, 1500, 1), (1520, 1700, 1), (1900, 2200, -1), (2500, 2700, 1), (2700, 2800, -1), (2850, 3000, -1), (3100, 3500, 1), (3600, 3800, -1), (3900, 4200, -1), (4300, 4700, -1), (4800, 4850, 1))

gv = GenomeViz()
track = gv.add_feature_track(name, genome_size)
for idx, cds in enumerate(cds_list, 1):
    start, end, strand = cds
    track.add_feature(start, end, strand, label=f"CDS{idx:02d}")

fig = gv.plotfig()
```
