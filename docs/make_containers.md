---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## How to develop your own Docker image

1. [Install Docker](#install-docker)
2. [Create a Dockerfile](#create-a-dockerfile)
   1. [Template](#template)
   2. [Best-practices checklist](#best-practices-checklist)
3. [Build the image](#build-the-image)
4. [Running a container based on your image](#running-a-container-based-on-your-image)

### Install Docker

Docker can be installed from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

### Create a Dockerfile

In order to build your own docker image you need a `Dockerfile`.
This file is basically a set of instructions that are passed to the docker daemon in order to build your image.
It is similar to a `.yml` file for making/sharing conda environments, or really any kind of installation script.
We recommend a multistage Dockerfile to break the instructions up into different stages.
This way, you can keep the instructions for building your production image separate from instructions for testing it.
Once you have your Dockerfile, your can spin up either your test image or your production image with `docker run`.

Here's a working example of a Dockerfile for the SPAdes software:
```Dockerfile
# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:jammy AS app

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL software.version="3.12.0"

# RUN executes code during the build
# If you're using a Ubuntu base image, run apt-get update to update the package list first
RUN apt-get update && apt-get install -y \
    python \
    wget

# Download and install the tool
RUN wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz && \
    tar -xzf SPAdes-3.12.0-Linux.tar.gz && \
    rm -r SPAdes-3.12.0-Linux.tar.gz && \
    mkdir /data

# ENV instructions set environment variables that persist from the build into the resulting image
ENV PATH="${PATH}:/SPAdes-3.12.0-Linux/bin"

# WORKDIR sets working directory, this persists from the build into the resulting image
WORKDIR /data

# A second FROM insruction creates a new stage
# Here we add a test stage to run internal tests on the installed software.
FROM app AS test

RUN spades.py --test
```
#### Template

Fill in [this template](https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile) to create your own Dockerfile.

#### Best-practices checklist

- **Include an `app` stage and a `test` stage**

    This requirement is specific to StaPH-B, it enables automated testing and pushing images to Docker Hub.
    The `app` stage should include all the layers for the tool to run. 
    The `test` stage should run a few commands to demonstrate that the program is successfully installed and runs as expected. 
    
    See the [template](https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile) for test suggestions.

    For more information on how these stages are used, see the contribution guide ["How to create automated GitHub Actions tests for a Docker image"](https://staphb.org/docker-builds/contribute/#:~:text=How%20to%20create%20automated%20GitHub%20Actions%20tests%20for%20a%20Docker%20image).

- **Use a standard base image**


    We typically use the official docker `ubuntu:jammy` image (Ubuntu 22.04.5 LTS) as our base because it's a reliable and trusted base image and because Ubuntu is the OS we typically work on and are most familiar with.

    `alpine` is another frequently used image, and has the added benefit of being smaller than most other images.


- **Minimize the number of layers**

    The dockerfile commands (`FROM`, `RUN`, `CMD`, and `COPY`) will each add an additional layer (every time you use one), increasing the size of the image.
    There are two ways to reduce the size of your image.

    1. As recommended in Docker docs: [utilize the features of a multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/).
       You can use the following Dockerfile structure to isolate installation layers in a builder stage. Then, you can copy only the necessary layers into the production image stage, called "app". This keeps the production image small.
       ```Dockerfile
       FROM ubuntu:jammy AS builder

       # install the program here, using lots of RUN commands

       FROM ubuntu:jammy AS app

       COPY --from=builder /path/to/<program executable> /usr/local/bin/<program executable>
       ```

    2. Combine multiple commands in one RUN command using `&&` as below. The `\` is used to break a one-line command into multiple lines (for readability).

        ```Dockerfile
        # Using one layer
        RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && \
           tar -xzf SPAdes-3.13.0-Linux.tar.gz && \
           rm -r SPAdes-3.13.0-Linux.tar.gz && \
           mkdir /data

        # ...is much more efficient and will create a smaller docker image than using multiple layers:
        RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz
        RUN tar -xzf SPAdes-3.13.0-Linux.tar.gz
        RUN rm -r SPAdes-3.13.0-Linux.tar.gz
        RUN mkdir /data
        ```

- **Pin program versions**

    In your Dockerfile, specify downloading a specific version `wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz` instead of cloning the repo `git clone https://github.com/ablab/spades.git`.
    These docker images are intended to be static (clinical testing validation), and this helps keep them that way.

    One way to pin versions is to use the `ARG` command to set a build-time environment variable.
    Note: the scope of ARG variables is the stage in which they are defined.

    ```Dockerfile
    # For example
    ARG SPADES_VER=3.13.0
    wget http://cab.spbu.ru/files/release${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz
    ```

- **Keep the container directory structure clean**

    Remove as many unnecessary files as possible (tarballs, temporary files, etc.) and don't install unnecessary dependencies/programs.
    This keeps the container small if you are not utilizing a separate builder/install stage.
    It also helps with debugging to have a clean filesystem inside containers.

    Put program executables in /usr/local/bin. This is automatically in the PATH for a container.

    Create a `/data` directory, and set it as the working directory with `WORKDIR /data` in your Dockerfile.
    Sometimes programs don't like it when they are run in the `/` root directory, which is the default working directory.
    This also makes it easy for mounting a volume when you run a container.


### Build the image

Once you have a `Dockerfile` created, name it as `Dockerfile` and store it in a empty directory (unless you need files to build the docker image).
Note the path to the directory containing your Dockerfile.
Then, to build a test image, run:

```bash
# Replace <placeholder text> with your information
docker build \
    --target=test \
    --progress=plain \
    --tag <your name>/<program name>-test-build:<program version> \
    /path/to/DIR/with/Dockerfile/  # or . if you are in the same directory as where the Dockerfile is located

# For example
docker build \
    --target=test \
    --progress=plain \
    --tag kapsakcj/spades-test-build:3.12.0 \
    .
```
You should then see detailed output from the docker daemon, which builds your docker image.
If any errors occurred, the build will fail, and you'll need to make changes to your Dockerfile to fix the error before trying to build again.
The flag `--progress=plain` increases the level of detail in the output to help with debugging.

If the build is successful and the tests pass, you should see all steps completed successfully and the last lines will look similar to this:
```
#10 writing image sha256:dded88a5f25b392a3138a32ca8069c1fa4364af0369e3831594e8421203dcfdf done
#10 naming to docker.io/kapsakcj/spades-test-build:3.12.0 done
```
Then, you can spin up the production image by targeting the `app` stage. Run:
```bash
docker build \
    --target=app \
    --tag <your name>/<program name>:<program version> \
    /path/to/DIR/with/Dockerfile/
```

### Run a container based on your image

Now, your docker image is ready to spin up containers with `docker run`!
Here are some basic run commands that may be useful for debugging your image:
```bash
# Replace <placeholder text> with your information
docker run --rm=True <your name>/<program name>:<program version> <command>

# SPAdes example
docker run --rm=True kapsakcj/spades:3.12.0 spades.py --help

# Interactive run
docker run --rm=True -it kapsakcj/spades:3.12.0
# run commands like `pwd` or `spades.py --help` inside the container
# run `exit` to exit the container
```
For more information, see [running a Docker container](https://staphb.org/docker-builds/run_containers/).
