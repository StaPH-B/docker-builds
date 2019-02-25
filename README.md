# [docker-builds](#)
This repository contains the Dockerfiles and other assorted files necessary for building Docker images for a variety of programs used by members of the StaPH-B (State Public Health Lab Bioinformatics) consortium. The purpose of this repository is to provide a centralized location for Docker images that is easily accessible for users, with clear documentation on how the containers were built and how to use them.

Each Dockerfile lists author/maintainer for that specific Docker image, but the authors/maintainers of the docker images are:
  * [@kapsakcj](https://github.com/kapsakcj)
  * [@nwflorek](https://github.com/nwflorek)
  * [@garfinjm](https://github.com/garfinjm)
  * [@kevinlibuit](https://github.com/kevinlibuit)

If you would like to contribute with your own Docker image or perhaps improve upon the existing images, please fork the repository, make your changes/additions, and submit a pull request. If you are having an issue with an existing image, please submit an issue. We welcome any and all feedback!  
[See more details on how to contribute here](https://staph-b.github.io/docker-builds/contribute/)

## [Docker User Guide](https://staph-b.github.io/docker-builds/)
We have also created a user guide that outlines methods and best practices for using and developing docker containers.  
[Docker User Guide](https://staph-b.github.io/docker-builds/)

## [Available Docker images](https://hub.docker.com/r/staphb/)
| Software | Version | Link |
| :--------: | :-------: | -------- |
| [SRA-toolkit](https://hub.docker.com/r/staphb/sratoolkit/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/sratoolkit.svg?style=popout)](https://hub.docker.com/r/staphb/sratoolkit) | 2.9.2 | https://github.com/ncbi/sra-tools |
| [Lyve-SET (includes CG-Pipeline scripts and raxml)](https://hub.docker.com/r/staphb/lyveset/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/lyveset.svg?style=popout)](https://hub.docker.com/r/staphb/lyveset) | 1.1.4f, 2.0.1 (lyve-SET) | https://github.com/lskatz/lyve-SET https://github.com/lskatz/CG-Pipeline |
| [Kraken](https://hub.docker.com/r/staphb/kraken/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/kraken.svg?style=popout)](https://hub.docker.com/r/staphb/kraken) | 1.0 | https://github.com/DerrickWood/kraken |
| [SPAdes](https://hub.docker.com/r/staphb/spades/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/spades.svg?style=popout)](https://hub.docker.com/r/staphb/spades) | 3.12.0, 3.13.0 | http://cab.spbu.ru/software/spades/ |
| [QUAST](https://hub.docker.com/r/staphb/quast/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/quast.svg?style=popout)](https://hub.docker.com/r/staphb/quast) | 5.0.0 | https://github.com/ablab/quast |
|  [Mash](https://hub.docker.com/r/staphb/mash/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/mash.svg?style=popout)](https://hub.docker.com/r/staphb/mash)  | 2.1 | https://github.com/marbl/Mash |
| [SerotypeFinder](https://hub.docker.com/r/staphb/serotypefinder/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/serotypefinder.svg?style=popout)](https://hub.docker.com/r/staphb/serotypefinder) | 1.1 (I think? Bitbucket repo does not list older versions like the one in this docker image) | https://bitbucket.org/genomicepidemiology/serotypefinder/ |
| [SeqSero](https://hub.docker.com/r/staphb/seqsero/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seqsero.svg?style=popout)](https://hub.docker.com/r/staphb/seqsero) | 1.0.1 | https://github.com/denglab/SeqSero |
| [SeqSero2](https://hub.docker.com/r/staphb/seqsero2/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seqsero2.svg?style=popout)](https://hub.docker.com/r/staphb/seqsero2) | 0.1.0 | https://github.com/denglab/SeqSero2/ |
| [SISTR](https://hub.docker.com/r/staphb/sistr/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/sistr.svg?style=popout)](https://hub.docker.com/r/staphb/sistr) | 1.0.2 | https://github.com/peterk87/sistr_cmd |
| [ABRicate](https://hub.docker.com/r/staphb/abricate/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/abricate.svg?style=popout)](https://hub.docker.com/r/staphb/abricate) | 0.8.7 | https://github.com/tseemann/abricate |
| [Prokka](https://hub.docker.com/r/staphb/prokka/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/prokka.svg?style=popout)](https://hub.docker.com/r/staphb/prokka) | 1.13 | https://github.com/tseemann/prokka |
| [Trimmomatic](https://hub.docker.com/r/staphb/trimmomatic/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/trimmomatic.svg?style=popout)](https://hub.docker.com/r/staphb/trimmomatic) | 0.38 | http://www.usadellab.org/cms/?page=trimmomatic |
| [iqtree](https://hub.docker.com/r/staphb/iqtree/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/iqtree.svg?style=popout)](https://hub.docker.com/r/staphb/iqtree) | 1.6.7 | http://www.iqtree.org/ |
| [Unicycler](https://hub.docker.com/r/staphb/unicycler/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/unicycler.svg?style=popout)](https://hub.docker.com/r/staphb/unicycler) | 0.4.7 | https://github.com/rrwick/Unicycler |
| [Canu-Racon](https://hub.docker.com/r/staphb/canu-racon/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/canu-racon.svg?style=popout)](https://hub.docker.com/r/staphb/canu-racon) | 1.7.1 (Canu) 1.3.1 (Racon) 2.13 (minimap2) | https://canu.readthedocs.io/en/latest/ https://github.com/isovic/racon https://lh3.github.io/minimap2/ |
|[Roary](https://hub.docker.com/r/staphb/roary/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/roary.svg?style=popout)](https://hub.docker.com/r/staphb/roary) | 3.12.0 | https://github.com/sanger-pathogens/Roary |
|[CDC-SPN](https://hub.docker.com/r/staphb/cdc-spn/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/cdc-spn.svg?style=popout)](https://hub.docker.com/r/staphb/cdc-spn) | 0.1 (no version) | https://github.com/BenJamesMetcalf/Spn_Scripts_Reference |
| [Shovill](https://hub.docker.com/r/staphb/shovill/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/shovill.svg?style=popout)](https://hub.docker.com/r/staphb/shovill) | 1.0.4 | https://github.com/tseemann/shovill |
| [BWA](https://hub.docker.com/r/staphb/bwa) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/bwa.svg?style=popout)](https://hub.docker.com/r/staphb/bwa) | 0.7.17 | https://github.com/lh3/bwa |
| [Samtools](https://hub.docker.com/r/staphb/samtools) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/samtools.svg?style=popout)](https://hub.docker.com/r/staphb/samtools) | 1.9 | https://github.com/samtools/samtools |
| [cfsan-snp-pipeline](https://hub.docker.com/r/staphb/cfsan-snp-pipeline) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/cfsan-snp-pipeline.svg?style=popout)](https://hub.docker.com/r/staphb/cfsan-snp-pipeline) | 2.0.2 | https://github.com/CFSAN-Biostatistics/snp-pipeline |

You can also view the list of images on Docker hub here: https://hub.docker.com/r/staphb/
