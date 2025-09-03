# UShER container

Main tool: [UShER](https://usher-wiki.readthedocs.io/en/latest/)
  
Code repository: [https://github.com/yatisht/usher](https://github.com/yatisht/usher)

Basic information on how to use this tool:

- executable: `usher`
- help: `--help`
- version: `--version`
- description: __UShER is a program for rapid, accurate placement of samples to existing phylogenies.__
  
Full documentation: [https://usher-wiki.readthedocs.io/en/latest/](https://usher-wiki.readthedocs.io/en/latest/)

Also contains (same version):

- matUtils
- matOptimize
- ripples

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name               Version       Build                  Channel    
───────────────────────────────────────────────────────────────────────
  _libgcc_mutex      0.1           conda_forge            conda-forge
  _openmp_mutex      4.5           2_gnu                  conda-forge
  attr               2.5.1         h166bdaf_1             conda-forge
  boost-cpp          1.85.0        h3c6214e_4             conda-forge
  bzip2              1.0.8         h4bc722e_7             conda-forge
  ca-certificates    2025.7.14     hbd8a1cb_0             conda-forge
  gawk               5.3.1         hcd3d067_0             conda-forge
  gmp                6.3.0         hac33072_2             conda-forge
  icu                75.1          he02047a_0             conda-forge
  isa-l              2.31.1        hb9d3cd8_1             conda-forge
  keyutils           1.6.1         h166bdaf_0             conda-forge
  krb5               1.21.3        h659f571_0             conda-forge
  ld_impl_linux-64   2.44          h1423503_1             conda-forge
  libasprintf        0.25.1        h8e693c7_0             conda-forge
  libboost           1.85.0        h0ccab89_4             conda-forge
  libboost-devel     1.85.0        h00ab1b0_4             conda-forge
  libboost-headers   1.85.0        ha770c72_4             conda-forge
  libcap             2.75          h39aace5_0             conda-forge
  libcbor            0.10.2        hcb278e6_0             conda-forge
  libedit            3.1.20250104  pl5321h7949ede_0       conda-forge
  libexpat           2.7.1         hecca717_0             conda-forge
  libffi             3.4.6         h2dba641_1             conda-forge
  libfido2           1.15.0        hdd1f21f_0             conda-forge
  libgcc             15.1.0        h767d61c_3             conda-forge
  libgcc-ng          15.1.0        h69a702a_3             conda-forge
  libgettextpo       0.25.1        h5888daf_0             conda-forge
  libgfortran        15.1.0        h69a702a_3             conda-forge
  libgfortran-ng     15.1.0        h69a702a_3             conda-forge
  libgfortran5       15.1.0        hcea5267_3             conda-forge
  libgomp            15.1.0        h767d61c_3             conda-forge
  libhwloc           2.12.1        default_h3d81e11_1000  conda-forge
  libiconv           1.18          h4ce23a2_1             conda-forge
  liblzma            5.8.1         hb9d3cd8_2             conda-forge
  liblzma-devel      5.8.1         hb9d3cd8_2             conda-forge
  libnsl             2.0.1         hb9d3cd8_1             conda-forge
  libopenssl-static  3.5.1         hb9d3cd8_0             conda-forge
  libpng             1.6.50        h943b412_0             conda-forge
  libprotobuf        3.20.3        h3eb15da_0             conda-forge
  libsqlite          3.50.3        hee844dc_1             conda-forge
  libstdcxx          15.1.0        h8f9b012_3             conda-forge
  libstdcxx-ng       15.1.0        h4852527_3             conda-forge
  libudev1           257.7         hbe16f8c_0             conda-forge
  libuuid            2.38.1        h0b41bf4_0             conda-forge
  libxcrypt          4.4.36        hd590300_1             conda-forge
  libxml2            2.13.8        h4bc477f_0             conda-forge
  libzlib            1.3.1         hb9d3cd8_2             conda-forge
  mafft              7.526         h4bc722e_0             conda-forge
  mpfr               4.2.1         h90cbb55_3             conda-forge
  mpi                1.0           openmpi                conda-forge
  mysql-connector-c  6.1.11        h659d440_1008          conda-forge
  ncurses            6.5           h2d0b736_3             conda-forge
  openmpi            4.1.6         hc5af2df_101           conda-forge
  openssh            10.0p1        hc830a30_0             conda-forge
  openssl            3.5.1         h7b32b05_0             conda-forge
  pip                25.1.1        pyh8b19718_0           conda-forge
  protobuf           3.20.3        py311hcafe171_1        conda-forge
  python             3.11.13       h9e4cc4f_0_cpython     conda-forge
  python_abi         3.11          8_cp311                conda-forge
  readline           8.2           h8c095d6_2             conda-forge
  setuptools         80.9.0        pyhff2d567_0           conda-forge
  six                1.17.0        pyhe01879c_1           conda-forge
  tbb                2022.2.0      hb60516a_0             conda-forge
  tbb-devel          2022.2.0      h74b38a2_0             conda-forge
  tk                 8.6.13        noxft_hd72426e_102     conda-forge
  tzdata             2025b         h78e105d_0             conda-forge
  ucsc-fatovcf       482           hdc0a859_1             bioconda   
  usher              0.6.6         h719ac0c_1             bioconda   
  wheel              0.45.1        pyhd8ed1ab_1           conda-forge
  xz                 5.8.1         hbcc6ac9_2             conda-forge
  xz-gpl-tools       5.8.1         hbcc6ac9_2             conda-forge
  xz-tools           5.8.1         hb9d3cd8_2             conda-forge
  zlib               1.3.1         hb9d3cd8_2             conda-forge
  zstd               1.5.7         hb8e6e7a_2             conda-forge
```
</details>


## Example Usage

```bash
# create mutation annotated tree object
usher --tree global_phylo.nh --vcf global_samples.vcf --collapse-tree --save-mutation-annotated-tree global_phylo.pb

# place samples onto tree
usher --vcf new_samples.vcf --load-mutation-annotated-tree global_phylo.pb --write-uncondensed-final-tree
```
