# Medaka container

Main tool : [medaka](https://github.com/nanoporetech/medaka)

Additional tools:

- bcftools version 1.21
- samtools version 1.21
- htslib version 1.21
- minimap2 version 2.28
- pyabpoa verson 1.5.3

Full documentation: [https://github.com/nanoporetech/medaka](https://github.com/nanoporetech/medaka)

> medaka is a tool to create consensus sequences and variant calls from nanopore sequencing data. This task is performed using neural networks applied a pileup of individual sequencing reads against a draft assembly. It provides state-of-the-art results outperforming sequence-graph based methods and signal-based methods, whilst also being faster.

## Example Usage

```bash
# listing models
medaka tools list\_models

# polishing
medaka_consensus -i sample.fastq.gz -d sample.fasta -o medaka/sample -t 4
```

## Medaka models

Medaka updates frequently. These are the medaka models in this image:

```
Available: r103_fast_g507, r103_fast_snp_g507, r103_fast_variant_g507, r103_hac_g507, r103_hac_snp_g507, r103_hac_variant_g507, r103_sup_g507, r103_sup_snp_g507, r103_sup_variant_g507, r1041_e82_260bps_fast_g632, r1041_e82_260bps_fast_variant_g632, r1041_e82_260bps_hac_g632, r1041_e82_260bps_hac_v4.0.0, r1041_e82_260bps_hac_v4.1.0, r1041_e82_260bps_hac_variant_g632, r1041_e82_260bps_hac_variant_v4.1.0, r1041_e82_260bps_joint_apk_ulk_v5.0.0, r1041_e82_260bps_sup_g632, r1041_e82_260bps_sup_v4.0.0, r1041_e82_260bps_sup_v4.1.0, r1041_e82_260bps_sup_variant_g632, r1041_e82_260bps_sup_variant_v4.1.0, r1041_e82_400bps_bacterial_methylation, r1041_e82_400bps_fast_g615, r1041_e82_400bps_fast_g632, r1041_e82_400bps_fast_variant_g615, r1041_e82_400bps_fast_variant_g632, r1041_e82_400bps_hac_g615, r1041_e82_400bps_hac_g632, r1041_e82_400bps_hac_v4.0.0, r1041_e82_400bps_hac_v4.1.0, r1041_e82_400bps_hac_v4.2.0, r1041_e82_400bps_hac_v4.3.0, r1041_e82_400bps_hac_v5.0.0, r1041_e82_400bps_hac_variant_g615, r1041_e82_400bps_hac_variant_g632, r1041_e82_400bps_hac_variant_v4.1.0, r1041_e82_400bps_hac_variant_v4.2.0, r1041_e82_400bps_hac_variant_v4.3.0, r1041_e82_400bps_hac_variant_v5.0.0, r1041_e82_400bps_sup_g615, r1041_e82_400bps_sup_v4.0.0, r1041_e82_400bps_sup_v4.1.0, r1041_e82_400bps_sup_v4.2.0, r1041_e82_400bps_sup_v4.3.0, r1041_e82_400bps_sup_v5.0.0, r1041_e82_400bps_sup_variant_g615, r1041_e82_400bps_sup_variant_v4.1.0, r1041_e82_400bps_sup_variant_v4.2.0, r1041_e82_400bps_sup_variant_v4.3.0, r1041_e82_400bps_sup_variant_v5.0.0, r104_e81_fast_g5015, r104_e81_fast_variant_g5015, r104_e81_hac_g5015, r104_e81_hac_variant_g5015, r104_e81_sup_g5015, r104_e81_sup_g610, r104_e81_sup_variant_g610, r941_e81_fast_g514, r941_e81_fast_variant_g514, r941_e81_hac_g514, r941_e81_hac_variant_g514, r941_e81_sup_g514, r941_e81_sup_variant_g514, r941_min_fast_g507, r941_min_fast_snp_g507, r941_min_fast_variant_g507, r941_min_hac_g507, r941_min_hac_snp_g507, r941_min_hac_variant_g507, r941_min_sup_g507, r941_min_sup_snp_g507, r941_min_sup_variant_g507, r941_prom_fast_g507, r941_prom_fast_snp_g507, r941_prom_fast_variant_g507, r941_prom_hac_g507, r941_prom_hac_snp_g507, r941_prom_hac_variant_g507, r941_prom_sup_g507, r941_prom_sup_snp_g507, r941_prom_sup_variant_g507, r941_sup_plant_g610, r941_sup_plant_variant_g610
Default consensus:  r1041_e82_400bps_sup_v5.0.0
Default variant:  r1041_e82_400bps_sup_variant_v5.0.0
```
