# Dorado container

Main tool: [dorado](https://github.com/nanoporetech/dorado)

Code repository: https://github.com/nanoporetech/dorado

Basic information on how to use this tool:
- executable: dorado
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.

Additional information:

- Cuda drivers >= 12.2.0 are required for gpu support.
- Use **"--gpus all"** flag to activate gpu support in docker. E.g.
`docker run -it --gpus all staphb/dorado:1.1.0-cuda12.2.0-no_model bash`
- support for Fast5 files and basecalling models for DNA R10.4.1 4kHz data, DNA R9.4.1, and RNA002 were removed after v0.9.6
- Below is the list of basecalling models included in the Docker image:
<details><summary>Click to see all models</summary>

```bash
variant models:
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_variant_mv@v1.0"
correction models:
  - "herro-v1"
simplex models:
  - "dna_r10.4.1_e8.2_400bps_fast@v4.2.0"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.2.0"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0"
  - "dna_r10.4.1_e8.2_400bps_fast@v4.3.0"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0"
  - "dna_r10.4.1_e8.2_400bps_fast@v5.0.0"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0"
  - "dna_r10.4.1_e8.2_apk_sup@v5.0.0"
  - "dna_r10.4.1_e8.2_400bps_fast@v5.2.0"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0"
  - "rna004_130bps_fast@v3.0.1"
  - "rna004_130bps_hac@v3.0.1"
  - "rna004_130bps_sup@v3.0.1"
  - "rna004_130bps_fast@v5.0.0"
  - "rna004_130bps_hac@v5.0.0"
  - "rna004_130bps_sup@v5.0.0"
  - "rna004_130bps_fast@v5.1.0"
  - "rna004_130bps_hac@v5.1.0"
  - "rna004_130bps_sup@v5.1.0"
  - "rna004_130bps_fast@v5.2.0"
  - "rna004_130bps_hac@v5.2.0"
  - "rna004_130bps_sup@v5.2.0"
polish models:
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_polish_rl"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_polish_rl_mv"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_polish_rl"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_polish_rl_mv"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_polish_rl"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_polish_rl_mv"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_polish_rl"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_polish_rl_mv"
  - "dna_r10.4.1_e8.2_400bps_polish_bacterial_methylation_v5.0.0"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.2.0_polish"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_polish"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_polish"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_polish"
modification models:
  - "dna_r10.4.1_e8.2_400bps_fast@v4.2.0_5mCG_5hmCG@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.2.0_5mCG_5hmCG@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mCG_5hmCG@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mCG_5hmCG@v3.1"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mC@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_6mA@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_6mA@v3"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_6mA@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_6mA@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_6mA@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_6mA@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_4mC_5mC@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_4mC_5mC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_4mC_5mC@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_4mC_5mC@v3"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_4mC_5mC@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_4mC_5mC@v3"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mC_5hmC@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mC_5hmC@v3"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mC_5hmC@v2.0.1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mC_5hmC@v3"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mCG_5hmCG@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mCG_5hmCG@v3"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mCG_5hmCG@v2.0.1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mCG_5hmCG@v3"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_6mA@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_6mA@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_6mA@v2"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_6mA@v3"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_6mA@v2"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_6mA@v3"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_4mC_5mC@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_4mC_5mC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_5mC_5hmC@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_5mCG_5hmCG@v1"
  - "dna_r10.4.1_e8.2_400bps_hac@v5.2.0_6mA@v1"
  - "dna_r10.4.1_e8.2_400bps_sup@v5.2.0_6mA@v1"
  - "rna004_130bps_sup@v3.0.1_m6A_DRACH@v1"
  - "rna004_130bps_hac@v5.0.0_m6A@v1"
  - "rna004_130bps_sup@v5.0.0_m6A@v1"
  - "rna004_130bps_hac@v5.0.0_m6A_DRACH@v1"
  - "rna004_130bps_sup@v5.0.0_m6A_DRACH@v1"
  - "rna004_130bps_hac@v5.0.0_pseU@v1"
  - "rna004_130bps_sup@v5.0.0_pseU@v1"
  - "rna004_130bps_hac@v5.1.0_m5C@v1"
  - "rna004_130bps_sup@v5.1.0_m5C@v1"
  - "rna004_130bps_hac@v5.1.0_inosine_m6A@v1"
  - "rna004_130bps_sup@v5.1.0_inosine_m6A@v1"
  - "rna004_130bps_hac@v5.1.0_m6A_DRACH@v1"
  - "rna004_130bps_sup@v5.1.0_m6A_DRACH@v1"
  - "rna004_130bps_hac@v5.1.0_pseU@v1"
  - "rna004_130bps_sup@v5.1.0_pseU@v1"
  - "rna004_130bps_sup@v5.2.0_2OmeG@v1"
  - "rna004_130bps_hac@v5.2.0_m5C@v1"
  - "rna004_130bps_sup@v5.2.0_m5C_2OmeC@v1"
  - "rna004_130bps_hac@v5.2.0_inosine_m6A@v1"
  - "rna004_130bps_sup@v5.2.0_inosine_m6A_2OmeA@v1"
  - "rna004_130bps_hac@v5.2.0_m6A_DRACH@v1"
  - "rna004_130bps_sup@v5.2.0_m6A_DRACH@v1"
  - "rna004_130bps_hac@v5.2.0_pseU@v1"
  - "rna004_130bps_sup@v5.2.0_pseU_2OmeU@v1"
stereo models:
  - "dna_r10.4.1_e8.2_5khz_stereo@v1.1"
  - "dna_r10.4.1_e8.2_5khz_stereo@v1.2"
  - "dna_r10.4.1_e8.2_5khz_stereo@v1.3"
  - "dna_r10.4.1_e8.2_5khz_stereo@v1.4"
```
</details></br>

Full documentation: https://dorado-docs.readthedocs.io/en/latest/

## Example Usage
```bash
# list models
dorado download --list
# download a single model
dorado download --model {model_name}
# download all models
dorado download
# basecaller
dorado basecaller {model} {data} > calls.bam
```