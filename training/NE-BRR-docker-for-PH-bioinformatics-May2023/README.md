# Intro To Docker for Public Health Bioinformatics

## Prerequisites

- GitHub Account
  - If you don't already have a GitHub account, please go to github.com and register (it's free!)
  - Once you have registered ensure you are signed into your account on github.com
- Navigate to GitPod & start a Workspace:
  - https://gitpod.io/
  - Select "Continue with GitHub", sign in with your credentials
  - Start New Workspace
  - Context URL: `https://github.com/theiagen/docker-builds`
  - Select the default Editor and Class, click "Continue"
- Once finished working in the workspace, make sure to shut down your workspace to save your allotted free hours in GitPod. There are a few ways to stop your workspace from running:
  - In GitPod environment (VSCode interface), click on gear icon in bottom left corner. Select "Stop Workspace"
  - OR you can navigate to https://gitpod.io/, find your workspace in the list, click on the three-dot button, and select "Stop"

## Week 1 Exercise 1

Goal: Use NCBI `datasets` to download a genome FASTA file - Klebsiella pneumoniae

### Docker basics

```bash
docker run hello-world
```


## Week 1 Exercise 2

Goal: Run `kleborate` on FASTA file for subtyping, serotyping, virulence and AMR prediction