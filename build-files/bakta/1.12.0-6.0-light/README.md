# bakta container

Main tool: [bakta](https://github.com/oschwengers/bakta)

<details>
<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name                     Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────────
  _openmp_mutex            4.5           20_gnu                conda-forge
  about-time               4.2.1         pyhd8ed1ab_1          conda-forge
  alive-progress           3.0.1         pyhd8ed1ab_0          conda-forge
  aragorn                  1.2.41        h7b50bb2_5            bioconda   
  perl-io-zlib             1.15          pl5321hdfd78af_1      bioconda   
  perl-json                4.10          pl5321hdfd78af_1      bioconda   
  perl-json-xs             4.04          pl5321h9948957_0      bioconda   
  perl-list-moreutils      0.430         pl5321hdfd78af_0      bioconda   
  perl-list-moreutils-xs   0.430         pl5321h7b50bb2_5      bioconda   
  perl-parent              0.243         pl5321hd8ed1ab_0      conda-forge
  perl-pathtools           3.75          pl5321hb9d3cd8_2      conda-forge
  perl-scalar-list-utils   1.70          pl5321hb03c661_0      conda-forge
  perl-storable            3.15          pl5321hb9d3cd8_2      conda-forge
  perl-types-serialiser    1.01          pl5321hdfd78af_0      bioconda   
  pigz                     2.8           h421ea60_2            conda-forge
  piler-cr                 1.06          h9948957_6            bioconda   
  pillow                   12.1.1        py313h80991f8_0       conda-forge
  pip                      26.0.1        pyh145f28c_0          conda-forge
  psutil                   7.2.2         py313h54dd161_0       conda-forge
  pthread-stubs            0.4           hb9d3cd8_1002         conda-forge
  pycirclize               1.10.1        pyhd8ed1ab_0          conda-forge
  pycparser                2.22          pyh29332c3_1          conda-forge
  pyhmmer                  0.12.0        py313h8c92656_1       bioconda   
  pyparsing                3.3.2         pyhcf101f3_0          conda-forge
  pyrodigal                3.7.1         py313h8c92656_1       bioconda   
  pysocks                  1.7.1         pyha55dd90_7          conda-forge
  python                   3.13.12       hc97d973_100_cp313    conda-forge
  python-dateutil          2.9.0.post0   pyhe01879c_2          conda-forge
  python-isal              1.8.0         py313h07c4f96_1       conda-forge
  python-zlib-ng           1.0.0         py313ha345abf_1       conda-forge
  python_abi               3.13          8_cp313               conda-forge
  pyyaml                   6.0.3         py313h3dea7bd_1       conda-forge
  qhull                    2020.2        h434a139_5            conda-forge
  readline                 8.3           h853b02a_0            conda-forge
  requests                 2.32.5        pyhcf101f3_1          conda-forge
  six                      1.17.0        pyhe01879c_1          conda-forge
  tk                       8.6.13        noxft_h366c992_103    conda-forge
  trnascan-se              2.0.12        pl5321h7b50bb2_2      bioconda   
  tzdata                   2025c         hc9c84f9_1            conda-forge
  urllib3                  2.6.3         pyhd8ed1ab_0          conda-forge
  wget                     1.25.0        h653f8fd_1            conda-forge
  xopen                    2.0.2         pyh707e725_2          conda-forge
  xorg-libxau              1.0.12        hb03c661_1            conda-forge
  xorg-libxdmcp            1.1.5         hb03c661_1            conda-forge
  yaml                     0.2.5         h280c20c_3            conda-forge
  zlib                     1.3.1         hb9d3cd8_2            conda-forge
  zlib-ng                  2.3.3         hceb46e0_1            conda-forge
  zstandard                0.25.0        py313h54dd161_1       conda-forge
  zstd                     1.5.7         hb78ec9c_6            conda-forge
```
</details>
</br>

Code repository: https://github.com/oschwengers/bakta

Basic information on how to use this tool:
- executable: bakta
- help: -h
- version: -v
- description: Annotates bacterial genomes

> Bakta is a tool for the rapid & standardized annotation of bacterial genomes and plasmids from both isolates and MAGs. It provides dbxref-rich, sORF-including and taxon-independent annotations in machine-readable JSON & bioinformatics standard file formats for automated downstream analysis.

Additional information:

This image contains the version 6.0 light database. It is located in /db/db-light and set as BAKTA_DB so that --db doesn't have to be used.

Full documentation: https://github.com/oschwengers/bakta/

Example Usage
```bash
bakta sample.fasta --threads 20 --prefix sample 
```
