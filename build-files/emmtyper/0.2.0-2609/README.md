# emmtyper container

Main tool : [emmtyper](https://github.com/MDU-PHL/emmtyper)

Code repository: https://github.com/MDU-PHL/emmtyper

Basic information on how to use this tool:
- executable: emmtyper
- help: --help
- version: --version
- description: |

'emmtyper' is a command line tool for emm-typing of _Streptococcus pyogenes_ using a _de novo_ or complete assembly.

Additional information:

This image uses the most up-to-date fasta file for emm typing by downloading from https://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/alltrimmed.tfa. The out-of-date files are removed and overwritten at the time of building and deployment.

This image is rebuilt every month on Dockerhub and Quay.io with the tag ${emmtyper version}-${data image was deployed}. 

Run `micromamba list -n emmtyper` to get the list of all dependencies and versions installed via micrombamba for any image.

<details>
<summary>Additional tools installed via micromamba for 0.2.0-2609:</summary>

```
List of packages in environment: "/opt/conda/envs/emmtyper"

  Name                     Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────────
  _openmp_mutex            4.5           20_gnu                conda-forge
  blast                    2.17.0        hb02a186_1            bioconda   
  bzip2                    1.0.8         hda65f42_10           conda-forge
  c-ares                   1.34.8        hebe6cf0_2            conda-forge
  ca-certificates          2026.7.22     hbd8a1cb_0            conda-forge
  click                    8.5.0         pyh5ded981_0          conda-forge
  curl                     8.22.0        ha042cf0_0            conda-forge
  emmtyper                 0.2.0         py_0                  bioconda   
  entrez-direct            26.0          h1079eea_0            bioconda   
  icu                      78.3          py310h44b86e0_2       conda-forge
  ispcr                    33            h7b50bb2_6            bioconda   
  keyutils                 1.6.3         h7cc23a3_1            conda-forge
  krb5                     1.22.2        hbc21106_2            conda-forge
  ld_impl_linux-64         2.46.1        default_hbd61a6d_102  conda-forge
  libblas                  3.11.0        11_h4a7cf45_openblas  conda-forge
  libcblas                 3.11.0        11_h0358290_openblas  conda-forge
  libcurl                  8.22.0        ha042cf0_0            conda-forge
  libedit                  3.1.20250104  pl5321h373387f_1      conda-forge
  libev                    4.33          h280c20c_3            conda-forge
  libexpat                 2.8.1         hecca717_1            conda-forge
  libffi                   3.7.0         h81df57d_1            conda-forge
  libgcc                   16.2.0        ha9f2e26_5            conda-forge
  libgcc-ng                16.2.0        h69a702a_5            conda-forge
  libgfortran              16.2.0        h69a702a_5            conda-forge
  libgfortran5             16.2.0        h6b99dfc_5            conda-forge
  libgomp                  16.2.0        he0feb66_5            conda-forge
  libidn2                  2.3.8         hfac485b_1            conda-forge
  liblapack                3.11.0        11_h47877c9_openblas  conda-forge
  liblzma                  5.8.3         hb03c661_1            conda-forge
  libmpdec                 4.0.0         hb03c661_2            conda-forge
  libnghttp2               1.68.1        h74cf4be_1            conda-forge
  libopenblas              0.3.34        pthreads_hf13c14d_2   conda-forge
  libpsl                   0.23.1        hd9e3e90_1            conda-forge
  libpython                3.14.7        hdc7f604_106_cp314    conda-forge
  libsqlite                3.53.4        h13e7031_1            conda-forge
  libssh2                  1.11.1        h6154650_1            conda-forge
  libstdcxx                16.2.0        h934c35e_5            conda-forge
  libunistring             0.9.10        h7f98852_0            conda-forge
  libuuid                  2.42.3        hcfc3c73_0            conda-forge
  libxcrypt                4.4.38        h280c20c_0            conda-forge
  libzlib                  1.3.2         h25fd6f3_3            conda-forge
  ncbi-vdb                 3.4.1         hd63eeec_0            bioconda   
  ncurses                  6.6           hdb14827_1            conda-forge
  numpy                    2.5.3         py314hd3a7d6b_0       conda-forge
  openssl                  3.6.4         h781a0a9_0            conda-forge
  pcre2                    10.47         h8b3dc9c_1            conda-forge
  perl                     5.32.1        9_h7cc23a3_perl5      conda-forge
  perl-archive-tar         3.12          pl5321hdfd78af_0      bioconda   
  perl-carp                1.50          pl5321hd8ed1ab_0      conda-forge
  perl-common-sense        3.75          pl5321hd8ed1ab_0      conda-forge
  perl-compress-raw-bzip2  2.214         pl5321hda65f42_0      conda-forge
  perl-compress-raw-zlib   2.214         pl5321h4dac143_0      conda-forge
  perl-encode              3.24          pl5321hb03c661_0      conda-forge
  perl-exporter            5.74          pl5321hd8ed1ab_0      conda-forge
  perl-exporter-tiny       1.002002      pl5321hd8ed1ab_0      conda-forge
  perl-extutils-makemaker  7.70          pl5321hd8ed1ab_0      conda-forge
  perl-io-compress         2.216         pl5321h503566f_0      bioconda   
  perl-io-zlib             1.15          pl5321hdfd78af_1      bioconda   
  perl-json                4.11          pl5321hdfd78af_0      bioconda   
  perl-json-xs             4.04          pl5321h9948957_0      bioconda   
  perl-list-moreutils      0.430         pl5321hdfd78af_0      bioconda   
  perl-list-moreutils-xs   0.430         pl5321h7b50bb2_5      bioconda   
  perl-parent              0.243         pl5321hd8ed1ab_0      conda-forge
  perl-pathtools           3.75          pl5321hb9d3cd8_2      conda-forge
  perl-scalar-list-utils   1.70          pl5321hb03c661_0      conda-forge
  perl-storable            3.15          pl5321hb9d3cd8_2      conda-forge
  perl-types-serialiser    1.01          pl5321hdfd78af_0      bioconda   
  python                   3.14.7        hcd007b5_106_cp314    conda-forge
  python-dateutil          2.9.0.post0   pyhe01879c_2          conda-forge
  python_abi               3.14          9_cp314               conda-forge
  readline                 8.3           hd6e31c0_1            conda-forge
  scipy                    1.18.1        py314h36f0660_0       conda-forge
  six                      1.17.0        pyhe01879c_1          conda-forge
  tk                       8.6.13        noxft_h1df4ec4_4      conda-forge
  tzdata                   2026c         h151e31d_0            conda-forge
  wget                     1.25.0        h653f8fd_1            conda-forge
  zlib                     1.3.2         h25fd6f3_3            conda-forge
  zstd                     1.5.7         hb78ec9c_7            conda-forge
```
</details>
</br>

Full documentation: https://github.com/MDU-PHL/emmtyper

## Example Usage

```bash
# run emmtyper in BLAST (default) mode:

emmtyper <file name(s)>.fasta -o <output_file>

# or with output written in verbose format:

emmtyper <file name(s)>.fasta -o <output_file> -f verbose

# run emmtyper in PCR mode (useful for troubleshooting, see documentation)

emmtyper -w pcr <file name(s)>.fasta -o <output_file_2> 

```