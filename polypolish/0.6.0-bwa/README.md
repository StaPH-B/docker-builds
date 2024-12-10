# polypolish container

Main tool: [polypolish](https://github.com/rrwick/Polypolish/wiki/How-to-run-Polypolish) v0.6.0

Code repository: [polypolish](https://github.com/rrwick/Polypolish)

Additional tools:

- bwa: 0.7.18
- python: 3.10

Basic information on how to use this tool:

- executable: polypolish
- help: --help
- version: --version
- description: "Polypolish "polishes" consensus files created during assembly of long reads with Illumina short reads. Polypolish is a little different than other polishing tools in that paired-end reads need to be aligned separatly to generate two sam files."

Additional information: This container also includes BWA v0.7.18 so that the user can align their short reads within the same container.

Full documentation: [https://github.com/rrwick/Polypolish/wiki](https://github.com/rrwick/Polypolish/wiki)

## Example Usage

Use the included bwa software to align reads to the draft sequence. Please note that bbamp, minimap2 or any other similar software can perform a similar step that may be better suited for your use-case.

```bash
bwa index draft.fasta
bwa mem -t 16 -a draft.fasta reads_1.fastq.gz > alignments_1.sam
bwa mem -t 16 -a draft.fasta reads_2.fastq.gz > alignments_2.sam
```

Once the sam files are generated, they can be used with polypolish.

```bash
# paired end
polypolish filter --in1 alignments_1.sam --in2 alignments_2.sam --out1 filtered_1.sam --out2 filtered_2.sam
polypolish polish draft.fasta filtered_1.sam filtered_2.sam > polished.fasta

# single end
polypolish polish draft.fasta input.sam > polished.fasta
```
