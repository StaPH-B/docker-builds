---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## Download Docker images
You can view the list of images on Docker hub here: [https://hub.docker.com/r/staphb/](https://hub.docker.com/r/staphb/)

Docker CE must first be downloaded/installed onto your system. Check that it is installed by running:
```bash
docker info
# or
docker images
# or
docker ps
```
If it is not installed, visit: [https://docs.docker.com/install/](https://docs.docker.com/install/) and follow the install instructions according to your operating system. 

Images can be downloaded by running:
```bash
docker pull staphb/<name-of-container>:<tag>

# for example, SPAdes
docker pull staphb/spades:3.12.0

# or get the latest by using
docker pull staphb/spades:latest

# or
docker pull staphb/spades
```

NOTE: Each container will have a different docker image `tag` that is named after the version of the main program within the docker image. You can view the available tags for each docker image on the docker hub repository page under the 'tag' tab.

The `latest` tag is usually the default tag associated with the latest version of the Docker image, however we have specified these image tags to be named after the version of the program. Downloading one of these docker images with the "latest" tag will download the latest version of the program we have available. Check the "Tags" tab on the docker hub repository to see what tag was used to build the image originally.

## Download Docker images using Singularity
Singularity was built with the intention of being compatible with Docker, therefore most if not all Docker images can be converted to singularity format, and run using Singularity.

First check to make sure Singularity is installed:
```bash
singularity --version
# or
singularity --help
```
If it is not installed, please visit the following link for installing the latest version of Singularity (at time of writing this). You will need administrator priveleges and to install some additional dependencies before installing singularity itself. [https://sylabs.io/guides/3.4/user-guide/quick_start.html#quick-installation-steps](https://sylabs.io/guides/3.4/user-guide/quick_start.html#quick-installation-steps)

Images can then be downloaded from dockerhub by running the following commands. This is similar to the way you would download an image using docker.
```bash
# you can name the image whatever you want 'name-of-image-on-your-machine.simg' 
# '.simg' is the suffix for singularity image. 
# The syntax of the URL looking part of this command is important (see example below)
singularity build <name-of-image-on-your-machine>.simg <url://repo-name/image-name:tag>

# download the spades image from staphb repository on dockerhub and place the executable in your current directory. 
singularity build spades.3.13.0.simg docker://staphb/spades:3.13.0
```
