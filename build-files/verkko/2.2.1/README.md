# Verkko container

Main tool: [verkko](https://github.com/marbl/verkko)
  
Code repository: https://github.com/marbl/verkko

Basic information on how to use this tool:
- executable: verkko
- help: --help
- version: --version
- description: Verkko is a hybrid genome assembly pipeline developed for telomere-to-telomere assembly of PacBio HiFi or Oxford Nanopore Duplex and Oxford Nanopore simplex reads.
  
Full documentation: https://github.com/marbl/verkko

## Additional included tools/dependencies

verkko is installed with micromamba. These are the dependencies installed alongside verkko:
```bash
  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex              0.1           conda_forge           conda-forge
  _openmp_mutex              4.5           2_gnu                 conda-forge
  amply                      0.1.6         pyhd8ed1ab_1          conda-forge
  appdirs                    1.4.4         pyhd8ed1ab_1          conda-forge
  attrs                      25.1.0        pyh71513ae_0          conda-forge
  bamtools                   2.5.2         hdcf5f25_5            bioconda   
  biopython                  1.85          py39h8cd3c5a_1        conda-forge
  brotli-python              1.1.0         py39hf88036b_2        conda-forge
  bwa                        0.7.18        he4a0461_1            bioconda   
  bzip2                      1.0.8         h4bc722e_7            conda-forge
  c-ares                     1.34.4        hb9d3cd8_0            conda-forge
  ca-certificates            2025.1.31     hbcca054_0            conda-forge
  certifi                    2025.1.31     pyhd8ed1ab_0          conda-forge
  cffi                       1.17.1        py39h15c3d72_0        conda-forge
  charset-normalizer         3.4.1         pyhd8ed1ab_0          conda-forge
  coin-or-cbc                2.10.12       h8b142ea_1            conda-forge
  coin-or-cgl                0.60.7        h516709c_0            conda-forge
  coin-or-clp                1.17.8        h1ee7a9c_0            conda-forge
  coin-or-osi                0.108.10      haf5fa05_0            conda-forge
  coin-or-utils              2.11.11       hee58242_0            conda-forge
  coincbc                    2.10.12       1_metapackage         conda-forge
  configargparse             1.7           pyhd8ed1ab_1          conda-forge
  connection_pool            0.0.3         pyhd3deb0d_0          conda-forge
  datrie                     0.8.2         py39h8cd3c5a_8        conda-forge
  docutils                   0.21.2        pyhd8ed1ab_1          conda-forge
  dpath                      2.2.0         pyha770c72_0          conda-forge
  findutils                  4.6.0         h166bdaf_1001         conda-forge
  gettext                    0.23.1        h5888daf_0            conda-forge
  gettext-tools              0.23.1        h5888daf_0            conda-forge
  gitdb                      4.0.12        pyhd8ed1ab_0          conda-forge
  gitpython                  3.1.44        pyhff2d567_0          conda-forge
  graphaligner               1.0.20        h06902ac_0            bioconda   
  gsl                        2.7           he838d99_0            conda-forge
  h2                         4.2.0         pyhd8ed1ab_0          conda-forge
  hpack                      4.1.0         pyhd8ed1ab_0          conda-forge
  htslib                     1.21          h5efdd21_0            bioconda   
  humanfriendly              10.0          pyh707e725_8          conda-forge
  hyperframe                 6.1.0         pyhd8ed1ab_0          conda-forge
  idna                       3.10          pyhd8ed1ab_1          conda-forge
  importlib_resources        6.5.2         pyhd8ed1ab_0          conda-forge
  jemalloc                   5.2.0         he1b5a44_0            conda-forge
  jinja2                     3.1.5         pyhd8ed1ab_0          conda-forge
  jsonschema                 4.23.0        pyhd8ed1ab_1          conda-forge
  jsonschema-specifications  2024.10.1     pyhd8ed1ab_1          conda-forge
  jupyter_core               5.7.2         pyh31011fe_1          conda-forge
  k8                         0.2.5         hdcf5f25_4            bioconda   
  keyutils                   1.6.1         h166bdaf_0            conda-forge
  krb5                       1.21.3        h659f571_0            conda-forge
  ld_impl_linux-64           2.43          h712a8e2_4            conda-forge
  libasprintf                0.23.1        h8e693c7_0            conda-forge
  libasprintf-devel          0.23.1        h8e693c7_0            conda-forge
  libblas                    3.9.0         31_h59b9bed_openblas  conda-forge
  libcblas                   3.9.0         31_he106b2a_openblas  conda-forge
  libcurl                    8.8.0         hca28451_1            conda-forge
  libdeflate                 1.23          h4ddbbb0_0            conda-forge
  libdivsufsort              2.0.2         h7b50bb2_10           bioconda   
  libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                      4.33          hd590300_2            conda-forge
  libffi                     3.4.6         h2dba641_0            conda-forge
  libgcc                     14.2.0        h767d61c_2            conda-forge
  libgcc-ng                  14.2.0        h69a702a_2            conda-forge
  libgettextpo               0.23.1        h5888daf_0            conda-forge
  libgettextpo-devel         0.23.1        h5888daf_0            conda-forge
  libgfortran                14.2.0        h69a702a_2            conda-forge
  libgfortran-ng             14.2.0        h69a702a_2            conda-forge
  libgfortran5               14.2.0        hf1ad2bd_2            conda-forge
  libgomp                    14.2.0        h767d61c_2            conda-forge
  liblapack                  3.9.0         31_h7ac8fdf_openblas  conda-forge
  liblapacke                 3.9.0         31_he2f377e_openblas  conda-forge
  liblzma                    5.6.4         hb9d3cd8_0            conda-forge
  liblzma-devel              5.6.4         hb9d3cd8_0            conda-forge
  libnghttp2                 1.58.0        h47da74e_1            conda-forge
  libnsl                     2.0.1         hd590300_0            conda-forge
  libopenblas                0.3.29        pthreads_h94d23a6_0   conda-forge
  libprotobuf                3.14.0        h780b84a_0            conda-forge
  libsqlite                  3.46.0        hde9e2c9_0            conda-forge
  libssh2                    1.11.0        h0841786_0            conda-forge
  libstdcxx                  14.2.0        h8f9b012_2            conda-forge
  libstdcxx-ng               14.2.0        h4852527_2            conda-forge
  libuuid                    2.38.1        h0b41bf4_0            conda-forge
  libxcrypt                  4.4.36        hd590300_1            conda-forge
  libzlib                    1.2.13        h4ab18f5_6            conda-forge
  markupsafe                 3.0.2         py39h9399b63_1        conda-forge
  mashmap                    3.1.3         h07ea13f_1            bioconda   
  meryl                      1.4.1         h9948957_2            bioconda   
  minimap2                   2.28          he4a0461_3            bioconda   
  nbformat                   5.10.4        pyhd8ed1ab_1          conda-forge
  ncurses                    6.5           h2d0b736_3            conda-forge
  networkx                   3.2.1         pyhd8ed1ab_0          conda-forge
  numpy                      2.0.2         py39h9cb892a_1        conda-forge
  openblas                   0.3.29        pthreads_h6ec200e_0   conda-forge
  openssl                    3.4.1         h7b32b05_0            conda-forge
  packaging                  24.2          pyhd8ed1ab_2          conda-forge
  parasail-python            1.3.4         py39heaaa4ec_2        bioconda   
  perl                       5.32.1        7_hd590300_perl5      conda-forge
  pip                        25.0.1        pyh8b19718_0          conda-forge
  pkgutil-resolve-name       1.3.10        pyhd8ed1ab_2          conda-forge
  plac                       1.4.3         pyhd8ed1ab_1          conda-forge
  platformdirs               4.3.6         pyhd8ed1ab_1          conda-forge
  protobuf                   3.14.0        py39he80948d_1        conda-forge
  psutil                     6.1.1         py39h8cd3c5a_0        conda-forge
  pulp                       2.7.0         py39hf3d152e_1        conda-forge
  pycparser                  2.22          pyh29332c3_1          conda-forge
  pyparsing                  3.2.1         pyhd8ed1ab_0          conda-forge
  pysam                      0.22.1        py39h61809e1_2        bioconda   
  pysocks                    1.7.1         pyha55dd90_7          conda-forge
  python                     3.9.19        h0755675_0_cpython    conda-forge
  python-fastjsonschema      2.21.1        pyhd8ed1ab_0          conda-forge
  python_abi                 3.9           5_cp39                conda-forge
  pyyaml                     6.0.2         py39h9399b63_2        conda-forge
  readline                   8.2           h8c095d6_2            conda-forge
  referencing                0.36.2        pyh29332c3_0          conda-forge
  requests                   2.32.3        pyhd8ed1ab_1          conda-forge
  reretry                    0.11.8        pyhd8ed1ab_1          conda-forge
  rpds-py                    0.23.1        py39h3506688_0        conda-forge
  samtools                   1.21          h50ea8bc_0            bioconda   
  seqtk                      1.4           he4a0461_2            bioconda   
  setuptools                 75.8.0        pyhff2d567_0          conda-forge
  six                        1.17.0        pyhd8ed1ab_0          conda-forge
  smart_open                 7.1.0         pyhd8ed1ab_0          conda-forge
  smmap                      5.0.2         pyhd8ed1ab_0          conda-forge
  snakemake-minimal          7.32.4        pyhdfd78af_1          bioconda   
  stopit                     1.1.2         pyhd8ed1ab_1          conda-forge
  tabulate                   0.9.0         pyhd8ed1ab_2          conda-forge
  throttler                  1.2.2         pyhd8ed1ab_0          conda-forge
  tk                         8.6.13        noxft_h4845f30_101    conda-forge
  toposort                   1.10          pyhd8ed1ab_1          conda-forge
  traitlets                  5.14.3        pyhd8ed1ab_1          conda-forge
  typing_extensions          4.12.2        pyha770c72_1          conda-forge
  tzdata                     2025a         h78e105d_0            conda-forge
  urllib3                    2.3.0         pyhd8ed1ab_0          conda-forge
  verkko                     2.2.1         h45dadce_0            bioconda   
  wheel                      0.45.1        pyhd8ed1ab_1          conda-forge
  winnowmap                  2.03          h43eeafb_2            bioconda   
  wrapt                      1.17.2        py39h8cd3c5a_0        conda-forge
  xz                         5.6.4         hbcc6ac9_0            conda-forge
  xz-gpl-tools               5.6.4         hbcc6ac9_0            conda-forge
  xz-tools                   5.6.4         hb9d3cd8_0            conda-forge
  yaml                       0.2.5         h7f98852_2            conda-forge
  yte                        1.5.7         pyha770c72_0          conda-forge
  zipp                       3.21.0        pyhd8ed1ab_1          conda-forge
  zlib                       1.2.13        h4ab18f5_6            conda-forge
  zstandard                  0.23.0        py39h08a7858_1        conda-forge
  zstd                       1.5.6         ha6fb4c9_0            conda-forge
```

## Example Usage

```bash
verkko -d <work-directory> --hifi <hifi-read-files> [--nano <ont-read-files>]
```

 