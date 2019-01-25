---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## Contributing
So far, we've created a bunch of docker images that we use in our day-to-day activities, but if there is a specific tool you do not see on our list and would like to add your own docker image, we would love to add it to the list.

Discover a bug or having issues with our images? Do you have a suggestion or advice for improving our docker images? [Please submit an issue under the Issues tab on our github repository](https://github.com/StaPH-B/docker-builds/issues)

### How to contribute a new Docker image
1. Build your own docker image using a Dockerfile (some information on this above)
2. Test to make sure it works in the way that you intend it to (e.g. give ILMN reads to a SPAdes docker container, receive SPAdes assembly out)
3. Fork this github repository using the fork button at the top right hand of the github page.
4. Add your Dockerfile (and any other required files required for building) to your forked repository following this convention:
    * The first directory should be the name of the program with special characters removed, and it's preferable to remove uppercase - `/spades`
    * The second directory should be the version number of the program, in X.X.X format - `/spades/3.12.0`
    * Lastly the Dockerfile and any other files required for building (hopefully there are none) belong in the sub-directory - `/spades/3.12.0/Dockerfile` and `/spades/3.12.0/some-other-file-needed-for-building.txt`
    * NOTE: There is a file size limit for github (I believe 100MB/file), so if you have a program with a huge database or file of some kind -  we won't be able to store the it in our github repository, and that database should be downloaded as part of the Dockerfile instructions with `wget`, `curl`, etc.
5.  Visit our docker-auto-builds github repository and a green "Submit Pull Request" button should appear near the top of the page. Click it, and submit a pull request to merge your forked repository into our repository.
6. We will take a look at your additions/changes, do some testing, and decide on whether or not to incorporate the changes into the master branch. We will most likely accept all new docker images, but if you have a specific change to an existing image we may not accept it. These images were built with the purpose of being used for clinical lab validations, so they should stay static, especially if a particular public health lab has incorporated that image into their clinically validated workflow.
7. If we accept your pull request, we will then add your docker image to the StaPH-B docker hub repository. Once the docker-hub autobuilds the image (successfully), it will be available and downloadable via `docker pull staphb/name-of-your-image:0.0.0`
