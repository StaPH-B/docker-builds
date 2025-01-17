# samtools container

Main tool:

* [https://www.htslib.org/](https://www.htslib.org/)
* [https://github.com/samtools/samtools](https://github.com/samtools/samtools)

Additional tools:

* perl 5.34.0

## Note about `staphb/samtools:1.17-2023-06`

This docker image is considerably smaller than the original `staphb/samtools:1.17` docker image that was built using `samtools/1.17/Dockerfile`. Many unnecessary programs were removed and a `builder` stage was added for compiling & building the `samtools` executables. Programs such as `python3` and `gawk` are no longer included in the final docker image.

If your workflows are failing, it may be because these programs were removed from the docker image to reduce the image size. We recommend using a different docker image (such as the docker image `staphb/samtools:1.17`!) if your pipeline requires the use of `python3` or another program that was removed.

## Example Usage

```bash
samtools ampliconclip -b bed.file input.bam

samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
```

Better documentation can be found at [https://www.htslib.org/doc/samtools.html](https://www.htslib.org/doc/samtools.html)