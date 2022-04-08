# SerotypeFinder container

Main tool : [SerotypeFinder](https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/)

Additional tools:
- ncbi-blast
- kma 

Full documentation: https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/

A docker container that contains SerotypeFinder, a tool for serotyping E. coli isolates from reads or assemblies

# Example Usage

```
# make an output directory
mkdir output-dir-reads output-dir-asm

# query reads
serotypefinder.py -i /data/E-coli.R1.fastq.gz /data/E-coli.R2.fastq.gz -o /data/output-dir-reads

# query assembly
serotypefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```

## Notes and Recommendations
  * You do not need to supply a database or use the `-p` or `-d` flags
    * Database is included in the container and is in the default/expected location within the container: `/database`
    * (*NOT RECOMMENDED*) If you do need to use your own database, you will need to first index it with `kma` and use the `serotypefinder.py -p` flag. You can find instructions for this on the SerotypeFinder Bitbucket README. `kma` is included in this docker container for database indexing.
  * SerotypeFinder does **NOT** create an output directory when you use the `-o` flag. You MUST create it beforehand or it will throw an error.
  * **Default % Identity threshold: 90%**. Adjust with `-t 0.95`
  * **Default % coverage threshold: 60%**. Adjust with `-l 0.70`
  * Use the `-x` flag (extended output) if you want the traditional/legacy SerotypeFinder output files `results_tab.tsv  results.txt  Serotype_allele_seq.fsa  Hit_in_genome_seq.fsa`. Otherwise you will need to parse the default output file `data.json` for results
  * (*RECOMMENDED*) Use raw reads due to the increased sensitivity (without loss of specificity) and the additional information gleaned from KMA output (specifically the depth metric). You also save time from having to assemble the genome first. [CITATION NEEDED, PROBABLY THE KMA PAPER]
  * Querying reads:
    * This will run SerotypeFinder with `kma` (instead of ncbi-blast+)
    * Only one of the PE read files is necessary. There is likely little benefit to using both R1 and R2. It will take slightly longer to run (a few extra seconds) if you use both R1 and R2 files.
  * Querying assemblies:
    * This will run SerotypeFinder with `ncbi-blast+`
    * SerotypeFinder does not clean up after itself. `tmp/out_H_type.xml` and `tmp/out_O_type.xml` will exist in the specified output directory
