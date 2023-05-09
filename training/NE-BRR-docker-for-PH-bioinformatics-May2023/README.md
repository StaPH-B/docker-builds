# Intro To Docker for Public Health Bioinformatics Training

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
  - In GitPod environment (VSCode interface), click on gear icon in bottom left corner. Select "Stop Workspace"
  - OR you can navigate to https://gitpod.io/, find your workspace in the list, click on the three-dot button, and select "Stop"

## Week 1 Exercise 1

End goal: Use NCBI `datasets` to download a genome FASTA file - Klebsiella pneumoniae

### Docker basics

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

Now that we've covered some of the basics of `docker` on the command line, let's download a *Klebsiella pneumoniae* genome FASTA file from NCBI.

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
# download the docker image "staphb/kleborate:2.3.2" and launch interactive mode
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -it staphb/kleborate:2.3.2-2023-05

# run kleborate using the FASTA file as input (be patient, this step may take a few minutes to run....)
kleborate --all -o results.tsv -a ncbi_dataset/data/GCF_000240185.1/GCF_000240185.1_ASM24018v2_genomic.fna

# exit the container
exit

# view results of Kleborate
cat results.tsv
```

## Resources

- You can find all of StaPH-B's dockerfiles & documentation here: https://github.com/StaPH-B/docker-builds
- You can find all of StaPH-B's docker images on dockerhub here: https://hub.docker.com/u/staphb