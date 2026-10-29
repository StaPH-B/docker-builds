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
   _python_abi3_support              1.0           hd8ed1ab_3               conda-forge
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
   c-ares                            1.34.9        hebe6cf0_0               conda-forge
   ca-certificates                   2026.10.19    hbd8a1cb_0               conda-forge
   certifi                           2026.10.23    pyhd8ed1ab_0             conda-forge
   cffi                              2.1.1         py311h904a5e5_3          conda-forge
   charset-normalizer                3.5.2         h1114479_0               conda-forge
   clarabel                          0.11.1        py311hc8fb587_2          conda-forge
   click                             8.5.0         pyh5ded981_0             conda-forge
   cloudpickle                       3.1.2         pyhcf101f3_1             conda-forge
   colorama                          0.4.6         pyhd8ed1ab_1             conda-forge
   contourpy                         1.3.3         py311h724c32c_4          conda-forge
   cpython                           3.11.17       py311hd8ed1ab_2          conda-forge
   cvxpy                             1.9.3         py311hda200f6_1          conda-forge
   cvxpy-base                        1.9.3         np2py311h5a3f614_1       conda-forge
   cycler                            0.12.1        pyhcf101f3_2             conda-forge
   docutils                          0.22.4        pyhd8ed1ab_0             conda-forge
   epiweeks                          2.4.0         pyhdfd78af_0             bioconda   
   fonttools                         4.67.0        py311h92159aa_1          conda-forge
   freetype                          2.14.3        ha770c72_2               conda-forge
   freyja                            2.0.7         pyhdfd78af_0             bioconda   
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
   python                            3.11.17       h5f976f7_1_cpython       conda-forge
   python-dateutil                   3.0.0         pyh5ded981_0             conda-forge
   python-gil                        3.11.17       hd8ed1ab_2               conda-forge
   python-tzdata                     2026.5        pyh5ded981_0             conda-forge
   python_abi                        3.11          9_cp311                  conda-forge
   pytz                              2026.5        pyh5ded981_0             conda-forge
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
   setuptools                        84.2.1        pyhe730653_0             conda-forge
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
   sphinxcontrib-jsmath              2.0.0         pyh5ded981_0             conda-forge
   sphinxcontrib-qthelp              2.0.0         pyhd8ed1ab_1             conda-forge
   sphinxcontrib-serializinghtml     2.0.0         pyhd8ed1ab_0             conda-forge
   tbb                               2020.2        h4bd325d_4               conda-forge
   tbb-devel                         2020.2        h4bd325d_4               conda-forge
   tk                                8.6.13        noxft_h1df4ec4_4         conda-forge
   tqdm                              4.70.1        pyhfa0c392_0             conda-forge
   tzdata                            2026e         h5d301ff_0               conda-forge
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
