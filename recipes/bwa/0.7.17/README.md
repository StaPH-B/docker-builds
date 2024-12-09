# bwa container

Main tool:

* [https://bio-bwa.sourceforge.net/](https://bio-bwa.sourceforge.net/)
* [GitHub](https://github.com/lh3/bwa)

## Example Usage

```bash
bwa mem ref.fa reads.fq > aln.sam

bwa aln ref.fa reads.fq > reads.sai; bwa samse ref.fa reads.sai reads.fq > aln-se.sam
```

Better documentation can be found at [https://bio-bwa.sourceforge.net/bwa.shtml](https://bio-bwa.sourceforge.net/bwa.shtml)
