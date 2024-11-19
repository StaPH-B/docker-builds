# assembly_snptyper container

Main tool: [assembly_snptyper](https://github.com/boasvdp/assembly_snptyper)
  
Code repository: https://github.com/boasvdp/assembly_snptyper

Additional tools:
- samtools: 1.19
- minimap2: 2.28

Basic information on how to use this tool:
- executable: assembly_snptyper
- help: -h
- version: -v
- description: |

> This software can take a bacterial genome assembly in fasta format, align it to a reference genome and search for specific SNPs based on the alignment. It uses minimap2 and samtools to do this. You would typically only run this tool instead of a read mapping tool if you don't have access to the sequence reads.


> The tool was written with M1UK typing in mind. In this specific case, the reference genome is an M1global strain, from which M1UK can be discerned by only 27 lineage-specific SNPs. Important assumptions here are that the type of interest (here, M1UK) is closely related to the reference genome, warranting the use of the asm5 preset for minimap2.

Additional information:

M1UK reference and SNP vcf are located in /assembly_snptyper/data
  
Full documentation: https://github.com/boasvdp/assembly_snptyper

## Example Usage

```bash
# with a list of fasta files listed in fastas.txt
assembly_snptyper --list_input fastas.txt -p 20 --reference /assembly_snptyper/data/MGAS5005.fa --vcf /assembly_snptyper/data/M1UK.vcf > m1uk.txt
```

