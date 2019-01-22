# Docker User Guide

## How to develop your own Docker image
In order to build your own docker image you need one file, the `Dockerfile`. This file is basically a set of instructions that are passed to the docker daemon in order to build your image. It is similar to a `.yml` file for making/sharing conda environments, or really any kind of installation script. Docker images need to be built once in order to spin up containers with `docker run`. Here's a simple example, our Dockerfile for SPAdes with some added explanation:
```Dockerfile
# FROM defines the base docker image to start from. This command has to come first in the file
FROM ubuntu:xenial

# metadata (there are a few other labels you can add, these are optional but preferred!)
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SPAdes"
LABEL software.version="3.13.0"
LABEL description="de novo DBG genome assembler"
LABEL website="http://cab.spbu.ru/files/release3.13.0/manual.html"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# If you're using Ubuntu as the base image, it's best to run apt-get update and install prior to doing anything else
RUN apt-get update && apt-get install -y python \
  wget

# download, unpack SPAdes
RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && \
  tar -xzf SPAdes-3.13.0-Linux.tar.gz && \
  rm -r SPAdes-3.13.0-Linux.tar.gz && \
  mkdir /data

# set the PATH to include the path to the SPAdes executables (python scripts)
ENV PATH="${PATH}:/SPAdes-3.13.0-Linux/bin"

# set the working directory as /data so that SPAdes.py runs in that directory, not the root DIR /
WORKDIR /data
```
[If you want a more complex example where more dependencies are installed and I had work some magic to get java executables to run, check out the Dockerfile for Shovill](https://github.com/StaPH-B/docker-builds/blob/master/shovill/1.0.4/Dockerfile)

Once you have a `Dockerfile` created, name it as `Dockerfile` and store it in a empty directory (unless you need files to build the docker image). Note the path to the directory containing your dockerfile. Then, run:
```
docker build --tag your-name-here/name-of-your-program:0.1.0 /path/to/DIR/with/Dockerfile/

# OR if you are in the same directory as where the docker file is located:
docker build --tag your-name-here/name-of-your-program:0.1.0 .
```
You should then see outputs from the docker daemon, which builds your docker image. If any errors occurred, the build will fail, and you'll need to make changes to your Dockerfile to fix the error before trying to build again.

If the build is successful, you should see all steps completed successfully and the last two lines will look similar to this
```
Successfully built ecfebf076715
Successfully tagged kapsakcj/spades-test-build:3.12.0
```
Then, your docker image is ready to be used to spin up containers with `docker run`!

### Best practices for developing your own docker image
  * Pick out a base image, and stick with it. We typically use the offical docker `ubuntu:xenial` image (Ubuntu 16.04) as our base because it's a reliable and trusted base image and because Ubuntu is the OS we typically work on and are most familiar with. `alpine` is another frequently used image, and has the added benefit of being smaller than the `ubuntu:xenial` image. There are thousands out there to choose from.
  * If you're using Ubuntu as the base image, it's best to run `apt-get update` and `apt-get install [packages]` prior to doing anything else
  * Write your dockerfile with as few layers as possible to reduce the size of the image - combine multiple commands in one RUN command using `&&`. The `\` is used to break a one-line command into multiple lines (for readability).
  * Pin the exact versions of the programs that you download. In your dockerfile, specify downloading a specific version `wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz` instead of cloning the repo `git clone https://github.com/ablab/spades.git`. These docker images are intended to be static (clinical testing validation), and this helps keep them that way.

  This:
  ```Dockerfile
  RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && \
      tar -xzf SPAdes-3.13.0-Linux.tar.gz && \
      rm -r SPAdes-3.13.0-Linux.tar.gz && \
      mkdir /data
  ```
  ...is much more efficient and will create a smaller docker image with less layers than this:
  ```Dockerfile
  RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz
  RUN tar -xzf SPAdes-3.13.0-Linux.tar.gz
  RUN rm -r SPAdes-3.13.0-Linux.tar.gz
  RUN mkdir /data
  ```
  The dockerfile commands (`FROM`, `RUN`, `CMD`, and `COPY`) will each add an additional layer (everytime you use one), increasing the size of the image. The less the better!

  * Remove as many unnecessary files as possible (tarballs, temporary files, etc.) and don't install unnecessary dependencies/programs (again, the smaller the image the better)
  * Create a `/data` directory, and set it as the working directory with `WORKDIR /data` in your Dockerfile. Sometimes programs don't like it when they are run in the `/` root directory, which is the default working directory. This also makes it easy for mounting a volume when you run a container. I typically run a container like so:
```
$ docker run --rm=True -v $PWD:/data -u $(id -u):$(id -g) staphb/quast:5.0.0 quast.py /data/spades_assembly/$i/contigs.fasta -o /data/quast/$i
```
