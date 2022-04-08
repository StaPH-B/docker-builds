# GNU parallel container

Main tool : [GNU parallel](https://www.gnu.org/software/parallel)

Additional tools:
- perl
- will add python3 on request

Allows easy parallelization of command line.

# Example Usage

If there was a file like sample_ids.txt with the following text

```
Sample_Id Alternative_Id
12345 X0987
23456 X9876
34567 X8765
```
And a bunch of fasta files:
```
12345.fa
23456.fa
34567.fa
```

```
grep -v "Sample_Id" | parallel --colsep "\t" "cp {1}.fa {2}.fa"
```

Will create the following fasta files:
```
X0987.fa
X9876.fa
X8765.fa
```
