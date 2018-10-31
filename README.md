# docker-auto-builds
This repo contains the Dockerfiles and other assorted files necessary for building Docker images/containers for a variety of programs used by members of the StaPH-B (State Public Health Lab Bioinformatics) consortium. The purpose of this repo is to provide a centralized location for Docker images that is easily accessible for users, with clear documentation on how the containers were built and how to use them.

Each Dockerfile lists author/maintainer for that specific Docker image, but the authors/maintainers of the docker images are:
  * [@kapsakcj](https://github.com/kapsakcj)
  * [@nwflorek](https://github.com/nwflorek)

If you would like to contribute with your own Docker image or perhaps improve upon the existing containers, please submit a pull request (or an issue). We welcome any and all feedback!

## Available Docker images
| Software | Version | Link |
| -------- | ------- | -------- |
| [SRA-toolkit](https://hub.docker.com/r/staphb/sratoolkit-v2.9.2/) | 2.9.2 | https://github.com/ncbi/sra-tools |
| [Lyve-SET (includes CG-Pipeline scripts and raxml)](https://hub.docker.com/r/staphb/lyveset-v2.0/) | 2.0.1 (lyve-SET) | https://github.com/lskatz/lyve-SET https://github.com/lskatz/CG-Pipeline |
| [Kraken]() | 1.0 | https://github.com/DerrickWood/kraken |
| [SPAdes](https://hub.docker.com/r/staphb/spades-v3.12/) | 3.12.0 | http://cab.spbu.ru/software/spades/ |
| [QUAST](https://hub.docker.com/r/staphb/quast-v5.0.0/) | 5.0.0 | https://github.com/ablab/quast |
| [Mash](https://hub.docker.com/r/staphb/mash/) | 2.0 | https://github.com/marbl/Mash |
| [SerotypeFinder](https://hub.docker.com/r/staphb/serotypefinder-v1.1/) | 1.1 | https://bitbucket.org/genomicepidemiology/serotypefinder/ |
| [SeqSero](https://hub.docker.com/r/staphb/seqsero-v1.0.1/) | 1.0.1 | https://github.com/denglab/SeqSero |
| [SISTR](https://hub.docker.com/r/staphb/sistr-v1.0.2/) | 1.0.2 | https://github.com/peterk87/sistr_cmd |
| [ABRicate](https://hub.docker.com/r/staphb/abricate-v0.8.7/) | 0.8.7 | https://github.com/tseemann/abricate |
| [Prokka](https://hub.docker.com/r/staphb/prokka-v1.13/) | 1.13.3 | https://github.com/tseemann/prokka |
| [Trimmomatic](https://hub.docker.com/r/staphb/trimmomatic-0.38/) | 0.38 | http://www.usadellab.org/cms/?page=trimmomatic |
| [iqtree](https://hub.docker.com/r/staphb/iqtree-v1.6.7/) | 1.6.7 | http://www.iqtree.org/ |
| [Unicycler](https://hub.docker.com/r/staphb/unicycler-v0.4.7/) | 0.4.7 | https://github.com/rrwick/Unicycler |

## Download Docker images
You can view the list of containers on Docker hub here: https://hub.docker.com/r/staphb/

Docker CE must first be downloaded/installed onto your system. Check that it is installed by running:
```
docker images
# or
docker ps
```
If it is not installed, visit: https://docs.docker.com/install/ and follow the install instructions according to your operating system. For Ubuntu users, please see my install instructions here: https://github.com/StaPH-B/scripts/blob/master/image-information.md#docker-ce

Containers can be downloaded by running:
```
docker pull staphb/<name-of-container>:latest

# for example, SPAdes
docker pull staphb/spades-v3.12:latest
```
NOTE: The `latest` tag is usually the default tag associated with the latest version of the Docker image, however if a container fails to download, check the "Tags" tab on the docker hub repo to see what tag was used to build the image originally.

## Usage of Docker containers


