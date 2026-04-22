# Verkko container

Main tool: [verkko](https://github.com/marbl/verkko)
  
Code repository: https://github.com/marbl/verkko

Basic information on how to use this tool:
- executable: `verkko`
- help: `--help`
- version: `--version`
- description: Verkko is a hybrid genome assembly pipeline developed for telomere-to-telomere assembly of PacBio HiFi or Oxford Nanopore Duplex and Oxford Nanopore simplex reads.
  
Full documentation: https://github.com/marbl/verkko

<details>

<summary>Additional tools installed via micromamba:</summary>

```bash
  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
  _openmp_mutex              4.5           20_gnu                conda-forge
  amply                      0.1.6         pyhd8ed1ab_1          conda-forge
  appdirs                    1.4.4         pyhd8ed1ab_1          conda-forge
  argparse-dataclass         2.0.0         pyhd8ed1ab_1          conda-forge
  attrs                      26.1.0        pyhcf101f3_0          conda-forge
  backports.zstd             1.3.0         py311h6b1f9c4_0       conda-forge
  bamtools                   2.5.3         he132191_0            bioconda   
  biopython                  1.87          py311h49ec1c0_0       conda-forge
  brotli-python              1.2.0         py311h66f275b_1       conda-forge
  bwa                        0.7.19        h577a1d6_1            bioconda   
  bzip2                      1.0.8         hda65f42_9            conda-forge
  c-ares                     1.34.6        hb03c661_0            conda-forge
  ca-certificates            2026.2.25     hbd8a1cb_0            conda-forge
  certifi                    2026.2.25     pyhd8ed1ab_0          conda-forge
  charset-normalizer         3.4.7         pyhd8ed1ab_0          conda-forge
  coin-or-cbc                2.10.13       h4d16d09_0            conda-forge
  coin-or-cgl                0.60.10       hc46dffc_0            conda-forge
  coin-or-clp                1.17.11       hc03379b_0            conda-forge
  coin-or-osi                0.108.12      hf4fecb4_0            conda-forge
  coin-or-utils              2.11.13       hc93afbd_0            conda-forge
  coincbc                    2.10.13       0_metapackage         conda-forge
  configargparse             1.7.5         pyhcf101f3_0          conda-forge
  connection_pool            0.0.3         pyhd3deb0d_0          conda-forge
  datrie                     0.8.3         py311h49ec1c0_0       conda-forge
  docutils                   0.22.4        pyhd8ed1ab_0          conda-forge
  dpath                      2.2.0         pyha770c72_1          conda-forge
  findutils                  4.10.0        h86094a7_1            conda-forge
  gitdb                      4.0.12        pyhd8ed1ab_0          conda-forge
  gitpython                  3.1.46        pyhd8ed1ab_0          conda-forge
  graphaligner               1.0.20        h06902ac_1            bioconda   
  gsl                        2.7           he838d99_0            conda-forge
  h2                         4.3.0         pyhcf101f3_0          conda-forge
  hpack                      4.1.0         pyhd8ed1ab_0          conda-forge
  htslib                     1.23.1        h633afcb_0            bioconda   
  humanfriendly              10.0          pyh707e725_8          conda-forge
  hyperframe                 6.1.0         pyhd8ed1ab_0          conda-forge
  icu                        78.3          h33c6efd_0            conda-forge
  idna                       3.11          pyhd8ed1ab_0          conda-forge
  jemalloc                   5.2.0         he1b5a44_0            conda-forge
  jinja2                     3.1.6         pyhcf101f3_1          conda-forge
  jsoncpp                    1.9.6         hf42df4d_1            conda-forge
  jsonschema                 4.26.0        pyhcf101f3_0          conda-forge
  jsonschema-specifications  2025.9.1      pyhcf101f3_0          conda-forge
  jupyter_core               5.9.1         pyhc90fa1f_0          conda-forge
  k8                         1.2           he8db53b_6            bioconda   
  kernel-headers_linux-64    5.14.0        he073ed8_3            conda-forge
  keyutils                   1.6.3         hb9d3cd8_0            conda-forge
  krb5                       1.22.2        ha1258a1_0            conda-forge
  ld_impl_linux-64           2.45.1        default_hbd61a6d_102  conda-forge
  libabseil                  20240116.2    cxx17_he02047a_1      conda-forge
  libblas                    3.11.0        6_h4a7cf45_openblas   conda-forge
  libcblas                   3.11.0        6_h0358290_openblas   conda-forge
  libcurl                    8.19.0        hcf29cc6_0            conda-forge
  libdeflate                 1.25          h17f619e_0            conda-forge
  libdivsufsort              2.0.2         h7b50bb2_10           bioconda   
  libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                      4.33          hd590300_2            conda-forge
  libexpat                   2.7.5         hecca717_0            conda-forge
  libffi                     3.5.2         h3435931_0            conda-forge
  libgcc                     15.2.0        he0feb66_18           conda-forge
  libgcc-ng                  15.2.0        h69a702a_18           conda-forge
  libgfortran                15.2.0        h69a702a_18           conda-forge
  libgfortran5               15.2.0        h68bc16d_18           conda-forge
  libgomp                    15.2.0        he0feb66_18           conda-forge
  liblapack                  3.11.0        6_h47877c9_openblas   conda-forge
  liblapacke                 3.11.0        6_h6ae95b6_openblas   conda-forge
  liblzma                    5.8.3         hb03c661_0            conda-forge
  libnghttp2                 1.68.1        h877daf1_0            conda-forge
  libnsl                     2.0.1         hb9d3cd8_1            conda-forge
  libopenblas                0.3.32        pthreads_h94d23a6_0   conda-forge
  libprotobuf                4.25.3        hd5b35b9_1            conda-forge
  libsqlite                  3.53.0        hf4e2dac_0            conda-forge
  libssh2                    1.11.1        hcf80075_0            conda-forge
  libstdcxx                  15.2.0        h934c35e_18           conda-forge
  libstdcxx-ng               15.2.0        hdf11a46_18           conda-forge
  libuuid                    2.42          h5347b49_0            conda-forge
  libxcrypt                  4.4.36        hd590300_1            conda-forge
  libzlib                    1.3.2         h25fd6f3_2            conda-forge
  markupsafe                 3.0.3         py311h3778330_1       conda-forge
  mashmap                    3.1.3         pl5321hb4818e0_2      bioconda   
  meryl                      1.4.1         h9948957_2            bioconda   
  minimap2                   2.30          h577a1d6_0            bioconda   
  nbformat                   5.10.4        pyhd8ed1ab_1          conda-forge
  ncurses                    6.5           h2d0b736_3            conda-forge
  networkx                   3.5           pyhe01879c_0          conda-forge
  numpy                      2.4.3         py311h2e04523_0       conda-forge
  openblas                   0.3.32        pthreads_h6ec200e_0   conda-forge
  openssl                    3.6.2         h35e630c_0            conda-forge
  packaging                  26.0          pyhcf101f3_0          conda-forge
  parasail-python            1.3.4         py311h6947f6e_6       bioconda   
  perl                       5.32.1        7_hd590300_perl5      conda-forge
  pip                        26.0.1        pyh8b19718_0          conda-forge
  platformdirs               4.9.6         pyhcf101f3_0          conda-forge
  protobuf                   4.25.3        py311hbffca5d_1       conda-forge
  psutil                     7.2.2         py311haee01d2_0       conda-forge
  pulp                       2.7.0         py311h38be061_1       conda-forge
  pyparsing                  3.3.2         pyhcf101f3_0          conda-forge
  pysam                      0.23.3        py311haeb7863_2       bioconda   
  pysocks                    1.7.1         pyha55dd90_7          conda-forge
  python                     3.11.15       hd63d673_0_cpython    conda-forge
  python-fastjsonschema      2.21.2        pyhe01879c_0          conda-forge
  python_abi                 3.11          8_cp311               conda-forge
  pyyaml                     6.0.3         py311h3778330_1       conda-forge
  readline                   8.3           h853b02a_0            conda-forge
  referencing                0.37.0        pyhcf101f3_0          conda-forge
  requests                   2.33.1        pyhcf101f3_0          conda-forge
  reretry                    0.11.8        pyhd8ed1ab_1          conda-forge
  rpds-py                    0.30.0        py311h902ca64_0       conda-forge
  samtools                   1.23.1        ha83d96e_0            bioconda   
  seqtk                      1.5           h577a1d6_1            bioconda   
  setuptools                 81.0.0        pyh332efcf_0          conda-forge
  smart_open                 7.6.0         pyhcf101f3_0          conda-forge
  smmap                      5.0.3         pyhd8ed1ab_0          conda-forge
  snakemake-minimal          7.32.4        pyhdfd78af_1          bioconda   
  stopit                     1.1.2         pyhcf101f3_2          conda-forge
  sysroot_linux-64           2.34          h087de78_3            conda-forge
  tabulate                   0.10.0        pyhcf101f3_0          conda-forge
  throttler                  1.2.2         pyhd8ed1ab_0          conda-forge
  tk                         8.6.13        noxft_h366c992_103    conda-forge
  toml                       0.10.2        pyhcf101f3_3          conda-forge
  toposort                   1.10          pyhd8ed1ab_1          conda-forge
  traitlets                  5.14.3        pyhd8ed1ab_1          conda-forge
  typing_extensions          4.15.0        pyhcf101f3_0          conda-forge
  tzdata                     2025c         hc9c84f9_1            conda-forge
  urllib3                    2.6.3         pyhd8ed1ab_0          conda-forge
  verkko                     2.3.2         hb0edd9e_0            bioconda   
  wheel                      0.46.3        pyhd8ed1ab_0          conda-forge
  winnowmap                  2.03          h5ca1c30_4            bioconda   
  wrapt                      2.1.2         py311h49ec1c0_0       conda-forge
  yaml                       0.2.5         h280c20c_3            conda-forge
  yte                        1.9.4         pyhd8ed1ab_0          conda-forge
  zstd                       1.5.7         hb78ec9c_6            conda-forge
```

</details>

## Example Usage

```bash
verkko -d <work-directory> --hifi <hifi-read-files> [--nano <ont-read-files>]
```

 
