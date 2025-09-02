# SeqSero2 docker image

> SeqSero2: Salmonella enterica serotype prediction from genome sequencing data

Main tool : [SeqSero2](https://github.com/denglab/SeqSero2)

Additional tools:

- bedtools 2.17.0
- biopython 1.73
- bwa 0.7.18
- python3 3.7.12
- ncbi-blast+ 2.16.0
- SalmID 0.1.23
- samtools 1.21
- seqtk 1.4
- spades 3.15.5
- sra-toolkit 3.2.1

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                       Version       Build                 Channel    
──────────────────────────────────────────────────────────────────────────────
_libgcc_mutex              0.1           conda_forge           conda-forge
_openmp_mutex              4.5           2_gnu                 conda-forge
bedtools                   2.17.0        0                     bioconda   
biopython                  1.73          py37h14c3975_0        conda-forge
blast                      2.16.0        hc155240_3            bioconda   
bwa                        0.7.18        he4a0461_1            bioconda   
bzip2                      1.0.8         h4bc722e_7            conda-forge
c-ares                     1.34.5        hb9d3cd8_0            conda-forge
ca-certificates            2025.8.3      hbd8a1cb_0            conda-forge
curl                       8.8.0         he654da7_1            conda-forge
entrez-direct              22.4          he881be0_0            bioconda   
htslib                     1.21          h5efdd21_0            bioconda   
icu                        70.1          h27087fc_0            conda-forge
kernel-headers_linux-64    3.10.0        he073ed8_18           conda-forge
keyutils                   1.6.3         hb9d3cd8_0            conda-forge
krb5                       1.21.3        h659f571_0            conda-forge
ld_impl_linux-64           2.44          h1423503_1            conda-forge
libasprintf                0.25.1        h3f43e3d_1            conda-forge
libblas                    3.9.0         34_h59b9bed_openblas  conda-forge
libcblas                   3.9.0         34_he106b2a_openblas  conda-forge
libcurl                    8.8.0         hca28451_1            conda-forge
libdeflate                 1.24          h86f0d12_0            conda-forge
libedit                    3.1.20250104  pl5321h7949ede_0      conda-forge
libev                      4.33          hd590300_2            conda-forge
libffi                     3.4.6         h2dba641_1            conda-forge
libgcc                     15.1.0        h767d61c_4            conda-forge
libgcc-ng                  15.1.0        h69a702a_4            conda-forge
libgettextpo               0.25.1        h3f43e3d_1            conda-forge
libgfortran                15.1.0        h69a702a_4            conda-forge
libgfortran5               15.1.0        hcea5267_4            conda-forge
libgomp                    15.1.0        h767d61c_4            conda-forge
libiconv                   1.18          h3b78370_2            conda-forge
libidn2                    2.3.8         ha4ef2c3_0            conda-forge
liblapack                  3.9.0         34_h7ac8fdf_openblas  conda-forge
liblzma                    5.8.1         hb9d3cd8_2            conda-forge
liblzma-devel              5.8.1         hb9d3cd8_2            conda-forge
libnghttp2                 1.58.0        h47da74e_1            conda-forge
libnsl                     2.0.1         hb9d3cd8_1            conda-forge
libopenblas                0.3.30        pthreads_h94d23a6_2   conda-forge
libsqlite                  3.46.0        hde9e2c9_0            conda-forge
libssh2                    1.11.0        h0841786_0            conda-forge
libstdcxx                  15.1.0        h8f9b012_4            conda-forge
libstdcxx-ng               15.1.0        h4852527_4            conda-forge
libunistring               0.9.10        h7f98852_0            conda-forge
libxcrypt                  4.4.36        hd590300_1            conda-forge
libxml2                    2.9.14        h22db469_4            conda-forge
libzlib                    1.2.13        h4ab18f5_6            conda-forge
llvm-openmp                8.0.1         hc9558a2_0            conda-forge
ncbi-vdb                   3.2.1         h9948957_0            bioconda   
ncurses                    6.5           h2d0b736_3            conda-forge
numpy                      1.21.6        py37h976b520_0        conda-forge
openmp                     8.0.1         0                     conda-forge
openssl                    3.5.2         h26f9b46_0            conda-forge
ossuuid                    1.6.2         h5888daf_1001         conda-forge
perl                       5.32.1        7_hd590300_perl5      conda-forge
perl-alien-build           2.48          pl5321hec16e2b_0      bioconda   
perl-alien-libxml2         0.17          pl5321hec16e2b_0      bioconda   
perl-archive-tar           3.04          pl5321hdfd78af_0      bioconda   
perl-business-isbn         3.007         pl5321hd8ed1ab_0      conda-forge
perl-business-isbn-data    20210112.006  pl5321hd8ed1ab_0      conda-forge
perl-capture-tiny          0.48          pl5321ha770c72_1      conda-forge
perl-carp                  1.50          pl5321hd8ed1ab_0      conda-forge
perl-common-sense          3.75          pl5321hd8ed1ab_0      conda-forge
perl-compress-raw-bzip2    2.213         pl5321hda65f42_0      conda-forge
perl-compress-raw-zlib     2.213         pl5321h4dac143_0      conda-forge
perl-constant              1.33          pl5321hd8ed1ab_0      conda-forge
perl-encode                3.21          pl5321hb9d3cd8_1      conda-forge
perl-exporter              5.74          pl5321hd8ed1ab_0      conda-forge
perl-exporter-tiny         1.002002      pl5321hd8ed1ab_0      conda-forge
perl-extutils-makemaker    7.70          pl5321hd8ed1ab_0      conda-forge
perl-ffi-checklib          0.28          pl5321hdfd78af_0      bioconda   
perl-file-chdir            0.1011        pl5321hd8ed1ab_0      conda-forge
perl-file-path             2.18          pl5321hd8ed1ab_0      conda-forge
perl-file-temp             0.2304        pl5321hd8ed1ab_0      conda-forge
perl-file-which            1.24          pl5321hd8ed1ab_0      conda-forge
perl-importer              0.026         pl5321hd8ed1ab_0      conda-forge
perl-io-compress           2.213         pl5321h503566f_0      bioconda   
perl-io-zlib               1.15          pl5321hdfd78af_1      bioconda   
perl-json                  4.10          pl5321hdfd78af_1      bioconda   
perl-json-xs               4.03          pl5321h9948957_4      bioconda   
perl-list-moreutils        0.430         pl5321hdfd78af_0      bioconda   
perl-list-moreutils-xs     0.430         pl5321h7b50bb2_5      bioconda   
perl-parent                0.243         pl5321hd8ed1ab_0      conda-forge
perl-path-tiny             0.124         pl5321hd8ed1ab_0      conda-forge
perl-pathtools             3.75          pl5321hb9d3cd8_2      conda-forge
perl-scalar-list-utils     1.70          pl5321hb03c661_0      conda-forge
perl-scope-guard           0.21          pl5321hd8ed1ab_0      conda-forge
perl-storable              3.15          pl5321hb9d3cd8_2      conda-forge
perl-sub-info              0.002         pl5321hd8ed1ab_0      conda-forge
perl-term-table            0.024         pl5321hdfd78af_0      bioconda   
perl-test-fatal            0.016         pl5321ha770c72_0      conda-forge
perl-test-warnings         0.031         pl5321ha770c72_0      conda-forge
perl-test2-suite           0.000145      pl5321hdfd78af_0      bioconda   
perl-try-tiny              0.31          pl5321ha770c72_0      conda-forge
perl-types-serialiser      1.01          pl5321hdfd78af_0      bioconda   
perl-uri                   5.32          pl5321ha770c72_1      conda-forge
perl-xml-libxml            2.0207        pl5321h661654b_0      bioconda   
perl-xml-namespacesupport  1.12          pl5321hd8ed1ab_0      conda-forge
perl-xml-sax               1.02          pl5321hd8ed1ab_0      conda-forge
perl-xml-sax-base          1.09          pl5321hd8ed1ab_0      conda-forge
pip                        24.0          pyhd8ed1ab_0          conda-forge
python                     3.7.12        hf930737_100_cpython  conda-forge
python_abi                 3.7           4_cp37m               conda-forge
readline                   8.2           h8c095d6_2            conda-forge
rpsbproc                   0.5.0         h6a68c12_1            bioconda   
salmid                     0.1.23        py_0                  bioconda   
samtools                   1.21          h50ea8bc_0            bioconda   
seqsero2                   1.3.1         pyhdfd78af_1          bioconda   
seqtk                      1.4           he4a0461_2            bioconda   
setuptools                 69.0.3        pyhd8ed1ab_0          conda-forge
spades                     3.15.5        h95f258a_1            bioconda   
sqlite                     3.46.0        h6d4b2fc_0            conda-forge
sra-tools                  3.2.1         h4304569_1            bioconda   
sysroot_linux-64           2.17          h0157908_18           conda-forge
tk                         8.6.13        noxft_h4845f30_101    conda-forge
tzdata                     2025b         h78e105d_0            conda-forge
wget                       1.21.4        hda4d442_0            conda-forge
wheel                      0.42.0        pyhd8ed1ab_0          conda-forge
xz                         5.8.1         hbcc6ac9_2            conda-forge
xz-gpl-tools               5.8.1         hbcc6ac9_2            conda-forge
xz-tools                   5.8.1         hb9d3cd8_2            conda-forge
zlib                       1.2.13        h4ab18f5_6            conda-forge
zstd                       1.5.6         ha6fb4c9_0            conda-forge
```
</details>

## Example Usage

```bash
# paired end Illumina reads as input for allele mode
$ SeqSero2_package.py \
      -i SRR6082043_1.fastq.gz SRR6082043_2.fastq.gz \
      -t 2 \
      -m a \
      -d SRR6082043-seqsero2-reads-allele-mode \
      -n SRR6082043 \
      -p 2
[bam_sort_core] merging from 0 files and 2 in-memory blocks...
building database...
mapping...
check samtools version: 1.9
assembling...
blasting... 

Sample name:    SRR6082043
Output directory:       /test/SRR6082043-seqsero2-reads-allele-mode
Input files:    /test/SRR6082043_1.fastq.gz     /test/SRR6082043_2.fastq.gz
O antigen prediction:   7
H1 antigen prediction(fliC):    r
H2 antigen prediction(fljB):    1,5
Predicted identification:       Salmonella enterica subspecies enterica (subspecies I)
Predicted antigenic profile:    7:r:1,5
Predicted serotype:     Infantis
Note:

# genome assembly FASTA as input for kmer mode
$ SeqSero2_package.py \
      -i GCA_007765495.1.genomic.fna \
      -t 4 \
      -m k \
      -d GCA_007765495.1-seqsero2-assembly-kmer-mode \
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
Note:
```
