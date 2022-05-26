---
layout: page
---

<img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:400px">

## Contributing
So far, we've created a bunch of docker images that we use in our day-to-day activities, but if there is a specific tool you do not see on our list and would like to add your own docker image, we would love to add it to the list.

Discover a bug or having issues with our images? Do you have a suggestion or advice for improving our docker images? [Please submit an issue under the Issues tab on our github repository](https://github.com/StaPH-B/docker-builds/issues)

### How to contribute a new Docker image
1. Build your own docker image using a Dockerfile (information on this in [Develop your own container](https://staph-b.github.io/docker-builds/make_containers/))
2. Write a GitHub actions workflow that shows it works in the way that you intend it to (information on this [below](#how-to-create-automated-github-actions-tests-for-a-docker-image))
3. Fork this github repository using the fork button at the top right hand of the github page.
4. Add your Dockerfile (and any other required files required for building) and your GitHub workflow YAML files to your forked repository following these conventions:
    * The first directory should be the name of the program with special characters removed, and it's preferable to remove uppercase - `/spades`
    * The second directory should be the version number of the program, in X.X.X format - `/spades/3.12.0`
    * The Dockerfile and any other files required for building and testing belong in the sub-directory - `/spades/3.12.0/Dockerfile` and `/spades/3.12.0/my_spades_tests.sh`
    * The GitHub workflow YAML file should be in `.github/workflows/` and named in the format test-\<program name\>.yml - `test-spades.yml`
    * NOTE: There is a file size limit for github (I believe 100MB/file), so if you have a program with a huge database or file of some kind -  we won't be able to store the it in our github repository, and that database should be downloaded as part of the Dockerfile instructions with `wget`, `curl`, etc.
5. Please edit the `README.md` and `LICENSE.md` with the appropriate information for your program (follow alphabetical order please!) and commit changes to your forked repo. It's easiest to copy a line for an existing program from the raw markdown documents [README.md](https://raw.githubusercontent.com/StaPH-B/docker-builds/master/README.md) or [LICENSE.md](https://raw.githubusercontent.com/StaPH-B/docker-builds/master/LICENSE.md) and replace the information with your new image.
6. Open your forked repository in the GitHub user interface and run the workflow "Test \<program name\> image". If it passes, you're ready to submit a pull request!
   <details>
         <summary>How to manually run the GitHub actions workflow.</summary>
      <br>
      Find the button to manually trigger the workflow for your image:
      <img src="../assets/trigger_github_actions_workflow.png">
      <br>
      <br>
      Note: if you added your files to a branch, you need to have that branch set as default to be able to manually trigger the workflow:
      <img src="../assets/set_github_default_branch.png">
   </details>
7. Visit our docker-builds github repository and a green "Submit Pull Request" button should appear near the top of the page. Click it, and submit a pull request to merge your forked repository into our repository.
8. We will take a look at your additions/changes, run your test workflow again, and decide on whether or not to incorporate the changes into the master branch. We will most likely accept all new docker images, but if you have a specific change to an existing image we may not accept it. These images were built with the purpose of being used for clinical lab validations, so they should stay static, especially if a particular public health lab has incorporated that image into their clinically validated workflow.
9. If we accept your pull request, we will then add your docker image to the StaPH-B docker hub repository. Once the docker-hub builds the image (successfully), it will be available and downloadable via `docker pull staphb/name-of-your-image:0.0.0` or `docker pull staphb/name-of-your-image:latest`

### How to create automated GitHub Actions tests for a Docker image

1. Make sure you have a stage in your Dockerfile named `test`. This stage should run a few commands to demonstrate that the program is successfully installed in your image and runs as expected. Information on this in point 1 above. See the [Dockerfile template](../dockerfile-template/Dockerfile) for test suggestions.
2. Copy the template GitHub workflow file for testing `.github/workflow-templates/test-template.yml` to `.github/workflows/test-<program name>.yml` for your image.
3. Overwrite all instances of `<placeholder text>` in the files with information on your image.
4. Continue from Step 6 above to run your new test workflow via the GitHub user interface.