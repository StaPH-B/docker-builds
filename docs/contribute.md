---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## Contributing
Discover a bug or having issues with our images? Do you have a suggestion or advice for improving our docker images? [Please submit an issue under the Issues tab on our github repository](https://github.com/StaPH-B/docker-builds/issues)

Regardless of how many docker images are available via staphb/docker-builds or other efforts, there are still tools that are not available in a container. We would welcome your contribution if you do not see a tool on our list and would like to add your own docker image.

### How to contribute a new Docker image
1. Build your own docker image using a Dockerfile (information on this in [Develop your own container](https://staph-b.github.io/docker-builds/make_containers/))
2. Fork this github repository using the fork button at the top right hand of the github page.
    * There are Dockerfile and README templates that can be copied from https://github.com/StaPH-B/docker-builds/tree/master/dockerfile-template and edited
3. Add your Dockerfile, README, and test files to your forked repository following these conventions:
    * The first directory should be the name of the program with special characters removed, and it's preferable to remove uppercase - `/build-files/spades`
    * The second directory should be the version number of the program, in X.X.X format - `/build-files/spades/3.12.0`
    * The Dockerfile and any other files required for building and testing belong in the sub-directory - `/spades/3.12.0/Dockerfile` and `/spades/3.12.0/my_spades_tests.sh`
    * NOTE: There is a file size limit for github (~100MB/file), so if you have a program with a huge database or file of some kind -  we won't be able to store the it in our github repository, and that database should be downloaded as part of the Dockerfile instructions with `wget`, `curl`, etc.
4. Please edit the `README.md` and `LICENSE.md` with the appropriate information for your program (follow alphabetical order please!) and commit changes to your forked repo. It's easiest to copy a line for an existing program from the raw markdown documents [README.md](https://raw.githubusercontent.com/StaPH-B/docker-builds/master/README.md) or [LICENSE.md](https://raw.githubusercontent.com/StaPH-B/docker-builds/master/LICENSE.md) and replace the information with your new image.
5. Open your github actions tab in the forked repository in the GitHub user interface and use the 'Manual Test' with the corresponding tool and version to test. If it passes, the files are ready to submit in a pull request!
6. Visit our docker-builds github repository and a green "Submit Pull Request" button should appear near the top of the page. Click it, and submit a pull request to merge your forked repository into our repository.
7. We will take a look at your additions/changes, run your test workflow again, and decide on whether or not to incorporate the changes into the master branch. We will most likely accept all new docker images, but if you have a specific change to an existing image we may not accept it. These images were built with the purpose of being used for public health laboraties and may be involved in CLIA compliant processes, so each image should be as static as possible.
8. If the pull request is accepted, the docker image will be to the [StaPH-B docker hub repository](https://hub.docker.com/u/staphb). Once the docker-hub builds the image (successfully), it will be available and downloadable via `docker pull staphb/name-of-your-image:0.0.0` or `docker pull staphb/name-of-your-image:latest`
