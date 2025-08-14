# freyja container

Main tool & documentation: [freyja](https://github.com/andersen-lab/Freyja)

Freyja is a tool to recover relative lineage abundances from mixed samples from a sequencing dataset . The method uses lineage-determining mutational "barcodes" derived from the UShER global phylogenetic tree as a basis set to solve the constrained (unit sum, non-negative) de-mixing problem.

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                           Version       Build                    Channel    
─────────────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex                  0.1           conda_forge              conda-forge
  _openmp_mutex                  4.5           2_gnu                    conda-forge
  alabaster                      1.0.0         pyhd8ed1ab_1             conda-forge
  arrow-cpp                      11.0.0        ha770c72_12_cpu          conda-forge
  attr                           2.5.1         h166bdaf_1               conda-forge
  aws-c-auth                     0.6.26        h987a71b_2               conda-forge
  aws-c-cal                      0.5.21        h48707d8_2               conda-forge
  aws-c-common                   0.8.14        h0b41bf4_0               conda-forge
  aws-c-compression              0.2.16        h03acc5a_5               conda-forge
  aws-c-event-stream             0.2.20        h00877a2_4               conda-forge
  aws-c-http                     0.7.6         hf342b9f_0               conda-forge
  aws-c-io                       0.13.19       h5b20300_3               conda-forge
  aws-c-mqtt                     0.8.6         hc4349f7_12              conda-forge
  aws-c-s3                       0.2.7         h909e904_1               conda-forge
  aws-c-sdkutils                 0.1.9         h03acc5a_0               conda-forge
  aws-checksums                  0.1.14        h03acc5a_5               conda-forge
  aws-crt-cpp                    0.19.8        hf7fbfca_12              conda-forge
  aws-sdk-cpp                    1.10.57       h17c43bd_8               conda-forge
  babel                          2.17.0        pyhd8ed1ab_0             conda-forge
  biopython                      1.85          py311h9ecbd09_1          conda-forge
  boost-cpp                      1.78.0        h2c5509c_4               conda-forge
  brotli                         1.0.9         h166bdaf_9               conda-forge
  brotli-bin                     1.0.9         h166bdaf_9               conda-forge
  brotli-python                  1.0.9         py311ha362b79_9          conda-forge
  bzip2                          1.0.8         h4bc722e_7               conda-forge
  c-ares                         1.34.5        hb9d3cd8_0               conda-forge
  ca-certificates                2025.7.14     hbd8a1cb_0               conda-forge
  certifi                        2025.7.14     pyhd8ed1ab_0             conda-forge
  cffi                           1.17.1        py311hf29c0ef_0          conda-forge
  charset-normalizer             3.4.2         pyhd8ed1ab_0             conda-forge
  clarabel                       0.11.1        py311heb70b45_0          conda-forge
  click                          8.2.1         pyh707e725_0             conda-forge
  colorama                       0.4.6         pyhd8ed1ab_1             conda-forge
  contourpy                      1.3.2         py311hd18a35c_0          conda-forge
  cvxpy                          1.7.1         py311h38be061_0          conda-forge
  cvxpy-base                     1.7.1         py311hed34c8f_0          conda-forge
  cycler                         0.12.1        pyhd8ed1ab_1             conda-forge
  docutils                       0.21.2        pyhd8ed1ab_1             conda-forge
  epiweeks                       2.3.0         pyhdfd78af_0             bioconda   
  fonttools                      4.59.0        py311h3778330_0          conda-forge
  freetype                       2.12.1        h267a509_2               conda-forge
  freyja                         2.0.0         py311h9ee0642_0          bioconda   
  gawk                           5.3.1         hcd3d067_0               conda-forge
  gflags                         2.2.2         h5888daf_1005            conda-forge
  glog                           0.6.0         h6f12383_0               conda-forge
  gmp                            6.3.0         hac33072_2               conda-forge
  h2                             4.2.0         pyhd8ed1ab_0             conda-forge
  hpack                          4.1.0         pyhd8ed1ab_0             conda-forge
  htslib                         1.21          h5efdd21_0               bioconda   
  hyperframe                     6.1.0         pyhd8ed1ab_0             conda-forge
  icu                            73.2          h59595ed_0               conda-forge
  idna                           3.10          pyhd8ed1ab_1             conda-forge
  imagesize                      1.4.1         pyhd8ed1ab_0             conda-forge
  isa-l                          2.31.1        hb9d3cd8_1               conda-forge
  ivar                           1.4.3         h43eeafb_0               bioconda   
  jinja2                         3.1.6         pyhd8ed1ab_0             conda-forge
  joblib                         1.5.1         pyhd8ed1ab_0             conda-forge
  keyutils                       1.6.1         h166bdaf_0               conda-forge
  kiwisolver                     1.4.8         py311hd18a35c_1          conda-forge
  krb5                           1.21.3        h659f571_0               conda-forge
  lcms2                          2.16          hb7c19ff_0               conda-forge
  ld_impl_linux-64               2.44          h1423503_1               conda-forge
  lerc                           4.0.0         h0aef613_1               conda-forge
  libabseil                      20230125.0    cxx17_hcb278e6_1         conda-forge
  libarrow                       11.0.0        h51ec05e_12_cpu          conda-forge
  libasprintf                    0.25.1        h8e693c7_0               conda-forge
  libblas                        3.9.0         32_h59b9bed_openblas     conda-forge
  libbrotlicommon                1.0.9         h166bdaf_9               conda-forge
  libbrotlidec                   1.0.9         h166bdaf_9               conda-forge
  libbrotlienc                   1.0.9         h166bdaf_9               conda-forge
  libcap                         2.75          h39aace5_0               conda-forge
  libcblas                       3.9.0         32_he106b2a_openblas     conda-forge
  libcbor                        0.10.2        hcb278e6_0               conda-forge
  libcrc32c                      1.1.2         h9c3ff4c_0               conda-forge
  libcurl                        8.8.0         hca28451_1               conda-forge
  libdeflate                     1.20          hd590300_0               conda-forge
  libedit                        3.1.20250104  pl5321h7949ede_0         conda-forge
  libev                          4.33          hd590300_2               conda-forge
  libevent                       2.1.12        hf998b51_1               conda-forge
  libexpat                       2.7.1         hecca717_0               conda-forge
  libffi                         3.4.6         h2dba641_1               conda-forge
  libfido2                       1.14.0        h4446dcb_0               conda-forge
  libgcc                         15.1.0        h767d61c_3               conda-forge
  libgcc-ng                      15.1.0        h69a702a_3               conda-forge
  libgettextpo                   0.25.1        h5888daf_0               conda-forge
  libgfortran                    15.1.0        h69a702a_3               conda-forge
  libgfortran-ng                 15.1.0        h69a702a_3               conda-forge
  libgfortran5                   15.1.0        hcea5267_3               conda-forge
  libgomp                        15.1.0        h767d61c_3               conda-forge
  libgoogle-cloud                2.8.0         h0bc5f78_1               conda-forge
  libgrpc                        1.52.1        hcf146ea_1               conda-forge
  libjpeg-turbo                  3.1.0         hb9d3cd8_0               conda-forge
  liblapack                      3.9.0         32_h7ac8fdf_openblas     conda-forge
  liblzma                        5.8.1         hb9d3cd8_2               conda-forge
  liblzma-devel                  5.8.1         hb9d3cd8_2               conda-forge
  libnghttp2                     1.58.0        h47da74e_1               conda-forge
  libnsl                         2.0.1         hb9d3cd8_1               conda-forge
  libopenblas                    0.3.30        pthreads_h94d23a6_0      conda-forge
  libopenssl-static              3.5.1         hb9d3cd8_0               conda-forge
  libosqp                        0.6.3         h5888daf_1               conda-forge
  libpng                         1.6.43        h2797004_0               conda-forge
  libprotobuf                    3.21.12       hfc55251_2               conda-forge
  libqdldl                       0.1.7         hcb278e6_0               conda-forge
  libsqlite                      3.46.0        hde9e2c9_0               conda-forge
  libssh2                        1.11.0        h0841786_0               conda-forge
  libstdcxx                      15.1.0        h8f9b012_3               conda-forge
  libstdcxx-ng                   15.1.0        h4852527_3               conda-forge
  libthrift                      0.18.1        h8fd135c_2               conda-forge
  libtiff                        4.6.0         h1dd3fc0_3               conda-forge
  libudev1                       257.7         hbe16f8c_0               conda-forge
  libutf8proc                    2.8.0         hf23e847_1               conda-forge
  libuuid                        2.38.1        h0b41bf4_0               conda-forge
  libwebp-base                   1.6.0         hd42ef1d_0               conda-forge
  libxcb                         1.15          h0b41bf4_0               conda-forge
  libxcrypt                      4.4.36        hd590300_1               conda-forge
  libzlib                        1.2.13        h4ab18f5_6               conda-forge
  lz4-c                          1.9.4         hcb278e6_0               conda-forge
  mafft                          7.526         h4bc722e_0               conda-forge
  markupsafe                     3.0.2         py311h2dc5d0c_1          conda-forge
  matplotlib-base                3.10.1        py311h2b939e6_0          conda-forge
  mpfr                           4.2.1         h90cbb55_3               conda-forge
  mpi                            1.0           openmpi                  conda-forge
  munkres                        1.1.4         pyhd8ed1ab_1             conda-forge
  mysql-connector-c              6.1.11        h659d440_1008            conda-forge
  narwhals                       1.48.0        pyhe01879c_0             conda-forge
  ncurses                        6.5           h2d0b736_3               conda-forge
  numpy                          1.26.4        py311h64a7726_0          conda-forge
  openjpeg                       2.5.2         h488ebb8_0               conda-forge
  openmpi                        4.1.2         hbfc84c5_0               conda-forge
  openssh                        9.6p1         h2d3b35a_0               conda-forge
  openssl                        3.5.1         h7b32b05_0               conda-forge
  orc                            1.8.3         h2f23424_1               conda-forge
  osqp                           0.6.7.post3   py311h7db5c69_1          conda-forge
  packaging                      25.0          pyh29332c3_1             conda-forge
  pandas                         2.3.1         py311hed34c8f_0          conda-forge
  parquet-cpp                    1.5.1         2                        conda-forge
  pillow                         10.3.0        py311h18e6fac_0          conda-forge
  pip                            25.1.1        pyh8b19718_0             conda-forge
  plotly                         6.2.0         pyhd8ed1ab_0             conda-forge
  pthread-stubs                  0.4           hb9d3cd8_1002            conda-forge
  pyarrow                        11.0.0        py311hbdf6286_12_cpu     conda-forge
  pycparser                      2.22          pyh29332c3_1             conda-forge
  pygments                       2.19.2        pyhd8ed1ab_0             conda-forge
  pyparsing                      3.2.3         pyhd8ed1ab_1             conda-forge
  pysam                          0.22.1        py311h1f0e11c_2          bioconda   
  pysocks                        1.7.1         pyha55dd90_7             conda-forge
  python                         3.11.9        hb806964_0_cpython       conda-forge
  python-dateutil                2.9.0.post0   pyhe01879c_2             conda-forge
  python-tzdata                  2025.2        pyhd8ed1ab_0             conda-forge
  python_abi                     3.11          8_cp311                  conda-forge
  pytz                           2025.2        pyhd8ed1ab_0             conda-forge
  pyyaml                         6.0.2         py311h2dc5d0c_2          conda-forge
  qdldl-python                   0.1.7.post5   np20py311h31610b7_1      conda-forge
  qhull                          2020.2        h434a139_5               conda-forge
  re2                            2023.02.02    hcb278e6_0               conda-forge
  readline                       8.2           h8c095d6_2               conda-forge
  requests                       2.32.4        pyhd8ed1ab_0             conda-forge
  roman-numerals-py              3.1.0         pyhd8ed1ab_0             conda-forge
  s2n                            1.3.41        h3358134_0               conda-forge
  samtools                       1.21          h50ea8bc_0               bioconda   
  scipy                          1.16.0        py311h2d3ef60_0          conda-forge
  scs                            3.2.7.post2   default_py311he11e7d9_0  conda-forge
  seaborn-base                   0.13.2        pyhd8ed1ab_3             conda-forge
  setuptools                     80.9.0        pyhff2d567_0             conda-forge
  six                            1.17.0        pyhe01879c_1             conda-forge
  snappy                         1.1.10        hdb0a2a9_1               conda-forge
  snowballstemmer                3.0.1         pyhd8ed1ab_0             conda-forge
  sphinx                         8.2.3         pyhd8ed1ab_0             conda-forge
  sphinx-click                   6.0.0         pyhd8ed1ab_1             conda-forge
  sphinx_rtd_theme               3.0.1         pyha770c72_0             conda-forge
  sphinxcontrib-applehelp        2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-devhelp          2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-htmlhelp         2.1.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jquery           4.1           pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jsmath           1.0.1         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-qthelp           2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-serializinghtml  1.1.10        pyhd8ed1ab_1             conda-forge
  tk                             8.6.13        noxft_h4845f30_101       conda-forge
  tqdm                           4.67.1        pyhd8ed1ab_1             conda-forge
  tzdata                         2025b         h78e105d_0               conda-forge
  ucsc-fatovcf                   473           he8037a5_0               bioconda   
  ucsc-stringify                 472           he8037a5_0               bioconda   
  unicodedata2                   16.0.0        py311h9ecbd09_0          conda-forge
  urllib3                        2.5.0         pyhd8ed1ab_0             conda-forge
  usher                          0.6.3         hb389108_1               bioconda   
  wheel                          0.45.1        pyhd8ed1ab_1             conda-forge
  xorg-libxau                    1.0.12        hb9d3cd8_0               conda-forge
  xorg-libxdmcp                  1.1.5         hb9d3cd8_0               conda-forge
  xz                             5.8.1         hbcc6ac9_2               conda-forge
  xz-gpl-tools                   5.8.1         hbcc6ac9_2               conda-forge
  xz-tools                       5.8.1         hb9d3cd8_2               conda-forge
  yaml                           0.2.5         h7f98852_2               conda-forge
  zlib                           1.2.13        h4ab18f5_6               conda-forge
  zstandard                      0.23.0        py311h9ecbd09_2          conda-forge
  zstd                           1.5.6         ha6fb4c9_0               conda-forge
```
</details>

## freyja barcodes

This docker image was built on **2025-07-22** and the command `freyja update` is run as part of the build to retrieve the most up-to-date database. The barcode version included in this docker image is **`07_21_2025-00-46`** as reported by `freyja demix --version`

This image is rebuilt every week on Dockerhub and Quay.io with the tag ${freyja version}-${freyja database version}-${data image was deployed}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants 
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write privileges, such as a mounted volume.
