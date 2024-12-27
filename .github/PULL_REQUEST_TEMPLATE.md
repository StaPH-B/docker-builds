<!--
Thank your for contributing to the Staph-B community!
Please fill in the appropriate checklist below and delete whatever is not relevant.

These recommendations are not meant as a means to keep people from contributing. 
If you need assistance with the following measures, submit your pull request anyway, and we will work with you...
Or you can contact us beforehand via slack or by sumitting a pull request https://github.com/StaPH-B/docker-builds/issues

Documentation on how to contribute can be found at https://staphb.org/docker-builds/contribute/
Documentation for how to create a Dockerfile can be found at https://staph-b.github.io/docker-builds/make_containers
A recommended Dockerfile template can be found at https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile


Please replace all '[ ]' with '[X]' to demonstrate completion.
-->

Pull Request (PR) checklist:
- [ ] Include a description of what is in this pull request in this message.
- [ ] The dockerfile successfully builds to a test target for the user creating the PR. (i.e. `docker build --tag samtools:1.15test --target test docker-builds/build-files/samtools/1.15` )
- [ ] Directory structure as name of the tool in lower case with special characters removed with a subdirectory of the version number in build-files (i.e. `docker-builds/build-files/spades/3.12.0/Dockerfile`)
   - [ ] (optional) All test files are located in same directory as the Dockerfile (i.e. `build-files/shigatyper/2.0.1/test.sh`)
- [ ] Create a simple container-specific [README.md](https://github.com/StaPH-B/docker-builds/blob/master/.github/workflow-templates/readme-template.md) in the same directory as the Dockerfile (i.e. `docker-builds/build-files/spades/3.12.0/README.md`)
   - [ ] If this README is longer than 30 lines, there is an explanation as to why more detail was needed
- [ ] Dockerfile includes the recommended [LABELS](https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile#L8-L18) 
- [ ] Main [README.md](https://github.com/StaPH-B/docker-builds/blob/master/README.md) has been updated to include the tool and/or version of the dockerfile(s) in this PR
- [ ] [Program_Licenses.md](https://github.com/StaPH-B/docker-builds/blob/master/Program_Licenses.md) contains the tool(s) used in this PR and has been updated for any missing


<!-- If this PR is for something else, please add extra descriptions -->
