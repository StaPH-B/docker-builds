# pbsim3 container

Main tool: [pbsim3](https://github.com/yukiteruono/pbsim3)
  
Code repository: https://github.com/yukiteruono/pbsim3

Additional tools:
- none

Basic information on how to use this tool:
- executable: `pbsim`
- help: 
- version:
- description: PBSIM can simulate whole genome sequencing (WGS) and transcriptome sequencing (TS) of the PacBio RS II continuous long reads (CLR), PacBio Sequel CLR, PacBio Sequel high-fidelity (HiFi) reads, and ONT reads. 
 
Full documentation: https://github.com/yukiteruono/pbsim3

## Example Usage

```bash
pbsim --strategy wgs 
      --method qshmm
      --qshmm /method/QSHMM-RSII.model
      --depth 20
      --genome sample/sample.fasta
```
