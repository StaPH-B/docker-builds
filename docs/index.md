---
layout: page
subtitle: Docker User Guide
---

<a href="https://www.docker.com/"><img src="/docker-builds/assets/user_guide.png" style="display:block;margin-left:auto;margin-right:auto;width:600px"></a>

Traditionally software is developed in a specific compute environment often requiring numerous dependencies to function correctly. This can be an issue especially for bioinformatics where compute environments from one location to another are very different. This can lead to bugs and glitches that could impact reproducibility of sequencing data analysis.

Containerization was developed to solve this problem.

Containerization involves bundling an application together with all of the necessary configuration files, libraries, and dependencies to ensure the software can run in a reproducible fashion across a diversity of computing environments.

[Docker](https://www.docker.com/) is one of the most common containerization engines and is what this guide is based on. However, [Singularity](https://sylabs.io) is also a popular containerization engine due to the extra layers of security. While this guide is focused specifically on the use of Docker, docker images can be used with Singularity.

The following guide is written for use on an Ubuntu/Debian OS, but the Docker commands should be the same for all operating systems (MacOS and Windows).
