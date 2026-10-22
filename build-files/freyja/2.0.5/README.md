# freyja container

Main tool & documentation: [freyja](https://github.com/andersen-lab/Freyja)

Freyja is a tool to recover relative lineage abundances from mixed samples from a sequencing dataset . The method uses lineage-determining mutational "barcodes" derived from the UShER global phylogenetic tree as a basis set to solve the constrained (unit sum, non-negative) de-mixing problem.

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/freyja-env"

  Name                              Version       Build                    Channel    
────────────────────────────────────────────────────────────────────────────────────────
  _openmp_mutex                     4.5           20_gnu                   conda-forge
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
  babel                             2.18.0        pyhcf101f3_1             conda-forge
  biopython                         1.88          py311h0d48ccd_1          conda-forge
  boost-cpp                         1.85.0        h3c6214e_4               conda-forge
  brotli                            1.1.0         hb03c661_4               conda-forge
  brotli-bin                        1.1.0         hb03c661_4               conda-forge
  brotli-python                     1.1.0         py311h1ddb823_4          conda-forge
  bzip2                             1.0.8         hda65f42_10              conda-forge
  c-ares                            1.34.8        hebe6cf0_2               conda-forge
  ca-certificates                   2026.7.22     hbd8a1cb_0               conda-forge
  certifi                           2026.7.22     pyhd8ed1ab_0             conda-forge
  cffi                              2.1.1         py311h904a5e5_3          conda-forge
  charset-normalizer                3.5.1         pyhd8ed1ab_0             conda-forge
  clarabel                          0.11.1        py311hc8fb587_2          conda-forge
  click                             8.5.0         pyh5ded981_0             conda-forge
  cloudpickle                       3.1.2         pyhcf101f3_1             conda-forge
  colorama                          0.4.6         pyhd8ed1ab_1             conda-forge
  contourpy                         1.3.3         py311h724c32c_4          conda-forge
  cvxpy                             1.9.2         py311h735f00c_0          conda-forge
  cvxpy-base                        1.9.2         np2py311h912ec1f_0       conda-forge
  cycler                            0.12.1        pyhcf101f3_2             conda-forge
  docutils                          0.22.4        pyhd8ed1ab_0             conda-forge
  epiweeks                          2.4.0         pyhdfd78af_0             bioconda   
  fonttools                         4.66.0        py311h92159aa_0          conda-forge
  freetype                          2.14.3        ha770c72_2               conda-forge
  freyja                            2.0.5         pyhdfd78af_0             bioconda   
  gawk                              5.4.1         h0a3468a_0               conda-forge
  gflags                            2.2.2         h5888daf_1005            conda-forge
  glog                              0.7.1         hbabe93e_0               conda-forge
  gmp                               6.3.0         hfd2156b_3               conda-forge
  h2                                4.4.1         pyhcf101f3_0             conda-forge
  highspy                           1.15.1        np2py311h5a3f614_1       conda-forge
  hpack                             4.2.0         pyhd8ed1ab_0             conda-forge
  htslib                            1.24          ha79157c_0               bioconda   
  hyperframe                        6.1.0         pyhd8ed1ab_0             conda-forge
  icu                               75.1          he02047a_0               conda-forge
  idna                              3.20          pyh5ded981_0             conda-forge
  imagesize                         2.0.1         pyhd8ed1ab_0             conda-forge
  isa-l                             2.32.1        hb03c661_0               conda-forge
  ivar                              1.4.4         h077b44d_0               bioconda   
  jinja2                            3.1.6         pyhcf101f3_1             conda-forge
  joblib                            1.6.0         pyhcf101f3_0             conda-forge
  keyutils                          1.6.3         h7cc23a3_1               conda-forge
  kiwisolver                        1.5.1         py311h4c6fd42_3          conda-forge
  krb5                              1.22.2        hbc21106_2               conda-forge
  lcms2                             2.19.1        h9073bf1_3               conda-forge
  ld_impl_linux-64                  2.46.1        default_hbd61a6d_102     conda-forge
  lerc                              4.2.0         hdb68285_0               conda-forge
  libabseil                         20240116.2    cxx17_he02047a_1         conda-forge
  libarrow                          17.0.0        had3b6fe_16_cpu          conda-forge
  libarrow-acero                    17.0.0        h5888daf_16_cpu          conda-forge
  libarrow-dataset                  17.0.0        h5888daf_16_cpu          conda-forge
  libarrow-substrait                17.0.0        hf54134d_16_cpu          conda-forge
  libasprintf                       0.25.1        h0e23cf9_2               conda-forge
  libblas                           3.11.0        11_h4a7cf45_openblas     conda-forge
  libboost                          1.85.0        h0ccab89_4               conda-forge
  libboost-devel                    1.85.0        h00ab1b0_4               conda-forge
  libboost-headers                  1.85.0        ha770c72_4               conda-forge
  libbrotlicommon                   1.1.0         hb03c661_4               conda-forge
  libbrotlidec                      1.1.0         hb03c661_4               conda-forge
  libbrotlienc                      1.1.0         hb03c661_4               conda-forge
  libcblas                          3.11.0        11_h0358290_openblas     conda-forge
  libcrc32c                         1.1.2         h9c3ff4c_0               conda-forge
  libcurl                           8.21.0        hcf29cc6_1               conda-forge
  libdeflate                        1.25          hd45a770_1               conda-forge
  libedit                           3.1.20250104  pl5321h373387f_1         conda-forge
  libev                             4.33          h280c20c_3               conda-forge
  libevent                          2.1.12        h5348a74_2               conda-forge
  libexpat                          2.8.5         hd2095e1_0               conda-forge
  libffi                            3.7.0         h81df57d_1               conda-forge
  libfreetype                       2.14.3        ha770c72_2               conda-forge
  libfreetype6                      2.14.3        h5e6c136_2               conda-forge
  libgcc                            16.2.0        ha9f2e26_7               conda-forge
  libgcc-ng                         16.2.0        h69a702a_7               conda-forge
  libgettextpo                      0.25.1        h0e23cf9_2               conda-forge
  libgfortran                       16.2.0        h69a702a_7               conda-forge
  libgfortran-ng                    16.2.0        h69a702a_7               conda-forge
  libgfortran5                      16.2.0        h6b99dfc_7               conda-forge
  libgomp                           16.2.0        he0feb66_7               conda-forge
  libgoogle-cloud                   2.29.0        h435de7b_0               conda-forge
  libgoogle-cloud-storage           2.29.0        h0121fbd_0               conda-forge
  libgrpc                           1.62.2        h15f2491_0               conda-forge
  libiconv                          1.18          h0cb94f2_3               conda-forge
  libjpeg-turbo                     3.2.0         hb03c661_1               conda-forge
  liblapack                         3.11.0        11_h47877c9_openblas     conda-forge
  liblzma                           5.8.3         hb03c661_1               conda-forge
  liblzma-devel                     5.8.3         hb03c661_1               conda-forge
  libnghttp2                        1.68.1        h74cf4be_1               conda-forge
  libnsl                            2.0.1         hb9d3cd8_1               conda-forge
  libopenblas                       0.3.34        pthreads_hf13c14d_2      conda-forge
  libopenssl-static                 3.6.4         h7cc23a3_0               conda-forge
  libosqp                           1.0.0         np2py312h1a77e3e_2       conda-forge
  libparquet                        17.0.0        h39682fd_16_cpu          conda-forge
  libpng                            1.6.58        h922cc85_1               conda-forge
  libprotobuf                       4.25.3        hd5b35b9_1               conda-forge
  libpython                         3.11.16       h0c77377_2_cpython       conda-forge
  libqdldl                          0.1.8         h3f2d84a_1               conda-forge
  libre2-11                         2023.09.01    h5a48ba9_2               conda-forge
  libsqlite                         3.53.4        h0737f62_1               conda-forge
  libssh2                           1.11.1        h6154650_1               conda-forge
  libstdcxx                         16.2.0        h934c35e_7               conda-forge
  libstdcxx-ng                      16.2.0        hdf11a46_7               conda-forge
  libthrift                         0.20.0        h0e7cc3e_1               conda-forge
  libtiff                           4.7.2         hcc2c06a_1               conda-forge
  libutf8proc                       2.8.0         hf23e847_1               conda-forge
  libuuid                           2.42.4        hcfc3c73_0               conda-forge
  libwebp-base                      1.6.0         hd42ef1d_1               conda-forge
  libxcb                            1.17.0        hb83e432_2               conda-forge
  libxcrypt                         4.4.38        h280c20c_0               conda-forge
  libxml2                           2.13.9        h04c0eec_0               conda-forge
  libzlib                           1.3.2         h25fd6f3_3               conda-forge
  lz4-c                             1.9.4         hcb278e6_0               conda-forge
  mafft                             7.526         h4bc722e_0               conda-forge
  markupsafe                        3.0.3         py311h3778330_1          conda-forge
  matplotlib-base                   3.10.9        py311h0f3be63_0          conda-forge
  mpfr                              4.2.2         ha2cb11d_1               conda-forge
  mpi                               1.0           openmpi                  conda-forge
  munkres                           1.1.4         pyhd8ed1ab_1             conda-forge
  mysql-connector-c                 6.1.11        h659d440_1008            conda-forge
  narwhals                          2.26.0        pyh5ded981_0             conda-forge
  ncurses                           6.6           hdb14827_1               conda-forge
  numpy                             2.4.6         py311h2e04523_0          conda-forge
  openjpeg                          2.5.4         heb1ab33_2               conda-forge
  openmpi                           4.1.6         hc5af2df_101             conda-forge
  openssl                           3.6.4         h781a0a9_0               conda-forge
  orc                               2.0.2         h669347b_0               conda-forge
  osqp                              1.1.3         np2py311h5a3f614_2       conda-forge
  packaging                         26.3          pyhc364b38_0             conda-forge
  pandas                            2.3.3         py311hed34c8f_2          conda-forge
  pillow                            12.3.0        py311hf303fd3_4          conda-forge
  pip                               26.2.1        pyh8b19718_0             conda-forge
  plotly                            7.1.0         pyhd8ed1ab_0             conda-forge
  protobuf                          4.25.3        py311hbffca5d_1          conda-forge
  pthread-stubs                     0.4           h7cc23a3_1004            conda-forge
  pyarrow                           17.0.0        py311hbd00459_2          conda-forge
  pyarrow-core                      17.0.0        py311h4854187_2_cpu      conda-forge
  pycparser                         3.0           pyhcf101f3_0             conda-forge
  pygments                          2.21.0        pyhcf101f3_0             conda-forge
  pyparsing                         3.3.3         pyh5ded981_0             conda-forge
  pysam                             0.24.0        py311h5f69268_1          bioconda   
  pysocks                           1.7.1         pyha55dd90_7             conda-forge
  python                            3.11.16       h5f976f7_2_cpython       conda-forge
  python-dateutil                   2.9.0.post0   pyhe01879c_2             conda-forge
  python-tzdata                     2026.4        pyh5ded981_0             conda-forge
  python_abi                        3.11          9_cp311                  conda-forge
  pytz                              2026.4        pyh5ded981_0             conda-forge
  pyyaml                            6.0.3         py311h3778330_1          conda-forge
  qdldl-python                      0.1.9.post1   np2py311h5a3f614_2       conda-forge
  qhull                             2020.2        h434a139_5               conda-forge
  re2                               2023.09.01    h7f4b329_2               conda-forge
  readline                          8.3           hd6e31c0_1               conda-forge
  requests                          2.34.2        pyhcf101f3_0             conda-forge
  roman-numerals                    4.1.0         pyhd8ed1ab_0             conda-forge
  s2n                               1.5.5         h3931f03_0               conda-forge
  samtools                          1.24          h9dcdb79_1               bioconda   
  scipy                             1.17.1        py311hbe70eeb_1          conda-forge
  scs                               3.3.1         default_py311h19b9619_2  conda-forge
  seaborn-base                      0.13.2        pyhd8ed1ab_3             conda-forge
  setuptools                        84.0.0        pyh332efcf_0             conda-forge
  six                               1.17.0        pyhe01879c_1             conda-forge
  snappy                            1.2.2         h34e00bb_2               conda-forge
  snowballstemmer                   3.1.1         pyhd8ed1ab_0             conda-forge
  sphinx                            9.0.4         pyhd8ed1ab_0             conda-forge
  sphinx-click                      6.2.0         pyhcf101f3_0             conda-forge
  sphinx_rtd_theme                  3.1.0         pyhcf101f3_2             conda-forge
  sphinxcontrib-applehelp           2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-devhelp             2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-htmlhelp            2.1.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jquery              4.1           pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jsmath              1.0.1         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-qthelp              2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-serializinghtml     2.0.0         pyhd8ed1ab_0             conda-forge
  tbb                               2020.2        h4bd325d_4               conda-forge
  tbb-devel                         2020.2        h4bd325d_4               conda-forge
  tk                                8.6.13        noxft_h1df4ec4_4         conda-forge
  tqdm                              4.70.1        pyhfa0c392_0             conda-forge
  tzdata                            2026c         h151e31d_0               conda-forge
  ucsc-fatovcf                      482           hdc0a859_1               bioconda   
  unicodedata2                      18.0.0        py311h0d48ccd_0          conda-forge
  urllib3                           2.5.0         pyhd8ed1ab_0             conda-forge
  usher                             0.6.6         hdd55de9_4               bioconda   
  wheel                             0.48.0        pyhd8ed1ab_0             conda-forge
  xorg-libxau                       1.0.12        h7cc23a3_2               conda-forge
  xorg-libxdmcp                     1.1.5         h7cc23a3_2               conda-forge
  xz                                5.8.3         ha02ee65_1               conda-forge
  xz-gpl-tools                      5.8.3         ha02ee65_1               conda-forge
  xz-tools                          5.8.3         hb03c661_1               conda-forge
  yaml                              0.2.5         hebe6cf0_3               conda-forge
  zlib                              1.3.2         h25fd6f3_3               conda-forge
  zlib-ng                           2.3.3         hce19668_1               conda-forge
  zstandard                         0.25.0        py311h194be0f_4          conda-forge
  zstd                              1.5.7         hb78ec9c_7               conda-forge
```
</details>

## freyja barcodes

This docker image was built on **2026-02-04** and the command `freyja update` is run as part of the build to retrieve the most up-to-date database. The barcode version included in this docker image is **`02_04_2026-00-43`** as reported by `freyja demix --version --pathogen SARS-CoV-2`

This image is rebuilt every week on Dockerhub and Quay.io with the tag ${{ base FREYJA version }}-${{ pathogen }}-${{ FREYJA database version }}-${{ date the image was deployed }}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write privileges, such as a mounted volume.
