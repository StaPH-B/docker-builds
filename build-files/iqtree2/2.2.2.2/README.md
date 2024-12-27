Tools installed in image: wget, iqtree2 version 2.2.2.2
ENV path set to: /iqtree-2.2.2.2-Linux/bin
Working directory set in /data

To use this image:

1) Build docker image
```
docker build -t <REPOSITORY>:<TAG> /path/to/iqtree2/Dockerfile
```
2) Run docker image with iqtree2 commands
```
docker run -i -t <REPOSITORY>:<TAG> iqtree2 [OPTIONS] -s FILE[,...,FILE]
```

For more details on how to run iqtree2 v2.2.2.2, check out iqtree2 documentation: http://www.iqtree.org/doc/
