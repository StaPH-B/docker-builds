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
  attr                              2.5.1         h166bdaf_1               conda-forge
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
  biopython                         1.85          py312h66e93f0_1          conda-forge
  boost-cpp                         1.85.0        h3c6214e_4               conda-forge
  brotli                            1.1.0         hb9d3cd8_3               conda-forge
  brotli-bin                        1.1.0         hb9d3cd8_3               conda-forge
  brotli-python                     1.1.0         py312h2ec8cdc_3          conda-forge
  bzip2                             1.0.8         h4bc722e_7               conda-forge
  c-ares                            1.34.5        hb9d3cd8_0               conda-forge
  ca-certificates                   2025.8.3      hbd8a1cb_0               conda-forge
  certifi                           2025.8.3      pyhd8ed1ab_0             conda-forge
  cffi                              1.17.1        py312h06ac9bb_0          conda-forge
  charset-normalizer                3.4.3         pyhd8ed1ab_0             conda-forge
  clarabel                          0.11.1        py312h407087e_0          conda-forge
  click                             8.2.1         pyh707e725_0             conda-forge
  colorama                          0.4.6         pyhd8ed1ab_1             conda-forge
  contourpy                         1.3.3         py312hd9148b4_1          conda-forge
  cvxpy                             1.7.2         py312h7900ff3_0          conda-forge
  cvxpy-base                        1.7.2         py312hf79963d_0          conda-forge
  cycler                            0.12.1        pyhd8ed1ab_1             conda-forge
  docutils                          0.21.2        pyhd8ed1ab_1             conda-forge
  epiweeks                          2.3.0         pyhdfd78af_0             bioconda   
  fonttools                         4.59.2        py312h8a5da7c_0          conda-forge
  freetype                          2.13.3        ha770c72_1               conda-forge
  freyja                            2.0.1         pyhdfd78af_0             bioconda   
  gawk                              5.3.1         hcd3d067_0               conda-forge
  gflags                            2.2.2         h5888daf_1005            conda-forge
  glog                              0.7.1         hbabe93e_0               conda-forge
  gmp                               6.3.0         hac33072_2               conda-forge
  h2                                4.3.0         pyhcf101f3_0             conda-forge
  hpack                             4.1.0         pyhd8ed1ab_0             conda-forge
  htslib                            1.22.1        h566b1c6_0               bioconda   
  hyperframe                        6.1.0         pyhd8ed1ab_0             conda-forge
  icu                               75.1          he02047a_0               conda-forge
  idna                              3.10          pyhd8ed1ab_1             conda-forge
  imagesize                         1.4.1         pyhd8ed1ab_0             conda-forge
  isa-l                             2.31.1        hb9d3cd8_1               conda-forge
  ivar                              1.4.4         h077b44d_0               bioconda   
  jinja2                            3.1.6         pyhd8ed1ab_0             conda-forge
  joblib                            1.5.2         pyhd8ed1ab_0             conda-forge
  keyutils                          1.6.3         hb9d3cd8_0               conda-forge
  kiwisolver                        1.4.9         py312h0a2e395_0          conda-forge
  krb5                              1.21.3        h659f571_0               conda-forge
  lcms2                             2.17          h717163a_0               conda-forge
  ld_impl_linux-64                  2.44          h1423503_1               conda-forge
  python-dateutil                   2.9.0.post0   pyhe01879c_2             conda-forge
  python-tzdata                     2025.2        pyhd8ed1ab_0             conda-forge
  python_abi                        3.12          8_cp312                  conda-forge
  pytz                              2025.2        pyhd8ed1ab_0             conda-forge
  pyyaml                            6.0.2         py312h178313f_2          conda-forge
  qdldl-python                      0.1.7.post5   np20py312h6792212_1      conda-forge
  qhull                             2020.2        h434a139_5               conda-forge
  re2                               2023.09.01    h7f4b329_2               conda-forge
  readline                          8.2           h8c095d6_2               conda-forge
  requests                          2.32.5        pyhd8ed1ab_0             conda-forge
  roman-numerals-py                 3.1.0         pyhd8ed1ab_0             conda-forge
  s2n                               1.5.5         h3931f03_0               conda-forge
  samtools                          1.22.1        h96c455f_0               bioconda   
  scipy                             1.16.1        py312h4ebe9ca_0          conda-forge
  scs                               3.2.7.post2   default_py312hfaafd5f_0  conda-forge
  seaborn-base                      0.13.2        pyhd8ed1ab_3             conda-forge
  setuptools                        80.9.0        pyhff2d567_0             conda-forge
  six                               1.17.0        pyhe01879c_1             conda-forge
  snappy                            1.2.2         h03e3b7b_0               conda-forge
  snowballstemmer                   3.0.1         pyhd8ed1ab_0             conda-forge
  sphinx                            8.3.0         pyhd8ed1ab_0             conda-forge
  sphinx-click                      6.0.0         pyhd8ed1ab_1             conda-forge
  sphinx_rtd_theme                  3.0.1         pyha770c72_0             conda-forge
  sphinxcontrib-applehelp           2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-devhelp             2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-htmlhelp            2.1.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jquery              4.1           pyhd8ed1ab_1             conda-forge
  sphinxcontrib-jsmath              1.0.1         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-qthelp              2.0.0         pyhd8ed1ab_1             conda-forge
  sphinxcontrib-serializinghtml     1.1.10        pyhd8ed1ab_1             conda-forge
  tbb                               2022.2.0      hb60516a_1               conda-forge
  tbb-devel                         2022.2.0      h74b38a2_1               conda-forge
  tk                                8.6.13        noxft_hd72426e_102       conda-forge
  tqdm                              4.67.1        pyhd8ed1ab_1             conda-forge
  tzdata                            2025b         h78e105d_0               conda-forge
  ucsc-fatovcf                      482           hdc0a859_1               bioconda   
  unicodedata2                      16.0.0        py312h66e93f0_0          conda-forge
  urllib3                           2.5.0         pyhd8ed1ab_0             conda-forge
  usher                             0.6.6         h719ac0c_2               bioconda   
  wheel                             0.45.1        pyhd8ed1ab_1             conda-forge
  xorg-libxau                       1.0.12        hb9d3cd8_0               conda-forge
  xorg-libxdmcp                     1.1.5         hb9d3cd8_0               conda-forge
  xz                                5.8.1         hbcc6ac9_2               conda-forge
  xz-gpl-tools                      5.8.1         hbcc6ac9_2               conda-forge
  xz-tools                          5.8.1         hb9d3cd8_2               conda-forge
  yaml                              0.2.5         h280c20c_3               conda-forge
  zlib                              1.3.1         hb9d3cd8_2               conda-forge
  zstandard                         0.23.0        py312h4c3975b_3          conda-forge
  zstd                              1.5.7         hb8e6e7a_2               conda-forge

```
</details>

## freyja barcodes

This docker image was built on **2025-07-22** and the command `freyja update` is run as part of the build to retrieve the most up-to-date database. The barcode version included in this docker image is **`08_28_2025-00-33`** as reported by `freyja demix --version`

This image is rebuilt every week on Dockerhub and Quay.io with the tag ${freyja version}-${freyja database version}-${data image was deployed}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants 
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write privileges, such as a mounted volume.
