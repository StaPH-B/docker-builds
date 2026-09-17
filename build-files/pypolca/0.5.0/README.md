# pypolca container

Main tool: [pypolca](https://github.com/gbouras13/pypolca)
  
Code repository: https://github.com/gbouras13/pypolca

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name              Version       Build                 Channel    
─────────────────────────────────────────────────────────────────────
  _openmp_mutex     4.5           20_gnu                conda-forge
  biopython         1.88          py314h89acca1_1       conda-forge
  bwa               0.7.19        h577a1d6_1            bioconda   
  bzip2             1.0.8         hda65f42_10           conda-forge
  c-ares            1.34.8        hebe6cf0_2            conda-forge
  ca-certificates   2026.7.22     hbd8a1cb_0            conda-forge
  click             8.5.0         pyh5ded981_0          conda-forge
  fastahack         2016.07.2     h4ac6f70_6            bioconda   
  freebayes         1.3.10        h3752d28_1            bioconda   
  htslib            1.24          ha79157c_0            bioconda   
  icu               78.3          py310h44b86e0_2       conda-forge
  keyutils          1.6.3         h7cc23a3_1            conda-forge
  krb5              1.22.2        hbc21106_2            conda-forge
  ld_impl_linux-64  2.46.1        default_hbd61a6d_102  conda-forge
  libblas           3.11.0        11_h4a7cf45_openblas  conda-forge
  libcblas          3.11.0        11_h0358290_openblas  conda-forge
  libcurl           8.22.0        ha042cf0_0            conda-forge
  libdeflate        1.25          hd45a770_1            conda-forge
  libedit           3.1.20250104  pl5321h373387f_1      conda-forge
  libev             4.33          h280c20c_3            conda-forge
  libexpat          2.8.1         hecca717_1            conda-forge
  libffi            3.7.0         h81df57d_1            conda-forge
  libgcc            16.2.0        ha9f2e26_5            conda-forge
  libgcc-ng         16.2.0        h69a702a_5            conda-forge
  libgfortran       16.2.0        h69a702a_5            conda-forge
  libgfortran5      16.2.0        h6b99dfc_5            conda-forge
  libgomp           16.2.0        he0feb66_5            conda-forge
  libidn2           2.3.8         hfac485b_1            conda-forge
  liblapack         3.11.0        11_h47877c9_openblas  conda-forge
  liblzma           5.8.3         hb03c661_1            conda-forge
  libmpdec          4.0.0         hb03c661_2            conda-forge
  libnghttp2        1.68.1        h74cf4be_1            conda-forge
  libopenblas       0.3.34        pthreads_hf13c14d_2   conda-forge
  libpsl            0.23.1        hd9e3e90_1            conda-forge
  libpython         3.14.7        hdc7f604_106_cp314    conda-forge
  libsqlite         3.53.4        h13e7031_1            conda-forge
  libssh2           1.11.1        h6154650_1            conda-forge
  libstdcxx         16.2.0        h934c35e_5            conda-forge
  libstdcxx-ng      16.2.0        hdf11a46_5            conda-forge
  libunistring      0.9.10        h7f98852_0            conda-forge
  libuuid           2.42.3        hcfc3c73_0            conda-forge
  libxcrypt         4.4.38        h280c20c_0            conda-forge
  libzlib           1.3.2         h25fd6f3_3            conda-forge
  loguru            0.7.3         pyh707e725_0          conda-forge
  ncurses           6.6           hdb14827_1            conda-forge
  numpy             2.5.3         py314hd3a7d6b_0       conda-forge
  openssl           3.6.4         h781a0a9_0            conda-forge
  pandas            3.0.5         py314hb4ffadd_1       conda-forge
  parallel          20260722      hd8ed1ab_0            conda-forge
  pcre2             10.47         h8b3dc9c_1            conda-forge
  perl              5.32.1        9_h7cc23a3_perl5      conda-forge
  pypolca           0.5.0         pyhdfd78af_0          bioconda   
  python            3.14.7        hcd007b5_106_cp314    conda-forge
  python-dateutil   2.9.0.post0   pyhe01879c_2          conda-forge
  python_abi        3.14          9_cp314               conda-forge
  pyyaml            6.0.3         py314h67df5f8_1       conda-forge
  readline          8.3           hd6e31c0_1            conda-forge
  samtools          1.24          h9dcdb79_1            bioconda   
  seqlib            1.2.0         hbefcdb2_0            bioconda   
  six               1.17.0        pyhe01879c_1          conda-forge
  tabixpp           1.1.2         hbefcdb2_4            bioconda   
  tk                8.6.13        noxft_h1df4ec4_4      conda-forge
  tzdata            2026c         h151e31d_0            conda-forge
  vcflib            1.0.15        h3fa9d83_1            bioconda   
  wget              1.25.0        h653f8fd_1            conda-forge
  yaml              0.2.5         hebe6cf0_3            conda-forge
  zlib              1.3.2         h25fd6f3_3            conda-forge
  zstd              1.5.7         hb78ec9c_7            conda-forge
```

</details>

Basic information on how to use this tool:
- executable: pypolca
- help: pypolca -h
- version: pypolca -v
- description: Polished long-read assemblies with Illumina reads

> pypolca is a Standalone Python re-implementation of the POLCA polisher from the MaSuRCA genome assembly and analysis toolkit.
  
Full documentation: [https://github.com/rrwick/Polypolish](https://github.com/rrwick/Polypolish)

## Example Usage

```bash
pypolca run -a assembly.fasta -1 R1.fastq.gz -2 R2.fastq.gz -t 4 -o output 
```
