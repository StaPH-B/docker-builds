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

This container bundles Mash 2.3 with a refreshed RefSeq prokaryotic reference sketch at `/db/RefSeqProkSketchesv235.msh`.

The sketch replaces the 2019 `RefSeqSketchesDefaults.msh` that ships with `staphb/mash:2.3`. It is regenerated from RefSeq representative bacterial genomes by Erin Young's [`update_mash_dist`](https://github.com/erinyoung/update_mash_dist) pipeline (Mash 2.3, default k=21 / s=1000) and published to Zenodo:
- Version: v235 (published 2026-05-19)
- Zenodo record: 20293962
- DOI: [10.5281/zenodo.20293962](https://doi.org/10.5281/zenodo.20293962)
- Source file: `RefSeqSketches_235.msh.gz` (MD5 `2885e98f2d985b2b4f8f8ce9978040d2`)

Full documentation: https://mash.readthedocs.io/en/latest/

## Example Usage

```bash
# genome vs. genome
mash dist genome1.fna genome2.fna
# screen reads or an assembly against the bundled RefSeq sketch
mash screen /db/RefSeqProkSketchesv235.msh assembly.fna | sort -gr > screen.tab
# identify the closest reference for an assembly
mash dist /db/RefSeqProkSketchesv235.msh assembly.fna | sort -gk3 | head
```
