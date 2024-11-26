# Intro To Docker for Public Health Bioinformatics Training

## Table of Contents

- [Prerequisites](#prerequisites)
- [Docker basics](#docker-basics)
  - [Downloading docker images](#downloading-docker-images)
  - [Docker images vs containers](#docker-images-vs-containers)
  - [Running docker images](#running-docker-images)
  - [File permissions \& passing files in and out of containers](#file-permissions--passing-files-in-and-out-of-containers)
    - [File permissions](#file-permissions)
    - [Passing files in and out of containers](#passing-files-in-and-out-of-containers)
- [Week 1 Exercise 1](#week-1-exercise-1)
- [Week 1 Exercise 2](#week-1-exercise-2)
- [Week 2 Exercises](#week-2-exercises)
  - [NCBI `datasets`](#ncbi-datasets)
  - [SPAdes](#spades)
  - [Experiment](#experiment)
- [Week 3 Exercises](#week-3-exercises)
- [Resources](#resources)

## Prerequisites

- GitHub Account
  - If you don't already have a GitHub account, please go to github.com and register (it's free!)
  - Once you have registered ensure you are signed into your account on github.com
- Navigate to GitPod & start a Workspace:
  - https://gitpod.io/
  - Select "Continue with GitHub", authorize Gitpod to access your GitHub account, and sign in with your credentials
  - Start New Workspace
  - Set the "Context URL": `https://github.com/theiagen/docker-builds`
  - Select the default Editor and default Class, click "Continue"
- :rotating_light: Once you're finished working, make sure to shut down your workspace to save your allotted free hours in GitPod :rotating_light:. There are a few ways to stop your workspace from running:
  - In GitPod environment (VSCode interface), click on the orange Gidpod in bottom left corner. Select "Stop Workspace"
  - OR you can navigate to https://gitpod.io/, find your workspace in the list, click on the three-dot button, and select "Stop"

## Docker basics

Check to ensure docker is installed, look at help options for `docker` and `docker pull`. Run the following commands in the Terminal:

```
docker --version
docker --help
command -v docker
docker pull --help
```

The `hello world` exercise for docker! What happens when you run this command?

```bash
docker run hello-world
```

`docker images` = command used to list all docker images available on your computer. What docker images are available on your computer now?

```bash
docker images
```

### Downloading docker images

Let's download another docker image to practice with.

We're going to download a docker image from this docker hub repository: [https://hub.docker.com/r/staphb/ncbi-datasets](https://hub.docker.com/r/staphb/ncbi-datasets). Run the following command to download the StaPH-B docker image that contains the NCBI `datasets` command-line tool. [More info on the command line tool `datasets` can be found here](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/getting_started/)

```bash
docker pull staphb/ncbi-datasets:14.20.0
```

Now run the command `docker images` - what has changed?

QUIZ: What command would I use to download the StaPH-B docker image for the `mlst` software? (hint: see https://hub.docker.com/r/staphb/mlst/tags)

<details>
  <summary>Answer can be found here. Click to show answer:</summary>

  ```bash
  docker pull staphb/mlst:latest
  ```

</details>

### Docker images vs containers

When you ran the command `docker run hello-world` earlier, docker started a container using the docker image called `hello-world`, ran some things, and then the container automatically exited. The container did not delete itself, and we can see that by running the command `docker ps --all`. Run the command:

```
docker ps --all
```

You can tell `docker` to automatically delete the container after exiting with the `docker run --rm` flag. Let's try it out. Run the following command which will download and run a command in a new docker container:

```
docker run --rm ubuntu:focal echo "hello from inside the container!"
```

Now, run `docker ps --all` - do we see a container listed for the command we just ran? We should **not see it listed**, as long as the `docker run --rm` flag was included.

Now try the same command without the `--rm` flag:

```bash
docker run ubuntu:focal echo "hello from inside the container!"

# look at the list of containers again:
docker ps --all
```

### Running docker images

Interactive mode: You can launch into a container interactively, and be given a pseudo-shell from which you can run commands. You will need to use the `docker run -it` flags to do this:

```bash
# your command prompt will change after launching interactive mode
$ docker run -it staphb/ncbi-datasets:14.20.0
Unable to find image 'staphb/ncbi-datasets:14.20.0' locally
14.20.0: Pulling from staphb/ncbi-datasets
2ab09b027e7f: Already exists 
d6391dffcf79: Pull complete 
4f4fb700ef54: Pull complete 
eaa7a46260b5: Pull complete 
05a7178bde59: Pull complete 
Digest: sha256:4441c4556698fce13a2612889d467435eb8cec096565233da0e7b74fbae4a3fb
Status: Downloaded newer image for staphb/ncbi-datasets:14.20.0
root@d1c3f33f5fc9:/data

# now run the following commands:
pwd
ls 
cd /
ls

# you can exit the interactive container with the 'exit' command
exit
```

Non-interactive mode: The default method of running a container does not launch an interactive terminal, but rather, a command or set of commands is passed into the container. The format is as follows:

```bash
# format
docker run <name-of-docker-image>:<tag> <command>

# example
docker run ubuntu:focal echo "hello!"
```

### File permissions & passing files in and out of containers

#### File permissions

By default, when you launch a container with `docker run`, any commands run will be run as the `root` linux user. Thus, any files created will be owned by the `root` user, limiting the downstream use of these files by non-`root` linux users. Non-`root` users may encounter file permission errors if attempting to delete or edit files owned by `root`.

To avoid these issues, you can pass in your linux user ID (UID) and group ID (GID) so that the container runs with your user and group IDs. The flag to pass in user and group IDs is `docker run --user <user-id>:<group-id>` or `docker run -u <user-id>:<group-id>` for short

To test let's run the StaPH-B NCBI `datasets` docker container and create some files. Run the following commands:

```bash
# change directories so that we have a relatively clean working environment
cd training/

# launch the container in interactive mode
docker run -it staphb/ncbi-datasets:14.20.0

# create a file called "test.txt"
touch test.txt

# look at the permissions for this file
ls -lh

# see what the current user you're logged in as
whoami

# exit the container with the command 'exit'
exit
```

Now let's launch the container in interactive mode, but pass in our user and group id. Instead of looking up your user and group IDs, you can look up these IDs on-the-fly with `id -u` and `id -g`

```bash
# launch the container in interactive mode again, but this time pass in our user and group IDs
docker run -u $(id -u):$(id -g) -it staphb/ncbi-datasets:14.20.0

# change to /tmp
cd /tmp

# create a file called "test.txt"
touch test.txt

# look at the permissions for this file
ls -lh

# see what the current user you're logged in as
whoami

# exit the container with the command 'exit'. Your command prompt should go back to it's default
exit
```

#### Passing files in and out of containers

Docker containers have filesystems that are completely separate and isolated from your host computer's filesystem. You can mount a "volume" between your host computer's filesystem and the container filesystem to pass files in and out.

Files created inside of containers are not automatically exported from the container so we must use the `--volume <path-on-host>:<path-in-container>` or `-v <path-on-host>:<path-in-container>` (short hand). You must tell `docker` which path to mount from your host system, and the path on the container's filesystem to mount the volume to. It's OK if the path inside the container does not exist, it will be created.

If my present working directory (`$PWD`) is `/home/curtis_kapsak`, then I can mount my $PWD to `/data` in the container's filesystem like so:

```
docker run --volume $PWD:/data ubuntu:focal <command>
```

Let's pass a file into a container. First make an test text file, and then pass into the container:

```bash
# create the text file which contains the text "this is a test
echo "this is a test">text.txt

# mount your PWD to /data inside the container and list the contents of /data in the container filesystem
docker run --volume $PWD:/data ubuntu:focal ls /data

# same as before, but cat the test.txt file from inside the container
docker run --volume $PWD:/data ubuntu:focal cat /data/text.txt
```

Now let's create a file inside the docker container, and then save it to our host computer for usage later:

```bash
# create a file inside the container using the "touch" command, writing to /data in the container
docker run --volume $PWD:/data ubuntu:focal touch /data/file-made-inside-container.txt

# let's check and make sure that new file exists on our host computer filesystem:
ls

# what happens when we don't mount a volume and create a file inside the container?
docker run ubuntu:focal touch file-made-inside-container-NO-VOLUME.txt

# is this new file present on our host filesystem? Run this command to check:
ls file-made-inside-container-NO-VOLUME.txt
```

## Week 1 Exercise 1

Now that we've covered some of the basics of `docker` on the command line, let's download a *Klebsiella pneumoniae* genome FASTA file from NCBI.

End goal: Use NCBI `datasets` to download a genome FASTA file - Klebsiella pneumoniae

We downloaded the docker image called earlier, so now let's use it to download the FASTA file.

We're going to download this genome: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_000240185.1/

Let's launch the `datasets` docker image interactively, and use the flags you learned about earlier:

```bash
### launch the container in interactive mode ###
# --rm is to remove the container after it exits (i.e. delete the container)
# -v is for mounting my filesystem to the container filesystem
# -u is for passing in my user ID and group ID
# -it is 2 flags for launching interactive mode
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -it staphb/ncbi-datasets:14.20.0

# run the datasets tool to download the FASTA file (along with some other metadata)
datasets download genome accession GCF_000240185.1

# unzip the .zip archive
unzip ncbi_dataset.zip

# exit the container
exit

# take a peek at the top of the FASTA file
head -n 4 ncbi_dataset/data/GCF_000240185.1/GCF_000240185.1_ASM24018v2_genomic.fna
```

## Week 1 Exercise 2

Goal: Run `kleborate` on FASTA file for subtyping, serotyping, virulence and AMR prediction

Now that we have downloaded our FASTA file, let's launch into the container in interactive mode, and run `kleborate`

```bash
# download the docker image "staphb/kleborate:2.3.2-2023-05" and launch interactive mode
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -it staphb/kleborate:2.3.2-2023-05

# run kleborate using the FASTA file as input (be patient, this step may take a few minutes to run....)
kleborate --all -o results.tsv -a ncbi_dataset/data/GCF_000240185.1/GCF_000240185.1_ASM24018v2_genomic.fna

# exit the container
exit

# view results of Kleborate
cat results.tsv
```

## Week 2 Exercises

Let's build some docker images! In today's exercise we are going to practice building docker image in various ways. Let's tweak the dockerfiles and see how those changes impact the final docker image.

### NCBI `datasets`

Let's build the most recent version of NCBI `datasets` using the dockerfile located here: `ncbi-datasets/14.20.0/Dockerfile`

Reminder - the basic `docker build` command structure:

```bash
docker build --tag <name>:<tag> <directory-with-dockerfile>
```

Now with real values filled in, run the following command:

```bash
docker build --tag ncbi-datasets:14.20.0 ncbi-datasets/14.20.0/
```

What happened when we ran this command?

- Docker daemon read & interpreted the dockerfile. It also ensured correct syntax & format.
- The base image `ubuntu:jammy` was downloaded if not already present on computer.
- Daemon began running subsequent Dockerfile instructions (`RUN`, `WORKDIR`, etc) in order through to the end of the dockerfile.
- Docker image was given a sha256 hash & we received a message saying docker image was named & built successfully.

When we ran the previous command, it built all stages of the dockerfile. BUT we can tell `docker` to build to a specific stage using `docker build --target <stage>`. Let's try building to the `test` stage specifically:

```bash
# note the new option '--target test'
docker build --target test --tag ncbi-datasets:14.20.0-test-stage ncbi-datasets/14.20.0/
```

That command finished running almost instantaneously, why?

<details>
  <summary>Answer can be found here. Click to show answer:</summary>

**Answer: The image has already been built previously (with last `docker build` command we ran) and thus the layers are "cached" or stored locally to be re-used. No need to spend time & resources building an image when it has already been built!**

</details>
</br>
Now lets build to only the `app` stage, as this will be the final docker image that we share via dockerhub, quay, whatever container registry. This means we will use `--target app` which will skip building the layers in the `test` stage:

```bash
# note the new option '--target app'
docker build --target app --tag ncbi-datasets:14.20.0-app-stage ncbi-datasets/14.20.0/
```

### SPAdes

The SPAdes dockerfile is a bit more complex as it's test stage runs the SPAdes software on a toy dataset and assembles a plasmid sequence.

Let's build the most recent version of SPAdes, but this time start with only building the `app` stage. We are going to use the dockerfile located at `spades/3.15.5/Dockerfile`:

```bash
# note the new option '--target app'
docker build --target app --tag spades:3.15.5-app-stage spades/3.15.5/
```

Now let's build all the way through the `test` stage and see the test assembly process run:

```bash
# note the new option '--target test'
docker build --target test --tag spades:3.15.5-test-stage spades/3.15.5/
```

### Experiment

Let's try changing a few things in the dockerfile to see the effect of the changes.

_Hypothetical (& false) scenario 1 - SPAdes produced a `.zip` output file and my bioinformatics pipeline needs to `unzip` this file to extract the contents. I have to install the `unzip` software in the SPAdes docker image to accomplish this_

Steps:

1. Open up the SPAdes dockerfile in the GitPod/VSCode editor
2. Navigate to the top of dockerfile and look for the `apt-get install` step on lines 18-22.
3. Add a return and `unzip \` after line 21. The entire `RUN` layer should look like this:
```Dockerfile
RUN apt-get update && apt-get install --no-install-recommends -y python3 \
 python3-distutils \
 wget \
 pigz \
 unzip \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10
```

4. Once added, save the file (CTRL + S) and let's rebuild the image with a new tag (`spades:3.15.5-test-unzip-added`):

```bash
# same command as before, but now with an updated dockerfile
docker build --target test --tag spades:3.15.5-test-stage-unzip-added spades/3.15.5/
```

5. Launch an interactive container to see if `unzip` is actually installed:

```bash
# launch into interactive mode in container
docker run -ti spades:3.15.5-test-stage-unzip-added

# pull up unzip help options
unzip --help
```

_Hypothetical scenario 2 - I don't think the SPAdes test (`spades.py --test`) is good enough, I want to make sure it works on some real data. Let's try using SPAdes to assemble some real bacterial WGS data_

The current test is sufficient, but let's add another layer to the dockerfile to bolster the `test` stage. We are going to add some lines to download some real bacterial WGS data and assemble in the test stage. We are going to download some E. coli WGS data, Illumina paired-end, and assemble the genome with SPAdes. Here's the dataset on ENA: [https://www.ebi.ac.uk/ena/browser/view/SRR6903006](https://www.ebi.ac.uk/ena/browser/view/SRR6903006)

Steps:

1. Open up the SPAdes dockerfile in the GitPod/VSCode editor
2. Navigate to bottom of dockerfile and add these lines of code:

```Dockerfile
# download test FASTQ files from ENA
# run SPAdes on FASTQ files
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_2.fastq.gz && \
spades.py -t 4 --isolate --only-assembler -1 SRR6903006_1.fastq.gz -2 SRR6903006_2.fastq.gz -o spades-output
```

3. Once added, save the file (CTRL + S) and let's rebuild the image:

```bash
# same command as before, but now with an updated dockerfile
docker build --target test --tag spades:3.15.5-test-stage-added-test spades/3.15.5/
```

Adding this test will ensure the robustness of the docker image, but the tradeoff is that it takes longer to run the test. The assembly process can take a while (5-15 min or longer), especially if the input dataset is large.

## Week 3 Exercises

Currently in this repository, the latest available version of NCBI `datasets` is 14.20.0 (located at `ncbi-datasets/14.20.0/Dockerfile`). As of today 2023-06-01, more versions have been released, up to 15.2.0 and the repository is out of date. Let's change that and create another dockerfile for version 15.2.0.

Let's navigate to the `datasets` GitHub & documentation to ensure that the installation process is still the same as before. We don't want to be caught by any surprises.

- [https://github.com/ncbi/datasets/releases](https://github.com/ncbi/datasets/releases)
- [https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/)

:warning: **Spoiler alert!** Installation has not changed from previous versions. We will continue using the current installation method from the 14.20.0 dockerfile. This installation method downloads a pre-compiled binary (AKA executable file) that requires little-to-no setup.

Steps:

1. In the file explorer on the left-hand side, right-click on the directory `ncbi-datasets/14.20.0/` and select Copy.
2. Create a copy by pressing CTRL + V to paste the directory.
3. Rename the directory (F2 or right-click on copied directory and select rename) to the new version `15.2.0`.
4. Open the Dockerfile located at `ncbi-datasets/15.2.0/Dockerfile` in the editor.
5. On line 3, replace the old version `14.20.0` with the new version `15.2.0`. Do not change anything else!
6. Save the file by pressing CTRL + S, or selecting File :arrow_right: Save
7. Open a terminal if one isn't already open by navigating to the hamburger menu in the top left, select Terminal, and then select New Terminal.
8. Build your new docker image by using `docker build` in the terminal. You can use the following command:

```bash
docker build -t ncbi-datasets:15.2.0 ncbi-datasets/15.2.0/
```

9. Verify that the new version has been installed by running the `datasets --version` command inside the container:

```bash
# non-interactive mode:
docker run ncbi-datasets:15.2.0 datasets --version

# interactive mode:
docker run -it ncbi-datasets:15.2.0

# once interactive container is launched, run the same command:
datasets --version
```

## Resources

- You can find all of StaPH-B's dockerfiles & documentation here: https://github.com/StaPH-B/docker-builds
- StaPH-B's docker images on dockerhub here: https://hub.docker.com/u/staphb
- StaPH-B's docker image on quay.io here: https://quay.io/organization/staphb
