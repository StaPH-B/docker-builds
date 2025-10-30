# SeqSero2S docker image

> SeqSero2S: Salmonella enterica serotype prediction from genome sequencing data

Main tool : [SeqSero2S](https://github.com/LSTUGA/SeqSero2S/)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
_libgcc_mutex                          0.1               conda_forge            conda-forge
_openmp_mutex                          4.5               2_gnu                  conda-forge
alsa-lib                               1.1.5             h516909a_1002          conda-forge
any2fasta                              0.4.2             hdfd78af_3             bioconda   
argtable2                              2.13              hd590300_1004          conda-forge
bedtools                               2.31.1            hf5e1c6e_2             bioconda   
biopython                              1.86              py312h4c3975b_0        conda-forge
blast                                  2.16.0            hc155240_3             bioconda   
blast-legacy                           2.2.26            h9ee0642_4             bioconda   
bwa                                    0.7.18            he4a0461_1             bioconda   
bzip2                                  1.0.8             hda65f42_8             conda-forge
c-ares                                 1.34.5            hb9d3cd8_0             conda-forge
ca-certificates                        2025.10.5         hbd8a1cb_0             conda-forge
clustalo                               1.2.4             h503566f_10            bioconda   
clustalw                               2.1               h9948957_12            bioconda   
consan                                 1.2               h7b50bb2_7             bioconda   
curl                                   8.8.0             he654da7_1             conda-forge
dendropy                               5.0.8             pyhdfd78af_1           bioconda   
dialign-tx                             1.0.2             h7b50bb2_8             bioconda   
dnspython                              2.8.0             pyhcf101f3_0           conda-forge
entrez-direct                          22.4              he881be0_0             bioconda   
expat                                  2.7.1             hecca717_0             conda-forge
famsa                                  2.2.3             h9948957_1             bioconda   
fasttree                               2.2.0             h7b50bb2_0             bioconda   
fontconfig                             2.14.2            h14ed4e7_0             conda-forge
freetype                               2.12.1            h267a509_2             conda-forge
gawk                                   5.3.1             hcd3d067_0             conda-forge
giflib                                 5.2.2             hd590300_0             conda-forge
gmp                                    6.3.0             hac33072_2             conda-forge
gsl                                    2.7               he838d99_0             conda-forge
hmmer                                  3.4               hb6cb901_4             bioconda   
htslib                                 1.21              h5efdd21_0             bioconda   
icu                                    73.2              h59595ed_0             conda-forge
importlib-metadata                     8.7.0             pyhe01879c_1           conda-forge
jpeg                                   9e                h0b41bf4_3             conda-forge
kalign2                                2.04              h7b50bb2_8             bioconda   
keyutils                               1.6.3             hb9d3cd8_0             conda-forge
krb5                                   1.21.3            h659f571_0             conda-forge
lcms2                                  2.12              hddcbb42_0             conda-forge
ld_impl_linux-64                       2.44              ha97dd6f_2             conda-forge
libasprintf                            0.25.1            h3f43e3d_1             conda-forge
libblas                                3.9.0             38_h4a7cf45_openblas   conda-forge
libcblas                               3.9.0             38_h0358290_openblas   conda-forge
libcurl                                8.8.0             hca28451_1             conda-forge
libdb                                  6.2.32            h9c3ff4c_0             conda-forge
libdeflate                             1.24              h86f0d12_0             conda-forge
libedit                                3.1.20250104      pl5321h7949ede_0       conda-forge
libev                                  4.33              hd590300_2             conda-forge
libexpat                               2.7.1             hecca717_0             conda-forge
libffi                                 3.5.2             h9ec8514_0             conda-forge
libgcc                                 15.2.0            h767d61c_7             conda-forge
libgcc-ng                              15.2.0            h69a702a_7             conda-forge
libgettextpo                           0.25.1            h3f43e3d_1             conda-forge
libgfortran                            15.2.0            h69a702a_7             conda-forge
libgfortran-ng                         15.2.0            h69a702a_7             conda-forge
libgfortran5                           15.2.0            hcd61629_7             conda-forge
libgomp                                15.2.0            h767d61c_7             conda-forge
libiconv                               1.18              h3b78370_2             conda-forge
libidn2                                2.3.8             hfac485b_1             conda-forge
liblapack                              3.9.0             38_h47877c9_openblas   conda-forge
liblzma                                5.8.1             hb9d3cd8_2             conda-forge
liblzma-devel                          5.8.1             hb9d3cd8_2             conda-forge
libnghttp2                             1.58.0            h47da74e_1             conda-forge
libnsl                                 2.0.1             hb9d3cd8_1             conda-forge
libopenblas                            0.3.30            pthreads_h94d23a6_3    conda-forge
libpng                                 1.6.43            h2797004_0             conda-forge
libsqlite                              3.46.0            hde9e2c9_0             conda-forge
libssh2                                1.11.0            h0841786_0             conda-forge
libstdcxx                              15.2.0            h8f9b012_7             conda-forge
libstdcxx-ng                           15.2.0            h4852527_7             conda-forge
libtiff                                4.2.0             hf544144_3             conda-forge
libunistring                           0.9.10            h7f98852_0             conda-forge
libuuid                                2.41.2            he9a06e4_0             conda-forge
libwebp-base                           1.6.0             hd42ef1d_0             conda-forge
libxcb                                 1.17.0            h8a09558_0             conda-forge
libxcrypt                              4.4.36            hd590300_1             conda-forge
libxml2                                2.12.7            hc051c1a_1             conda-forge
libxslt                                1.1.39            h76b75d6_0             conda-forge
libzlib                                1.2.13            h4ab18f5_6             conda-forge
lxml                                   5.2.2             py312hb90d8a5_0        conda-forge
mafft                                  7.526             h4bc722e_0             conda-forge
mlst                                   2.22.1            hdfd78af_0             bioconda   
mpfr                                   4.2.1             h90cbb55_3             conda-forge
mpi                                    1.0               openmpi                conda-forge
muscle                                 3.8.1551          h9948957_9             bioconda   
mustang                                3.2.4             h9948957_0             bioconda   
ncbi-vdb                               3.2.1             h9948957_0             bioconda   
ncurses                                6.5               h2d0b736_3             conda-forge
numpy                                  2.3.4             py312h33ff503_0        conda-forge
openjdk                                11.0.1            h600c080_1018          conda-forge
openmpi                                4.1.6             hc5af2df_101           conda-forge
openssl                                3.5.4             h26f9b46_0             conda-forge
packaging                              25.0              pyh29332c3_1           conda-forge
paml                                   4.10.9            h7b50bb2_1             bioconda   
pasta                                  1.9.2             py312hccd54bf_5        bioconda   
pcre                                   8.45              h9c3ff4c_0             conda-forge
perl                                   5.32.1            7_hd590300_perl5       conda-forge
perl-algorithm-diff                    1.201             pl5321hd8ed1ab_0       conda-forge
perl-archive-tar                       3.04              pl5321hdfd78af_0       bioconda   
perl-b-cow                             0.007             pl5321hb9d3cd8_1       conda-forge
perl-base                              2.23              pl5321hd8ed1ab_0       conda-forge
perl-bio-asn1-entrezgene               1.73              pl5321hdfd78af_3       bioconda   
perl-bio-coordinate                    1.007001          pl5321hdfd78af_3       bioconda   
perl-bio-featureio                     1.6.905           pl5321hdfd78af_4       bioconda   
perl-bio-samtools                      1.43              pl5321he4a0461_4       bioconda   
perl-bio-searchio-hmmer                1.7.3             pl5321hdfd78af_0       bioconda   
perl-bio-tools-phylo-paml              1.7.3             pl5321hdfd78af_3       bioconda   
perl-bio-tools-run-alignment-clustalw  1.7.4             pl5321hdfd78af_3       bioconda   
perl-bio-tools-run-alignment-tcoffee   1.7.4             pl5321hdfd78af_5       bioconda   
perl-bioperl                           1.7.8             hdfd78af_1             bioconda   
perl-bioperl-core                      1.7.8             pl5321hdfd78af_1       bioconda   
perl-bioperl-run                       1.007003          pl5321hdfd78af_0       bioconda   
perl-business-isbn                     3.007             pl5321hd8ed1ab_0       conda-forge
perl-business-isbn-data                20210112.006      pl5321hd8ed1ab_0       conda-forge
perl-carp                              1.50              pl5321hd8ed1ab_0       conda-forge
perl-class-data-inheritable            0.09              pl5321ha770c72_0       conda-forge
perl-class-method-modifiers            2.13              pl5321ha770c72_0       conda-forge
perl-clone                             0.46              pl5321hb9d3cd8_1       conda-forge
perl-common-sense                      3.75              pl5321hd8ed1ab_0       conda-forge
perl-compress-raw-bzip2                2.214             pl5321hda65f42_0       conda-forge
perl-compress-raw-zlib                 2.214             pl5321h4dac143_0       conda-forge
perl-constant                          1.33              pl5321hd8ed1ab_0       conda-forge
perl-data-dump                         1.25              pl5321h7b50bb2_2       bioconda   
perl-data-dumper                       2.183             pl5321hb9d3cd8_1       conda-forge
perl-db_file                           1.858             pl5321hb9d3cd8_0       conda-forge
perl-devel-stacktrace                  2.04              pl5321h296ab09_0       conda-forge
perl-digest-hmac                       1.05              pl5321hdfd78af_0       bioconda   
perl-digest-md5                        2.59              pl5321hb9d3cd8_3       conda-forge
perl-encode                            3.21              pl5321hb9d3cd8_1       conda-forge
perl-encode-locale                     1.05              pl5321hdfd78af_7       bioconda   
perl-exception-class                   1.45              pl5321ha770c72_0       conda-forge
perl-exporter                          5.74              pl5321hd8ed1ab_0       conda-forge
perl-exporter-tiny                     1.002002          pl5321hd8ed1ab_0       conda-forge
perl-extutils-makemaker                7.70              pl5321hd8ed1ab_0       conda-forge
perl-file-listing                      6.16              pl5321hdfd78af_0       bioconda   
perl-file-slurper                      0.014             pl5321hdfd78af_0       bioconda   
perl-file-sort                         1.01              pl5321hdfd78af_3       bioconda   
perl-file-spec                         3.48_01           pl5321hdfd78af_2       bioconda   
perl-getopt-long                       2.58              pl5321hdfd78af_0       bioconda   
perl-html-parser                       3.81              pl5321h4ac6f70_1       bioconda   
perl-html-tagset                       3.24              pl5321hdfd78af_0       bioconda   
perl-http-cookiejar-lwp                0.014             pl5321hdfd78af_0       bioconda   
perl-http-cookies                      6.11              pl5321hdfd78af_0       bioconda   
perl-http-daemon                       6.16              pl5321hdfd78af_0       bioconda   
perl-http-date                         6.06              pl5321hdfd78af_0       bioconda   
perl-http-message                      7.01              pl5321hdfd78af_0       bioconda   
perl-http-negotiate                    6.01              pl5321hdfd78af_4       bioconda   
perl-inc-latest                        0.500             pl5321ha770c72_0       conda-forge
perl-io-compress                       2.213             pl5321h503566f_0       bioconda   
perl-io-html                           1.004             pl5321hdfd78af_0       bioconda   
perl-io-socket-ssl                     2.075             pl5321hd8ed1ab_0       conda-forge
perl-io-string                         1.08              pl5321hdfd78af_4       bioconda   
perl-io-tty                            1.20              pl5321hb9d3cd8_3       conda-forge
perl-io-zlib                           1.15              pl5321hdfd78af_1       bioconda   
perl-ipc-run                           20250809.0        pl5321hdfd78af_0       bioconda   
perl-json                              4.10              pl5321hdfd78af_1       bioconda   
perl-json-xs                           4.04              pl5321h9948957_0       bioconda   
perl-libwww-perl                       6.81              pl5321hdfd78af_0       bioconda   
perl-libxml-perl                       0.08              pl5321hdfd78af_3       bioconda   
perl-list-moreutils                    0.430             pl5321hdfd78af_0       bioconda   
perl-list-moreutils-xs                 0.430             pl5321h7b50bb2_5       bioconda   
perl-lwp-mediatypes                    6.04              pl5321hdfd78af_1       bioconda   
perl-lwp-protocol-https                6.14              pl5321hdfd78af_1       bioconda   
perl-mime-base64                       3.16              pl5321hb9d3cd8_3       conda-forge
perl-module-build                      0.4234            pl5321ha770c72_1       conda-forge
perl-module-load                       0.34              pl5321hdfd78af_0       bioconda   
perl-moo                               2.005004          pl5321ha770c72_0       conda-forge
perl-mozilla-ca                        20250602          pl5321hdfd78af_0       bioconda   
perl-net-http                          6.24              pl5321hdfd78af_0       bioconda   
perl-net-ssleay                        1.92              pl5321hf14f497_1       conda-forge
perl-ntlm                              1.09              pl5321hdfd78af_5       bioconda   
perl-parent                            0.243             pl5321hd8ed1ab_0       conda-forge
perl-pathtools                         3.75              pl5321hb9d3cd8_2       conda-forge
perl-role-tiny                         2.002004          pl5321ha770c72_0       conda-forge
perl-scalar-list-utils                 1.70              pl5321hb03c661_0       conda-forge
perl-socket                            2.027             pl5321h5c03b87_6       bioconda   
perl-storable                          3.15              pl5321hb9d3cd8_2       conda-forge
perl-sub-quote                         2.006006          pl5321ha770c72_0       conda-forge
perl-sub-uplevel                       0.2800            pl5321hb9d3cd8_0       conda-forge
perl-test-deep                         1.130             pl5321hd8ed1ab_0       conda-forge
perl-test-differences                  0.72              pl5321ha770c72_0       conda-forge
perl-test-exception                    0.43              pl5321hd8ed1ab_0       conda-forge
perl-test-fatal                        0.016             pl5321ha770c72_0       conda-forge
perl-test-most                         0.38              pl5321hdfd78af_0       bioconda   
perl-test-needs                        0.002009          pl5321hd8ed1ab_0       conda-forge
perl-test-requiresinternet             0.05              pl5321hdfd78af_1       bioconda   
perl-test-warn                         0.37              pl5321hd8ed1ab_0       conda-forge
perl-test-warnings                     0.031             pl5321ha770c72_0       conda-forge
perl-text-diff                         1.45              pl5321hd8ed1ab_0       conda-forge
perl-time-local                        1.35              pl5321hdfd78af_0       bioconda   
perl-timedate                          2.33              pl5321hdfd78af_2       bioconda   
perl-tree-dag_node                     1.35              pl5321hdfd78af_0       bioconda   
perl-try-tiny                          0.31              pl5321ha770c72_0       conda-forge
perl-types-serialiser                  1.01              pl5321hdfd78af_0       bioconda   
perl-uri                               5.34              pl5321ha770c72_0       conda-forge
perl-url-encode                        0.03              pl5321h9ee0642_1       bioconda   
perl-www-robotrules                    6.02              pl5321hdfd78af_4       bioconda   
perl-xml-dom                           1.46              pl5321hdfd78af_1       bioconda   
perl-xml-dom-xpath                     0.14              pl5321hdfd78af_2       bioconda   
perl-xml-parser                        2.44_01           pl5321hf2e2c51_1004    conda-forge
perl-xml-regexp                        0.04              pl5321hdfd78af_3       bioconda   
perl-xml-xpathengine                   0.14              pl5321hdfd78af_3       bioconda   
phylip                                 3.697             h7b50bb2_3             bioconda   
pip                                    25.2              pyh8b19718_0           conda-forge
poa                                    2.0               h7b50bb2_6             bioconda   
prank                                  170427            h9948957_1             bioconda   
probcons                               1.12              h8b12597_1             bioconda   
probconsrna                            1.10              h9f5acd7_4             bioconda   
proda                                  1.0               h503566f_7             bioconda   
pthread-stubs                          0.4               hb9d3cd8_1002          conda-forge
pyfaidx                                0.9.0.3           pyhdfd78af_0           bioconda   
pymongo                                4.15.3            py312h1289d80_0        conda-forge
python                                 3.12.3            hab00c5b_0_cpython     conda-forge
python_abi                             3.12              8_cp312                conda-forge
pyvcf3                                 1.0.4             py312h0fa9677_0        bioconda   
raxml                                  8.2.13            h7b50bb2_3             bioconda   
readline                               8.2               h8c095d6_2             conda-forge
rpsbproc                               0.5.0             h6a68c12_1             bioconda   
salmid                                 0.1.23            py_0                   bioconda   
samtools                               1.21              h50ea8bc_0             bioconda   
sap                                    1.1.3             h7b50bb2_5             bioconda   
seqsero2s                              1.1.4             pyhdfd78af_0           bioconda   
seqtk                                  1.4               he4a0461_2             bioconda   
setuptools                             80.9.0            pyhff2d567_0           conda-forge
six                                    1.17.0            pyhe01879c_1           conda-forge
sniffio                                1.3.1             pyhd8ed1ab_1           conda-forge
spades                                 4.0.0             h6dccd9a_3             bioconda   
sra-tools                              2.9.6             hf484d3e_0             bioconda   
stringmlst                             0.6.3             py_0                   bioconda   
t-coffee                               13.46.2.7c9e712d  pl5321hb2a3317_0       bioconda   
tk                                     8.6.13            noxft_h4845f30_101     conda-forge
tmalign                                20170708          h8d36177_7             bioconda   
tzdata                                 2025b             h78e105d_0             conda-forge
viennarna                              2.7.0             py312pl5321h9f0f9fd_0  bioconda   
wget                                   1.21.4            hda4d442_0             conda-forge
wheel                                  0.45.1            pyhd8ed1ab_1           conda-forge
xorg-libx11                            1.8.12            h4f16b4b_0             conda-forge
xorg-libxau                            1.0.12            hb9d3cd8_0             conda-forge
xorg-libxdmcp                          1.1.5             hb9d3cd8_0             conda-forge
xorg-libxext                           1.3.6             hb9d3cd8_0             conda-forge
xorg-libxfixes                         6.0.2             hb03c661_0             conda-forge
xorg-libxi                             1.8.2             hb9d3cd8_0             conda-forge
xorg-libxrender                        0.9.12            hb9d3cd8_0             conda-forge
xorg-libxtst                           1.2.5             hb9d3cd8_3             conda-forge
xz                                     5.8.1             hbcc6ac9_2             conda-forge
xz-gpl-tools                           5.8.1             hbcc6ac9_2             conda-forge
xz-tools                               5.8.1             hb9d3cd8_2             conda-forge
zipp                                   3.23.0            pyhd8ed1ab_0           conda-forge
zlib                                   1.2.13            h4ab18f5_6             conda-forge
zstd                                   1.5.6             ha6fb4c9_0             conda-forge
```
</details>

## Example Usage

Please note that although the `SeqSero2S.py --version` command works as anticipated (output: `SeqSero2S.py 1.1.4`), there are two "Predicted serotype" outputs, one of which says `(SeqSero2 v1.3.2)`. [This is hardcoded in the SeqSero2S.py script](https://github.com/search?q=repo%3ALSTUGA%2FSeqSero2S+1.3.2&type=code).

```bash
# paired end Illumina reads as input for allele mode
$ SeqSero2S.py \
    -i SRR6082043_1.fastq.gz SRR6082043_2.fastq.gz \
    -t 2 \
    -m a \
    -d SRR6082043-seqsero2s-reads-allele-mode
    -n SRR6082043 \
    -p 2
/opt/conda/bin/SeqSero2S.py:1238: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
  if LooseVersion(version)<=LooseVersion("1.2"):
[bam_sort_core] merging from 0 files and 2 in-memory blocks...
building database...
mapping...
check samtools version: 1.21
assembling...
blasting... 

Sample name:    SRR6082043
Output directory:       /test/SRR6082043-seqsero2s-reads-allele-mode
Input files:    /test/SRR6082043_1.fastq.gz     /test/SRR6082043_2.fastq.gz
O antigen prediction:   7
H1 antigen prediction(fliC):    r
H2 antigen prediction(fljB):    1,5
Predicted identification:       Salmonella enterica subspecies enterica (subspecies I)
Predicted antigenic profile:    7:r:1,5
Predicted serotype:     Infantis
Predicted serotype (SeqSero2 v1.3.2):   Infantis
Note:

Sequence type: 32
Number of ST32 strains in EnteroBase: 19554
aroC: 17
dnaN: 18
hemD: 22
hisD: 17
purE: 5
sucA: 21
thrA: 19

Predicted serotype:     Infantis
Predicted serotype (SeqSero2 v1.3.2):   Infantis

# genome assembly FASTA as input for kmer mode
$ SeqSero2S.py \
      -i GCA_007765495.1.genomic.fna \
      -t 4 \
      -m k \
      -d GCA_007765495.1-seqsero2s-assembly-kmer-mode \
      -n GCA_007765495.1 \
      -p 2
Sample name:    GCA_007765495.1
Output directory:       /test/GCA_007765495.1-seqsero2-assembly-kmer-mode
Input files:    GCA_007765495.1.genomic.fna
O antigen prediction:   7
H1 antigen prediction(fliC):    r
H2 antigen prediction(fljB):    1,5
Predicted identification:       Salmonella enterica subspecies enterica (subspecies I)
Predicted antigenic profile:    7:r:1,5
Predicted serotype:     Infantis
Predicted serotype (SeqSero2 v1.3.2):   Infantis
Note:

Sequence type: 32
Number of ST32 strains in EnteroBase: 19554
aroC: 17
dnaN: 18
hemD: 22
hisD: 17
purE: 5
sucA: 21
thrA: 19


Predicted serotype:     Infantis
Predicted serotype (SeqSero2 v1.3.2):   Infantis
```
