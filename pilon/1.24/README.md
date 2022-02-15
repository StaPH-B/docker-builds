# pilon container

Main tool : [pilon](https://github.com/broadinstitute/pilon)

Additional tools (required):
* java

# Example Usage
(both bam files must be indexed with samtools prior to usage)
```
java -jar -Xmx16G /pilon/pilon.jar \
  --genome fasta --frags paired_bam \
  --unpaired unpaired_bam \
  --output outdir \
  --changes
```

WARNING : pilon is included as a jarfile at /pilon/pilon-${PILONVER}.jar and copied to /pilon/pilon.jar
