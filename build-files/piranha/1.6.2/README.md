# piranha container

Main tool : [piranha](https://github.com/polio-nanopore/piranha)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/piranha"

  Name                                   Version       Build                         Channel    
──────────────────────────────────────────────────────────────────────────────────────────────────
  Mako                                   1.2.0         pypi_0                        pypi       
  _openmp_mutex                          5.1           52_gnu                        pkgs/main  
  alsa-lib                               1.2.16.1      hb03c661_0                    conda-forge
  appdirs                                1.4.4         pyhd8ed1ab_1                  conda-forge
  argparse-dataclass                     2.0.0         pyhd8ed1ab_1                  conda-forge
  attrs                                  26.1.0        pyhcf101f3_0                  conda-forge
  aws-c-auth                             0.10.1        ha62d5e7_3                    conda-forge
  aws-c-cal                              0.9.13        h2c9d079_1                    conda-forge
  aws-c-common                           0.12.6        hb03c661_0                    conda-forge
  aws-c-compression                      0.3.2         h8b1a151_0                    conda-forge
  aws-c-http                             0.10.13       h4bacb7b_0                    conda-forge
  aws-c-io                               0.26.3        hb18f61d_2                    conda-forge
  aws-c-s3                               0.12.0        h1b28b03_1                    pkgs/main  
  aws-c-sdkutils                         0.2.4         h8b1a151_4                    conda-forge
  aws-checksums                          0.2.10        h8b1a151_0                    conda-forge
  backports.zstd                         1.6.0         py312h90b7ffd_0               conda-forge
#14 1.080   tabix                                  1.11          hdfd78af_0                    bioconda   
#14 1.080   tabixpp                                1.1.2         hbefcdb2_4                    bioconda   
#14 1.080   tabulate                               0.10.0        pyhcf101f3_0                  conda-forge
#14 1.080   tar                                    1.35          h3b78370_0                    conda-forge
#14 1.080   tenacity                               9.1.4         pyhcf101f3_0                  conda-forge
#14 1.080   tensordict                             0.1.2         pyh6074d0b_0                  conda-forge
#14 1.080   throttler                              1.2.2         pyhd8ed1ab_0                  conda-forge
#14 1.080   tk                                     8.6.13        noxft_h366c992_103            conda-forge
#14 1.080   toml                                   0.10.2        pyhcf101f3_3                  conda-forge
#14 1.080   tqdm                                   4.68.3        pyh8f84b5b_0                  conda-forge
#14 1.080   traitlets                              5.15.1        pyhcf101f3_0                  conda-forge
#14 1.080   typing-extensions                      4.15.0        h396c80c_0                    conda-forge
#14 1.080   typing_extensions                      4.15.0        pyhcf101f3_0                  conda-forge
#14 1.080   tzdata                                 2025c         hc9c84f9_1                    conda-forge
#14 1.080   urllib3                                2.7.0         pyhd8ed1ab_0                  conda-forge
#14 1.080   vcflib                                 1.0.15        h3fa9d83_1                    bioconda   
#14 1.080   wget                                   1.25.0        h653f8fd_1                    conda-forge
#14 1.080   wheel                                  0.47.0        pyhd8ed1ab_0                  conda-forge
#14 1.080   wrapt                                  1.17.0        py312h5eee18b_0               pkgs/main  
#14 1.080   wurlitzer                              3.1.1         pyhd8ed1ab_1                  conda-forge
#14 1.080   xorg-libice                            1.1.2         hb9d3cd8_0                    conda-forge
#14 1.080   xorg-libsm                             1.2.6         he73a12e_0                    conda-forge
#14 1.080   xorg-libx11                            1.8.13        he1eb515_0                    conda-forge
#14 1.080   xorg-libxau                            1.0.12        hb03c661_1                    conda-forge
#14 1.080   xorg-libxdmcp                          1.1.5         hb03c661_1                    conda-forge
#14 1.080   xorg-libxext                           1.3.7         hb03c661_0                    conda-forge
#14 1.080   xorg-libxfixes                         6.0.2         hb03c661_0                    conda-forge
#14 1.080   xorg-libxi                             1.8.3         hb03c661_0                    conda-forge
#14 1.080   xorg-libxrandr                         1.5.5         hb03c661_0                    conda-forge
#14 1.080   xorg-libxrender                        0.9.12        hb9d3cd8_0                    conda-forge
#14 1.080   xorg-libxt                             1.3.1         hb9d3cd8_0                    conda-forge
#14 1.080   xorg-libxtst                           1.2.5         hb9d3cd8_3                    conda-forge
#14 1.080   yaml                                   0.2.5         h280c20c_3                    conda-forge
#14 1.080   yte                                    1.9.4         pyhd8ed1ab_0                  conda-forge
#14 1.080   zlib                                   1.3.2         h25fd6f3_2                    conda-forge
#14 1.080   zstd                                   1.5.7         hb78ec9c_6                    conda-forge
```

</details>


Full documentation: [https://github.com/polio-nanopore/piranha](https://github.com/polio-nanopore/piranha)

> Poliovirus Investigation Resource Automating Nanopore Haplotype Analysis. <br><br> piranha is a tool in development as part of the Poliovirus Sequencing Consortium. It runs an automated analysis pipeline for sequencing VP1 regions of the poliovirus or non-polio enterovirus genome (whole genome analysis to be implemented soon) and produces an interactive report alongside the consensus data.

## Example Usage

```bash
# run Piranha on a directory of FASTQs (Guppy output)
piranha -i /piranha/test/pak_run/demultiplexed --verbose -b piranha/test/pak_run/barcodes01.csv -t 2 2>&1 | tee piranha.log
```
