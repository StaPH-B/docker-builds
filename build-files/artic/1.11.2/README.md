# artic fieldbioinformatics container

Main tool : [artic](https://github.com/artic-network/fieldbioinformatics)

Full documentation: [https://github.com/artic-network/fieldbioinformatics](https://github.com/artic-network/fieldbioinformatics)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/artic"

  Name                       Version       Build                       Channel    
────────────────────────────────────────────────────────────────────────────────────
  _openmp_mutex              4.5           8_kmp_llvm                  conda-forge
  _python_abi3_support       1.0           hd8ed1ab_3                  conda-forge
  align_trim                 1.2.0         pyhdfd78af_0                bioconda   
  amply                      0.1.7         pyhd8ed1ab_0                conda-forge
  annotated-types            0.8.0         pyhd8ed1ab_0                conda-forge
  args                       0.1.0         pyhd8ed1ab_1004             conda-forge
  artic                      1.11.2        pyhdfd78af_0                bioconda   
  attrs                      26.1.0        pyhcf101f3_0                conda-forge
  aws-c-auth                 0.10.4        h4610da3_2                  conda-forge
  aws-c-cal                  0.9.15        h6bbde05_1                  conda-forge
  aws-c-common               0.14.3        hb03c661_0                  conda-forge
  aws-c-compression          0.3.2         h01ee8f8_5                  conda-forge
  aws-c-http                 0.11.0        hbe094ff_5                  conda-forge
  aws-c-io                   0.27.5        h4f381ba_1                  conda-forge
  aws-c-s3                   0.13.1        h7508075_1                  conda-forge
  spectra                    0.0.11        pyhd8ed1ab_2                conda-forge
  sqlite                     3.53.4        h9ffa6c4_1                  conda-forge
  sympy                      1.14.0        pyh2585a3b_106              conda-forge
  sysroot_linux-64           2.39          hc4b9eeb_6                  conda-forge
  tbb                        2023.1.0      hfd44327_0                  conda-forge
  tiktoken                   0.14.0        py311hc3af579_1             conda-forge
  tk                         8.6.13        noxft_h1df4ec4_4            conda-forge
  tomli                      2.4.1         pyhcf101f3_0                conda-forge
  torchmetrics               1.9.0         pyhd8ed1ab_0                conda-forge
  tqdm                       4.70.1        pyhfa0c392_0                conda-forge
  typeguard                  4.6.0         pyhcf101f3_0                conda-forge
  typing-extensions          4.16.0        h69aa097_0                  conda-forge
  typing-inspection          0.4.4         pyhcf101f3_0                conda-forge
  typing_extensions          4.16.0        pyhcf101f3_0                conda-forge
  tzdata                     2026c         h151e31d_0                  conda-forge
  urllib3                    2.8.0         pyhd8ed1ab_0                conda-forge
  whatshap                   2.8           py311he264feb_0             bioconda   
  wheel                      0.48.0        pyhd8ed1ab_0                conda-forge
  xopen                      2.1.0         pyh707e725_0                conda-forge
  xorg-libxau                1.0.12        h7cc23a3_2                  conda-forge
  xorg-libxdmcp              1.1.5         h7cc23a3_2                  conda-forge
  yaml                       0.2.5         hebe6cf0_3                  conda-forge
  zipp                       4.1.0         pyhcf101f3_0                conda-forge
  zlib-ng                    2.3.3         hce19668_1                  conda-forge
  zstd                       1.5.7         hb78ec9c_7                  conda-forge
```
</details>


There is also a very useful SOP: [https://artic.network/fieldbioinformatics/fieldbioinformatics-sop.html](https://artic.network/fieldbioinformatics/fieldbioinformatics-sop.html)

And additional documentation: [https://artic.readthedocs.io/en/latest/](https://artic.readthedocs.io/en/latest/)

> A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore.

WARNING : This container does not contain the primer schemes found at [https://github.com/artic-network/primer-schemes](https://github.com/artic-network/primer-schemes). Those will have to be downloaded and mounted separately. There are now commands to download the use the primers at runtime.

This image DOES contain the models downloaded with `artic_get_models`

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

## Clair3 models

Artic uses [Clair3](https://github.com/HKU-BAL/Clair3), which uses its own models for polishing. ONT chemistries update frequently, and artic can throw errors when corresponding ONT models are not found.

These are the models in this image:

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
r1041_e82_400bps_fast_g615
r1041_e82_400bps_fast_g632
r1041_e82_400bps_hac_g615
r1041_e82_400bps_hac_g632
r1041_e82_400bps_hac_v400
r1041_e82_400bps_hac_v410
r1041_e82_400bps_hac_v420
r1041_e82_400bps_hac_v430
r1041_e82_400bps_hac_v500
r1041_e82_400bps_hac_v520
r1041_e82_400bps_hac_v520_with_mv
r1041_e82_400bps_hac_v600
r1041_e82_400bps_hac_v600_with_mv
r1041_e82_400bps_hac_with_mv
r1041_e82_400bps_sup_g615
r1041_e82_400bps_sup_v400
r1041_e82_400bps_sup_v410
r1041_e82_400bps_sup_v420
r1041_e82_400bps_sup_v430
r1041_e82_400bps_sup_v430_bacteria_finetuned
r1041_e82_400bps_sup_v500
r1041_e82_400bps_sup_v520
r1041_e82_400bps_sup_v520_with_mv
r1041_e82_400bps_sup_with_mv
r104_e81_hac_g5015
r104_e81_sup_g5015
r941_prom_hac_g360+g422
r941_prom_sup_g5014
```
