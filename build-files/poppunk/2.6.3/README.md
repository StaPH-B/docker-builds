# PopPUNK container

Main tool : 
- [PopPUNK](https://github.com/bacpop/PopPUNK)

Additional tools:
- biopython 1.82
- pp-sketchlib 2.1.2
- python 3.10.13
- rapidnj 2.3.2
- treeswift 1.1.39

Full documentation: [https://poppunk.readthedocs.io/en/latest/](https://poppunk.readthedocs.io/en/latest/)

PopPUNK is also available as a webtool: [https://www.poppunk.net/](https://www.poppunk.net/)

PopPUNK is a tool for clustering genomes.

*NOTE: This docker image is intended for the CLI usage of the PopPUNK tool. It has not been built with the full web-interface functionality in mind.*

## Example Usage

This example is for usage of PopPUNK for Streptococcus pneumoniae clustering using a database & reference files provided by the [Global Pneumococcal Sequencing Project](https://www.pneumogen.net/gps/training_command_line.html). An example S. pneumoniae genome can be obtained from [here](https://github.com/rpetit3/pbptyper/blob/main/test/SRR2912551.fna.gz)

```bash
# poppunk requires an input File Of File Names (FOFN). headerless TSV with a sample name (first column), followed by path to input FASTA
$ echo -e "SRR2912551\t/data/SRR2912551.fna.gz" > poppunk_input.tsv

# showing reference files, FASTA input, and poppunk_input.tsv
$ ls
GPS_v6/  GPS_v6_external_clusters.csv  SRR2912551.fna.gz  poppunk_input.tsv

# run the docker container interactively
# followed by poppunk command run inside the container
$ docker run --rm -ti -v ${PWD}:/data -u $(id -u):$(id -g) staphb/poppunk:2.6.2
$ poppunk_assign --db GPS_v6 --distances GPS_v6/GPS_v6.dists --query /data/poppunk_input.tsv --output docker_test --external-clustering GPS_v6_external_clusters.csv
PopPUNK: assign
        (with backend: sketchlib v2.0.0
         sketchlib: /opt/conda/envs/poppunk-env/lib/python3.10/site-packages/pp_sketchlib.cpython-310-x86_64-linux-gnu.so)

Graph-tools OpenMP parallelisation enabled: with 1 threads
Mode: Assigning clusters of query sequences

Loading previously refined model
Completed model loading
Sketching 1 genomes using 1 thread(s)
Progress (CPU): 1 / 1
Writing sketches to file
WARNING: versions of input databases sketches are different, results may not be compatible
Calculating distances using 1 thread(s)
Progress (CPU): 100.0%
Selected type isolate for distance QC is 10050_2#1
Network loaded: 42163 samples

Done
```
