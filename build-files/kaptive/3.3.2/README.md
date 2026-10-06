# Kaptive Container

Main tool: [Kaptive](https://github.com/klebgenomics/Kaptive)

Additional tools:

- minimap2 2.31
- mash 2.3

<details>
<summary>Additional tools installed via pip:</summary>

```
Package    Version
---------- -------
gb-io      0.4.0
kaptive    3.3.2
llvmlite   0.49.0
numba      0.67.0
numpy      2.5.3
pip        24.0
rammappy   0.1.3
setuptools 68.1.2
wheel      0.42.0
```

</details>


## Kaptive databases

There are few databases included in this docker image:

```
$ kaptive db ls
ab_k
kosc_k
kpsc_o
kosc_o
kpsc_k
vpar_o
ecoli_kps
vpar_k
ab_o

```
Of note, `vpar_o` and `vpar_k`
  - Located in separate GitHub repo: https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping
  - Downloaded from this location: https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping/pull/6
  - Publication: https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.001007

Example commands for each of these databases can be found below.

## Example Usage

```bash
# the basic command uses positional arguments and flags
kaptive type <database> <input fasta files> -o outfile.txt

# K locus, A. baumannii
kaptive type ab_k assembly.fasta -o outfile.txt
# O locus, A. baumannii
kaptive type ab_k assembly.fasta -o outfile.txt
```
