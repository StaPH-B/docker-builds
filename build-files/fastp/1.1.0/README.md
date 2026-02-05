# fastp container

Main tool : [fastp](https://github.com/OpenGene/fastp)

Code repository: https://github.com/OpenGene/fastp

Additional tools:
- jq: 1.6

Basic information on how to use this tool:
- executable: `fastp`
- help: `-?` , `--helpfastp `
- version: `-v` , `--version`
- description: A tool designed to provide ultrafast all-in-one preprocessing and quality control for FastQ data.

Additional information:

Shifu Chen. 2023. Ultrafast one-pass FASTQ data preprocessing, quality control, and deduplication using fastp. iMeta 2: e107. https://doi.org/10.1002/imt2.107

Shifu Chen, Yanqing Zhou, Yaru Chen, Jia Gu; fastp: an ultra-fast all-in-one FASTQ preprocessor, Bioinformatics, Volume 34, Issue 17, 1 September 2018, Pages i884–i890, https://doi.org/10.1093/bioinformatics/bty560
  
Full documentation: https://github.com/OpenGene/fastp

## Example Usage

```bash
fastp -i SRR13957123_1.fastq.gz -I SRR13957123_2.fastq.gz -o SRR13957123_PE1.fastq.gz -O SRR13957123_PE2.fastq.gz -h SRR13957123_fastp.html -j SRR13957123_fastp.json
```
