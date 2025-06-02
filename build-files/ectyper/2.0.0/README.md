# ECTyper container

Main tool: [ectyper](https://github.com/phac-nml/ecoli_serotyping)
  
Code repository: https://github.com/phac-nml/ecoli_serotyping

<details>
<summary>Additional tools installed via micromamba:</summary> 

```
  Name                     Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex            0.1           conda_forge           conda-forge
  _openmp_mutex            4.5           2_gnu                 conda-forge
  bcftools                 1.21          h3a4d415_1            bioconda   
  biopython                1.85          py313h536fd9c_1       conda-forge
  blast                    2.16.0        h66d330f_5            bioconda   
  bowtie2                  2.5.4         he96a11b_5            bioconda   
  brotli-python            1.1.0         py313h46c70d0_2       conda-forge
  bzip2                    1.0.8         h4bc722e_7            conda-forge
  c-ares                   1.34.5        hb9d3cd8_0            conda-forge
  ca-certificates          2025.4.26     hbd8a1cb_0            conda-forge
  capnproto                1.0.2         h766bdaa_3            conda-forge
  certifi                  2025.4.26     pyhd8ed1ab_0          conda-forge
  cffi                     1.17.1        py313hfab6e84_0       conda-forge
  charset-normalizer       3.4.2         pyhd8ed1ab_0          conda-forge
  colorama                 0.4.6         pyhd8ed1ab_1          conda-forge
  curl                     8.14.0        h332b0f4_0            conda-forge
  ectyper                  2.0.0         pyhdfd78af_4          bioconda   
  entrez-direct            22.4          he881be0_0            bioconda   
  exceptiongroup           1.3.0         pyhd8ed1ab_0          conda-forge
  gsl                      2.7           he838d99_0            conda-forge
  h2                       4.2.0         pyhd8ed1ab_0          conda-forge
  hpack                    4.1.0         pyhd8ed1ab_0          conda-forge
  htslib                   1.21          h566b1c6_1            bioconda   
  hyperframe               6.1.0         pyhd8ed1ab_0          conda-forge
  idna                     3.10          pyhd8ed1ab_1          conda-forge
  iniconfig                2.0.0         pyhd8ed1ab_1          conda-forge
  keyutils                 1.6.1         h166bdaf_0            conda-forge
  krb5                     1.21.3        h659f571_0            conda-forge
  ld_impl_linux-64         2.43          h712a8e2_4            conda-forge
  libasprintf              0.24.1        h8e693c7_0            conda-forge
  libblas                  3.9.0         31_h59b9bed_openblas  conda-forge
  libcblas                 3.9.0         31_he106b2a_openblas  conda-forge
  libcurl                  8.14.0        h332b0f4_0            conda-forge
  libdeflate               1.24          h86f0d12_0            conda-forge
  libedit                  3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                    4.33          hd590300_2            conda-forge
  libexpat                 2.7.0         h5888daf_0            conda-forge
  libffi                   3.4.6         h2dba641_1            conda-forge
  libgcc                   15.1.0        h767d61c_2            conda-forge
  libgcc-ng                15.1.0        h69a702a_2            conda-forge
  libgettextpo             0.24.1        h5888daf_0            conda-forge
  libgfortran              15.1.0        h69a702a_2            conda-forge
  libgfortran5             15.1.0        hcea5267_2            conda-forge
  libgomp                  15.1.0        h767d61c_2            conda-forge
  libidn2                  2.3.8         ha4ef2c3_0            conda-forge
  liblapack                3.9.0         31_h7ac8fdf_openblas  conda-forge
  liblzma                  5.8.1         hb9d3cd8_1            conda-forge
  libmpdec                 4.0.0         hb9d3cd8_0            conda-forge
  libnghttp2               1.64.0        h161d5f1_0            conda-forge
  libopenblas              0.3.29        pthreads_h94d23a6_0   conda-forge
  libsqlite                3.49.2        hee588c1_0            conda-forge
  libssh2                  1.11.1        hcf80075_0            conda-forge
  libstdcxx                15.1.0        h8f9b012_2            conda-forge
  libstdcxx-ng             15.1.0        h4852527_2            conda-forge
  libunistring             0.9.10        h7f98852_0            conda-forge
  libuuid                  2.38.1        h0b41bf4_0            conda-forge
  libxcrypt                4.4.36        hd590300_1            conda-forge
  libzlib                  1.3.1         hb9d3cd8_2            conda-forge
  mash                     2.3           hb105d93_9            bioconda   
  ncbi-vdb                 3.2.1         h9948957_0            bioconda   
  ncurses                  6.5           h2d0b736_3            conda-forge
  numpy                    2.2.6         py313h17eae1a_0       conda-forge
  openssl                  3.5.0         h7b32b05_1            conda-forge
  packaging                25.0          pyh29332c3_1          conda-forge
  pandas                   2.2.3         py313ha87cce1_3       conda-forge
  perl                     5.32.1        7_hd590300_perl5      conda-forge
  perl-archive-tar         2.40          pl5321hdfd78af_0      bioconda   
  perl-carp                1.50          pl5321hd8ed1ab_0      conda-forge
  perl-common-sense        3.75          pl5321hd8ed1ab_0      conda-forge
  perl-compress-raw-bzip2  2.201         pl5321hbf60520_1      conda-forge
  perl-compress-raw-zlib   2.202         pl5321hadc24fc_0      conda-forge
  perl-encode              3.21          pl5321hb9d3cd8_1      conda-forge
  perl-exporter            5.74          pl5321hd8ed1ab_0      conda-forge
  perl-exporter-tiny       1.002002      pl5321hd8ed1ab_0      conda-forge
  perl-extutils-makemaker  7.70          pl5321hd8ed1ab_0      conda-forge
  perl-io-compress         2.201         pl5321h503566f_5      bioconda   
  perl-io-zlib             1.14          pl5321hdfd78af_0      bioconda   
  perl-json                4.10          pl5321hdfd78af_1      bioconda   
  perl-json-xs             4.03          pl5321h9948957_4      bioconda   
  perl-list-moreutils      0.430         pl5321hdfd78af_0      bioconda   
  perl-list-moreutils-xs   0.430         pl5321h7b50bb2_5      bioconda   
  perl-parent              0.243         pl5321hd8ed1ab_0      conda-forge
  perl-pathtools           3.75          pl5321hb9d3cd8_2      conda-forge
  perl-scalar-list-utils   1.69          pl5321hb9d3cd8_0      conda-forge
  perl-storable            3.15          pl5321hb9d3cd8_2      conda-forge
  perl-types-serialiser    1.01          pl5321hdfd78af_0      bioconda   
  pip                      25.1.1        pyh145f28c_0          conda-forge
  pluggy                   1.6.0         pyhd8ed1ab_0          conda-forge
  pycparser                2.22          pyh29332c3_1          conda-forge
  pysocks                  1.7.1         pyha55dd90_7          conda-forge
  pytest                   8.3.5         pyhd8ed1ab_0          conda-forge
  python                   3.13.3        hf636f53_101_cp313    conda-forge
  python-dateutil          2.9.0.post0   pyhff2d567_1          conda-forge
  python-tzdata            2025.2        pyhd8ed1ab_0          conda-forge
  python_abi               3.13          7_cp313               conda-forge
  pytz                     2025.2        pyhd8ed1ab_0          conda-forge
  readline                 8.2           h8c095d6_2            conda-forge
  requests                 2.32.3        pyhd8ed1ab_1          conda-forge
  rpsbproc                 0.5.0         hd6d6fdc_3            bioconda   
  samtools                 1.21          h96c455f_1            bioconda   
  seqtk                    1.4           h577a1d6_3            bioconda   
  six                      1.17.0        pyhd8ed1ab_0          conda-forge
  tk                       8.6.13        noxft_hd72426e_102    conda-forge
  tomli                    2.2.1         pyhd8ed1ab_1          conda-forge
  typing_extensions        4.13.2        pyh29332c3_0          conda-forge
  tzdata                   2025b         h78e105d_0            conda-forge
  urllib3                  2.4.0         pyhd8ed1ab_0          conda-forge
  wget                     1.21.4        hda4d442_0            conda-forge
  zlib                     1.3.1         hb9d3cd8_2            conda-forge
  zstandard                0.23.0        py313h536fd9c_2       conda-forge
  zstd                     1.5.7         hb8e6e7a_2            conda-forge
```

</details>
</br>

Basic information on how to use this tool:

- executable: `ectyper`
- help: `-h`, `--help`
- version: `--version`
- description: Prediction of Escherichia coli serotype, pathotype and shiga toxin tying from raw reads or assembled genome sequences.

## Additional information

This docker container contains a few databases used by ECTyper:

- O and H antigen database version 1.0 found in [this JSON file](https://github.com/phac-nml/ecoli_serotyping/blob/master/ectyper/Data/ectyper_alleles_db.json)
- species identification Mash sketch database created on 2023-10-03 and found [here on Zenodo](https://zenodo.org/records/13969103)
- Toxin and pathotype signature marker sequences found in [this JSON file](https://github.com/phac-nml/ecoli_serotyping/blob/master/ectyper/Data/ectyper_patho_stx_toxin_typing_database.json)

## Example Usage

```bash
# run ECTyper on an assembled genome sequence using 2 threads. Also run QC verification steps and pathotype prediction.
ectyper -i E-coli-assembly.fasta -o ectyper-outdir -c 2 --verify --pathotype
```
