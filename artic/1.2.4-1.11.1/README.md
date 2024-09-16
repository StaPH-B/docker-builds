# artic fieldbioinformatics container

Main tool : [artic](https://github.com/artic-network/fieldbioinformatics)

Additional tools:

- medaka=1.11.1

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

## Medaka models

Medaka updates frequently, and artic can throw errors when corresponding ONT models are not found.

These are the medaka models in this image:
```
Available: r103_fast_g507, r103_fast_snp_g507, r103_fast_variant_g507, r103_hac_g507, r103_hac_snp_g507, r103_hac_variant_g507, r103_min_high_g345, r103_min_high_g360, r103_prom_high_g360, r103_prom_snp_g3210, r103_prom_variant_g3210, r103_sup_g507, r103_sup_snp_g507, r103_sup_variant_g507, r1041_e82_260bps_fast_g632, r1041_e82_260bps_fast_variant_g632, r1041_e82_260bps_hac_g632, r1041_e82_260bps_hac_v4.0.0, r1041_e82_260bps_hac_v4.1.0, r1041_e82_260bps_hac_variant_g632, r1041_e82_260bps_hac_variant_v4.1.0, r1041_e82_260bps_sup_g632, r1041_e82_260bps_sup_v4.0.0, r1041_e82_260bps_sup_v4.1.0, r1041_e82_260bps_sup_variant_g632, r1041_e82_260bps_sup_variant_v4.1.0, r1041_e82_400bps_fast_g615, r1041_e82_400bps_fast_g632, r1041_e82_400bps_fast_variant_g615, r1041_e82_400bps_fast_variant_g632, r1041_e82_400bps_hac_g615, r1041_e82_400bps_hac_g632, r1041_e82_400bps_hac_v4.0.0, r1041_e82_400bps_hac_v4.1.0, r1041_e82_400bps_hac_v4.2.0, r1041_e82_400bps_hac_variant_g615, r1041_e82_400bps_hac_variant_g632, r1041_e82_400bps_hac_variant_v4.1.0, r1041_e82_400bps_hac_variant_v4.2.0, r1041_e82_400bps_sup_g615, r1041_e82_400bps_sup_v4.0.0, r1041_e82_400bps_sup_v4.1.0, r1041_e82_400bps_sup_v4.2.0, r1041_e82_400bps_sup_variant_g615, r1041_e82_400bps_sup_variant_v4.1.0, r1041_e82_400bps_sup_variant_v4.2.0, r104_e81_fast_g5015, r104_e81_fast_variant_g5015, r104_e81_hac_g5015, r104_e81_hac_variant_g5015, r104_e81_sup_g5015, r104_e81_sup_g610, r104_e81_sup_variant_g610, r10_min_high_g303, r10_min_high_g340, r941_e81_fast_g514, r941_e81_fast_variant_g514, r941_e81_hac_g514, r941_e81_hac_variant_g514, r941_e81_sup_g514, r941_e81_sup_variant_g514, r941_min_fast_g303, r941_min_fast_g507, r941_min_fast_snp_g507, r941_min_fast_variant_g507, r941_min_hac_g507, r941_min_hac_snp_g507, r941_min_hac_variant_g507, r941_min_high_g303, r941_min_high_g330, r941_min_high_g340_rle, r941_min_high_g344, r941_min_high_g351, r941_min_high_g360, r941_min_sup_g507, r941_min_sup_snp_g507, r941_min_sup_variant_g507, r941_prom_fast_g303, r941_prom_fast_g507, r941_prom_fast_snp_g507, r941_prom_fast_variant_g507, r941_prom_hac_g507, r941_prom_hac_snp_g507, r941_prom_hac_variant_g507, r941_prom_high_g303, r941_prom_high_g330, r941_prom_high_g344, r941_prom_high_g360, r941_prom_high_g4011, r941_prom_snp_g303, r941_prom_snp_g322, r941_prom_snp_g360, r941_prom_sup_g507, r941_prom_sup_snp_g507, r941_prom_sup_variant_g507, r941_prom_variant_g303, r941_prom_variant_g322, r941_prom_variant_g360, r941_sup_plant_g610, r941_sup_plant_variant_g610
```
