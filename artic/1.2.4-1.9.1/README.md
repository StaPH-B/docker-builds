# artic fieldbioinformatics container

Main tool : [artic](https://github.com/artic-network/fieldbioinformatics)

Additional tools:

- medaka=1.9.1

Full documentation: [https://github.com/artic-network/fieldbioinformatics](https://github.com/artic-network/fieldbioinformatics)

There is also a very useful SOP: [https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html](https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html)
And additional documentation: [https://artic.readthedocs.io/en/latest/](https://artic.readthedocs.io/en/latest/)

> A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore.

WARNING : This container does not contain the primer schemes found at [https://github.com/artic-network/primer-schemes](https://github.com/artic-network/primer-schemes). Those will have to be downloaded and mounted separately.

## Example Usage with the artic primers

```bash
# get primers
git clone https://github.com/artic-network/primer-schemes

# download reads for example
wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR224/050/SRR22452250/SRR22452250_1.fastq.gz

# read filtering
docker run -v $(pwd):/data staphb/artic:latest artic guppyplex --min-length 400 --max-length 700  --directory . --prefix SRR22452250_1.fastq.gz --output SRR22452250_1_filtered.fastq.gz

# running the artic minion workflow with medaka
docker run -v $(pwd):/data staphb/artic:latest artic minion --normalise 200 --skip-nanopolish --medaka --medaka-model r941_min_high_g360 --threads 4 --read-file SRR22452250_1_filtered.fastq.gz --scheme-directory primer-schemes --scheme-version 5.3.2 nCoV-2019 test

# the result files will all start with test*
```

In general, any primer scheme can be used as long as it meeds [artic's requirments](https://github.com/artic-network/primer-schemes).

This is the recommended directory structure with corresponding files:

```bash
${diretory}/${name}/V${version}/${name}.primer.bed
${diretory}/${name}/V${version}/${name}.scheme.bed
${diretory}/${name}/V${version}/${name}.reference.fasta
${diretory}/${name}/V${version}/${name}.reference.fasta.fai
```

The command to use this primer scheme would be

```bash
artic minion --normalise 200 --skip-nanopolish --medaka --medaka-model r941_min_high_g360 --threads 4 --read-file input.fastq.gz --scheme-directory ${directory} --scheme-version ${version} ${name} outputprefix
```

Different primer schemes can be validated via artic-tools (already in PATH) via

```bash
artic-tools validate_scheme ${basename}.primer.bed --outputInserts ${basename}.insert.bed
```
