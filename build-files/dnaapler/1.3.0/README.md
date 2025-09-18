# dnaapler container

Main tool : [dnappler](https://github.com/gbouras13/dnaapler)

<details>
<summary>Additional tools installed via micromamba:</summary>


```
List of packages in environment: "/opt/conda/envs/dnaapler"

  Name              Version      Build                 Channel    
────────────────────────────────────────────────────────────────────
  _libgcc_mutex     0.1          conda_forge           conda-forge
  _openmp_mutex     4.5          2_gnu                 conda-forge
  archspec          0.2.5        pyhd8ed1ab_0          conda-forge
  aria2             1.37.0       hbc8128a_2            conda-forge
  biopython         1.85         py313h07c4f96_2       conda-forge
  bzip2             1.0.8        hda65f42_8            conda-forge
  c-ares            1.34.5       hb9d3cd8_0            conda-forge
  ca-certificates   2025.8.3     hbd8a1cb_0            conda-forge
  click             8.2.1        pyh707e725_0          conda-forge
  dnaapler          1.3.0        pyhdfd78af_0          bioconda   
  gawk              5.3.1        hcd3d067_0            conda-forge
  gmp               6.3.0        hac33072_2            conda-forge
  ld_impl_linux-64  2.44         h1423503_1            conda-forge
  libasprintf       0.25.1       h3f43e3d_1            conda-forge
  libblas           3.9.0        35_h4a7cf45_openblas  conda-forge
  libcblas          3.9.0        35_h0358290_openblas  conda-forge
  libexpat          2.7.1        hecca717_0            conda-forge
  libffi            3.4.6        h2dba641_1            conda-forge
  libgcc            15.1.0       h767d61c_5            conda-forge
  libgcc-ng         15.1.0       h69a702a_5            conda-forge
  libgettextpo      0.25.1       h3f43e3d_1            conda-forge
  libgfortran       15.1.0       h69a702a_5            conda-forge
  libgfortran5      15.1.0       hcea5267_5            conda-forge
  libgomp           15.1.0       h767d61c_5            conda-forge
  libiconv          1.18         h3b78370_2            conda-forge
  liblapack         3.9.0        35_h47877c9_openblas  conda-forge
  liblzma           5.8.1        hb9d3cd8_2            conda-forge
  libmpdec          4.0.0        hb9d3cd8_0            conda-forge
  libopenblas       0.3.30       pthreads_h94d23a6_2   conda-forge
  libsqlite         3.50.4       h0c1763c_0            conda-forge
  libssh2           1.11.1       hcf80075_0            conda-forge
  libstdcxx         15.1.0       h8f9b012_5            conda-forge
  libstdcxx-ng      15.1.0       h4852527_5            conda-forge
  libuuid           2.41.1       he9a06e4_0            conda-forge
  libxml2           2.13.8       h2cb61b6_1            conda-forge
  libzlib           1.3.1        hb9d3cd8_2            conda-forge
  loguru            0.7.3        pyh707e725_0          conda-forge
  mmseqs2           18.8cc5c     hd6d6fdc_0            bioconda   
  mpfr              4.2.1        h90cbb55_3            conda-forge
  ncurses           6.5          h2d0b736_3            conda-forge
  numpy             2.3.3        py313hf6604e3_0       conda-forge
  openssl           3.5.3        h26f9b46_0            conda-forge
  pandas            2.3.2        py313h08cd8bf_0       conda-forge
  pip               25.2         pyh145f28c_0          conda-forge
  pyrodigal         3.6.3.post1  py313h366bbf7_1       bioconda   
  python            3.13.7       h2b335a9_100_cp313    conda-forge
  python-dateutil   2.9.0.post0  pyhe01879c_2          conda-forge
  python-tzdata     2025.2       pyhd8ed1ab_0          conda-forge
  python_abi        3.13         8_cp313               conda-forge
  pytz              2025.2       pyhd8ed1ab_0          conda-forge
  pyyaml            6.0.2        py313h8060acc_2       conda-forge
  readline          8.2          h8c095d6_2            conda-forge
  six               1.17.0       pyhe01879c_1          conda-forge
  tk                8.6.13       noxft_hd72426e_102    conda-forge
  tzdata            2025b        h78e105d_0            conda-forge
  yaml              0.2.5        h280c20c_3            conda-forge
  zlib              1.3.1        hb9d3cd8_2            conda-forge
```

</details>
</br>

Full documentation: [https://github.com/gbouras13/dnaapler](https://github.com/gbouras13/dnaapler)

> `dnaapler` is a simple python program that takes a single nucleotide input sequence (in FASTA format), finds the desired start gene using MMSeqs2, checks that the start codon of this gene is found, and if so, then reorients the chromosome to begin with this gene on the forward strand.

Note: As of v1.0.0, 'dnaapler' uses MMSeqs2 v13.45111 instead of BLAST for sequence alignment. MMSeqs2 is faster and compatible across platforms, including MacOS with Apple Silicon. As of v1.2.0, GFA input file format is supported.

dnaapler has several commands for chromosomes, plasmids, and more.

```
Usage: dnaapler [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help     Show this message and exit.
  -V, --version  Show the version and exit.

Commands:
  all         Reorients contigs to begin with any of dnaA, repA, terL, or...
  archaea     Reorients your genome to begin with the archaeal COG1474...
  bulk        Reorients multiple genomes to begin with the same gene.
  chromosome  Reorients your genome to begin with the dnaA chromosomal...
  citation    Print the citation(s) for this tool.
  custom      Reorients your genome with a custom database.
  mystery     Reorients your genome with a random CDS.
  nearest     Reorients your genome to begin with the first CDS as...
  phage       Reorients your genome to begin with the terL large...
  plasmid     Reorients your genome to begin with the repA replication...
```

WARNING: Does not support multifasta files. Each sequence must be processed individually.

## Example Usage

```bash
# Reorienting for a fasta of a chromsome sequence
dnaapler chromosome --input chromosome.fasta --output dnaapler_chr

# Reorienting for a fasta of a plasmid sequence
dnaapler plasmid --input plasmid.fasta --output dnaapler_plasmid

# Reorienting Mixed Contigs
dnaapler all -i input_mixed_contigs.fasta -o output_directory_path -p my_bacteria_name
```
