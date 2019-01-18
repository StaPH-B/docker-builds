# Docker User Guide

## Usage of Docker containers
I (Curtis) typically run Docker containers on an Ubuntu OS, but I believe the Docker commands will be the same for all operating systems (MacOS and Windows).

Once a Docker image has been pulled with `docker pull`, you should see an output similar to this...
```
latest: Pulling from staphb/spades
18d680d61657: Already exists
0addb6fece63: Already exists
78e58219b215: Already exists
eb6959a66df2: Already exists
2ab7d8aa6fdf: Pull complete
194b04b3cee9: Pull complete
Digest: sha256:e7053ba61a9a9a24810a9fa04c7967d364e53f0f5a87ba5d64689eb092488e0d
Status: Downloaded newer image for staphb/spades:3.12.0
```
...meaning the image has been built on your machine and is ready for use. No further installation required!

Each time you use the `docker run` command, a brand new Docker container is then spun up, and will run the program of choice on files located on your machine locally. Most containers should be run using this command:
```
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/<name-of-docker-image>:<tag> <command> <--flags --go --here>

# example: SPAdes
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/spades:3.12.0 \
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

Containers can also be run in an interactive mode allowing you to execute commands and access the file system within the docker container. To run containers in this mode simply add the `-it` flag to the `docker run` command. This instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container. You can exit this mode using the `exit` command which shuts down the running container.

### `$SHELL` within containers and wildcards
Due to the way that these containers were built (built using the base `ubuntu:xenial` Docker image) and the way the docker daemon operates, the `$SHELL` that is used by the Docker container is `/bin/sh` and not `/bin/bash` or BASH shell that Ubuntu users are used to. For this part of the example command below `roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff` is interpreted literally when it is passed into the docker container, and the wildcard will not be expanded.
```bash
# Run Roary on a directory containing multiple annotated genome files (.GFF) to generate pangenome
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/roary:3.12.0 \
  roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff

# results in the following output, due to the /bin/sh interpreting /data/*.gff literally as one file
2018/10/31 21:19:43 Error: You need to provide at least 2 files to build a pan genome
```
The solution to this problem is to first call the `/bin/bash -c` shell when performing the `docker run` command, and to place the command for the specific program within single quotes:
```bash
# solution
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/roary:3.12.0 /bin/bash -c \
  'roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff'
```
This way when the container runs, it will use the bash shell to run Roary, and will expand the wildcard to include all gff files within the `/data` directory.

### Passing variables into containers
More detailed info: https://docs.docker.com/edge/engine/reference/commandline/run/#set-environment-variables--e---env---env-file

If you're like me, and would like to incorporate Docker images/containers to run as part of a script, containers need to be able to accept environmental variables (set within the bash script I use to string together all of these containers). Thankfully Docker has an easy way to pass variables so that the container $SHELL will recognize them.

You can use the `-e <variable>`, `--env <variable>` (equivalent flags), or `--env-file <ENV-FILE.LIST>` to pass environment variables set by your bash script into the docker container when it is run.

MyScript.sh
```bash
#!/bin/bash
# set the variables
variable1=isolate1
variable2=isolate2

# export them to make the variables global
export variable1
export variable2

# pass them into the container
docker run --env variable1 --env variable2 staphb/roary:3.12.0 /bin/bash -c \
  'roary -p 8 -e -n -v -f /data/roary-output/ /data/${variable1}.gff /data/${variable2}.gff'
```
#### NOTE: Passing variables to docker container not necessary if you don't call `/bin/bash -c`
For example, if you are running the following command which contains a variable and does NOT call the `/bin/bash` shell, there is no need to pass a variable in with `-e <variable>` or `--env <variable>`. The following command within this bash script will recognize the variable, since no new shell is called when run.
```bash
#!/bin/bash
# set the variable, no need to export
variable1=isolate1
variable2=isolate2
# run the container without calling the /bin/bash shell, no single quotes around roary command
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/roary:3.12.0 \
  roary -p 8 -e -n -v -f /data/roary-output/ /data/${variable1}.gff /data/${variable2}.gff
```
