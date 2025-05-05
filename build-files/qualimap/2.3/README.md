# QualiMap container

Main tool: [qualimap](http://qualimap.conesalab.org/)
  
Code repository: https://bitbucket.org/kokonech/qualimap

Basic information on how to use this tool:
- executable: `qualimap`
- help: `--help`
- version: `--help`
- description: the quality control of alignment sequencing data with GUI or CLI

Additional information:

    Supported types of experiments:
    - Whole-genome sequencing
    - Whole-exome sequencing
    - RNA-seq (speical mode available)
    - ChIP-seq
 
Full documentation: http://qualimap.conesalab.org/doc_html/index.html

<details>
<summary>Additional tools installed via micromamba:</summary>

```
  Name                               Version       Build                 Channel
──────────────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex                      0.1           conda_forge           conda-forge
  _openmp_mutex                      4.5           2_gnu                 conda-forge
  _r-mutex                           1.0.1         anacondar_1           conda-forge
  alsa-lib                           1.2.14        hb9d3cd8_0            conda-forge
  argcomplete                        3.6.2         pyhd8ed1ab_0          conda-forge
  binutils_impl_linux-64             2.43          h4bf12b8_4            conda-forge
  bioconductor-biobase               2.66.0        r44h3df3fcb_0         bioconda
  bioconductor-biocgenerics          0.52.0        r44hdfd78af_3         bioconda
  bioconductor-biocio                1.16.0        r44hdfd78af_0         bioconda
  bioconductor-biocparallel          1.40.0        r44he5774e6_1         bioconda
  bioconductor-biostrings            2.74.0        r44h3df3fcb_1         bioconda
  bioconductor-bsgenome              1.74.0        r44hdfd78af_0         bioconda
  bioconductor-data-packages         20250401      hdfd78af_0            bioconda
  bioconductor-delayedarray          0.32.0        r44h3df3fcb_1         bioconda
  bioconductor-dnacopy               1.80.0        r44h4d5c4aa_1         bioconda
  bioconductor-edger                 4.4.0         r44h3df3fcb_0         bioconda
  bioconductor-genomeinfodb          1.42.0        r44hdfd78af_2         bioconda
  bioconductor-genomeinfodbdata      1.2.13        r44hdfd78af_0         bioconda
  bioconductor-genomicalignments     1.42.0        r44h3df3fcb_1         bioconda
  bioconductor-genomicranges         1.58.0        r44h3df3fcb_2         bioconda
  bioconductor-iranges               2.40.0        r44h3df3fcb_2         bioconda
  bioconductor-limma                 3.62.1        r44h15a9599_1         bioconda
  bioconductor-matrixgenerics        1.18.0        r44hdfd78af_0         bioconda
  bioconductor-noiseq                2.50.0        r44hdfd78af_0         bioconda
  bioconductor-repitools             1.52.0        r44he5774e6_0         bioconda
  bioconductor-rhtslib               3.2.0         r44h15a9599_2         bioconda
  bioconductor-rsamtools             2.22.0        r44h77050f0_1         bioconda
  bioconductor-rtracklayer           1.66.0        r44h15a9599_1         bioconda
  bioconductor-s4arrays              1.6.0         r44h3df3fcb_1         bioconda
  bioconductor-s4vectors             0.44.0        r44h3df3fcb_2         bioconda
  bioconductor-sparsearray           1.6.0         r44h3df3fcb_1         bioconda
  bioconductor-summarizedexperiment  1.36.0        r44hdfd78af_0         bioconda
  bioconductor-ucsc.utils            1.2.0         r44h9ee0642_1         bioconda
  bioconductor-xvector               0.46.0        r44h15a9599_2         bioconda
  bioconductor-zlibbioc              1.52.0        r44h3df3fcb_2         bioconda
  bwidget                            1.10.1        ha770c72_0            conda-forge
  bzip2                              1.0.8         h4bc722e_7            conda-forge
  c-ares                             1.34.5        hb9d3cd8_0            conda-forge
  ca-certificates                    2025.4.26     hbd8a1cb_0            conda-forge
  cairo                              1.18.4        h3394656_0            conda-forge
  curl                               8.13.0        h332b0f4_0            conda-forge
  font-ttf-dejavu-sans-mono          2.37          hab24e00_0            conda-forge
  font-ttf-inconsolata               3.000         h77eed37_0            conda-forge
  font-ttf-source-code-pro           2.038         h77eed37_0            conda-forge
  font-ttf-ubuntu                    0.83          h77eed37_3            conda-forge
  fontconfig                         2.15.0        h7e30c49_1            conda-forge
  fonts-conda-ecosystem              1             0                     conda-forge
  fonts-conda-forge                  1             0                     conda-forge
  freetype                           2.13.3        ha770c72_1            conda-forge
  fribidi                            1.0.10        h36c2ea0_0            conda-forge
  gcc_impl_linux-64                  14.2.0        hdb7739f_2            conda-forge
  gfortran_impl_linux-64             14.2.0        h0ee6e4a_2            conda-forge
  giflib                             5.2.2         hd590300_0            conda-forge
  graphite2                          1.3.13        h59595ed_1003         conda-forge
  gsl                                2.7           he838d99_0            conda-forge
  gxx_impl_linux-64                  14.2.0        h2ead766_2            conda-forge
  harfbuzz                           11.1.0        h3beb420_0            conda-forge
  icu                                75.1          he02047a_0            conda-forge
  jq                                 1.7.1         hd590300_0            conda-forge
  kernel-headers_linux-64            3.10.0        he073ed8_18           conda-forge
  keyutils                           1.6.1         h166bdaf_0            conda-forge
  krb5                               1.21.3        h659f571_0            conda-forge
  lcms2                              2.17          h717163a_0            conda-forge
  ld_impl_linux-64                   2.43          h712a8e2_4            conda-forge
  lerc                               4.0.0         h0aef613_1            conda-forge
  libblas                            3.9.0         31_h59b9bed_openblas  conda-forge
  libcblas                           3.9.0         31_he106b2a_openblas  conda-forge
  libcups                            2.3.3         h4637d8d_4            conda-forge
  libcurl                            8.13.0        h332b0f4_0            conda-forge
  libdeflate                         1.23          h86f0d12_0            conda-forge
  libedit                            3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                              4.33          hd590300_2            conda-forge
  libexpat                           2.7.0         h5888daf_0            conda-forge
  libffi                             3.4.6         h2dba641_1            conda-forge
  libfreetype                        2.13.3        ha770c72_1            conda-forge
  libfreetype6                       2.13.3        h48d6fc4_1            conda-forge
  libgcc                             14.2.0        h767d61c_2            conda-forge
  libgcc-devel_linux-64              14.2.0        h9c4974d_102          conda-forge
  libgcc-ng                          14.2.0        h69a702a_2            conda-forge
  libgfortran                        14.2.0        h69a702a_2            conda-forge
  libgfortran-ng                     14.2.0        h69a702a_2            conda-forge
  libgfortran5                       14.2.0        hf1ad2bd_2            conda-forge
  libglib                            2.84.1        h2ff4ddf_0            conda-forge
  libgomp                            14.2.0        h767d61c_2            conda-forge
  libiconv                           1.18          h4ce23a2_1            conda-forge
  libjpeg-turbo                      3.1.0         hb9d3cd8_0            conda-forge
  liblapack                          3.9.0         31_h7ac8fdf_openblas  conda-forge
  liblzma                            5.8.1         hb9d3cd8_0            conda-forge
  libmpdec                           4.0.0         h4bc722e_0            conda-forge
  libnghttp2                         1.64.0        h161d5f1_0            conda-forge
  libopenblas                        0.3.29        pthreads_h94d23a6_0   conda-forge
  libpng                             1.6.47        h943b412_0            conda-forge
  libsanitizer                       14.2.0        hed042b8_2            conda-forge
  libsqlite                          3.49.1        hee588c1_2            conda-forge
  libssh2                            1.11.1        hcf80075_0            conda-forge
  libstdcxx                          14.2.0        h8f9b012_2            conda-forge
  libstdcxx-devel_linux-64           14.2.0        h9c4974d_102          conda-forge
  libstdcxx-ng                       14.2.0        h4852527_2            conda-forge
  libtiff                            4.7.0         hd9ff511_4            conda-forge
  libuuid                            2.38.1        h0b41bf4_0            conda-forge
  libwebp-base                       1.5.0         h851e524_0            conda-forge
  libxcb                             1.17.0        h8a09558_0            conda-forge
  libxml2                            2.13.7        h4bc477f_1            conda-forge
  libzlib                            1.3.1         hb9d3cd8_2            conda-forge
  make                               4.4.1         hb9d3cd8_2            conda-forge
  ncurses                            6.5           h2d0b736_3            conda-forge
  oniguruma                          6.9.10        hb9d3cd8_0            conda-forge
  openjdk                            23.0.2        h53dfc1b_2            conda-forge
  openssl                            3.5.0         h7b32b05_0            conda-forge
  pango                              1.56.3        h9ac818e_1            conda-forge
  pcre2                              10.44         hc749103_2            conda-forge
  pip                                25.1          pyh145f28c_0          conda-forge
  pixman                             0.46.0        h29eaf8c_0            conda-forge
  pthread-stubs                      0.4           hb9d3cd8_1002         conda-forge
  python                             3.13.3        hf636f53_101_cp313    conda-forge
  python_abi                         3.13          7_cp313               conda-forge
  pyyaml                             6.0.2         py313h8060acc_2       conda-forge
  qualimap                           2.3           hdfd78af_0            bioconda
  r-abind                            1.4_5         r44hc72bb7e_1006      conda-forge
  r-askpass                          1.2.1         r44h2b5f3a1_0         conda-forge
  r-base                             4.4.3         h9c32bc2_0            conda-forge
  r-bh                               1.87.0_1      r44hc72bb7e_0         conda-forge
  r-bitops                           1.0_9         r44h2b5f3a1_0         conda-forge
  r-catools                          1.18.3        r44h93ab643_0         conda-forge
  r-cluster                          2.1.8.1       r44hb67ce94_0         conda-forge
  r-codetools                        0.2_20        r44hc72bb7e_1         conda-forge
  r-cpp11                            0.5.2         r44h785f33e_1         conda-forge
  r-crayon                           1.5.3         r44hc72bb7e_1         conda-forge
  r-curl                             6.2.2         r44h2700575_0         conda-forge
  r-formatr                          1.14          r44hc72bb7e_2         conda-forge
  r-futile.logger                    1.4.3         r44hc72bb7e_1006      conda-forge
  r-futile.options                   1.0.1         r44hc72bb7e_1005      conda-forge
  r-getopt                           1.20.4        r44ha770c72_1         conda-forge
  r-gplots                           3.2.0         r44hc72bb7e_0         conda-forge
  r-gsmoothr                         0.1.7         r44hdb488b9_1007      conda-forge
  r-gtools                           3.9.5         r44hb1dbf0f_1         conda-forge
  r-httr                             1.4.7         r44hc72bb7e_1         conda-forge
  r-jsonlite                         2.0.0         r44h2b5f3a1_0         conda-forge
  r-kernsmooth                       2.23_26       r44h8461fee_0         conda-forge
  r-lambda.r                         1.2.4         r44hc72bb7e_4         conda-forge
  r-lattice                          0.22_7        r44h2b5f3a1_0         conda-forge
  r-locfit                           1.5_9.12      r44h2b5f3a1_0         conda-forge
  r-mass                             7.3_64        r44h2b5f3a1_0         conda-forge
  r-matrix                           1.7_3         r44h2ae2be5_0         conda-forge
  r-matrixstats                      1.5.0         r44h2b5f3a1_0         conda-forge
  r-mime                             0.13          r44h2b5f3a1_0         conda-forge
  r-openssl                          2.3.2         r44he8289e2_0         conda-forge
  r-optparse                         1.7.5         r44hc72bb7e_1         conda-forge
  r-r6                               2.6.1         r44hc72bb7e_0         conda-forge
  r-rcurl                            1.98_1.16     r44he8228da_1         conda-forge
  r-restfulr                         0.0.15        r44h5ef9028_6         bioconda
  r-rjson                            0.2.23        r44h93ab643_0         conda-forge
  r-rsolnp                           1.16          r44ha770c72_1006      conda-forge
  r-snow                             0.4_4         r44hc72bb7e_3         conda-forge
  r-statmod                          1.5.0         r44ha36c22a_2         conda-forge
  r-sys                              3.4.3         r44h2b5f3a1_0         conda-forge
  r-truncnorm                        1.0_9         r44h2b5f3a1_4         conda-forge
  r-xml                              3.99_0.17     r44h5bae778_2         conda-forge
  r-yaml                             2.3.10        r44hdb488b9_0         conda-forge
  readline                           8.2           h8c095d6_2            conda-forge
  sed                                4.8           he412f7d_0            conda-forge
  setuptools                         79.0.1        pyhff2d567_0          conda-forge
  sysroot_linux-64                   2.17          h0157908_18           conda-forge
  tk                                 8.6.13        noxft_h4845f30_101    conda-forge
  tktable                            2.10          h8bc8fbc_6            conda-forge
  toml                               0.10.2        pyhd8ed1ab_1          conda-forge
  tomlkit                            0.13.2        pyha770c72_1          conda-forge
  tzdata                             2025b         h78e105d_0            conda-forge
  xmltodict                          0.14.2        pyhd8ed1ab_1          conda-forge
  xorg-libice                        1.1.2         hb9d3cd8_0            conda-forge
  xorg-libsm                         1.2.6         he73a12e_0            conda-forge
  xorg-libx11                        1.8.12        h4f16b4b_0            conda-forge
  xorg-libxau                        1.0.12        hb9d3cd8_0            conda-forge
  xorg-libxdmcp                      1.1.5         hb9d3cd8_0            conda-forge
  xorg-libxext                       1.3.6         hb9d3cd8_0            conda-forge
  xorg-libxfixes                     6.0.1         hb9d3cd8_0            conda-forge
  xorg-libxi                         1.8.2         hb9d3cd8_0            conda-forge
  xorg-libxrandr                     1.5.4         hb9d3cd8_0            conda-forge
  xorg-libxrender                    0.9.12        hb9d3cd8_0            conda-forge
  xorg-libxt                         1.3.1         hb9d3cd8_0            conda-forge
  xorg-libxtst                       1.2.5         hb9d3cd8_3            conda-forge
  yaml                               0.2.5         h7f98852_2            conda-forge
  yq                                 3.4.3         pyhd8ed1ab_1          conda-forge
  zstd                               1.5.7         hb8e6e7a_2            conda-forge
```
</details>


## Example Usage

Using GUI
```
docker run -v $(pwd):/data -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY staphb/qualimap:2.3 qualimap
```

Using CLI
```bash
# HTML report
qualimap bamqc -bam file.bam -outdir qualimap_results

# PDF report
qualimap bamqc -bam file.bam -outfile result.pdf

# RNAseq
qualimap rnaseq -bam kidney.bam -gtf human.64.gtf -outdir rnaseq_qc_results

# CountsQC
qualimap counts -d GlcN_countsqc_input.txt -c -s mouse -outdir glcn_mice_counts

# Clustering
qualimap clustering -sample clustering/hmeDIP.bam -control clustering/input.bam -regions annotations/transcripts.human.64.bed -outdir clustering_result

# Compute counts
qualimap comp-counts -bam kidney.bam -gtf ../annotations/human.64.gtf  -out kidney.counts
```

