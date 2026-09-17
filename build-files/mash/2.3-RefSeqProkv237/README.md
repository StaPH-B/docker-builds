# mash container

Main tool: [mash](https://github.com/marbl/Mash)

Code repository: https://github.com/marbl/Mash

Additional tools:
- none

Basic information on how to use this tool:
- executable: mash
- help: -h
- version: --version
- description: Fast genome and metagenome distance estimation using MinHash

Additional information:

This container includes Mash 2.3 and a refreshed RefSeq prokaryotic reference sketch at `/db/RefSeqProkSketchesv235.msh`.

The sketch replaces the 2019 `RefSeqSketchesDefaults.msh` distributed with `staphb/mash:2.3`. It is regenerated from RefSeq representative bacterial genomes by Erin Young's [`update_mash_dist`](https://github.com/erinyoung/update_mash_dist) pipeline (Mash 2.3, default k=21 / s=1000) and published to Zenodo:
- Version: v236 (published 2026-07-13)
- Zenodo record: 21341143
- DOI: [10.5281/zenodo.21341143](https://doi.org/10.5281/zenodo.21341143)
- Source file: `RefSeqSketches_236.msh.gz`

The mash sketch file is located at /db/RefSeqProkSketchesv${SKETCH_VER}.msh where SKETCH_VER often coincides with the refseq version.

Full documentation: https://mash.readthedocs.io/en/latest/

## Example Usage

```bash
# genome vs. genome
mash dist genome1.fna genome2.fna
# screen reads or an assembly against the included RefSeq sketch
mash screen /db/RefSeqProkSketchesv236.msh assembly.fna | sort -gr > screen.tab
# identify the closest reference for an assembly
mash dist /db/RefSeqProkSketchesv236.msh assembly.fna | sort -gk3 | head
```
