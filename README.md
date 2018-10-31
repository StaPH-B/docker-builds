# docker-auto-builds
This repo contains the Dockerfiles and other assorted files necessary for building Docker images/containers for a variety of programs used by members of the StaPH-B (State Public Health Lab Bioinformatics) consortium. The purpose of this repo is to provide a centralized location for Docker images that is easily accessible for users, with clear documentation on how the containers were built and how to use them.

Each Dockerfile lists author/maintainer for that specific Docker image, but the authors/maintainers of the docker images are:
  * [@kapsakcj](https://github.com/kapsakcj)
  * [@nwflorek](https://github.com/nwflorek)

If you would like to contribute with your own Docker image or perhaps improve upon the existing images, please submit a pull request (or an issue). We welcome any and all feedback!

## Available Docker images
| Software | Version | Link |
| -------- | ------- | -------- |
| [SRA-toolkit](https://hub.docker.com/r/staphb/sratoolkit-v2.9.2/) | 2.9.2 | https://github.com/ncbi/sra-tools |
| [Lyve-SET (includes CG-Pipeline scripts and raxml)](https://hub.docker.com/r/staphb/lyveset-v2.0/) | 2.0.1 (lyve-SET) | https://github.com/lskatz/lyve-SET https://github.com/lskatz/CG-Pipeline |
| [Kraken](https://hub.docker.com/r/staphb/kraken-v1.0/) | 1.0 | https://github.com/DerrickWood/kraken |
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
You can view the list of images on Docker hub here: https://hub.docker.com/r/staphb/

Docker CE must first be downloaded/installed onto your system. Check that it is installed by running:
```
docker images
# or
docker ps
```
If it is not installed, visit: https://docs.docker.com/install/ and follow the install instructions according to your operating system. For Ubuntu users, please see my install instructions here: https://github.com/StaPH-B/scripts/blob/master/image-information.md#docker-ce

Images can be downloaded by running:
```
docker pull staphb/<name-of-container>:latest

# for example, SPAdes
docker pull staphb/spades-v3.12:latest
```
NOTE: The `latest` tag is usually the default tag associated with the latest version of the Docker image, however if a container fails to download, check the "Tags" tab on the docker hub repo to see what tag was used to build the image originally.

## Usage of Docker containers
I (Curtis) typically run Docker containers on an Ubuntu OS, but I believe the Docker commands will be the same for all operating systems (MacOS and Windows).

Once a Docker image has been pulled with `docker pull`, you should see an output similar to this...
```
latest: Pulling from staphb/spades-v3.12
18d680d61657: Already exists
0addb6fece63: Already exists
78e58219b215: Already exists
eb6959a66df2: Already exists
2ab7d8aa6fdf: Pull complete
194b04b3cee9: Pull complete
Digest: sha256:e7053ba61a9a9a24810a9fa04c7967d364e53f0f5a87ba5d64689eb092488e0d
Status: Downloaded newer image for staphb/spades-v3.12:latest
```
...meaning the image has been built on your machine and is ready for use. No further installation required!

Each time you use the `docker run` command, brand new Docker containers are then spun up, and will run the program of choice on files located on your machine locally. Most containers should be run using this command:
```
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/<name-of-docker-image>:latest <command> <--flags --go --here>

# example: SPAdes
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/spades-v3.12:latest \
    spades.py --pe1-12 /data/trimmed-reads.fastq.gz -o /data/docker-spades-output 
```
```
# explanation
  --rm=True
     By default, when a Docker container is run without this flag, the Docker container is created,
     the container runs, and then it shuts down, but is not deleted. In other words, Docker conainers
     are NOT ephemeral by default. A local copy of the container is kept and takes up unnecessary
     storage space. It is a good idea to always use this flag so that the container is removed after
     running it, unless for some reason you need the container after the specified program has been run.

  -v $PWD:/data
     The -v flag mounts a volume between your local machine and the Docker container. This specific
     command mounts the present working directory to the /data directory within the Docker container,
     which makes the files on your local machine accesible to the container. You can change these
     paths to meet the needs of your system, however it is a good idea to have a working directory
     in each of the containers, and thus each container contains the /data directory for such purpose.
     
  -u $(id -u):$(id -g)
     By default, when Docker containers are run, they are run as the root user. This can be problematic
     because any files created from within the container will have root permissions/ownership and
     the local user will not be able to do much with them. The -u flag sets the container's user and group 
     based on the user and group from the local machine, resulting in the correct file ownership.
```
### `$SHELL` within containers
Due to the way that these containers were built (built using the base `ubuntu:xenial` Docker image), the `$SHELL` that is used by the Docker container is `/bin/sh` and not `/bin/bash` or BASH shell that Ubuntu users are used to. This can cause for problems such as wildcard expansion, where a wildcard present in a command like so:
```
# Run Roary on a directory containing multiple annotated genome files (.GFF)
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/roary-3.12.0:latest \
  roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff
  
# results in the following output, due to the /bin/sh interpreting /data/*.gff literally as one file
2018/10/31 21:19:43 Error: You need to provide at least 2 files to build a pan genome
```
The solution to this problem is to first call the `/bin/bash -cl` shell when performing the `docker run` command, and to place the command for the specific program within single quotes:
```
# solution
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/roary-3.12.0:latest /bin/bash -cl 'roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff'
```
This way when the container runs, it will use the bash shell to run Roary, and will expand the wildcard to include all gff files within the `/data` directory.
