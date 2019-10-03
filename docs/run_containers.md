---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## Running a docker container

### Pull a docker image from docker hub
Before running a docker image you must first retrieve the image using the command `docker pull`, then you should see an output similar to this...
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
...this means the image has been downloaded on your machine and is ready for use. No further installation required!

### Running a docker image
Starting a container from a docker image is simply done using the `docker run` command, a brand new Docker container is then created, and will run any command you provide within the container.

For example running the following command will demonstrate how a container runs on your system `docker run hello-world`.

To run a staphb image you simply name the image you want to use.
```
docker run staphb/trimmomatic
```
The previous command did not give any instructions to the container so the container simply started and then exited.

To see an executed command run the following command.
```
docker run staphb/trimmomatic sh -c "echo Hello from inside the trimmomatic container"
```
There are a number of options you can also supply to the run command. We have found the following command is useful for running containers:
```
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/<name-of-docker-image>:<tag> <command> <--flags --go --here>

# example: SPAdes
docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/spades:3.12.0 \
    spades.py --pe1-12 /data/trimmed-reads.fastq.gz -o /data/docker-spades-output
```
Here is a description of each of the flags we used in the previous command.
```
# explanation
  --rm=True
     By default, when a Docker container is run without this flag, the Docker container is created,
     the container runs, and then exits, but is not deleted. In other words, Docker containers
     are NOT ephemeral by default. A local copy of the container is kept and takes up unnecessary
     storage space. It is a good idea to always use this flag so that the container is removed after
     running it, unless for some reason you need the container after the specified program has been run.

  -v $PWD:/data
     The -v flag mounts a volume between your local machine and the Docker container. This specific
     command mounts the present working directory to the /data directory within the Docker container,
     which makes the files on your local machine accessible to the container. You can change these
     paths to meet the needs of your system, however it is a good idea to have a working directory
     in each of the containers, and thus each container contains the /data directory for such purpose.

  -u $(id -u):$(id -g)
     By default, when Docker containers are run, they are run as the root user. This can be problematic
     because any files created from within the container will have root permissions/ownership and
     the local user will not be able to do much with them. The -u flag sets the container's user and group
     based on the user and group from the local machine, resulting in the correct file ownership.
```

##### NOTE: This can be incorporated into a bash function by including the following into your .bashrc
```
#docker_run function
function docker_run() {
docker run --rm=True -u $(id -u):$(id -g) -v $(pwd):/data "$@"
}
```
This allows you to use the `docker_run` command to automatically include the flags used above.

Containers can also be run in an interactive mode allowing you to execute commands and access the file system within the docker container. To run containers in this mode simply add the `-it` flag to the `docker run` command. This instructs Docker to allocate a pseudo-TTY connected to the container’s stdin; creating an interactive bash shell in the container just as if you were connected via ssh. You can exit this mode using the `exit` command which shuts down the running container.

#### `$SHELL` within containers and wildcards
The default shell in the container is `/bin/sh` and not `/bin/bash` or BASH shell that Ubuntu users are used to. For this part of the example command below `roary -p 8 -e -n -v -f /data/roary-output/ /data/*.gff` is interpreted literally when it is passed into the docker container, and the wildcard will not be expanded.
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

#### Passing environment variables into containers
More detailed info: [https://docs.docker.com/edge/engine/reference/commandline/run/#set-environment-variables--e---env---env-file](https://docs.docker.com/edge/engine/reference/commandline/run/#set-environment-variables--e---env---env-file)

If you would like to incorporate environmental variables in the container for example as part of a script, Docker has an easy way to pass them to the container so $SHELL will recognize them.

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
##### NOTE: Passing variables to docker container not necessary if you don't call `/bin/bash -c`
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

## Running a Singularity container
One major difference between docker and singularity is that docker containers are not visible files in your filesystem, while with singularity, containers are present as executable files in your filesystem. You need to tell singularity the path to your singularity image to run it.
```bash
# if our singularity image lies in a directory called 'singularity-images/` then we can run it like so:
singularity exec singularity-images/spades.3.13.0.simg echo "hello from inside the container"
```

In the above example, we ran the container from the 'non-interactive mode' using `singularity exec` where we tell the container what command to execute: `echo "hello from inside the container"`, and then the container exits. If we want to run the container in 'interactive mode' similar to using `docker run -it`, we are also able to do the same with Singularity and work from inside the container with `singularity shell`.
```bash
curtis@host:~/$ singularity shell singularity-images/spades.3.13.0.simg

# OUTPUT:
Singularity: Invoking an interactive shell within container...

Singularity spades.3.13.0.simg:~/>
```
Our terminal prompt changes to reflect that we are in a shell within the container.

It is also important to note that with Singularity it does the following automatically (unless you specify otherwise):
  * mounts your local home directory inside the container
    * You can disable this using the `--no-home` option: 
    ```
    singularity shell --no-home singularity-images/spades.3.13.0.simg
    ```
    * You can mount or Bind specific directories (similar to mounting volumes with `docker run -v`) to directories in the container filesystem using the `-B /local-dir:/dir-in-container` option: 
    ```
    # mount your present working directory to /data inside the container
    singularity shell --no-home -B $PWD:/data singularity-images/spades.3.13.0.simg
    ```
  * sets your user and group inside the container to match your local user and group. Try running `whoami` while inside your singularity container shell. 


#### Passing environment variables into singularity containers
You can pass environmental variables into containers at runtime a couple of different ways. If you do not call a separate `/bin/bash -c` shell you can easily pass the variable like so:
```bash
export exampleVar="WOMP WOMP"
singularity exec spades.3.13.0.simg echo $exampleVar
# OUTPUT:
WOMP WOMP
```
However, if you need to use `/bin/bash -c` at the beginning of the command you're passing into the container, you can use environmental variables like so from the command-line:
```bash
exampleVar="WOMP WOMP" singularity exec spades.3.13.0.simg /bin/bash -c 'echo $exampleVar'
# OUTPUT:
WOMP WOMP
```
or from inside of a bash script:
```bash
#!/bin/bash
export exampleVar="WOMP WOMP"
singularity exec spades.3.13.0.simg /bin/bash -c 'echo $exampleVar'
```
