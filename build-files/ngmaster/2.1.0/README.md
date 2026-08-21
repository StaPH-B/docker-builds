# ngmaster container

Main tool : [ngmaster](https://github.com/MDU-PHL/ngmaster)

In silico multi-antigen sequence typing for Neisseria gonorrhoeae (NG-MAST).

<details>
<summary>Additional tools installed via micromamba:</summary> 

```
List of packages in environment: "/opt/conda"

  Name                                   Version        Build                 Channel    
───────────────────────────────────────────────────────────────────────────────────────────
  _openmp_mutex                          4.5            20_gnu                conda-forge
  any2fasta                              0.8.1          hdfd78af_0            bioconda   
  argtable2                              2.13           hd590300_1004         conda-forge
  backports.zstd                         1.7.0          py314h680f03e_0       conda-forge
  beautifulsoup4                         4.15.0         pyha770c72_0          conda-forge
  biopython                              1.88           py314h5bd0f2a_0       conda-forge
  blast                                  2.17.0         h66d330f_0            bioconda   
  blast-legacy                           2.2.26         hf7ff83a_5            bioconda   
  brotli-python                          1.2.0          py314hcd2bdb6_3       conda-forge
  bs4                                    4.15.0         hd8ed1ab_0            conda-forge
  bzip2                                  1.0.8          hda65f42_10           conda-forge
  c-ares                                 1.34.8         hebe6cf0_2            conda-forge
  ca-certificates                        2026.7.22      hbd8a1cb_0            conda-forge
  certifi                                2026.7.22      pyhd8ed1ab_0          conda-forge
  charset-normalizer                     3.5.1          pyhd8ed1ab_0          conda-forge
  click                                  8.4.2          pyhc90fa1f_0          conda-forge
  clustalo                               1.2.4          h503566f_10           bioconda   
  clustalw                               2.1            hc52dbad_13           bioconda   
  configparser                           7.2.0          pyhd8ed1ab_0          conda-forge
  curl                                   8.21.0         ha042cf0_5            conda-forge
  entrez-direct                          24.0           he881be0_0            bioconda   
  expat                                  2.8.1          hecca717_1            conda-forge
  gawk                                   5.4.1          h0a3468a_0            conda-forge
  gmp                                    6.3.0          hfd2156b_3            conda-forge
  gnutls                                 3.8.13         h18acefa_0            conda-forge
  gzip                                   1.14           hb9d3cd8_0            conda-forge
  h2                                     4.4.1          pyhcf101f3_0          conda-forge
  hpack                                  4.2.0          pyhd8ed1ab_0          conda-forge
  hyperframe                             6.1.0          pyhd8ed1ab_0          conda-forge
  icu                                    78.3           py310h44b86e0_2       conda-forge
  idna                                   3.19           pyhcf101f3_0          conda-forge
  keyutils                               1.6.3          h7cc23a3_1            conda-forge
  krb5                                   1.22.2         hbc21106_2            conda-forge
  ld_impl_linux-64                       2.46.1         default_hbd61a6d_102  conda-forge
  libasprintf                            0.25.1         h3f43e3d_1            conda-forge
  libblas                                3.11.0         9_h4a7cf45_openblas   conda-forge
  libcblas                               3.11.0         9_h0358290_openblas   conda-forge
  libcurl                                8.21.0         ha042cf0_5            conda-forge
  libdb                                  6.2.32         h9c3ff4c_0            conda-forge
  libedit                                3.1.20250104   pl5321h373387f_1      conda-forge
  libev                                  4.33           h280c20c_3            conda-forge
  libexpat                               2.8.1          hecca717_1            conda-forge
  libffi                                 3.7.0          h3435931_0            conda-forge
  libgcc                                 16.1.0         ha9f2e26_2            conda-forge
  libgcc-ng                              16.1.0         h69a702a_2            conda-forge
  libgettextpo                           0.25.1         h3f43e3d_1            conda-forge
  libgfortran                            16.1.0         h69a702a_2            conda-forge
  libgfortran5                           16.1.0         h79bb938_2            conda-forge
  libgomp                                16.1.0         he0feb66_2            conda-forge
  libiconv                               1.18           h0cb94f2_3            conda-forge
  libidn2                                2.3.8          hfac485b_1            conda-forge
  liblapack                              3.11.0         9_h47877c9_openblas   conda-forge
  liblzma                                5.8.3          hb03c661_1            conda-forge
  liblzma-devel                          5.8.3          hb03c661_1            conda-forge
  libmpdec                               4.0.0          hb03c661_2            conda-forge
  libnghttp2                             1.68.1         h74cf4be_1            conda-forge
  libopenblas                            0.3.34         pthreads_h94d23a6_0   conda-forge
  libpsl                                 0.23.1         hd9e3e90_1            conda-forge
  libsqlite                              3.53.4         h13e7031_1            conda-forge
  libssh2                                1.11.1         h6154650_1            conda-forge
  libstdcxx                              16.1.0         h934c35e_2            conda-forge
  libstdcxx-ng                           16.1.0         hdf11a46_2            conda-forge
  libtasn1                               4.21.0         hb03c661_1            conda-forge
  libunistring                           0.9.10         h7f98852_0            conda-forge
  libuuid                                2.42.2         h5347b49_0            conda-forge
  libxcrypt                              4.4.38         h280c20c_0            conda-forge
  libxcrypt1                             4.4.38         pl5321h8c9361a_0      conda-forge
  libzlib                                1.3.2          h25fd6f3_3            conda-forge
  mafft                                  7.526          h4bc722e_0            conda-forge
  mlst                                   2.35.0         hdfd78af_0            bioconda   
  mlstdb                                 1.3.0          pyh106432d_0          bioconda   
  mpfr                                   4.2.2          ha2cb11d_1            conda-forge
  muscle                                 5.3            h9948957_3            bioconda   
  ncbi-vdb                               3.4.1          hd63eeec_0            bioconda   
  ncurses                                6.6            hdb14827_1            conda-forge
  nettle                                 3.10.1         h5ef0d04_1            conda-forge
  ngmaster                               2.1.0          pyhdfd78af_0          bioconda   
  numpy                                  2.5.2          py314h2b28147_0       conda-forge
  openssl                                3.6.3          h35e630c_1            conda-forge
  p11-kit                                0.26.5         h586ad30_1            conda-forge
  paml                                   4.10.10        h87e0c26_2            bioconda   
  pcre2                                  10.47          h8b3dc9c_1            conda-forge
  perl                                   5.32.1         7_hd590300_perl5      conda-forge
  perl-algorithm-diff                    1.201          pl5321hd8ed1ab_0      conda-forge
  perl-archive-tar                       3.12           pl5321hdfd78af_0      bioconda   
  perl-b-cow                             0.007          pl5321hb9d3cd8_1      conda-forge
  perl-base                              2.23           pl5321hd8ed1ab_0      conda-forge
  perl-bio-asn1-entrezgene               1.73           pl5321hdfd78af_3      bioconda   
  perl-bio-coordinate                    1.007001       pl5321hdfd78af_3      bioconda   
  perl-bio-featureio                     1.6.905        pl5321hdfd78af_4      bioconda   
  perl-bio-samtools                      1.43           pl5321h577a1d6_6      bioconda   
  perl-bio-searchio-hmmer                1.7.3          pl5321hdfd78af_0      bioconda   
  perl-bio-tools-phylo-paml              1.7.3          pl5321hdfd78af_3      bioconda   
  perl-bio-tools-run-alignment-clustalw  1.7.4          pl5321hdfd78af_3      bioconda   
  perl-bio-tools-run-alignment-tcoffee   1.7.4          pl5321hdfd78af_5      bioconda   
  perl-bioperl                           1.7.8          hdfd78af_1            bioconda   
  perl-bioperl-core                      1.7.8          pl5321hdfd78af_1      bioconda   
  perl-bioperl-run                       1.007003       pl5321hdfd78af_0      bioconda   
  perl-business-isbn                     3.007          pl5321hd8ed1ab_0      conda-forge
  perl-business-isbn-data                20210112.006   pl5321hd8ed1ab_0      conda-forge
  perl-carp                              1.50           pl5321hd8ed1ab_0      conda-forge
  perl-class-data-inheritable            0.09           pl5321ha770c72_0      conda-forge
  perl-class-method-modifiers            2.13           pl5321ha770c72_0      conda-forge
  perl-clone                             0.46           pl5321hb9d3cd8_1      conda-forge
  perl-common-sense                      3.75           pl5321hd8ed1ab_0      conda-forge
  perl-compress-raw-bzip2                2.214          pl5321hda65f42_0      conda-forge
  perl-compress-raw-zlib                 2.214          pl5321h4dac143_0      conda-forge
  perl-constant                          1.33           pl5321hd8ed1ab_0      conda-forge
  perl-data-dump                         1.25           pl5321h7b50bb2_2      bioconda   
  perl-data-dumper                       2.183          pl5321hb9d3cd8_1      conda-forge
  perl-db_file                           1.858          pl5321hb9d3cd8_0      conda-forge
  perl-devel-stacktrace                  2.04           pl5321h296ab09_0      conda-forge
  perl-digest-hmac                       1.05           pl5321hdfd78af_0      bioconda   
  perl-digest-md5                        2.59           pl5321hb9d3cd8_3      conda-forge
  perl-encode                            3.24           pl5321hb03c661_0      conda-forge
  perl-encode-locale                     1.05           pl5321hdfd78af_7      bioconda   
  perl-exception-class                   1.45           pl5321ha770c72_0      conda-forge
  perl-exporter                          5.74           pl5321hd8ed1ab_0      conda-forge
  perl-exporter-tiny                     1.002002       pl5321hd8ed1ab_0      conda-forge
  perl-extutils-makemaker                7.70           pl5321hd8ed1ab_0      conda-forge
  perl-file-listing                      6.16           pl5321hdfd78af_0      bioconda   
  perl-file-slurper                      0.014          pl5321hdfd78af_0      bioconda   
  perl-file-sort                         1.01           pl5321hdfd78af_3      bioconda   
  perl-file-spec                         3.48_01        pl5321hdfd78af_2      bioconda   
  perl-file-which                        1.24           pl5321hd8ed1ab_0      conda-forge
  perl-getopt-long                       2.58           pl5321hdfd78af_0      bioconda   
  perl-html-parser                       3.81           pl5321h4ac6f70_1      bioconda   
  perl-html-tagset                       3.24           pl5321hdfd78af_0      bioconda   
  perl-http-cookiejar-lwp                0.014          pl5321hdfd78af_0      bioconda   
  perl-http-cookies                      6.12           pl5321hdfd78af_0      bioconda   
  perl-http-daemon                       6.17           pl5321hdfd78af_0      bioconda   
  perl-http-date                         6.08           pl5321hdfd78af_0      bioconda   
  perl-http-message                      7.04           pl5321hdfd78af_0      bioconda   
  perl-http-negotiate                    6.01           pl5321hdfd78af_4      bioconda   
  perl-inc-latest                        0.500          pl5321ha770c72_0      conda-forge
  perl-io-compress                       2.216          pl5321h503566f_0      bioconda   
  perl-io-html                           1.004          pl5321hdfd78af_0      bioconda   
  perl-io-socket-ssl                     2.075          pl5321hd8ed1ab_0      conda-forge
  perl-io-string                         1.08           pl5321hdfd78af_4      bioconda   
  perl-io-tty                            1.31           pl5321hb03c661_0      conda-forge
  perl-io-zlib                           1.15           pl5321hdfd78af_1      bioconda   
  perl-ipc-run                           20250809.0     pl5321hdfd78af_0      bioconda   
  perl-json                              4.11           pl5321hdfd78af_0      bioconda   
  perl-json-xs                           4.04           pl5321h9948957_0      bioconda   
  perl-libwww-perl                       6.83           pl5321hdfd78af_0      bioconda   
  perl-libxml-perl                       0.08           pl5321hdfd78af_3      bioconda   
  perl-list-moreutils                    0.430          pl5321hdfd78af_0      bioconda   
  perl-list-moreutils-xs                 0.430          pl5321h7b50bb2_5      bioconda   
  perl-lwp-mediatypes                    6.04           pl5321hdfd78af_1      bioconda   
  perl-lwp-protocol-https                6.17           pl5321hdfd78af_0      bioconda   
  perl-mime-base64                       3.16           pl5321hb9d3cd8_3      conda-forge
  perl-module-build                      0.4234         pl5321ha770c72_1      conda-forge
  perl-module-load                       0.34           pl5321hdfd78af_0      bioconda   
  perl-moo                               2.005004       pl5321ha770c72_0      conda-forge
  perl-mozilla-ca                        20260813       pl5321hdfd78af_0      bioconda   
  perl-net-http                          6.24           pl5321hdfd78af_0      bioconda   
  perl-net-ssleay                        1.96           pl5321h34fdc24_0      conda-forge
  perl-ntlm                              1.09           pl5321hdfd78af_5      bioconda   
  perl-parent                            0.243          pl5321hd8ed1ab_0      conda-forge
  perl-pathtools                         3.75           pl5321hb9d3cd8_2      conda-forge
  perl-role-tiny                         2.002004       pl5321ha770c72_0      conda-forge
  perl-scalar-list-utils                 1.70           pl5321hb03c661_0      conda-forge
  perl-socket                            2.027          pl5321h5c03b87_6      bioconda   
  perl-storable                          3.15           pl5321hb9d3cd8_2      conda-forge
  perl-sub-quote                         2.006006       pl5321ha770c72_0      conda-forge
  perl-sub-uplevel                       0.2800         pl5321hb9d3cd8_0      conda-forge
  perl-test-deep                         1.130          pl5321hd8ed1ab_0      conda-forge
  perl-test-differences                  0.72           pl5321ha770c72_0      conda-forge
  perl-test-exception                    0.43           pl5321hd8ed1ab_0      conda-forge
  perl-test-fatal                        0.016          pl5321ha770c72_0      conda-forge
  perl-test-most                         0.42           pl5321hdfd78af_0      bioconda   
  perl-test-needs                        0.002009       pl5321hd8ed1ab_0      conda-forge
  perl-test-requiresinternet             0.05           pl5321hdfd78af_1      bioconda   
  perl-test-warn                         0.37           pl5321hd8ed1ab_0      conda-forge
  perl-test-warnings                     0.031          pl5321ha770c72_0      conda-forge
  perl-text-diff                         1.45           pl5321hd8ed1ab_0      conda-forge
  perl-time-local                        1.35           pl5321hdfd78af_0      bioconda   
  perl-timedate                          2.35           pl5321hdfd78af_0      bioconda   
  perl-tree-dag_node                     1.39           pl5321hdfd78af_0      bioconda   
  perl-try-tiny                          0.31           pl5321ha770c72_0      conda-forge
  perl-types-serialiser                  1.01           pl5321hdfd78af_0      bioconda   
  perl-uri                               5.36           pl5321ha770c72_0      conda-forge
  perl-url-encode                        0.03           pl5321h9ee0642_1      bioconda   
  perl-www-robotrules                    6.03           pl5321hdfd78af_0      bioconda   
  perl-xml-dom                           1.46           pl5321hdfd78af_1      bioconda   
  perl-xml-dom-xpath                     0.14           pl5321hdfd78af_2      bioconda   
  perl-xml-parser                        2.44_01        pl5321hf2e2c51_1004   conda-forge
  perl-xml-regexp                        0.04           pl5321hdfd78af_3      bioconda   
  perl-xml-xpathengine                   0.14           pl5321hdfd78af_3      bioconda   
  pip                                    26.2.1         pyh145f28c_0          conda-forge
  poa                                    2.0            h7b50bb2_6            bioconda   
  pysocks                                1.7.1          pyha55dd90_7          conda-forge
  python                                 3.14.7         h399a421_100_cp314    conda-forge
  python_abi                             3.14           8_cp314               conda-forge
  pyyaml                                 6.0.3          py314h67df5f8_1       conda-forge
  rauth                                  0.7.3          py_0                  conda-forge
  readline                               8.3            hd6e31c0_1            conda-forge
  requests                               2.34.2         pyhcf101f3_0          conda-forge
  samtools                               0.1.19         h9dcdb79_15           bioconda   
  soupsieve                              2.9.2          pyhd8ed1ab_0          conda-forge
  t-coffee                               12.00.7fb08c2  h26a2512_0            bioconda   
  tk                                     8.6.13         noxft_h1df4ec4_4      conda-forge
  tqdm                                   4.70.0         pyh8f84b5b_0          conda-forge
  typing-extensions                      4.16.0         h69aa097_0            conda-forge
  typing_extensions                      4.16.0         pyhcf101f3_0          conda-forge
  tzdata                                 2026c          h151e31d_0            conda-forge
  unzip                                  6.0            hb03c661_4            conda-forge
  urllib3                                2.7.0          pyhd8ed1ab_0          conda-forge
  viennarna                              2.4.7          py36_2                bioconda   
  wget                                   1.25.0         h653f8fd_1            conda-forge
  xz                                     5.8.3          ha02ee65_1            conda-forge
  xz-gpl-tools                           5.8.3          ha02ee65_1            conda-forge
  xz-tools                               5.8.3          hb03c661_1            conda-forge
  yaml                                   0.2.5          hebe6cf0_3            conda-forge
  zlib                                   1.3.2          h25fd6f3_3            conda-forge
  zstd                                   1.5.7          hb78ec9c_7            conda-forge
```
</details>
</br>

## Example Usage

```bash
# test ngmaster with the test FASTA file included with ngmaster code
$ ngmaster /opt/conda/lib/python3.9/site-packages/ngmaster/test/test.fa
FILE    SCHEME  NG-MAST/NG-STAR porB_NG-MAST    tbpB    penA    mtrR    porB_NG-STAR    ponA    gyrA    parC    23S
/opt/conda/lib/python3.9/site-packages/ngmaster/test/test.fa    ngmaSTar        4186/231        2569    241     23      42      100     100     10      2100
```

