# Shovill v1.4.2 docker image

Main tool : [Shovill](https://github.com/tseemann/shovill)

Additional tools:

- [bwa](https://github.com/lh3/bwa/) 0.7.19
- [kmc](https://github.com/refresh-bio/KMC) 3.2.4
- [lighter](https://github.com/mourisl/Lighter) 1.1.3
- [megahit](https://github.com/voutcn/megahit) 1.2.9
- perl 5.34.0
- [pilon](https://github.com/broadinstitute/pilon) 1.24
- python 3.10.42
- [samclip](https://github.com/tseemann/samclip) 0.4.0
- [samtools](https://github.com/samtools/samtools) 1.16.1
- [seqkit](https://github.com/shenwei356/seqkit) 2.12.0
- [SKESA and gfa_connector](https://github.com/ncbi/SKESA) 2.5.0
- [SPAdes](https://github.com/ablab/spades) 3.15.5
- [trimmomatic](https://github.com/usadellab/Trimmomatic) 0.40
- [velvet](https://github.com/dzerbino/velvet) 1.2.10

Full documentation: [https://github.com/tseemann/shovill](https://github.com/tseemann/shovill)

> *Assemble bacterial isolate genomes from Illumina paired-end reads*

## Example Usage

```bash
# run shovill on the test FASTQ files bundled with shovill
shovill --outdir /data/out.spades --assembler spades --R1 /shovill-1.1.0/test/R1.fq.gz --R2 /shovill-1.1.0/test/R2.fq.gz
```
