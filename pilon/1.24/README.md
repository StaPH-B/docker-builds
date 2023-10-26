# pilon container

Main tool : [pilon](https://github.com/broadinstitute/pilon)

Additional tools (required):

* java (specifically `openjdk-11-jre`)

## Example Usage

Note: both BAM files must be indexed with `samtools index` prior to usage

```bash
java -jar -Xmx16G /pilon/pilon.jar \
  --genome fasta --frags paired_bam \
  --unpaired unpaired_bam \
  --output outdir \
  --changes
```

WARNING : pilon is included as a jarfile at `/pilon/pilon-${PILONVER}.jar` and copied to `/pilon/pilon.jar`

Also, memory issues are common with pilon. From their [documentation](https://github.com/broadinstitute/pilon/wiki/Requirements-&-Usage):
> Generally, bacterial genomes with ~200x of Illumina coverage will require at least 8GB, though 16GB is recommended.
> Larger genomes will require more memory to process; exactly how much is very data-dependent, but as a rule of thumb, try to allocate 1GB per megabase of input genome to be processed.
