# QUAST slim container

Main tool: [QUAST](https://github.com/ablab/quast)
  
Code repository: https://github.com/ablab/quast

Additional tools:
- minimap2 2.24-r1122

Basic information on how to use this tool:
- executable: quast.py
- help: --help
- version: --version
- description: Genome assembly evaluation tool

Additional information:

This image provides minimal requirements of QUAST. Some of the functions may not work. Please use **staphb/quast:5.2.0** for the full functionality of the program.

Full documentation: https://quast.sourceforge.net/docs/manual.html

## Example Usage

```bash
# basic statistics without reference
quast.py contigs.fasta
# genome evaluation with reference
quast.py contigs.fasta -r reference.fasta.gz
# metagenomic assemblies
metaquast.py contigs_1 contigs_2 ... -r reference_1,reference_2,reference_3,...
```