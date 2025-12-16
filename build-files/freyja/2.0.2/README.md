# freyja container

Main tool & documentation: [freyja](https://github.com/andersen-lab/Freyja)

Freyja is a tool to recover relative lineage abundances from mixed samples from a sequencing dataset . The method uses lineage-determining mutational "barcodes" derived from the UShER global phylogenetic tree as a basis set to solve the constrained (unit sum, non-negative) de-mixing problem.

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/freyja-env"

  Name                              Version       Build                    Channel    
────────────────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex                     0.1           conda_forge              conda-forge
  _openmp_mutex                     4.5           2_gnu                    conda-forge
  alabaster                         1.0.0         pyhd8ed1ab_1             conda-forge
  aws-c-auth                        0.7.31        he1a10d6_2               conda-forge
  aws-c-cal                         0.7.4         hae4d56a_2               conda-forge
  aws-c-common                      0.9.29        hb9d3cd8_0               conda-forge
  aws-c-compression                 0.2.19        h2bff981_2               conda-forge
  aws-c-event-stream                0.4.3         h19b0707_4               conda-forge
  aws-c-http                        0.8.10        h14a7884_2               conda-forge
  aws-c-io                          0.14.19       hc9e6898_1               conda-forge
  aws-c-mqtt                        0.10.7        hb8d5873_2               conda-forge
  aws-c-s3                          0.6.7         h666547d_0               conda-forge
  aws-c-sdkutils                    0.1.19        h2bff981_4               conda-forge
  aws-checksums                     0.1.20        h2bff981_1               conda-forge
  aws-crt-cpp                       0.28.3        hbe26082_8               conda-forge
  aws-sdk-cpp                       1.11.407      h25d6d5c_1               conda-forge
  azure-core-cpp                    1.13.0        h935415a_0               conda-forge
  azure-identity-cpp                1.8.0         hd126650_2               conda-forge
  azure-storage-blobs-cpp           12.12.0       hd2e3451_0               conda-forge
  azure-storage-common-cpp          12.7.0        h10ac4d7_1               conda-forge
  azure-storage-files-datalake-cpp  12.11.0       h325d260_1               conda-forge
  babel                             2.17.0        pyhd8ed1ab_0             conda-forge
  biopython                         1.86          py312h4c3975b_0          conda-forge
  boost-cpp                         1.85.0        h3c6214e_4               conda-forge
  brotli                            1.1.0         hb03c661_4               conda-forge
  brotli-bin                        1.1.0         hb03c661_4               conda-forge
  brotli-python                     1.1.0         py312h1289d80_4          conda-forge
  bzip2                             1.0.8         hda65f42_8               conda-forge
  c-ares                            1.34.6        hb03c661_0               conda-forge
  ca-certificates                   2025.11.12    hbd8a1cb_0               conda-forge
  certifi                           2025.11.12    pyhd8ed1ab_0             conda-forge
  cffi                              2.0.0         py312h460c074_1          conda-forge
  charset-normalizer                3.4.4         pyhd8ed1ab_0             conda-forge
  clarabel                          0.11.1        py312h6b5fed6_1          conda-forge
  click                             8.3.1         pyh8f84b5b_1             conda-forge
  colorama                          0.4.6         pyhd8ed1ab_1             conda-forge
  contourpy                         1.3.3         py312hd9148b4_3          conda-forge
  cvxpy                             1.7.5         py312h7900ff3_0          conda-forge
  cvxpy-base                        1.7.5         py312hf79963d_0          conda-forge
  cycler                            0.12.1        pyhcf101f3_2             conda-forge
  docutils                          0.21.2        pyhd8ed1ab_1             conda-forge
  epiweeks                          2.3.0         pyhdfd78af_0             bioconda   
  fonttools                         4.61.1        py312h8a5da7c_0          conda-forge
  freetype                          2.14.1        ha770c72_0               conda-forge
  freyja                            2.0.2         pyhdfd78af_0             bioconda   
  gawk                              5.3.1         hcd3d067_0               conda-forge
  gflags                            2.2.2         h5888daf_1005            conda-forge
  glog                              0.7.1         hbabe93e_0               conda-forge
  gmp                               6.3.0         hac33072_2               conda-forge
  h2                                4.3.0         pyhcf101f3_0             conda-forge
  hpack                             4.1.0         pyhd8ed1ab_0             conda-forge
  htslib                            1.22.1        h566b1c6_0               bioconda   
  hyperframe                        6.1.0         pyhd8ed1ab_0             conda-forge
  icu                               75.1          he02047a_0               conda-forge
  idna                              3.11          pyhd8ed1ab_0             conda-forge
  imagesize                         1.4.1         pyhd8ed1ab_0             conda-forge
  isa-l                             2.31.1        hb9d3cd8_1               conda-forge
  ivar                              1.4.4         h077b44d_0               bioconda   
  jinja2                            3.1.6         pyhcf101f3_1             conda-forge
  joblib                            1.5.3         pyhd8ed1ab_0             conda-forge
  keyutils                          1.6.3         hb9d3cd8_0               conda-forge
  kiwisolver                        1.4.9         py312h0a2e395_2          conda-forge
  krb5                              1.21.3        h659f571_0               conda-forge
  lcms2                             2.17          h717163a_0               conda-forge
  ld_impl_linux-64                  2.45          default_hbd61a6d_104     conda-forge
  lerc                              4.0.0         h0aef613_1               conda-forge
  libabseil                         20240116.2    cxx17_he02047a_1         conda-forge
  libarrow                          17.0.0        had3b6fe_16_cpu          conda-forge
  libarrow-acero                    17.0.0        h5888daf_16_cpu          conda-forge
  libarrow-dataset                  17.0.0        h5888daf_16_cpu          conda-forge
  libarrow-substrait                17.0.0        hf54134d_16_cpu          conda-forge
  libasprintf                       0.25.1        h3f43e3d_1               conda-forge
  libblas                           3.11.0        5_h4a7cf45_openblas      conda-forge
  libboost                          1.85.0        h0ccab89_4               conda-forge
  libboost-devel                    1.85.0        h00ab1b0_4               conda-forge
  libboost-headers                  1.85.0        ha770c72_4               conda-forge
  libbrotlicommon                   1.1.0         hb03c661_4               conda-forge
  libbrotlidec                      1.1.0         hb03c661_4               conda-forge
  libbrotlienc                      1.1.0         hb03c661_4               conda-forge
  libcblas                          3.11.0        5_h0358290_openblas      conda-forge
  libcrc32c                         1.1.2         h9c3ff4c_0               conda-forge
  libcurl                           8.17.0        h4e3cde8_1               conda-forge
  libdeflate                        1.25          h17f619e_0               conda-forge
  libedit                           3.1.20250104  pl5321h7949ede_0         conda-forge
  libev                             4.33          hd590300_2               conda-forge
  libevent                          2.1.12        hf998b51_1               conda-forge
  libexpat                          2.7.3         hecca717_0               conda-forge
  libffi                            3.5.2         h9ec8514_0               conda-forge
  libfreetype                       2.14.1        ha770c72_0               conda-forge
  libfreetype6                      2.14.1        h73754d4_0               conda-forge
  libgcc                            15.2.0        he0feb66_16              conda-forge
  libgcc-ng                         15.2.0        h69a702a_16              conda-forge
  libgettextpo                      0.25.1        h3f43e3d_1               conda-forge
  libgfortran                       15.2.0        h69a702a_16              conda-forge
  libgfortran-ng                    15.2.0        h69a702a_16              conda-forge
  libgfortran5                      15.2.0        h68bc16d_16              conda-forge
  libgomp                           15.2.0        he0feb66_16              conda-forge
  libgoogle-cloud                   2.29.0        h435de7b_0               conda-forge
  libgoogle-cloud-storage           2.29.0        h0121fbd_0               conda-forge
  libgrpc                           1.62.2        h15f2491_0               conda-forge
  libiconv                          1.18          h3b78370_2               conda-forge
  libjpeg-turbo                     3.1.2         hb03c661_0               conda-forge
  liblapack                         3.11.0        5_h47877c9_openblas      conda-forge
  liblzma                           5.8.1         hb9d3cd8_2               conda-forge
  liblzma-devel                     5.8.1         hb9d3cd8_2               conda-forge
  libnghttp2                        1.67.0        had1ee68_0               conda-forge
  libnsl                            2.0.1         hb9d3cd8_1               conda-forge
  libopenblas                       0.3.30        pthreads_h94d23a6_4      conda-forge
  libopenssl-static                 3.6.0         hb03c661_0               conda-forge
  libosqp                           1.0.0         np2py312h1a77e3e_2       conda-forge
  libparquet                        17.0.0        h39682fd_16_cpu          conda-forge
  libpng                            1.6.53        h421ea60_0               conda-forge
  libprotobuf                       4.25.3        hd5b35b9_1               conda-forge
  libqdldl                          0.1.8         h3f2d84a_1               conda-forge
  libre2-11                         2023.09.01    h5a48ba9_2               conda-forge
  libsqlite                         3.51.1        h0c1763c_0               conda-forge
  libssh2                           1.11.1        hcf80075_0               conda-forge
  libstdcxx                         15.2.0        h934c35e_16              conda-forge
  libstdcxx-ng                      15.2.0        hdf11a46_16              conda-forge
  libthrift                         0.20.0        h0e7cc3e_1               conda-forge
  libtiff                           4.7.1         h9d88235_1               conda-forge
  libutf8proc                       2.8.0         hf23e847_1               conda-forge
  libuuid                           2.41.2        h5347b49_1               conda-forge
  libwebp-base                      1.6.0         hd42ef1d_0               conda-forge
  libxcb                            1.17.0        h8a09558_0               conda-forge
  libxcrypt                         4.4.36        hd590300_1               conda-forge
  libxml2                           2.13.9        h04c0eec_0               conda-forge
  libzlib                           1.3.1         hb9d3cd8_2               conda-forge
  lz4-c                             1.9.4         hcb278e6_0               conda-forge
  mafft                             7.526         h4bc722e_0               conda-forge
  markupsafe                        3.0.3         py312h8a5da7c_0          conda-forge
  matplotlib-base                   3.10.8        py312he3d6523_0          conda-forge
  mpfr                              4.2.1         h90cbb55_3               conda-forge
  mpi                               1.0           openmpi                  conda-forge
  munkres                           1.1.4         pyhd8ed1ab_1             conda-forge
  mysql-connector-c                 6.1.11        h659d440_1008            conda-forge
  narwhals                          2.14.0        pyhcf101f3_0             conda-forge
  ncurses                           6.5           h2d0b736_3               conda-forge
  numpy                             2.3.5         py312h33ff503_0          conda-forge
  openjpeg                          2.5.4         h55fea9a_0               conda-forge
  openmpi                           4.1.6         hc5af2df_101             conda-forge
  openssl                           3.6.0         h26f9b46_0               conda-forge
  orc                               2.0.2         h669347b_0               conda-forge
  osqp                              1.0.5         np2py312h0f77346_4       conda-forge
  packaging                         25.0          pyh29332c3_1             conda-forge
  pandas                            2.3.3         py312hf79963d_1          conda-forge
  pillow                            12.0.0        py312h50c33e8_2          conda-forge
  pip                               25.3          pyh8b19718_0             conda-forge
  plotly                            6.5.0         pyhd8ed1ab_0             conda-forge
  protobuf                          4.25.3        py312h83439f5_1          conda-forge
  pthread-stubs                     0.4           hb9d3cd8_1002            conda-forge
  pyarrow                           17.0.0        py312h9cebb41_2          conda-forge
  pyarrow-core                      17.0.0        py312h01725c0_2_cpu      conda-forge
  pycparser                         2.22          pyh29332c3_1             conda-forge
  pygments                          2.19.2        pyhd8ed1ab_0             conda-forge
  pyparsing                         3.2.5         pyhcf101f3_0             conda-forge
  pysam                             0.23.3        py312h47d5410_1          bioconda   
  pysocks                           1.7.1         pyha55dd90_7             conda-forge
  python                            3.12.12       hd63d673_1_cpython       conda-forge
  python-dateutil                   2.9.0.post0   pyhe01879c_2             conda-forge
  python-tzdata                     2025.3        pyhd8ed1ab_0             conda-forge
  python_abi                        3.12          8_cp312                  conda-forge
  pytz                              2025.2        pyhd8ed1ab_0             conda-forge
  pyyaml                            6.0.3         py312h8a5da7c_0          conda-forge
  qdldl-python                      0.1.7.post5   np2py312h0f77346_3       conda-forge
  qhull                             2020.2        h434a139_5               conda-forge
  re2                               2023.09.01    h7f4b329_2               conda-forge
  readline                          8.3           h853b02a_0               conda-forge
  requests                          2.32.5        pyhd8ed1ab_0             conda-forge
  roman-numerals-py                 3.1.0         pyhd8ed1ab_0             conda-forge
  s2n                               1.5.5         h3931f03_0               conda-forge
  samtools                          1.22.1        h96c455f_0               bioconda   
  scipy                             1.16.3        py312h7a1785b_1          conda-forge
  scs                               3.2.9         default_py312he8c76e8_1  conda-forge
  seaborn-base                      0.13.2        pyhd8ed1ab_3             conda-forge
  setuptools                        80.9.0        pyhff2d567_0             conda-forge
  six                               1.17.0        pyhe01879c_1             conda-forge
  snappy                            1.2.2         h03e3b7b_1               conda-forge
  snowballstemmer                   3.0.1         pyhd8ed1ab_0             conda-forge
  sphinx                            8.2.3         pyhd8ed1ab_0             conda-forge
  sphinx-click                      6.2.0         pyhcf101f3_0             conda-forge
  sphinx_rtd_theme                  3.0.2         pyha770c72_0             conda-forge
  sphinxcontrib-applehelp           2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-devhelp             2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-htmlhelp            2.1.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jquery              4.1           pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jsmath              1.0.1         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-qthelp              2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-serializinghtml     1.1.10        pyhd8ed1ab_1             conda-forge
  tbb                               2020.2        h4bd325d_4               conda-forge
  tbb-devel                         2020.2        h4bd325d_4               conda-forge
  tk                                8.6.13        noxft_ha0e22de_103       conda-forge
  tqdm                              4.67.1        pyhd8ed1ab_1             conda-forge
  tzdata                            2025c         h8577fbf_0               conda-forge
  ucsc-fatovcf                      482           hdc0a859_1               bioconda   
  unicodedata2                      17.0.0        py312h4c3975b_1          conda-forge
  urllib3                           2.5.0         pyhd8ed1ab_0             conda-forge
  usher                             0.6.6         hdd55de9_4               bioconda   
  wheel                             0.45.1        pyhd8ed1ab_1             conda-forge
  xorg-libxau                       1.0.12        hb03c661_1               conda-forge
  xorg-libxdmcp                     1.1.5         hb03c661_1               conda-forge
  xz                                5.8.1         hbcc6ac9_2               conda-forge
  xz-gpl-tools                      5.8.1         hbcc6ac9_2               conda-forge
  xz-tools                          5.8.1         hb9d3cd8_2               conda-forge
  yaml                              0.2.5         h280c20c_3               conda-forge
  zlib                              1.3.1         hb9d3cd8_2               conda-forge
  zlib-ng                           2.3.2         h54a6638_0               conda-forge
  zstandard                         0.25.0        py312h5253ce2_1          conda-forge
  zstd                              1.5.7         hb78ec9c_6               conda-forge

```
</details>

## freyja barcodes

This docker image was built on **2025-12-16** and the command `freyja update` is run as part of the build to retrieve the most up-to-date database. The barcode version included in this docker image is **`12_16_2025-00-37`** as reported by `freyja demix --version --pathogen SARS-CoV-2`

This image is rebuilt every week on Dockerhub and Quay.io with the tag ${{ base FREYJA version }}-${{ pathogen }}-${{ FREYJA database version }}-${{ date the image was deployed }}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants 
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write privileges, such as a mounted volume.
