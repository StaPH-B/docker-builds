# pangolin docker image

Main tool : [pangolin](https://github.com/cov-lineages/pangolin)

Full documentation: [https://cov-lineages.org/resources/pangolin.html](https://cov-lineages.org/resources/pangolin.html)

Phylogenetic Assignment of Named Global Outbreak LINeages

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/pangolin"

  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex              0.1           conda_forge           conda-forge
  _openmp_mutex              4.5           2_gnu                 conda-forge
  amply                      0.1.6         pyhd8ed1ab_0          conda-forge
  appdirs                    1.4.4         pyh9f0ad1d_0          conda-forge
  attr                       2.5.2         h39aace5_0            conda-forge
  attrs                      24.2.0        pyh71513ae_0          conda-forge
  biopython                  1.83          py38h01eb140_0        conda-forge
  boost-cpp                  1.78.0        h2c5509c_4            conda-forge
  brotli-python              1.1.0         py38h17151c0_1        conda-forge
  bzip2                      1.0.8         hda65f42_8            conda-forge
  ca-certificates            2025.11.12    hbd8a1cb_0            conda-forge
  certifi                    2024.8.30     pyhd8ed1ab_0          conda-forge
  cffi                       1.17.0        py38heb5c249_0        conda-forge
  charset-normalizer         3.4.0         pyhd8ed1ab_0          conda-forge
  coin-or-cbc                2.10.12       h8b142ea_1            conda-forge
  coin-or-cgl                0.60.7        h516709c_0            conda-forge
  coin-or-clp                1.17.8        h1ee7a9c_0            conda-forge
  coin-or-osi                0.108.10      haf5fa05_0            conda-forge
  coin-or-utils              2.11.11       hee58242_0            conda-forge
  coincbc                    2.10.12       4_metapackage         conda-forge
  configargparse             1.7           pyhd8ed1ab_0          conda-forge
  connection_pool            0.0.3         pyhd3deb0d_0          conda-forge
  datrie                     0.8.2         py38h01eb140_7        conda-forge
  docutils                   0.20.1        py38h578d9bd_3        conda-forge
  dpath                      2.2.0         pyha770c72_0          conda-forge
  filelock                   3.16.1        pyhd8ed1ab_0          conda-forge
  gawk                       5.3.1         hcd3d067_0            conda-forge
  git-lfs                    3.7.1         h6138981_0            conda-forge
  gitdb                      4.0.11        pyhd8ed1ab_0          conda-forge
  gitpython                  3.1.43        pyhd8ed1ab_0          conda-forge
  gmp                        6.3.0         hac33072_2            conda-forge
  gofasta                    1.2.3         h9ee0642_0            bioconda   
  h2                         4.1.0         pyhd8ed1ab_0          conda-forge
  hpack                      4.0.0         pyh9f0ad1d_0          conda-forge
  humanfriendly              10.0          pyhd8ed1ab_6          conda-forge
  hyperframe                 6.0.1         pyhd8ed1ab_0          conda-forge
  icu                        73.2          h59595ed_0            conda-forge
  idna                       3.10          pyhd8ed1ab_0          conda-forge
  importlib_resources        6.4.5         pyhd8ed1ab_0          conda-forge
  isa-l                      2.31.1        hb9d3cd8_1            conda-forge
  jinja2                     3.1.4         pyhd8ed1ab_0          conda-forge
  jsonschema                 4.23.0        pyhd8ed1ab_0          conda-forge
  jsonschema-specifications  2024.10.1     pyhd8ed1ab_0          conda-forge
  jupyter_core               5.8.1         pyh31011fe_0          conda-forge
  k8                         1.2           h6618dc6_1            bioconda   
  kernel-headers_linux-64    5.14.0        he073ed8_3            conda-forge
  keyutils                   1.6.3         hb9d3cd8_0            conda-forge
  krb5                       1.21.3        h659f571_0            conda-forge
  ld_impl_linux-64           2.45          bootstrap_ha15bf96_5  conda-forge
  libasprintf                0.25.1        h3f43e3d_1            conda-forge
  libblas                    3.11.0        5_h4a7cf45_openblas   conda-forge
  libcap                     2.77          h3ff7636_0            conda-forge
  libcblas                   3.11.0        5_h0358290_openblas   conda-forge
  libcbor                    0.10.2        hcb278e6_0            conda-forge
  libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
  libffi                     3.5.2         h9ec8514_0            conda-forge
  libfido2                   1.14.0        h4446dcb_0            conda-forge
  libgcc                     15.2.0        he0feb66_16           conda-forge
  libgcc-ng                  15.2.0        h69a702a_16           conda-forge
  libgettextpo               0.25.1        h3f43e3d_1            conda-forge
  libgfortran                15.2.0        h69a702a_16           conda-forge
  libgfortran-ng             15.2.0        h69a702a_16           conda-forge
  libgfortran5               15.2.0        h68bc16d_16           conda-forge
  libgomp                    15.2.0        he0feb66_16           conda-forge
  libiconv                   1.18          h3b78370_2            conda-forge
  liblapack                  3.11.0        5_h47877c9_openblas   conda-forge
  liblapacke                 3.11.0        5_h6ae95b6_openblas   conda-forge
  liblzma                    5.8.1         hb9d3cd8_2            conda-forge
  liblzma-devel              5.8.1         hb9d3cd8_2            conda-forge
  libnsl                     2.0.1         hb9d3cd8_1            conda-forge
  libopenblas                0.3.30        pthreads_h94d23a6_4   conda-forge
  libopenssl-static          3.6.0         hb03c661_0            conda-forge
  libpng                     1.6.43        h2797004_0            conda-forge
  libprotobuf                3.21.12       hfc55251_2            conda-forge
  libsqlite                  3.46.0        hde9e2c9_0            conda-forge
  libstdcxx                  15.2.0        h934c35e_16           conda-forge
  libstdcxx-ng               15.2.0        hdf11a46_16           conda-forge
  libudev1                   258.3         h6569c3e_0            conda-forge
  libuuid                    2.41.3        h5347b49_0            conda-forge
  libxcrypt                  4.4.36        hd590300_1            conda-forge
  libzlib                    1.2.13        h4ab18f5_6            conda-forge
  mafft                      7.526         h4bc722e_0            conda-forge
  markupsafe                 2.1.5         py38h01eb140_0        conda-forge
  minimap2                   2.28          he4a0461_3            bioconda   
  mpfr                       4.2.1         h90cbb55_3            conda-forge
  mpi                        1.0           openmpi               conda-forge
  mysql-connector-c          6.1.11        h659d440_1008         conda-forge
  nbformat                   5.10.4        pyhd8ed1ab_0          conda-forge
  ncurses                    6.5           h2d0b736_3            conda-forge
  numpy                      1.24.4        py38h59b608b_0        conda-forge
  openmpi                    4.1.2         hbfc84c5_0            conda-forge
  openssh                    9.6p1         h2d3b35a_0            conda-forge
  openssl                    3.6.0         h26f9b46_0            conda-forge
  pip                        19.3.1        py38_0                conda-forge
  pkgutil-resolve-name       1.3.10        pyhd8ed1ab_1          conda-forge
  plac                       1.4.3         pyhd8ed1ab_0          conda-forge
  platformdirs               4.3.6         pyhd8ed1ab_0          conda-forge
  psutil                     6.0.0         py38hfb59056_0        conda-forge
  pulp                       2.7.0         py38h578d9bd_1        conda-forge
  pycparser                  2.22          pyhd8ed1ab_0          conda-forge
  pyparsing                  3.1.4         pyhd8ed1ab_0          conda-forge
  pysocks                    1.7.1         pyha2e5f31_6          conda-forge
  python                     3.8.19        hd12c33a_0_cpython    conda-forge
  python-fastjsonschema      2.20.0        pyhd8ed1ab_0          conda-forge
  python_abi                 3.8           8_cp38                conda-forge
  pyyaml                     6.0.2         py38h2019614_0        conda-forge
  readline                   8.3           h853b02a_0            conda-forge
  referencing                0.35.1        pyhd8ed1ab_0          conda-forge
  requests                   2.32.3        pyhd8ed1ab_0          conda-forge
  reretry                    0.11.8        pyhd8ed1ab_0          conda-forge
  rpds-py                    0.20.0        py38h4005ec7_0        conda-forge
  setuptools                 75.3.0        pyhd8ed1ab_0          conda-forge
  smart_open                 7.0.5         pyhd8ed1ab_1          conda-forge
  smmap                      5.0.0         pyhd8ed1ab_0          conda-forge
  snakemake-minimal          7.24.0        pyhdfd78af_1          bioconda   
  stopit                     1.1.2         py_0                  conda-forge
  sysroot_linux-64           2.34          h087de78_3            conda-forge
  tabulate                   0.9.0         pyhd8ed1ab_1          conda-forge
  throttler                  1.2.2         pyhd8ed1ab_0          conda-forge
  tk                         8.6.13        noxft_h4845f30_101    conda-forge
  toposort                   1.10          pyhd8ed1ab_0          conda-forge
  traitlets                  5.14.3        pyhd8ed1ab_0          conda-forge
  typing_extensions          4.12.2        pyha770c72_0          conda-forge
  tzdata                     2025c         hc9c84f9_1            conda-forge
  ucsc-fatovcf               473           he8037a5_0            bioconda   
  ucsc-stringify             472           he8037a5_0            bioconda   
  urllib3                    2.2.3         pyhd8ed1ab_0          conda-forge
  usher                      0.6.3         hb389108_1            bioconda   
  wheel                      0.45.1        pyhd8ed1ab_0          conda-forge
  wrapt                      1.16.0        py38h01eb140_0        conda-forge
  xz                         5.8.1         hbcc6ac9_2            conda-forge
  xz-gpl-tools               5.8.1         hbcc6ac9_2            conda-forge
  xz-tools                   5.8.1         hb9d3cd8_2            conda-forge
  yaml                       0.2.5         h280c20c_3            conda-forge
  yte                        1.8.1         pyha770c72_0          conda-forge
  zipp                       3.21.0        pyhd8ed1ab_0          conda-forge
  zlib                       1.2.13        h4ab18f5_6            conda-forge
  zstandard                  0.23.0        py38h62bed22_0        conda-forge
  zstd                       1.5.6         ha6fb4c9_0            conda-forge
```

</details>

## pangoLEARN deprecation

As of pangolin version 4.3, pangoLEARN mode has been deprecated. [More info can be found here on the v4.3 release page.](https://github.com/cov-lineages/pangolin/releases/tag/v4.3)

> If `--analysis-mode fast` or `--analysis-mode pangolearn` is given, pangolin v4.3 will print out a warning and use UShER mode instead, unless `--datadir` is also given specifying a directory with pangoLEARN model files. The next release of pangolin-data (v1.20) will no longer include the model files which have not been updated since v1.18.

The pangoLEARN model has not been updated since pangolin-data version 1.18. Only the the underlying UShER tree/protobuf file will be maintained for the forseeable future.

**Please use the UShER mode of pangolin if you want to stay up-to-date with the most recent lineages.** [See pangolin-data release notes here for more details](https://github.com/cov-lineages/pangolin-data/releases)

## Example Usage

```bash
# run Pangolin in the default mode (usher). Can optionally supply --analysis-mode usher
$ pangolin /pangolin/pangolin/test/test_seqs.fasta  -o /data/test_seqs-output-pusher

# view the output CSV
$ column -t -s, /data/test_seqs-output-pusher/lineage_report.csv
taxon                                lineage     conflict  ambiguity_score  scorpio_call                  scorpio_support  scorpio_conflict  scorpio_notes                                                              version       pangolin_version  scorpio_version  constellation_version  is_designated  qc_status  qc_notes                note
India seq                            B.1.617.1   0.0                        B.1.617.1-like                1.0              0.0               scorpio call: Alt alleles 11; Ref alleles 0; Amb alleles 0; Oth alleles 0  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: B.1.617.1(1/1)
b117                                 B.1.1.7     0.0                        Alpha (B.1.1.7-like)          0.91             0.04              scorpio call: Alt alleles 21; Ref alleles 1; Amb alleles 1; Oth alleles 0  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: B.1.1.7(2/2)
outgroup_A                           A           0.0                                                                                                                                                                    PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: A(1/1)
issue_57_torsten_seq                 Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_has_6000_Ns_in_18000_bases  Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_has_no_seq                  Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_is_too_short                Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       Ambiguous_content:0.9   
This_seq_has_lots_of_Ns              Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       Ambiguous_content:0.98  
This_seq_is_literally_just_N         Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
Japan_seq                            B           0.0                                                                                                                                                                    PANGO-v1.16   4.1.3             0.3.17           v0.1.10                True           pass       Ambiguous_content:0.02  Assigned from designation hash.
USA_seq                              B.1.314     0.0                                                                                                                                                                    PANGO-v1.16   4.1.3             0.3.17           v0.1.10                True           pass       Ambiguous_content:0.02  Assigned from designation hash.
Unassigned_omicron_seq               BA.1        0.0                        Probable Omicron (BA.1-like)  0.71             0.08              scorpio call: Alt alleles 42; Ref alleles 5; Amb alleles 9; Oth alleles 3  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.03  Usher placements: BA.1(1/1)
```
