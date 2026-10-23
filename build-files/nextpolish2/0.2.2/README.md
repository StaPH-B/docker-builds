# NextPolish2 container

Main tool: [NextPolish2](https://github.com/Nextomics/NextPolish2)
  
Code repository: https://github.com/Nextomics/NextPolish2

Additional tools:
- yak: 0.1-r69
- meryl: 1.4.2
- winnowmap: 2.03
- samtools: 1.24
- minimap2: 2.31-r1302

<details><summary>Tools installed via micromamba:</summary>

```
  Name                     Version       Build             Channel    
────────────────────────────────────────────────────────────────────────
  _openmp_mutex            4.5           20_gnu            conda-forge
  bzip2                    1.0.8         hda65f42_10       conda-forge
  c-ares                   1.34.8        hebe6cf0_2        conda-forge
  ca-certificates          2026.7.22     hbd8a1cb_0        conda-forge
  htslib                   1.24          ha79157c_0        bioconda   
  icu                      78.3          py310h44b86e0_2   conda-forge
  k8                       1.2           he8db53b_6        bioconda   
  kernel-headers_linux-64  5.14.0        he073ed8_3        conda-forge
  keyutils                 1.6.3         h7cc23a3_1        conda-forge
  krb5                     1.22.2        hbc21106_2        conda-forge
  libcurl                  8.22.0        ha042cf0_0        conda-forge
  libdeflate               1.26          h351257e_0        conda-forge
  libedit                  3.1.20250104  pl5321h373387f_1  conda-forge
  libev                    4.33          h280c20c_3        conda-forge
  libgcc                   16.2.0        ha9f2e26_7        conda-forge
  libgomp                  16.2.0        he0feb66_7        conda-forge
  liblzma                  5.8.3         hb03c661_1        conda-forge
  libnghttp2               1.68.1        h74cf4be_1        conda-forge
  libpsl                   0.23.1        hd9e3e90_1        conda-forge
  libssh2                  1.11.1        h6154650_1        conda-forge
  libstdcxx                16.2.0        h934c35e_7        conda-forge
  libzlib                  1.3.2         h25fd6f3_3        conda-forge
  meryl                    1.4.2         hd19868c_0        bioconda   
  minimap2                 2.31          h118bc1c_0        bioconda   
  ncurses                  6.6           hdb14827_1        conda-forge
  nextpolish2              0.2.2         h74ec884_0        bioconda   
  openssl                  3.6.4         h781a0a9_0        conda-forge
  samtools                 1.24          h9dcdb79_1        bioconda   
  sysroot_linux-64         2.34          h087de78_3        conda-forge
  tzdata                   2026c         h151e31d_0        conda-forge
  winnowmap                2.03          h5ca1c30_4        bioconda   
  yak                      0.1           h577a1d6_6        bioconda   
  zstd                     1.5.7         hb78ec9c_7        conda-forge
```
</details><br>

Basic information on how to use this tool:
- executable: `nextPolish2`
- help: `-h`, `--help `
- version: `-V`, `--version`
- description: Repeat-aware polishing tool for genomes assembled using PacBio HiFi long reads

Additional information:

Jiang Hu, Zhuo Wang, Fan Liang, Shan-Lin Liu, Kai Ye, De-Peng Wang, NextPolish2: A Repeat-aware Polishing Tool for Genomes Assembled Using HiFi Long Reads, Genomics, Proteomics & Bioinformatics, 2024, qzad009, https://doi.org/10.1093/gpbjnl/qzad009
  
Full documentation: https://github.com/Nextomics/NextPolish2

## Example Usage

```bash
nextPolish2 -t 5 hifi.map.sort.bam asm.fa.gz k21.yak k31.yak > asm.np2.fa
```

 