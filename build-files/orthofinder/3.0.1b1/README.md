# OrthoFinder container

Main tool : 
- [OrthoFinder](https://github.com/davidemms/OrthoFinder)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                     Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex            0.1           conda_forge           conda-forge
  _openmp_mutex            4.5           2_gnu                 conda-forge
  aria2                    1.37.0        hbc8128a_2            conda-forge
  aster                    1.22          h9948957_1            bioconda   
  biopython                1.85          py311h9ecbd09_1       conda-forge
  blast                    2.16.0        h66d330f_5            bioconda   
  bzip2                    1.0.8         h4bc722e_7            conda-forge
  c-ares                   1.34.5        hb9d3cd8_0            conda-forge
  ca-certificates          2025.6.15     hbd8a1cb_0            conda-forge
  curl                     8.14.1        h332b0f4_0            conda-forge
  diamond                  2.1.12        h13889ed_2            bioconda   
  entrez-direct            22.4          he881be0_0            bioconda   
  fastme                   2.1.6.3       h7b50bb2_1            bioconda   
  fasttree                 2.1.11        h7b50bb2_5            bioconda   
  gawk                     5.3.1         hcd3d067_0            conda-forge
  gmp                      6.3.0         hac33072_2            conda-forge
  icu                      75.1          he02047a_0            conda-forge
  iqtree                   2.4.0         h503566f_0            bioconda   
  joblib                   1.5.1         pyhd8ed1ab_0          conda-forge
  keyutils                 1.6.1         h166bdaf_0            conda-forge
  krb5                     1.21.3        h659f571_0            conda-forge
  ld_impl_linux-64         2.43          h1423503_5            conda-forge
  libasprintf              0.24.1        h8e693c7_0            conda-forge
  libblas                  3.9.0         32_h59b9bed_openblas  conda-forge
  libcblas                 3.9.0         32_he106b2a_openblas  conda-forge
  libcurl                  8.14.1        h332b0f4_0            conda-forge
  libedit                  3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                    4.33          hd590300_2            conda-forge
  libexpat                 2.7.0         h5888daf_0            conda-forge
  libffi                   3.4.6         h2dba641_1            conda-forge
  libgcc                   15.1.0        h767d61c_3            conda-forge
  libgcc-ng                15.1.0        h69a702a_3            conda-forge
  libgettextpo             0.24.1        h5888daf_0            conda-forge
  libgfortran              15.1.0        h69a702a_3            conda-forge
  libgfortran-ng           15.1.0        h69a702a_3            conda-forge
  libgfortran5             15.1.0        hcea5267_3            conda-forge
  libgomp                  15.1.0        h767d61c_3            conda-forge
  libiconv                 1.18          h4ce23a2_1            conda-forge
  libidn2                  2.3.8         ha4ef2c3_0            conda-forge
  liblapack                3.9.0         32_h7ac8fdf_openblas  conda-forge
  liblzma                  5.8.1         hb9d3cd8_2            conda-forge
  libnghttp2               1.64.0        h161d5f1_0            conda-forge
  libnsl                   2.0.1         hb9d3cd8_1            conda-forge
  libopenblas              0.3.30        pthreads_h94d23a6_0   conda-forge
  libsqlite                3.50.2        h6cd9bfd_0            conda-forge
  libssh2                  1.11.1        hcf80075_0            conda-forge
  libstdcxx                15.1.0        h8f9b012_3            conda-forge
  libstdcxx-ng             15.1.0        h4852527_3            conda-forge
  libunistring             0.9.10        h7f98852_0            conda-forge
  libuuid                  2.38.1        h0b41bf4_0            conda-forge
  libxcrypt                4.4.36        hd590300_1            conda-forge
  libxml2                  2.13.8        h4bc477f_0            conda-forge
  libzlib                  1.3.1         hb9d3cd8_2            conda-forge
  mafft                    7.526         h4bc722e_0            conda-forge
  mcl                      22.282        pl5321h7b50bb2_4      bioconda   
  mmseqs2                  17.b804f      hd6d6fdc_1            bioconda   
  mpfr                     4.2.1         h90cbb55_3            conda-forge
  mpi                      1.0           openmpi               conda-forge
  muscle                   3.8.1551      h9948957_8            bioconda   
  ncbi-vdb                 3.2.1         h9948957_0            bioconda   
  ncurses                  6.5           h2d0b736_3            conda-forge
  numpy                    2.3.1         py311h519dc76_0       conda-forge
  openmpi                  4.1.6         hc5af2df_101          conda-forge
  openssl                  3.5.0         h7b32b05_1            conda-forge
  orthofinder              3.0.1b1       hdfd78af_0            bioconda   
  perl                     5.32.1        7_hd590300_perl5      conda-forge
  perl-archive-tar         3.04          pl5321hdfd78af_0      bioconda   
  perl-carp                1.50          pl5321hd8ed1ab_0      conda-forge
  perl-common-sense        3.75          pl5321hd8ed1ab_0      conda-forge
  perl-compress-raw-bzip2  2.201         pl5321hbf60520_1      conda-forge
  perl-compress-raw-zlib   2.202         pl5321hadc24fc_0      conda-forge
  perl-encode              3.21          pl5321hb9d3cd8_1      conda-forge
  perl-exporter            5.74          pl5321hd8ed1ab_0      conda-forge
  perl-exporter-tiny       1.002002      pl5321hd8ed1ab_0      conda-forge
  perl-extutils-makemaker  7.70          pl5321hd8ed1ab_0      conda-forge
  perl-io-compress         2.201         pl5321h503566f_5      bioconda   
  perl-io-zlib             1.15          pl5321hdfd78af_0      bioconda   
  perl-json                4.10          pl5321hdfd78af_1      bioconda   
  perl-json-xs             4.03          pl5321h9948957_4      bioconda   
  perl-list-moreutils      0.430         pl5321hdfd78af_0      bioconda   
  perl-list-moreutils-xs   0.430         pl5321h7b50bb2_5      bioconda   
  perl-parent              0.243         pl5321hd8ed1ab_0      conda-forge
  perl-pathtools           3.75          pl5321hb9d3cd8_2      conda-forge
  perl-scalar-list-utils   1.69          pl5321hb9d3cd8_0      conda-forge
  perl-storable            3.15          pl5321hb9d3cd8_2      conda-forge
  perl-types-serialiser    1.01          pl5321hdfd78af_0      bioconda   
  pip                      25.1.1        pyh8b19718_0          conda-forge
  python                   3.11.13       h9e4cc4f_0_cpython    conda-forge
  python_abi               3.11          7_cp311               conda-forge
  raxml                    8.2.13        h7b50bb2_3            bioconda   
  raxml-ng                 1.2.2         h6747034_2            bioconda   
  readline                 8.2           h8c095d6_2            conda-forge
  rpsbproc                 0.5.0         hd6d6fdc_3            bioconda   
  scikit-learn             1.7.0         py311h57cc02b_1       conda-forge
  scipy                    1.16.0        py311h2d3ef60_0       conda-forge
  setuptools               80.9.0        pyhff2d567_0          conda-forge
  threadpoolctl            3.6.0         pyhecae5ae_0          conda-forge
  tk                       8.6.13        noxft_hd72426e_102    conda-forge
  tzdata                   2025b         h78e105d_0            conda-forge
  wget                     1.21.4        hda4d442_0            conda-forge
  wheel                    0.45.1        pyhd8ed1ab_1          conda-forge
  zlib                     1.3.1         hb9d3cd8_2            conda-forge
  zstd                     1.5.7         hb8e6e7a_2            conda-forge
```

</details>

Basic information on how to use this tool:
- executable: orthofinder
- help: -h
- version: NA
- description: Phylogenetic orthology inference for comparative genomics

Full documentation: [https://davidemms.github.io/](https://davidemms.github.io/)


## Example Usage

```bash
orthofinder -f directory_with_data/
```
