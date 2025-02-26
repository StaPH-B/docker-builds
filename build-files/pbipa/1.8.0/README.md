# IPA container

Main tool: [IPA](https://github.com/PacificBiosciences/pbipa)
  
Code repository: https://github.com/PacificBiosciences/pbipa

Additional tools:
- falconc : 1.15.0
- minimap2 : 2.28-r1209
- Nighthawk : 1.0.0
- pancake : 1.6.0
- pblayout : 1.4.0
- racon : 1.5.0
- samtools : 1.20
- htslib : 1.20


Basic information on how to use this tool:
- executable: ipa
- help: -h, --help
- version: --version
- description: 
>Improved Phased Assembler (IPA) is the official PacBio software for HiFi genome assembly. IPA was designed to utilize the accuracy of PacBio HiFi reads to produce high-quality phased genome assemblies
  
Full documentation: https://github.com/PacificBiosciences/pbbioconda/wiki/Improved-Phased-Assembler

## Example Usage

```bash
ipa local --nthreads 8 --njobs 1 -i hifi.reads.[FASTA,FASTQ,BAM,XML,FOFN]
```
