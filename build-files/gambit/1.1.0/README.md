# gambit container

Main tool : [gambit](github.com/jlumpe/gambit)

Full documentation: https://gambit-genomics.readthedocs.io/en/latest/

GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking) is a tool for rapid taxonomic identification of microbial pathogens. It uses an extremely efficient genomic distance metric along with a curated database of approximately 50,000 reference genomes (derived from NCBI RefSeq) to identify unknown bacterial genomes within seconds.

## Dependencies

GAMBIT is built using [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) with the following dependencies:

<details>
<summary>Dependencies</summary>
  
List of packages in environment: "/opt/conda"

  Name                Version       Build                    Channel    
──────────────────────────────────────────────────────────────────────────
  _openmp_mutex       4.5           20_gnu                   conda-forge
  alembic             1.18.4        pyhcf101f3_0             conda-forge
  attrs               26.1.0        pyhcf101f3_0             conda-forge
  aws-c-auth          0.10.1        h2d2dd48_2               conda-forge
  aws-c-cal           0.9.13        h2c9d079_1               conda-forge
  aws-c-common        0.12.6        hb03c661_0               conda-forge
  aws-c-compression   0.3.2         h8b1a151_0               conda-forge
  aws-c-http          0.10.12       h4bacb7b_1               conda-forge
  aws-c-io            0.26.3        hc87160b_0               conda-forge
  aws-c-s3            0.11.5        h6d69fc9_5               conda-forge
  aws-c-sdkutils      0.2.4         h8b1a151_4               conda-forge
  aws-checksums       0.2.10        h8b1a151_0               conda-forge
  biopython           1.87          py311h49ec1c0_0          conda-forge
  bzip2               1.0.8         hda65f42_9               conda-forge
  c-ares              1.34.6        hb03c661_0               conda-forge
  ca-certificates     2026.2.25     hbd8a1cb_0               conda-forge
  cached-property     1.5.2         hd8ed1ab_1               conda-forge
  cached_property     1.5.2         pyha770c72_1             conda-forge
  cattrs              26.1.0        pyhcf101f3_1             conda-forge
  click               8.3.1         pyh8f84b5b_1             conda-forge
  exceptiongroup      1.3.1         pyhd8ed1ab_0             conda-forge
  gambit              1.1.0         pypi_0                   pypi       
  greenlet            3.3.2         py311hc665b79_0          conda-forge
  h5py                3.16.0        nompi_py311hfef529e_101  conda-forge
  hdf5                2.1.0         nompi_hd4fcb43_103       conda-forge
  icu                 78.3          h33c6efd_0               conda-forge
  importlib-metadata  8.8.0         pyhcf101f3_0             conda-forge
  keyutils            1.6.3         hb9d3cd8_0               conda-forge
  krb5                1.22.2        ha1258a1_0               conda-forge
  ld_impl_linux-64    2.45.1        default_hbd61a6d_102     conda-forge
  libaec              1.1.5         h088129d_0               conda-forge
  libblas             3.11.0        6_h4a7cf45_openblas      conda-forge
  libcblas            3.11.0        6_h0358290_openblas      conda-forge
  libcurl             8.19.0        hcf29cc6_0               conda-forge
  libedit             3.1.20250104  pl5321h7949ede_0         conda-forge
  libev               4.33          hd590300_2               conda-forge
  libffi              3.5.2         h3435931_0               conda-forge
  libgcc              15.2.0        he0feb66_18              conda-forge
  libgcc-ng           15.2.0        h69a702a_18              conda-forge
  libgfortran         15.2.0        h69a702a_18              conda-forge
  libgfortran5        15.2.0        h68bc16d_18              conda-forge
  libgomp             15.2.0        he0feb66_18              conda-forge
  liblapack           3.11.0        6_h47877c9_openblas      conda-forge
  liblzma             5.8.2         hb03c661_0               conda-forge
  liblzma-devel       5.8.2         hb03c661_0               conda-forge
  libnghttp2          1.68.1        h877daf1_0               conda-forge
  libnsl              2.0.1         hb9d3cd8_1               conda-forge
  libopenblas         0.3.32        pthreads_h94d23a6_0      conda-forge
  libsqlite           3.52.0        hf4e2dac_0               conda-forge
  libssh2             1.11.1        hcf80075_0               conda-forge
  libstdcxx           15.2.0        h934c35e_18              conda-forge
  libstdcxx-ng        15.2.0        hdf11a46_18              conda-forge
  libuuid             2.42          h5347b49_0               conda-forge
  libzlib             1.3.2         h25fd6f3_2               conda-forge
  mako                1.3.10        pyhcf101f3_1             conda-forge
  markupsafe          3.0.3         py311h3778330_1          conda-forge
  ncurses             6.5           h2d0b736_3               conda-forge
  numpy               1.26.4        py311h64a7726_0          conda-forge
  openssl             3.6.1         h35e630c_1               conda-forge
  packaging           26.0          pyhcf101f3_0             conda-forge
  pandas              3.0.2         py311h8032f78_0          conda-forge
  pip                 26.0.1        pyh8b19718_0             conda-forge
  python              3.11.0        he550d4f_1_cpython       conda-forge
  python-dateutil     2.9.0.post0   pyhe01879c_2             conda-forge
  python_abi          3.11          8_cp311                  conda-forge
  readline            8.3           h853b02a_0               conda-forge
  s2n                 1.7.1         h1cbb8d7_1               conda-forge
  scipy               1.17.1        py311hbe70eeb_0          conda-forge
  setuptools          82.0.1        pyh332efcf_0             conda-forge
  six                 1.17.0        pyhe01879c_1             conda-forge
  sqlalchemy          2.0.48        py311haee01d2_0          conda-forge
  tk                  8.6.13        noxft_h366c992_103       conda-forge
  tomli               2.4.1         pyhcf101f3_0             conda-forge
  typing-extensions   4.15.0        h396c80c_0               conda-forge
  typing_extensions   4.15.0        pyhcf101f3_0             conda-forge
  tzdata              2025c         hc9c84f9_1               conda-forge
  wheel               0.46.3        pyhd8ed1ab_0             conda-forge
  xz                  5.8.2         ha02ee65_0               conda-forge
  xz-gpl-tools        5.8.2         ha02ee65_0               conda-forge
  xz-tools            5.8.2         hb03c661_0               conda-forge
  zipp                3.23.0        pyhcf101f3_1             conda-forge
  zstd                1.5.7         hb78ec9c_6               conda-forge
</details>

## Example Usage

```bash
# run gambit on assembly 
gambit query GCF_000240185.1_ASM24018v2_genomic.fna
```
