# TBProfiler Container

Main tool: [TBProfiler](https://github.com/jodyphelan/TBProfiler)

The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database. It also predicts the number of reads supporting drug resistance variants as an insight into hetero-resistance.

## Database

This tool relies on a database to run. The version (AKA git commit hash) of the database that is included in the docker image is `00a0db4e`. This is from the GitHub repository https://github.com/jodyphelan/tbdb. This can be confirmed in the json file: `/opt/conda/share/tbprofiler/tbdb.variables.json`:

```bash
$ grep 'commit' /opt/conda/share/tbprofiler/tbdb.variables.json
{"db-schema-version": "2.0.0", "snpEff_db": "Mycobacterium_tuberculosis_h37rv", "drugs": ["rifampicin", "isoniazid", "ethambutol", "pyrazinamide", "moxifloxacin", "levofloxacin", "bedaquiline", "delamanid", "pretomanid", "linezolid", "streptomycin", "amikacin", "kanamycin", "capreomycin", "clofazimine", "ethionamide", "para-aminosalicylic_acid", "cycloserine"], "tb-profiler-version": ">=6.6.0,<7.0.0", "version": {"name": "tbdb", "repo": "https://github.com/jodyphelan/tbdb.git", "branch": "HEAD", "commit": "00a0db4e", "status": "clean", "author": "Jody Phelan", "date": "Sun Feb 16 11:09:04 2025 +0100", "db-schema-version": "2.0.0", "tb-profiler-version": ">=6.6.0,<7.0.0"}, "amplicon": false, "files": {"ref": "tbdb.fasta", "gff": "tbdb.gff", "bed": "tbdb.bed", "json_db": "tbdb.dr.json", "variables": "tbdb.variables.json", "spoligotype_spacers": "tbdb.spoligotype_spacers.txt", "spoligotype_annotations": "tbdb.spoligotype_list.csv", "bedmask": "tbdb.mask.bed", "rules": "tbdb.rules.yml", "barcode": "tbdb.barcode.bed"}}
```

Additionally you can run the command `tb-profiler list_db` to list the same information

```bash
$ tb-profiler list_db
tbdb    00a0db4e        Jody Phelan     Sun Feb 16 11:09:04 2025 +0100  /opt/conda/share/tbprofiler/tbdb
```

## Additional included tools/dependencies

Tb-profiler is installed with micromamba. These are the dependencies installed alongside tbprofiler:
```bash
  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex              0.1           conda_forge           conda-forge
  _openmp_mutex              4.5           2_gnu                 conda-forge
  alsa-lib                   1.2.13        hb9d3cd8_0            conda-forge
  annotated-types            0.7.0         pyhd8ed1ab_1          conda-forge
  babel                      2.17.0        pyhd8ed1ab_0          conda-forge
  bcftools                   1.21          h3a4d415_1            bioconda   
  bedtools                   2.31.1        h13024bc_3            bioconda   
  bitarray                   3.0.0         py312h66e93f0_0       conda-forge
  bitstring                  4.3.0         pyhd8ed1ab_0          conda-forge
  black                      24.10.0       py312h7900ff3_0       conda-forge
  boost-cpp                  1.78.0        h2c5509c_4            conda-forge
  brotli                     1.1.0         hb9d3cd8_2            conda-forge
  brotli-bin                 1.1.0         hb9d3cd8_2            conda-forge
  brotli-python              1.1.0         py312h2ec8cdc_2       conda-forge
  bwa                        0.7.18        h577a1d6_2            bioconda   
  bzip2                      1.0.8         h4bc722e_7            conda-forge
  c-ares                     1.34.4        hb9d3cd8_0            conda-forge
  ca-certificates            2025.1.31     hbcca054_0            conda-forge
  cachetools                 5.5.2         pyhd8ed1ab_0          conda-forge
  cairo                      1.18.0        hbb29018_2            conda-forge
  certifi                    2025.1.31     pyhd8ed1ab_0          conda-forge
  cffi                       1.17.1        py312h06ac9bb_0       conda-forge
  charset-normalizer         3.4.1         pyhd8ed1ab_0          conda-forge
  click                      8.1.8         pyh707e725_0          conda-forge
  colorama                   0.4.6         pyhd8ed1ab_1          conda-forge
  contourpy                  1.3.1         py312h68727a3_0       conda-forge
  cycler                     0.12.1        pyhd8ed1ab_1          conda-forge
  delly                      1.2.6         hdcf5f25_4            bioconda   
  deprecation                2.1.0         pyh9f0ad1d_0          conda-forge
  docxcompose                1.4.0         pyhd8ed1ab_1          conda-forge
  docxtpl                    0.19.0        pyhd8ed1ab_0          conda-forge
  dsk                        2.3.3         h5ca1c30_6            bioconda   
  filelock                   3.17.0        pyhd8ed1ab_0          conda-forge
  font-ttf-dejavu-sans-mono  2.37          hab24e00_0            conda-forge
  font-ttf-inconsolata       3.000         h77eed37_0            conda-forge
  font-ttf-source-code-pro   2.038         h77eed37_0            conda-forge
  font-ttf-ubuntu            0.83          h77eed37_3            conda-forge
  fontconfig                 2.15.0        h7e30c49_1            conda-forge
  fonts-conda-ecosystem      1             0                     conda-forge
  fonts-conda-forge          1             0                     conda-forge
  fonttools                  4.56.0        py312h178313f_0       conda-forge
  freebayes                  1.3.6         hb0f3ef8_7            bioconda   
  freetype                   2.12.1        h267a509_2            conda-forge
  gatk4                      4.6.1.0       py310hdfd78af_0       bioconda   
  gettext                    0.23.1        h5888daf_0            conda-forge
  gettext-tools              0.23.1        h5888daf_0            conda-forge
  giflib                     5.2.2         hd590300_0            conda-forge
  git                        2.48.1        pl5321h59d505e_0      conda-forge
  graphite2                  1.3.13        h59595ed_1003         conda-forge
  gsl                        2.7           he838d99_0            conda-forge
  h2                         4.2.0         pyhd8ed1ab_0          conda-forge
  harfbuzz                   9.0.0         hfac3d4d_0            conda-forge
  hpack                      4.1.0         pyhd8ed1ab_0          conda-forge
  htslib                     1.21          h566b1c6_1            bioconda   
  hyperframe                 6.1.0         pyhd8ed1ab_0          conda-forge
  icu                        73.2          h59595ed_0            conda-forge
  idna                       3.10          pyhd8ed1ab_1          conda-forge
  itol-config                0.1.0         pyhdfd78af_0          bioconda   
  jinja2                     3.1.5         pyhd8ed1ab_0          conda-forge
  joblib                     1.4.2         pyhd8ed1ab_1          conda-forge
  k8                         1.2           h6618dc6_3            bioconda   
  kernel-headers_linux-64    3.10.0        he073ed8_18           conda-forge
  keyutils                   1.6.1         h166bdaf_0            conda-forge
  kiwisolver                 1.4.8         py312h84d6215_0       conda-forge
  kmc                        3.2.4         haf24da9_3            bioconda   
  krb5                       1.21.3        h659f571_0            conda-forge
  lcms2                      2.17          h717163a_0            conda-forge
  ld_impl_linux-64           2.43          h712a8e2_4            conda-forge
  lerc                       4.0.0         h27087fc_0            conda-forge
  libasprintf                0.23.1        h8e693c7_0            conda-forge
  libasprintf-devel          0.23.1        h8e693c7_0            conda-forge
  libblas                    3.9.0         31_h59b9bed_openblas  conda-forge
  libbrotlicommon            1.1.0         hb9d3cd8_2            conda-forge
  libbrotlidec               1.1.0         hb9d3cd8_2            conda-forge
  libbrotlienc               1.1.0         hb9d3cd8_2            conda-forge
  libcblas                   3.9.0         31_he106b2a_openblas  conda-forge
  libcups                    2.3.3         h4637d8d_4            conda-forge
  libcurl                    8.12.1        h332b0f4_0            conda-forge
  libdeflate                 1.22          hb9d3cd8_0            conda-forge
  libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                      4.33          hd590300_2            conda-forge
  libexpat                   2.6.4         h5888daf_0            conda-forge
  libffi                     3.4.6         h2dba641_0            conda-forge
  libgcc                     14.2.0        h767d61c_2            conda-forge
  libgcc-ng                  14.2.0        h69a702a_2            conda-forge
  libgettextpo               0.23.1        h5888daf_0            conda-forge
  libgettextpo-devel         0.23.1        h5888daf_0            conda-forge
  libgfortran                14.2.0        h69a702a_2            conda-forge
  libgfortran5               14.2.0        hf1ad2bd_2            conda-forge
  libglib                    2.82.2        h2ff4ddf_1            conda-forge
  libgomp                    14.2.0        h767d61c_2            conda-forge
  libiconv                   1.18          h4ce23a2_1            conda-forge
  libidn2                    2.3.7         hd590300_0            conda-forge
  libjpeg-turbo              3.0.0         hd590300_1            conda-forge
  liblapack                  3.9.0         31_h7ac8fdf_openblas  conda-forge
  liblzma                    5.6.4         hb9d3cd8_0            conda-forge
  liblzma-devel              5.6.4         hb9d3cd8_0            conda-forge
  libnghttp2                 1.64.0        h161d5f1_0            conda-forge
  libnsl                     2.0.1         hd590300_0            conda-forge
  libopenblas                0.3.29        pthreads_h94d23a6_0   conda-forge
  libpng                     1.6.47        h943b412_0            conda-forge
  libsqlite                  3.49.1        hee588c1_1            conda-forge
  libssh2                    1.11.1        hf672d98_0            conda-forge
  libstdcxx                  14.2.0        h8f9b012_2            conda-forge
  libstdcxx-ng               14.2.0        h4852527_2            conda-forge
  libtiff                    4.7.0         hc4654cb_2            conda-forge
  libunistring               0.9.10        h7f98852_0            conda-forge
  libuuid                    2.38.1        h0b41bf4_0            conda-forge
  libwebp-base               1.5.0         h851e524_0            conda-forge
  libxcb                     1.17.0        h8a09558_0            conda-forge
  libxcrypt                  4.4.36        hd590300_1            conda-forge
  libxml2                    2.12.7        h4c95cb1_3            conda-forge
  libxslt                    1.1.39        h76b75d6_0            conda-forge
  libzlib                    1.3.1         hb9d3cd8_2            conda-forge
  lofreq                     2.1.5         py312ha5e83ca_15      bioconda   
  lxml                       5.3.0         py312he28fd5a_2       conda-forge
  markdown-it-py             3.0.0         pyhd8ed1ab_1          conda-forge
  markupsafe                 3.0.2         py312h178313f_1       conda-forge
  matplotlib-base            3.10.0        py312hd3ec401_0       conda-forge
  mdurl                      0.1.2         pyhd8ed1ab_1          conda-forge
  minimap2                   2.28          h577a1d6_4            bioconda   
  munkres                    1.1.4         pyh9f0ad1d_0          conda-forge
  mypy_extensions            1.0.0         pyha770c72_1          conda-forge
  ncurses                    6.5           h2d0b736_3            conda-forge
  numpy                      2.2.3         py312h72c5963_0       conda-forge
  openjdk                    17.0.13       he018374_0            conda-forge
  openjpeg                   2.5.3         h5fbd93e_0            conda-forge
  openssl                    3.4.1         h7b32b05_0            conda-forge
  packaging                  24.2          pyhd8ed1ab_2          conda-forge
  parallel                   20250222      ha770c72_0            conda-forge
  pathogen-profiler          4.8.0         pyh7e72e81_0          bioconda   
  pathspec                   0.12.1        pyhd8ed1ab_1          conda-forge
  pcre2                      10.44         hba22ea6_2            conda-forge
  perl                       5.32.1        7_hd590300_perl5      conda-forge
  pillow                     11.1.0        py312h80c1187_0       conda-forge
  pilon                      1.24          hdfd78af_0            bioconda   
  pip                        25.0.1        pyh8b19718_0          conda-forge
  pixman                     0.44.2        h29eaf8c_0            conda-forge
  platformdirs               4.3.6         pyhd8ed1ab_1          conda-forge
  pthread-stubs              0.4           hb9d3cd8_1002         conda-forge
  pycparser                  2.22          pyh29332c3_1          conda-forge
  pydantic                   2.10.6        pyh3cfb1c2_0          conda-forge
  pydantic-core              2.27.2        py312h12e396e_0       conda-forge
  pygments                   2.19.1        pyhd8ed1ab_0          conda-forge
  pyparsing                  3.2.1         pyhd8ed1ab_0          conda-forge
  pysam                      0.23.0        py312h47d5410_0       bioconda   
  pysocks                    1.7.1         pyha55dd90_7          conda-forge
  python                     3.12.9        h9e4cc4f_0_cpython    conda-forge
  python-dateutil            2.9.0.post0   pyhff2d567_1          conda-forge
  python-docx                1.1.2         pyhff2d567_1          conda-forge
  python_abi                 3.12          5_cp312               conda-forge
  pytz                       2025.1        pyhd8ed1ab_0          conda-forge
  pyyaml                     6.0.2         py312h178313f_2       conda-forge
  qhull                      2020.2        h434a139_5            conda-forge
  readline                   8.2           h8c095d6_2            conda-forge
  requests                   2.32.3        pyhd8ed1ab_1          conda-forge
  rich                       13.9.4        pyhd8ed1ab_1          conda-forge
  rich-argparse              1.7.0         pyhd8ed1ab_0          conda-forge
  samclip                    0.4.0         hdfd78af_1            bioconda   
  samtools                   1.21          h96c455f_1            bioconda   
  scipy                      1.15.2        py312ha707e6e_0       conda-forge
  screed                     1.1.3         pyhd8ed1ab_0          conda-forge
  seqkit                     2.9.0         h9ee0642_0            bioconda   
  setuptools                 75.8.0        pyhff2d567_0          conda-forge
  six                        1.17.0        pyhd8ed1ab_0          conda-forge
  snpeff                     5.2           hdfd78af_1            bioconda   
  sourmash                   4.8.14        hdfd78af_0            bioconda   
  sourmash-minimal           4.8.14        py312h3753b3a_1       conda-forge
  sysroot_linux-64           2.17          h0157908_18           conda-forge
  tabixpp                    1.1.2         hbefcdb2_4            bioconda   
  tb-profiler                6.6.2         pyhdfd78af_0          bioconda   
  tk                         8.6.13        noxft_h4845f30_101    conda-forge
  tomli                      2.2.1         pyhd8ed1ab_1          conda-forge
  tqdm                       4.67.1        pyhd8ed1ab_1          conda-forge
  trimmomatic                0.39          hdfd78af_2            bioconda   
  typing-extensions          4.12.2        hd8ed1ab_1            conda-forge
  typing_extensions          4.12.2        pyha770c72_1          conda-forge
  tzdata                     2025a         h78e105d_0            conda-forge
  unicodedata2               16.0.0        py312h66e93f0_0       conda-forge
  urllib3                    2.3.0         pyhd8ed1ab_0          conda-forge
  vcflib                     1.0.12        hbefcdb2_1            bioconda   
  wfa2-lib                   2.3.5         h9948957_3            bioconda   
  wget                       1.21.4        hda4d442_0            conda-forge
  wheel                      0.45.1        pyhd8ed1ab_1          conda-forge
  xorg-libice                1.1.2         hb9d3cd8_0            conda-forge
  xorg-libsm                 1.2.5         he73a12e_0            conda-forge
  xorg-libx11                1.8.11        h4f16b4b_0            conda-forge
  xorg-libxau                1.0.12        hb9d3cd8_0            conda-forge
  xorg-libxdmcp              1.1.5         hb9d3cd8_0            conda-forge
  xorg-libxext               1.3.6         hb9d3cd8_0            conda-forge
  xorg-libxfixes             6.0.1         hb9d3cd8_0            conda-forge
  xorg-libxi                 1.8.2         hb9d3cd8_0            conda-forge
  xorg-libxrandr             1.5.4         hb9d3cd8_0            conda-forge
  xorg-libxrender            0.9.12        hb9d3cd8_0            conda-forge
  xorg-libxt                 1.3.1         hb9d3cd8_0            conda-forge
  xorg-libxtst               1.2.5         hb9d3cd8_3            conda-forge
  xz                         5.6.4         hbcc6ac9_0            conda-forge
  xz-gpl-tools               5.6.4         hbcc6ac9_0            conda-forge
  xz-tools                   5.6.4         hb9d3cd8_0            conda-forge
  yaml                       0.2.5         h7f98852_2            conda-forge
  zlib                       1.3.1         hb9d3cd8_2            conda-forge
  zstandard                  0.23.0        py312hef9b889_1       conda-forge
  zstd                       1.5.6         ha6fb4c9_0            conda-forge
```

## Example Usage

Run whole pipeline on Illumina paired-end reads:

```bash
tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 4 -p ERR1664619 --txt
```

Make alternative database:

```bash
tb-profiler create_db --prefix <new_library_name>
tb-profiler load_library --prefix <new_library_name>
```

## Updates

Release 5.0.1 implemented sqlite3 database locking with https://py-filelock.readthedocs.io/en/latest/index.html. This should fix issues using it over network filing systems (NFS). For more information, official documentation can be found [here.](https://jodyphelan.gitbook.io/tb-profiler/)
