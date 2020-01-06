# [docker-builds](#)
This repository contains the Dockerfiles and other assorted files necessary for building Docker images for a variety of programs used by members of the StaPH-B (State Public Health Lab Bioinformatics) consortium. The purpose of this repository is to provide a centralized location for Docker images that is easily accessible for users, with clear documentation on how the containers were built and how to use them.

Each Dockerfile lists author/maintainer for that specific Docker image, but the authors/maintainers of the docker images are:
  * [@kapsakcj](https://github.com/kapsakcj)
  * [@k-florek](https://github.com/k-florek)
  * [@garfinjm](https://github.com/garfinjm)
  * [@kevinlibuit](https://github.com/kevinlibuit)
  * [@Ikkik](https://github.com/Ikkik)
  * [@lskatz](https://github.com/lskatz)
  * [@stjacqrm](https://github.com/stjacqrm)
  * [@AbigailShockey](https://github.com/AbigailShockey)

If you would like to contribute with your own Docker image or perhaps improve upon the existing images, please fork the repository, make your changes/additions, and submit a pull request. If you are having an issue with an existing image, please submit an issue. We welcome any and all feedback!  
[See more details on how to contribute here](https://staph-b.github.io/docker-builds/contribute/)

## [Docker User Guide](https://staph-b.github.io/docker-builds/)
We have also created a user guide that outlines methods and best practices for using and developing docker containers.  
[Docker User Guide](https://staph-b.github.io/docker-builds/)

### What about Singularity?
For many people Docker is not an option, but Singularity is. Most Docker containers are compatible with Singularity and can easily be converted to Singularity format. Please see the User Guide linked above to for instructions on how to download docker images from dockerhub and how to run them using Singularity. We've worked hard to ensure that our containers are compatibile with Singularity, but if you find one that isn't, please leave an issue and let us know!

## [Available Docker images](https://hub.docker.com/r/staphb/)
[![Build Status](https://travis-ci.com/StaPH-B/docker-builds.svg?branch=master)](https://travis-ci.com/StaPH-B/docker-builds) (Build only reflects those containers that have been added to the TravisCI tests)

| Software | Version | Link |
| :--------: | :-------: | -------- |
| [ABRicate](https://hub.docker.com/r/staphb/abricate/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/abricate.svg?style=popout)](https://hub.docker.com/r/staphb/abricate) | 0.8.7, 0.8.13, 0.8.13s (+serotypefinder db), 0.9.8 | https://github.com/tseemann/abricate |
| [BWA](https://hub.docker.com/r/staphb/bwa) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/bwa.svg?style=popout)](https://hub.docker.com/r/staphb/bwa) | 0.7.17 | https://github.com/lh3/bwa |
| [Canu-Racon](https://hub.docker.com/r/staphb/canu-racon/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/canu-racon.svg?style=popout)](https://hub.docker.com/r/staphb/canu-racon) | 1.9 (Canu) 1.4.3 (Racon) 2.17 (minimap2); <br/> 1.9i (Canu) 1.4.3 (Racon) 2.17 (minimap2) (+racon_preprocess.py); <br/> 1.7.1 (Canu) 1.3.1 (Racon) 2.13 (minimap2) | https://canu.readthedocs.io/en/latest/ https://github.com/isovic/racon https://lh3.github.io/minimap2/ |
| [CDC-SPN](https://hub.docker.com/r/staphb/cdc-spn/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/cdc-spn.svg?style=popout)](https://hub.docker.com/r/staphb/cdc-spn) | 0.1 (no version) | https://github.com/BenJamesMetcalf/Spn_Scripts_Reference |
| [cfsan-snp-pipeline](https://hub.docker.com/r/staphb/cfsan-snp-pipeline) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/cfsan-snp-pipeline.svg?style=popout)](https://hub.docker.com/r/staphb/cfsan-snp-pipeline) | 2.0.2 | https://github.com/CFSAN-Biostatistics/snp-pipeline |
| [Circlator](https://hub.docker.com/r/staphb/circlator) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/circlator.svg?style=popout)](https://hub.docker.com/r/staphb/circlator) | 1.5.6 | https://github.com/sanger-pathogens/circlator |
| [emm-typing-tool](https://hub.docker.com/r/staphb/emm-typing-tool) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/emm-typing-tool.svg?style=popout)](https://hub.docker.com/r/staphb/emm-typing-tool) | 0.0.1 (no version) | https://github.com/phe-bioinformatics/emm-typing-tool |
| [FastANI](https://hub.docker.com/r/staphb/fastani) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/fastani.svg?style=popout)](https://hub.docker.com/r/staphb/fastani) | 1.1 | https://github.com/ParBLiSS/FastANI |
| [FastTree](https://hub.docker.com/r/staphb/fasttree) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/fasttree.svg?style=popout)](https://hub.docker.com/r/staphb/fasttree) | 2.1.11 | http://www.microbesonline.org/fasttree/ |
| [FastQC](https://hub.docker.com/r/staphb/fastqc) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/fastqc.svg?style=popout)](https://hub.docker.com/r/staphb/fastqc) | 0.11.8 | https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ |
| [Filtlong](https://hub.docker.com/r/staphb/filtlong) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/filtlong.svg?style=popout)](https://hub.docker.com/r/staphb/filtlong) | 0.2.0 | https://github.com/rrwick/filtlong |
| [Flye](https://hub.docker.com/r/staphb/flye) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/flye.svg?style=popout)](https://hub.docker.com/r/staphb/flye) | 2.5 | https://github.com/fenderglass/Flye |
| [iqtree](https://hub.docker.com/r/staphb/iqtree/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/iqtree.svg?style=popout)](https://hub.docker.com/r/staphb/iqtree) | 1.6.7 | http://www.iqtree.org/ |
| [Kraken](https://hub.docker.com/r/staphb/kraken/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/kraken.svg?style=popout)](https://hub.docker.com/r/staphb/kraken) | 1.0, 1.1.1 | https://github.com/DerrickWood/kraken |
| [kSNP3](https://hub.docker.com/r/staphb/ksnp3/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/ksnp3.svg?style=popout)](https://hub.docker.com/r/staphb/ksnp3)| 3.1 | https://sourceforge.net/projects/ksnp/ |
| [legsta](https://hub.docker.com/r/staphb/legsta/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/legsta.svg?style=popout)](https://hub.docker.com/r/staphb/legsta)| 0.3.7 | https://github.com/tseemann/legsta |
| [Lyve-SET (includes CG-Pipeline scripts and raxml)](https://hub.docker.com/r/staphb/lyveset/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/lyveset.svg?style=popout)](https://hub.docker.com/r/staphb/lyveset) | 1.1.4f, 2.0.1 (lyve-SET) | https://github.com/lskatz/lyve-SET https://github.com/lskatz/CG-Pipeline |
| [Mash](https://hub.docker.com/r/staphb/mash/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/mash.svg?style=popout)](https://hub.docker.com/r/staphb/mash)  | 2.1 | https://github.com/marbl/Mash |
| [mashtree](https://hub.docker.com/r/staphb/mashtree) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/mashtree.svg?style=popout)](https://hub.docker.com/r/staphb/mashtree) | 0.52.0, 0.57.0, 1.0.4 | https://github.com/lskatz/mashtree |
| [medaka](https://hub.docker.com/r/staphb/medaka) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/medaka.svg?style=popout)](https://hub.docker.com/r/staphb/medaka) | 0.8.1 | https://github.com/nanoporetech/medaka |
| [mlst](https://hub.docker.com/r/staphb/mlst) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/mlst.svg?style=popout)](https://hub.docker.com/r/staphb/mlst) | 2.16.2, 2.17.6 | https://github.com/tseemann/mlst |
| [Mugsy](https://hub.docker.com/r/staphb/mugsy) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/mugsy.svg?style=popout)](https://hub.docker.com/r/staphb/mugsy) | 1r2.3 | http://mugsy.sourceforge.net/ |
| [MultiQC](https://hub.docker.com/r/staphb/multiqc) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/multiqc.svg?style=popout)](https://hub.docker.com/r/staphb/multiqc) | 1.7, 1.8 | https://github.com/ewels/MultiQC |
| [NanoPlot](https://hub.docker.com/r/staphb/nanoplot) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/nanoplot.svg?style=popout)](https://hub.docker.com/r/staphb/nanoplot) | 1.27.0 | https://github.com/wdecoster/NanoPlot |
| [NCBI AMRFinderPlus](https://github.com/ncbi/amr) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/ncbi-amrfinderplus.svg?style=popout)](https://hub.docker.com/r/staphb/ncbi-amrfinderplus) | 3.1.1b | [https://github.com/ncbi/amr](https://github.com/ncbi/amr) |
| [OrthoFinder](https://hub.docker.com/r/staphb/OrthoFinder) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/orthofinder.svg?style=popout)](https://hub.docker.com/r/staphb/orthofinder) | 2.17 | https://github.com/davidemms/OrthoFinder |
| [PlasmidSeeker](https://hub.docker.com/r/staphb/plasmidseeker) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/plasmidseeker.svg?style=popout)](https://hub.docker.com/r/staphb/plasmidseeker) | 1.0 | https://github.com/bioinfo-ut/PlasmidSeeker |
| [Prokka](https://hub.docker.com/r/staphb/prokka/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/prokka.svg?style=popout)](https://hub.docker.com/r/staphb/prokka) | 1.13.4, 1.14.0, 1.14.5 | https://github.com/tseemann/prokka |
| [QUAST](https://hub.docker.com/r/staphb/quast/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/quast.svg?style=popout)](https://hub.docker.com/r/staphb/quast) | 5.0.0, 5.0.2 | https://github.com/ablab/quast |
| [rasusa](https://hub.docker.com/r/staphb/rasusa/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/rasusa.svg?style=popout)](https://hub.docker.com/r/staphb/rasusa) | 0.1.0 | https://github.com/mbhall88/rasusa |
| [RAxML](https://hub.docker.com/r/staphb/raxml/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/raxml.svg?style=popout)](https://hub.docker.com/r/staphb/raxml) | 8.2.12 (RAxML) <br/> 0.9.0 (RAxML Next Generation) | https://github.com/stamatak/standard-RAxML <br/> https://github.com/amkozlov/raxml-ng |
| [Roary](https://hub.docker.com/r/staphb/roary/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/roary.svg?style=popout)](https://hub.docker.com/r/staphb/roary) | 3.12.0 | https://github.com/sanger-pathogens/Roary |
| [SalmID](https://hub.docker.com/r/staphb/salmid) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/salmid.svg?style=popout)](https://hub.docker.com/r/staphb/salmid) | 0.1.23 | https://github.com/hcdenbakker/SalmID |
| [Samtools](https://hub.docker.com/r/staphb/samtools) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/samtools.svg?style=popout)](https://hub.docker.com/r/staphb/samtools) | 1.9, 1.10 | https://github.com/samtools/samtools |
| [SeqSero](https://hub.docker.com/r/staphb/seqsero/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seqsero.svg?style=popout)](https://hub.docker.com/r/staphb/seqsero) | 1.0.1 | https://github.com/denglab/SeqSero |
| [SeqSero2](https://hub.docker.com/r/staphb/seqsero2/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seqsero2.svg?style=popout)](https://hub.docker.com/r/staphb/seqsero2) | 0.1.0, 1.0.0 | https://github.com/denglab/SeqSero2/ |
| [seqyclean](https://hub.docker.com/r/staphb/seqyclean) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seqyclean.svg?style=popout)](https://hub.docker.com/r/staphb/seqyclean) | 1.10.09 | https://github.com/ibest/seqyclean |
| [Seroba](https://hub.docker.com/r/staphb/seroba) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/seroba.svg?style=popout)](https://hub.docker.com/r/staphb/seroba) | 1.0.0 | https://github.com/sanger-pathogens/seroba |
| [SerotypeFinder](https://hub.docker.com/r/staphb/serotypefinder/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/serotypefinder.svg?style=popout)](https://hub.docker.com/r/staphb/serotypefinder) | 1.1 (I think? Bitbucket repo does not list older versions like the one in this docker image) | https://bitbucket.org/genomicepidemiology/serotypefinder/ |
| [Shovill](https://hub.docker.com/r/staphb/shovill/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/shovill.svg?style=popout)](https://hub.docker.com/r/staphb/shovill) | 1.0.4 | https://github.com/tseemann/shovill |
| [SISTR](https://hub.docker.com/r/staphb/sistr/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/sistr.svg?style=popout)](https://hub.docker.com/r/staphb/sistr) | 1.0.2 | https://github.com/peterk87/sistr_cmd |
| [SKESA](https://hub.docker.com/r/staphb/skesa) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/skesa.svg?style=popout)](https://hub.docker.com/r/staphb/skesa) | 2.3.0 | https://github.com/ncbi/SKESA |
| [Snippy](https://hub.docker.com/r/staphb/snippy) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/snippy.svg?style=popout)](https://hub.docker.com/r/staphb/snippy) | 4.4.5 | https://github.com/tseemann/snippy |
| [snp-dists](https://hub.docker.com/r/staphb/snp-dists) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/snp-dists.svg?style=popout)](https://hub.docker.com/r/staphb/snp-dists) | 0.6.2 | https://github.com/tseemann/snp-dists |
| [SPAdes](https://hub.docker.com/r/staphb/spades/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/spades.svg?style=popout)](https://hub.docker.com/r/staphb/spades) | 3.12.0, 3.13.0, 3.14.0 | http://cab.spbu.ru/software/spades/ |
| [SRA-toolkit](https://hub.docker.com/r/staphb/sratoolkit/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/sratoolkit.svg?style=popout)](https://hub.docker.com/r/staphb/sratoolkit) | 2.9.2 | https://github.com/ncbi/sra-tools |
| [Staramr](https://hub.docker.com/r/staphb/staramr/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/staramr.svg?style=popout)](https://hub.docker.com/r/staphb/staramr) | 0.5.1 | https://github.com/phac-nml/staramr |
| [TipToft](https://hub.docker.com/r/staphb/tiptoft/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/tiptoft.svg?style=popout)](https://hub.docker.com/r/staphb/tiptoft) | 1.0.0 | https://github.com/andrewjpage/tiptoft |
| [Trimmomatic](https://hub.docker.com/r/staphb/trimmomatic/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/trimmomatic.svg?style=popout)](https://hub.docker.com/r/staphb/trimmomatic) | 0.38, 0.39 | http://www.usadellab.org/cms/?page=trimmomatic |
| [Unicycler](https://hub.docker.com/r/staphb/unicycler/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/unicycler.svg?style=popout)](https://hub.docker.com/r/staphb/unicycler) | 0.4.7 | https://github.com/rrwick/Unicycler |
| [wtdbg2](https://hub.docker.com/r/staphb/wtdbg2/) <br/> [![docker pulls](https://img.shields.io/docker/pulls/staphb/wtdbg2.svg?style=popout)](https://hub.docker.com/r/staphb/wtdbg2) | 2.5 | https://github.com/ruanjue/wtdbg2 |

You can also view the list of images on Docker hub here: https://hub.docker.com/r/staphb/
