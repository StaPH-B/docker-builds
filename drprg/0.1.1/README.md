<!-- 
Please edit this readme with some basic information about the tool and how to use this container. 
- Include information about databases and additional files that are included.
- Keep it short - you don't need to recreate the documentation from the creators.
- Do not just copy and paste the readme or help for the tool. 
-->

# Dr. PRG - Drug resistance Prediction with Reference Graphs️ container

Main tool: [Dr. PRG](https://mbh.sh/drprg/)
  
Code repository: https://github.com/mbhall88/drprg

Additional tools:
- mafft version 7.505
- rasusa version 0.7.0
- seqfu version 1.16.0
- makeprg version 0.3.0
- pandora version 0.9.2

Basic information on how to use this tool:
- executable: drprg
- help: --help
- version: --version  
- description: Drug Resistance Prediction with Reference Graphs

Additional information:

Imagine contains the mtb@20230308 database. 

Full documentation: https://mbh.sh/drprg/guide/download.html

## Example Usage

```bash
# download latest TB database
drprg index --download mtb

# list available indices
drprg index --list

# prediction (paired-end fastq files much be contatenated together into one)
drprg predict -x mtb -i input.fastq.gz --illumina -o outdir/
```

