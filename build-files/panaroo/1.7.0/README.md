# Panaroo Container

Main tool : [Panaroo](https://github.com/gtonkinhill/panaroo)

<details>
<summary>Additional tools installed via micromamba:</summary> 

```
List of packages in environment: "/opt/conda"

  Name                                   Version        Build                 Channel    
───────────────────────────────────────────────────────────────────────────────────────────
  _openmp_mutex                          4.5            20_gnu                conda-forge
  alsa-lib                               1.2.16.1       hb03c661_0            conda-forge
  any2fasta                              0.8.1          hdfd78af_0            bioconda   
  aragorn                                1.2.41         h7b50bb2_5            bioconda   
  archspec                               0.2.5          pyhd8ed1ab_0          conda-forge
  argcomplete                            3.6.2          pyhd8ed1ab_0          conda-forge
  argh                                   0.31.3         pyhd8ed1ab_1          conda-forge
  argtable2                              2.13           hd590300_1004         conda-forge
  aria2                                  1.37.0         h4e1c2bf_3            conda-forge
  arpack                                 3.9.1          nompi_hf03ea27_102    conda-forge
  barrnap                                1.10.6         pl5321hdfd78af_0      bioconda   
  bedtools                               2.31.1         h13024bc_3            bioconda   
  biocode                                0.12.1         pyhdfd78af_0          bioconda   
  biopython                              1.85           py39h8cd3c5a_1        conda-forge
  blast                                  2.17.0         h66d330f_0            bioconda   
  blast-legacy                           2.2.26         hf7ff83a_5            bioconda   
  xorg-libxfixes                         6.0.2          hb03c661_0            conda-forge
  xorg-libxi                             1.8.3          hb03c661_0            conda-forge
  xorg-libxrandr                         1.5.5          hb03c661_0            conda-forge
  xorg-libxrender                        0.9.12         hb9d3cd8_0            conda-forge
  xorg-libxt                             1.3.1          hb9d3cd8_0            conda-forge
  xorg-libxtst                           1.2.5          hb9d3cd8_3            conda-forge
  xz                                     5.8.3          ha02ee65_0            conda-forge
  xz-gpl-tools                           5.8.3          ha02ee65_0            conda-forge
  xz-tools                               5.8.3          hb03c661_0            conda-forge
  ziggypep                               0.3.1          hdfd78af_0            bioconda   
  zipp                                   3.23.0         pyhd8ed1ab_0          conda-forge
  zlib                                   1.3.2          h25fd6f3_2            conda-forge
  zstandard                              0.23.0         py39hd399759_3        conda-forge
  zstd                                   1.5.7          hb78ec9c_6            conda-forge
```
</details>
</br>


Full documentation: https://gtonkinhill.github.io/panaroo/#/

Panaroo is an updated pipeline for pangenome investigation.

[Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, Gladstone RA, Lo S, Beaudoin C, Floto RA, Frost SDW, Corander J, Bentley SD, Parkhill J. 2020. Producing polished prokaryotic pangenomes with the Panaroo pipeline. Genome Biol 21:180.](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02090-4)


## Example Usage

```bash
# Using GFFs in the same format as output by Prokka run:
mkdir results
panaroo -i *.gff -o results --clean-mode strict
```
