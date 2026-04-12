# TBProfiler Container

Main tool: [TBProfiler](https://github.com/jodyphelan/TBProfiler)

The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database. It also predicts the number of reads supporting drug resistance variants as an insight into hetero-resistance.

## Database

This tool relies on a database to run. The version (AKA git commit hash) of the database that is included in the docker image is `13b6ed45`. This is from the GitHub repository https://github.com/jodyphelan/tbdb. This can be confirmed in the json file: `/opt/conda/share/tbprofiler/tbdb/variables.json`:

```bash
$ cat /opt/conda/share/tbprofiler/tbdb.variables.json
{
    "db-schema-version": "2.0.0",
    "snpEff_db": "Mycobacterium_tuberculosis_h37rv",
    "drugs": [
        "rifampicin",
        "isoniazid",
        "ethambutol",
        "pyrazinamide",
        "moxifloxacin",
        "levofloxacin",
        "bedaquiline",
        "delamanid",
        "pretomanid",
        "linezolid",
        "streptomycin",
        "amikacin",
        "kanamycin",
        "capreomycin",
        "clofazimine",
        "ethionamide",
        "para-aminosalicylic_acid",
        "cycloserine"
    ],
    "tb-profiler-version": ">=6.6.0,<7.0.0",
    "type": "reference",
    "version": {
        "name": "tbdb",
        "repo": "https://github.com/jodyphelan/tbdb.git",
        "branch": "HEAD",
        "commit": "13b6ed45",
        "status": "clean",
        "author": "jodyphelan",
        "date": "Tue Aug 5 10:37:18 2025 +0100",
        "db-schema-version": "2.0.0",
        "tb-profiler-version": ">=6.6.0,<7.0.0"
    },
    "amplicon": false,
    "files": {
        "snpEff_config": "snpeff/snpEff.config",
        "ref": "genome.fasta",
        "gff": "genome.gff",
        "bed": "genes.bed",
        "json_db": "mutations.json",
        "variables": "variables.json",
        "spoligotype_spacers": "spoligotype_spacers.txt",
        "spoligotype_annotations": "spoligotype_list.csv",
        "bedmask": "mask.bed",
        "rules": "rules.yml",
        "barcode": "barcode.bed"
    }
}
```

Additionally you can run the command `tb-profiler list_db` to list the same information

```bash
$ tb-profiler list_db
tbdb    13b6ed45        jodyphelan      Tue Aug 5 10:37:18 2025 +0100   /opt/conda/share/tbprofiler/tbdb
```

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
  _openmp_mutex              4.5           20_gnu                conda-forge
  alsa-lib                   1.2.15.3      hb03c661_0            conda-forge
  annotated-types            0.7.0         pyhd8ed1ab_1          conda-forge
  backports.zstd             1.3.0         py310h69bd2ac_0       conda-forge
  bcftools                   1.23.1        hb2cee57_0            bioconda   
  bedtools                   2.31.1        h13024bc_3            bioconda   
  bitarray                   3.8.0         py310h7c4b9e2_1       conda-forge
  bitstring                  4.4.0         pyhd8ed1ab_0          conda-forge
  boost-cpp                  1.85.0        h3c6214e_4            conda-forge
  brotli                     1.2.0         hed03a55_1            conda-forge
  brotli-bin                 1.2.0         hb03c661_1            conda-forge
  brotli-python              1.2.0         py310hba01987_1       conda-forge
  bwa                        0.7.19        h577a1d6_1            bioconda   
  bzip2                      1.0.8         hda65f42_9            conda-forge
  c-ares                     1.34.6        hb03c661_0            conda-forge
  ca-certificates            2026.2.25     hbd8a1cb_0            conda-forge
  cachetools                 5.5.2         pyhd8ed1ab_0          conda-forge
  cairo                      1.18.4        h3394656_0            conda-forge
  certifi                    2026.2.25     pyhd8ed1ab_0          conda-forge
  cffi                       2.0.0         py310he7384ee_1       conda-forge
  charset-normalizer         3.4.7         pyhd8ed1ab_0          conda-forge
  contourpy                  1.3.2         py310h3788b33_0       conda-forge
  cycler                     0.12.1        pyhcf101f3_2          conda-forge
  delly                      1.3.3         h4d20210_1            bioconda   
  deprecation                2.1.0         pyh9f0ad1d_0          conda-forge
  docxtpl                    0.11.5        pyhd8ed1ab_0          conda-forge
  dsk                        2.3.3         h5ca1c30_7            bioconda   
  fastahack                  2016.07.2     h4ac6f70_6            bioconda   
  filelock                   3.25.2        pyhd8ed1ab_0          conda-forge
  font-ttf-dejavu-sans-mono  2.37          hab24e00_0            conda-forge
  font-ttf-inconsolata       3.000         h77eed37_0            conda-forge
  font-ttf-source-code-pro   2.038         h77eed37_0            conda-forge
  font-ttf-ubuntu            0.83          h77eed37_3            conda-forge
  fontconfig                 2.17.1        h27c8c51_0            conda-forge
  fonts-conda-ecosystem      1             0                     conda-forge
  fonts-conda-forge          1             hc364b38_1            conda-forge
  fonttools                  4.62.0        py310h3406613_0       conda-forge
  freebayes                  1.3.10        hbefcdb2_0            bioconda   
  freetype                   2.14.3        ha770c72_0            conda-forge
  gatk4                      4.6.2.0       py310hdfd78af_1       bioconda   
  giflib                     5.2.2         hd590300_0            conda-forge
  git                        2.53.0        pl5321h6d3cee1_0      conda-forge
  graphite2                  1.3.14        hecca717_2            conda-forge
  gsl                        2.7           he838d99_0            conda-forge
  h2                         4.3.0         pyhcf101f3_0          conda-forge
  harfbuzz                   12.2.0        h15599e2_0            conda-forge
  hpack                      4.1.0         pyhd8ed1ab_0          conda-forge
  htslib                     1.23          h566b1c6_0            bioconda   
  hyperframe                 6.1.0         pyhd8ed1ab_0          conda-forge
  icu                        75.1          he02047a_0            conda-forge
  idna                       3.11          pyhd8ed1ab_0          conda-forge
  itol-config                0.1.0         pyhdfd78af_0          bioconda   
  jinja2                     3.1.6         pyhcf101f3_1          conda-forge
  joblib                     1.5.3         pyhd8ed1ab_0          conda-forge
  k8                         1.2           he8db53b_6            bioconda   
  kernel-headers_linux-64    6.12.0        he073ed8_6            conda-forge
  keyutils                   1.6.3         hb9d3cd8_0            conda-forge
  kiwisolver                 1.5.0         py310haaf941d_0       conda-forge
  kmc                        3.2.4         h5ca1c30_4            bioconda   
  krb5                       1.22.2        ha1258a1_0            conda-forge
  lcms2                      2.17          h717163a_0            conda-forge
  ld_impl_linux-64           2.45.1        default_hbd61a6d_102  conda-forge
  lerc                       4.1.0         hdb68285_0            conda-forge
  libblas                    3.11.0        6_h4a7cf45_openblas   conda-forge
  libboost                   1.85.0        h0ccab89_4            conda-forge
  libboost-devel             1.85.0        h00ab1b0_4            conda-forge
  libboost-headers           1.85.0        ha770c72_4            conda-forge
  libbrotlicommon            1.2.0         hb03c661_1            conda-forge
  libbrotlidec               1.2.0         hb03c661_1            conda-forge
  libbrotlienc               1.2.0         hb03c661_1            conda-forge
  libcblas                   3.11.0        6_h0358290_openblas   conda-forge
  libcups                    2.3.3         h7a8fb5f_6            conda-forge
  libcurl                    8.19.0        hcf29cc6_0            conda-forge
  libdeflate                 1.22          hb9d3cd8_0            conda-forge
  libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                      4.33          hd590300_2            conda-forge
  libexpat                   2.7.5         hecca717_0            conda-forge
  libffi                     3.5.2         h3435931_0            conda-forge
  libfreetype                2.14.3        ha770c72_0            conda-forge
  libfreetype6               2.14.3        h73754d4_0            conda-forge
  libgcc                     15.2.0        he0feb66_18           conda-forge
  libgcc-ng                  15.2.0        h69a702a_18           conda-forge
  libgfortran                15.2.0        h69a702a_18           conda-forge
  libgfortran5               15.2.0        h68bc16d_18           conda-forge
  libglib                    2.86.4        h6548e54_1            conda-forge
  libgomp                    15.2.0        he0feb66_18           conda-forge
  libiconv                   1.18          h3b78370_2            conda-forge
  libidn2                    2.3.8         hfac485b_1            conda-forge
  libjpeg-turbo              3.1.4.1       hb03c661_0            conda-forge
  liblapack                  3.11.0        6_h47877c9_openblas   conda-forge
  liblzma                    5.8.3         hb03c661_0            conda-forge
  liblzma-devel              5.8.3         hb03c661_0            conda-forge
  libnghttp2                 1.68.1        h877daf1_0            conda-forge
  libnsl                     2.0.1         hb9d3cd8_1            conda-forge
  libopenblas                0.3.32        pthreads_h94d23a6_0   conda-forge
  libpng                     1.6.57        h421ea60_0            conda-forge
  libsqlite                  3.53.0        h0c1763c_0            conda-forge
  libssh2                    1.11.1        hcf80075_0            conda-forge
  libstdcxx                  15.2.0        h934c35e_18           conda-forge
  libstdcxx-ng               15.2.0        hdf11a46_18           conda-forge
  libtiff                    4.7.0         hc4654cb_2            conda-forge
  libunistring               0.9.10        h7f98852_0            conda-forge
  libuuid                    2.42          h5347b49_0            conda-forge
  libwebp-base               1.6.0         hd42ef1d_0            conda-forge
  libxcb                     1.17.0        h8a09558_0            conda-forge
  libxcrypt                  4.4.36        hd590300_1            conda-forge
  libxml2                    2.15.1        h26afc86_0            conda-forge
  libxml2-16                 2.15.1        ha9997c6_0            conda-forge
  libxslt                    1.1.43        h711ed8c_1            conda-forge
  libzlib                    1.3.2         h25fd6f3_2            conda-forge
  lofreq                     2.1.5         py310h4966b78_15      bioconda   
  lxml                       6.0.3         py310he6d4be0_0       conda-forge
  markdown-it-py             4.0.0         pyhd8ed1ab_0          conda-forge
  markupsafe                 3.0.3         py310h3406613_1       conda-forge
  matplotlib-base            3.10.8        py310hfde16b3_0       conda-forge
  mdurl                      0.1.2         pyhd8ed1ab_1          conda-forge
  minimap2                   2.30          h577a1d6_0            bioconda   
  munkres                    1.1.4         pyhd8ed1ab_1          conda-forge
  ncurses                    6.5           h2d0b736_3            conda-forge
  numpy                      2.2.6         py310hefbff90_0       conda-forge
  openjdk                    25.0.1        h5755bd7_0            conda-forge
  openjpeg                   2.5.3         h55fea9a_1            conda-forge
  openssl                    3.6.2         h35e630c_0            conda-forge
  packaging                  26.0          pyhcf101f3_0          conda-forge
  pandas                     2.3.3         py310h0158d43_2       conda-forge
  parallel                   20260122      ha770c72_0            conda-forge
  pathogen-profiler          5.2.1         pyhdfd78af_0          bioconda   
  pcre2                      10.47         haa7fec5_0            conda-forge
  perl                       5.32.1        7_hd590300_perl5      conda-forge
  pillow                     11.3.0        py310h6557065_3       conda-forge
  pilon                      1.24          hdfd78af_0            bioconda   
  pip                        26.0.1        pyh8b19718_0          conda-forge
  pixman                     0.46.4        h54a6638_1            conda-forge
  pthread-stubs              0.4           hb9d3cd8_1002         conda-forge
  pycparser                  2.22          pyh29332c3_1          conda-forge
  pydantic                   2.12.5        pyhcf101f3_1          conda-forge
  pydantic-core              2.41.5        py310hd8f68c5_1       conda-forge
  pygments                   2.20.0        pyhd8ed1ab_0          conda-forge
  pyparsing                  3.3.2         pyhcf101f3_0          conda-forge
  pysam                      0.23.3        py310h64e62c9_1       bioconda   
  pysocks                    1.7.1         pyha55dd90_7          conda-forge
  python                     3.10.20       h3c07f61_0_cpython    conda-forge
  python-dateutil            2.9.0.post0   pyhe01879c_2          conda-forge
  python-docx                1.2.0         pyhff2d567_0          conda-forge
  python-tzdata              2026.1        pyhd8ed1ab_0          conda-forge
  python_abi                 3.10          8_cp310               conda-forge
  pytz                       2026.1.post1  pyhcf101f3_0          conda-forge
  pyyaml                     6.0.3         py310h3406613_1       conda-forge
  qhull                      2020.2        h434a139_5            conda-forge
  readline                   8.3           h853b02a_0            conda-forge
  requests                   2.33.1        pyhcf101f3_0          conda-forge
  rich                       15.0.0        pyhcf101f3_0          conda-forge
  rich-argparse              1.7.2         pyhd8ed1ab_0          conda-forge
  samclip                    0.4.0         hdfd78af_1            bioconda   
  samtools                   1.23          h96c455f_0            bioconda   
  scipy                      1.15.2        py310h1d65ade_0       conda-forge
  screed                     1.1.3         pyhd8ed1ab_0          conda-forge
  seqkit                     2.13.0        he881be0_0            bioconda   
  seqlib                     1.2.0         hbefcdb2_0            bioconda   
  setuptools                 82.0.1        pyh332efcf_0          conda-forge
  six                        1.17.0        pyhe01879c_1          conda-forge
  snpeff                     5.2           hdfd78af_3            bioconda   
  sourmash                   4.8.14        hdfd78af_0            bioconda   
  sourmash-minimal           4.8.14        py310h3f40857_1       conda-forge
  sylph                      0.9.0         ha6fb395_0            bioconda   
  sysroot_linux-64           2.39          hc4b9eeb_6            conda-forge
  tabixpp                    1.1.2         hbefcdb2_4            bioconda   
  tb-profiler                6.7.0         pyhdfd78af_0          bioconda   
  tibs                       0.5.7         py310h72bf493_1       conda-forge
  tk                         8.6.13        noxft_h366c992_103    conda-forge
  tomli                      2.4.1         pyhcf101f3_0          conda-forge
  tqdm                       4.67.3        pyh8f84b5b_0          conda-forge
  trimmomatic                0.40          hdfd78af_0            bioconda   
  typing-extensions          4.15.0        h396c80c_0            conda-forge
  typing-inspection          0.4.2         pyhd8ed1ab_1          conda-forge
  typing_extensions          4.15.0        pyhcf101f3_0          conda-forge
  tzdata                     2025c         hc9c84f9_1            conda-forge
  unicodedata2               17.0.1        py310h7c4b9e2_0       conda-forge
  urllib3                    2.6.3         pyhd8ed1ab_0          conda-forge
  vcflib                     1.0.14        h34261f4_0            bioconda   
  wget                       1.25.0        h653f8fd_1            conda-forge
  wheel                      0.46.3        pyhd8ed1ab_0          conda-forge
  xorg-libice                1.1.2         hb9d3cd8_0            conda-forge
  xorg-libsm                 1.2.6         he73a12e_0            conda-forge
  xorg-libx11                1.8.13        he1eb515_0            conda-forge
  xorg-libxau                1.0.12        hb03c661_1            conda-forge
  xorg-libxdmcp              1.1.5         hb03c661_1            conda-forge
  xorg-libxext               1.3.7         hb03c661_0            conda-forge
  xorg-libxfixes             6.0.2         hb03c661_0            conda-forge
  xorg-libxi                 1.8.2         hb9d3cd8_0            conda-forge
  xorg-libxrandr             1.5.5         hb03c661_0            conda-forge
  xorg-libxrender            0.9.12        hb9d3cd8_0            conda-forge
  xorg-libxt                 1.3.1         hb9d3cd8_0            conda-forge
  xorg-libxtst               1.2.5         hb9d3cd8_3            conda-forge
  xz                         5.8.3         ha02ee65_0            conda-forge
  xz-gpl-tools               5.8.3         ha02ee65_0            conda-forge
  xz-tools                   5.8.3         hb03c661_0            conda-forge
  yaml                       0.2.5         h280c20c_3            conda-forge
  zlib                       1.3.2         h25fd6f3_2            conda-forge
  zstd                       1.5.7         hb78ec9c_6            conda-forge
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
