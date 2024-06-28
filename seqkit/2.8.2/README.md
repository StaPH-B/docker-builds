# SeqKit container

Main tool : [SeqKit](https://github.com/shenwei356/seqkit)

SeqKit is a cross-platform and ultrafast toolkit for FASTA/Q file manipulation.

Citation:

W Shen, S Le, Y Li*, F Hu*. SeqKit: a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. PLOS ONE. doi:10.1371/journal.pone.0163962.


- **Documents:** [http://bioinf.shenwei.me/seqkit](http://bioinf.shenwei.me/seqkit)
([**Usage**](http://bioinf.shenwei.me/seqkit/usage/),
[**FAQ**](http://bioinf.shenwei.me/seqkit/faq/),
[**Tutorial**](http://bioinf.shenwei.me/seqkit/tutorial/),
and 
[**Benchmark**](http://bioinf.shenwei.me/seqkit/benchmark/))

## Example Usage

```bash
# get simple statistics from FASTA/Q files

seqkit stats <file name(s)>

# or with flags

seqkit stats --all --tabular <file name(s)>

# conversion from FASTA to FASTQ

seqkit fa2fq <file name(s)>



```
