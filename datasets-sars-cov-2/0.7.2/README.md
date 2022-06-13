# datasets-sars-cov-2 container

Main tool : [datasets-sars-cov-2](https://github.com/CDCgov/datasets-sars-cov-2)

Full documentation: https://github.com/CDCgov/datasets-sars-cov-2#datasets

https://github.com/CDCgov/datasets-sars-cov-2/blob/master/INSTALL.md#docker

Benchmark datasets for WGS analysis of SARS-CoV-2

# Example Usage

```bash
# download the docker image and start a container with an interactive terminal
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -ti staphb/datasets-sars-cov-2:latest

# to reduce NCBI API rate-limiting, set the NCBI_API_KEY environmenal variable before running GenFSGopher.pl
export NCBI_API_KEY="<your-NCBI-API-key-here>" 

# download the smallest dataset
GenFSGopher.pl -o vocvoi-output /home/user/datasets-sars-cov-2/datasets/sars-cov-2-voivoc.tsv --numcpus 2 --layout onedir --compressed
```