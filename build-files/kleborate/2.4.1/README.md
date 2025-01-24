# Kleborate container

Main tool : [Kleborate](https://github.com/katholt/Kleborate) 2.4.1

Additional tools:

- [kaptive](https://github.com/katholt/Kaptive) 2.0.8
- ncbi-blast+ 2.9.0
- [mash](https://github.com/marbl/Mash) 2.3
- python 3.8.2
- biopython 1.81

Full documentation: [https://github.com/katholt/Kleborate/wiki](https://github.com/katholt/Kleborate/wiki)

Kleborate is a tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC) for:

- MLST sequence type
- species (e.g. K. pneumoniae, K. quasipneumoniae, K. variicola, etc.)
- ICEKp associated virulence loci: yersiniabactin (ybt), colibactin (clb), salmochelin (iro), hypermucoidy (rmpA)
- virulence plasmid associated loci: salmochelin (iro), aerobactin (iuc), hypermucoidy (rmpA, rmpA2)
- antimicrobial resistance determinants: acquired genes, SNPs, gene truncations and intrinsic β-lactamases
- K (capsule) and O antigen (LPS) serotype prediction, via wzi alleles and Kaptive

## Why is there `staphb/kleborate:2.3.2` and `staphb/kleborate:2.3.2-2023-05`? What is the difference?

A small change was made to the Kleborate v2.3.2 dockerfile to account for an odd UID (1081147385) and GID (1360859114) that owns the `mash` executable and license file. This can cause problems in "rootless" environments or environments where `docker` is run inside of a docker container such as in GitPod. These environments have more limits placed on UIDs and GIDs than your typical linux computers. Error shown below:

```
$ docker pull staphb/kleborate:2.3.2
2.3.2: Pulling from staphb/kleborate
47c764472391: Pull complete 
f1582e59f07e: Pull complete 
a2c96ce05542: Pull complete 
213b944f2044: Pull complete 
e136842d98e3: Extracting [==================================================>]  1.847MB/1.847MB
d99354f29fdd: Download complete 
499193a95fe3: Download complete 
4f4fb700ef54: Download complete 
failed to register layer: ApplyLayer exit status 1 stdout:  stderr: failed to Lchown "/mash-Linux64-v2.3/LICENSE.txt" for UID 1081147385, GID 1360859114 (try increasing the number of subordinate IDs in /etc/subuid and /etc/subgid): lchown /mash-Linux64-v2.3/LICENSE.txt: invalid argument
```

The dockerfile now has a step to `chown` these files so that the `root` user owns them, which prevents these odd errors.

The updated docker image is available under the docker image name: `staphb/kleborate:2.3.2-2023-05`

## Example Usage

```bash
# run Kleborate on assembly supplied with Kleborate code
kleborate --resistance --kaptive --all \
        --assemblies /Kleborate/test/test_genomes/172.fasta.gz \
        --outfile /data/strain172-kleborate-test-out.tsv
```
