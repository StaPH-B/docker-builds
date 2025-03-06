# artic fieldbioinformatics container

Main tool : [artic](https://github.com/artic-network/fieldbioinformatics)

Full documentation: [https://github.com/artic-network/fieldbioinformatics](https://github.com/artic-network/fieldbioinformatics)

There is also a very useful SOP: [https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html](https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html)
And additional documentation: [https://artic.readthedocs.io/en/latest/](https://artic.readthedocs.io/en/latest/)

> A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore.

WARNING : This container does not contain the primer schemes found at [https://github.com/artic-network/primer-schemes](https://github.com/artic-network/primer-schemes). Those will have to be downloaded and mounted separately. There are now commands to download the use the primers at runtime.

This image DOES contain the medaka models downloaded with `artic_get_models`

## Example Usage with the artic primers

```bash
# filtering reads
artic guppyplex --min-length 400 --max-length 700  --directory . --prefix SRR22452250_1.fastq.gz --output SRR22452250_1_filtered.fastq

# downloading medaka models for clair3
artic_get_models

# running the artic minion workflow
# the result files will all start with test*
artic minion --normalise 200 --medaka-model ont --threads 4 --read-file sample.fastq --scheme-directory primer-schemes --scheme-version 5.3.2 nCoV-2019 test

# running the artic minion workflow with user-provided primer bedfiles and references
artic minion --normalise 200 --threads 4  --model ont --read-file sample.fastq --scheme-name sars-cov-2  --scheme-version  V5.3.2 name

```

In general, any primer scheme can be used as long as it meets [artic's requirements](https://github.com/artic-network/primer-schemes).

## Medaka models

Artic uses [Clair3](https://github.com/HKU-BAL/Clair3), which uses medaka models. Medaka updates frequently, and artic can throw errors when corresponding ONT models are not found.

These are the medaka models in this image:

```bash
# included models at /opt/conda/envs/artic/bin/models
hifi
hifi_revio
hifi_sequel2
ilmn
ont
ont_guppy5
r1041_e82_260bps_fast_g632
r1041_e82_260bps_hac_g632
r1041_e82_260bps_hac_v400
r1041_e82_260bps_hac_v410
r1041_e82_260bps_sup_g632
r1041_e82_260bps_sup_v400
r1041_e82_260bps_sup_v410
r1041_e82_400bps_fast_g632
r1041_e82_400bps_hac_g615
r1041_e82_400bps_hac_g632
r1041_e82_400bps_hac_v400
r1041_e82_400bps_hac_v410
r1041_e82_400bps_hac_v420
r1041_e82_400bps_hac_v430
r1041_e82_400bps_hac_v500
r1041_e82_400bps_sup_g615
r1041_e82_400bps_sup_v400
r1041_e82_400bps_sup_v410
r1041_e82_400bps_sup_v420
r1041_e82_400bps_sup_v430
r1041_e82_400bps_sup_v500
r104_e81_hac_g5015
r104_e81_sup_g5015
r941_prom_hac_g360+g422
r941_prom_sup_g5014
```
