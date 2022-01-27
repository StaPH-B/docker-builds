<!--
Thank your for contributing to the Staph-B community!
Please fill in the appropriate checklist below and delete whatever is not relevant.

These recommendations are not meant as a means to keep people from contributing. 
If you need assistance with the following measures, submit your pull request anyway, and we will work with you...
Or you can contact us beforehand via slack or by sumitting a pull request https://github.com/StaPH-B/docker-builds/issues

Documentation on how to contribute can be found at https://staphb.org/docker-builds/contribute/
Documentation for how to create a Dockerfile can be found at https://staph-b.github.io/docker-builds/make_containers
A recommended Dockerfile template can be found at https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile

To reiterate common comments in pull requests : 

Recommended ways to denote software versions
ARG SOFTWARENAME_VER="1.0.0"

Recommended labels:
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SoftwareName"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="This software does X, Y, AND Z!"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="FirstName LastName"
LABEL maintainer.email="my.email@email.com"
-->


- [ ] This comment contains a description of what is in the pull request.


<!-- If this PR is to add a dockerfile for a new tool -->
- [ ] Build your own docker image using a Dockerfile
  - [ ] Directory structure should be name of the tool in lower case with special characters removed with a subdirectory of the version number (i.e. spades/3.12.0/Dockerfile)
  - [ ] Includes the recommended LABELS
- [ ] (Optional) Dockerfile is built with best practices and has been approved by a linter (such as https://hadolint.github.io/hadolint/)
- [ ] Edit main README.md
- [ ] Edit Program_Licenses.md
- [ ] Create a simple container-specific README.md in the same directory as the Dockerfile (i.e. spades/3.12.0/README.md)
- [ ] Write a GitHub actions workflow
  - [ ] Should be located in .github/workflows/ and named test-<tool>.yml (i.e. .github/workflows/test-spades.yml)
  - [ ] Any files required for building are located in the same directory as the Dockerfile (i.e. spades/3.12.0/my_spades_tests.sh)
  - [ ] Have successfully run the workflow "Test <program name> image" in your forked repository

<!-- If this PR is to add a new version of a tool that already has a dockerfile -->
- [ ] Build your own docker image using a Dockerfile
  - [ ] Directory structure should be name of the tool in lower case with special characters removed with a subdirectory of the version number (i.e. spades/3.12.0/Dockerfile)
  - [ ] Includes the recommended LABELS
- [ ] (Optional) Dockerfile is built with best practices and has been approved by a linter (such as https://hadolint.github.io/hadolint/)
- [ ] Edit main README.md
- [ ] Ensure tool is listed in Program_Licenses.md
- [ ] Create a simple container-specific README.md in the same directory as the Dockerfile (i.e. spades/3.12.0/README.md)
- [ ] Update GitHub actions workflow if needed
- [ ] Any files required for building are located in the same directory as the Dockerfile (i.e. spades/3.12.0/my_spades_tests.sh)
- [ ] Have successfully run the workflow "Test <program name> image" in your forked repository

<!-- If this PR is to adjust an existing dockerfile  -->
- [ ] Build your own docker image using a Dockerfile
  - [ ] Includes the recommended LABELS
- [ ] (Optional) Dockerfile is built with best practices and has been approved by a linter (such as https://hadolint.github.io/hadolint/)
- [ ] Ensure tool is listed in Program_Licenses.md
- [ ] Ensure a simple container-specific README.md exists in the same directory as the Dockerfile (i.e. spades/3.12.0/README.md)
- [ ] Update GitHub actions workflow if needed
- [ ] Any files required for building are located in the same directory as the Dockerfile (i.e. spades/3.12.0/my_spades_tests.sh)
- [ ] Have successfully run the workflow "Test <program name> image" in your forked repository

<!-- If this PR is to adjust an existing GitHub actions workflow or to create one -->
- [ ] Update relevant GitHub actions workflow files
- [ ] Any files required for building are located in the same directory as the Dockerfile (i.e. spades/3.12.0/my_spades_tests.sh)
- [ ] Have successfully run the workflow "Test <program name> image" in your forked repository

<!-- If this PR is for something else, please add extra descriptions -->
