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
If it is not installed, visit: [https://docs.docker.com/install/](https://docs.docker.com/install/) and follow the install instructions according to your operating system. For Ubuntu users, please see my install instructions here: [https://github.com/StaPH-B/scripts/blob/master/image-information.md#docker-ce](https://github.com/StaPH-B/scripts/blob/master/image-information.md#docker-ce)

Images can be downloaded by running:
```
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
