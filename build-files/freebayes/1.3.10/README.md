# FreeBayes Container

Main Tool: [FreeBayes](https://arxiv.org/abs/1207.3907)

Code repository: https://github.com/freebayes/freebayes 

Basic information on how to use this tool:
- executable: `freebayes`
- help: `-h`, `--help`
- version: `--version`
- description: FreeBayes is a haplotype-based variant detector and is a great tool for calling variants from a population.

>FreeBayes is a Bayesian genetic variant detector designed to find small polymorphisms, specifically SNPs (single-nucleotide polymorphisms), indels (insertions and deletions), MNPs (multi-nucleotide polymorphisms), and complex events (composite insertion and substitution events) smaller than the length of a short-read sequencing alignment.
>FreeBayes is haplotype-based, in the sense that it calls variants based on the literal sequences of reads aligned to a particular target, not their precise alignment. This model is a straightforward generalization of previous ones (e.g. PolyBayes, samtools, GATK) which detect or report variants based on alignments. This method avoids one of the core problems with alignment-based variant detection — that identical sequences may have multiple possible alignments

<details>
<summary>Additional tools installed via micromamba:</summary>

```
  Name              Version       Build               Channel    
───────────────────────────────────────────────────────────────────
  _libgcc_mutex     0.1           conda_forge         conda-forge
  _openmp_mutex     4.5           2_gnu               conda-forge
  bzip2             1.0.8         h4bc722e_7          conda-forge
  c-ares            1.34.5        hb9d3cd8_0          conda-forge
  ca-certificates   2025.7.14     hbd8a1cb_0          conda-forge
  fastahack         2016.07.2     h4ac6f70_6          bioconda   
  freebayes         1.3.10        hbefcdb2_0          bioconda   
  htslib            1.22.1        h566b1c6_0          bioconda   
  icu               75.1          he02047a_0          conda-forge
  keyutils          1.6.1         h166bdaf_0          conda-forge
  krb5              1.21.3        h659f571_0          conda-forge
  ld_impl_linux-64  2.44          h1423503_1          conda-forge
  libasprintf       0.25.1        h8e693c7_0          conda-forge
  libcurl           8.14.1        h332b0f4_0          conda-forge
  libdeflate        1.22          hb9d3cd8_0          conda-forge
  libedit           3.1.20250104  pl5321h7949ede_0    conda-forge
  libev             4.33          hd590300_2          conda-forge
  libexpat          2.7.1         hecca717_0          conda-forge
  libffi            3.4.6         h2dba641_1          conda-forge
  libgcc            15.1.0        h767d61c_3          conda-forge
  libgcc-ng         15.1.0        h69a702a_3          conda-forge
  libgettextpo      0.25.1        h5888daf_0          conda-forge
  libgomp           15.1.0        h767d61c_3          conda-forge
  libidn2           2.3.8         ha4ef2c3_0          conda-forge
  liblzma           5.8.1         hb9d3cd8_2          conda-forge
  libmpdec          4.0.0         hb9d3cd8_0          conda-forge
  libnghttp2        1.64.0        h161d5f1_0          conda-forge
  libsqlite         3.50.3        hee844dc_0          conda-forge
  libssh2           1.11.1        hcf80075_0          conda-forge
  libstdcxx         15.1.0        h8f9b012_3          conda-forge
  libstdcxx-ng      15.1.0        h4852527_3          conda-forge
  libunistring      0.9.10        h7f98852_0          conda-forge
  libuuid           2.38.1        h0b41bf4_0          conda-forge
  libxcrypt         4.4.36        hd590300_1          conda-forge
  libzlib           1.3.1         hb9d3cd8_2          conda-forge
  ncurses           6.5           h2d0b736_3          conda-forge
  openssl           3.5.1         h7b32b05_0          conda-forge
  parallel          20250622      ha770c72_0          conda-forge
  perl              5.32.1        7_hd590300_perl5    conda-forge
  pip               25.1.1        pyh145f28c_0        conda-forge
  python            3.13.5        hec9711d_102_cp313  conda-forge
  python_abi        3.13          8_cp313             conda-forge
  readline          8.2           h8c095d6_2          conda-forge
  samtools          1.22.1        h96c455f_0          bioconda   
  seqlib            1.2.0         hbefcdb2_0          bioconda   
  tabixpp           1.1.2         hbefcdb2_4          bioconda   
  tk                8.6.13        noxft_hd72426e_102  conda-forge
  tzdata            2025b         h78e105d_0          conda-forge
  vcflib            1.0.14        h34261f4_0          bioconda   
  wget              1.21.4        hda4d442_0          conda-forge
  zlib              1.3.1         hb9d3cd8_2          conda-forge
  zstd              1.5.7         hb8e6e7a_2          conda-forge
```

</details>
</br>

Full documentation: [Garrison, E., & Marth, G. (2012). Haplotype-based variant detection from short-read sequencing. ArXiv.org.](https://arxiv.org/abs/1207.3907)

## Example Usage
```bash
# basic usage
freebayes -f [REFERENCE] [OPTIONS] [BAM FILES] > [OUTPUT]

# example 
freebayes --bam Sample_1_sorted.bam --ploidy 1 --fasta-reference reference.fasta --vcf Sample1_freebayes.vcf
```


