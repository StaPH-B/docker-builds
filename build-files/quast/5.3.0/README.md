# QUAST container

Main tool: [QUAST](https://github.com/ablab/quast)
  
Code repository: https://github.com/ablab/quast

Additional tools:
- gridss: 1.4.1


Basic information on how to use this tool:
- executable: quast.py
- help: --help
- version: --version
- description: Genome assembly evaluation tool

Additional information:

You may need a license key if you want to use GeneMark with Quast!<br>
This key can be downloaded from http://exon.gatech.edu/GeneMark/license_download.cgi page (GeneMark is free for non-commercial use).
You should choose GeneMarkS-T LINUX 64. Download your license key and add it to your data folder or another folder you will bind to the container. Inside the container, copy the key to your home folder.
```
cp  /data/gm_key_64 ~/.gm_key
```
Full documentation: https://quast.sourceforge.net/docs/manual.html

## Example Usage

```bash
# basic statistics without reference
quast.py contigs.fasta
# genome evaluation with reference
quast.py contigs.fasta -r reference.fasta.gz -g genes.gff
# metagenomic assemblies
metaquast.py contigs_1 contigs_2 ... -r reference_1,reference_2,reference_3,...
```