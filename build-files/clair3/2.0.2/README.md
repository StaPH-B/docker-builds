# Clair3 container

Main tool: [clair3](https://github.com/HKU-BAL/Clair3)


<details>
<summary>Additional tools installed via micromamba:</summary> 

```
  Name                 Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────
  Jinja2               3.1.6         pypi_0                pypi       
  MarkupSafe           3.0.3         pypi_0                pypi       
  _openmp_mutex        4.5           20_gnu                conda-forge
  amply                0.1.6         pyhd8ed1ab_1          conda-forge
  backports.zstd       1.6.0         py311h6b1f9c4_0       conda-forge
  biopython            1.87          py311h49ec1c0_0       conda-forge
  boost-cpp            1.85.0        h3c6214e_4            conda-forge
  bzip2                1.0.8         hda65f42_9            conda-forge
  c-ares               1.34.6        hb03c661_0            conda-forge
  ca-certificates      2026.6.17     hbd8a1cb_0            conda-forge
  cffi                 2.0.0         pypi_0                pypi       
  coin-or-cbc          2.10.13       h4d16d09_1            conda-forge
  coin-or-cgl          0.60.10       hc46dffc_1            conda-forge
  coin-or-clp          1.17.11       hc03379b_1            conda-forge
  coin-or-osi          0.108.12      hf4fecb4_1            conda-forge
  packaging            26.2          pyhc364b38_0          conda-forge
  parallel             20260422      ha770c72_0            conda-forge
  pbzip2               1.1.13        h1fcc475_2            conda-forge
  perl                 5.32.1        7_hd590300_perl5      conda-forge
  pigz                 2.8           h421ea60_2            conda-forge
  pillow               12.2.0        pypi_0                pypi       
  pip                  26.1.2        pyh8b19718_0          conda-forge
  pulp                 2.8.0         py311h77a8cca_3       conda-forge
  pycparser            3.0           pypi_0                pypi       
  pyfaidx              0.9.0.4       pyhdfd78af_0          bioconda   
  pyparsing            3.3.2         pyhcf101f3_0          conda-forge
  pysam                0.24.0        py311h5f69268_1       bioconda   
  python               3.11.15       h7508c33_1_cpython    conda-forge
  python-isal          1.8.0         py311h49ec1c0_2       conda-forge
  python-zlib-ng       1.0.0         py311h15805fc_1       conda-forge
  python_abi           3.11          8_cp311               conda-forge
  pyvcf3               1.0.4         py311haab0aaa_0       bioconda   
  readline             8.3           h853b02a_0            conda-forge
  samtools             1.23.1        ha83d96e_0            bioconda   
  scipy                1.17.1        py311hbe70eeb_1       conda-forge
  setuptools           82.0.1        pyh332efcf_0          conda-forge
  six                  1.17.0        pyhe01879c_1          conda-forge
  sympy                1.14.0        pypi_0                pypi       
  tk                   8.6.13        noxft_h366c992_103    conda-forge
  torch                2.12.1+cpu    pypi_0                pypi       
  torchmetrics         1.9.0         pypi_0                pypi       
  torchvision          0.27.1+cpu    pypi_0                pypi       
  tqdm                 4.68.3        pypi_0                pypi       
  typing_extensions    4.15.0        pypi_0                pypi       
  tzdata               2025c         hc9c84f9_1            conda-forge
  uv                   0.11.23       pypi_0                pypi       
  whatshap             2.8           py311he264feb_0       bioconda   
  wheel                0.47.0        pyhd8ed1ab_0          conda-forge
  xopen                2.1.0         pyh707e725_0          conda-forge
  xz                   5.8.3         ha02ee65_0            conda-forge
  xz-gpl-tools         5.8.3         ha02ee65_0            conda-forge
  xz-tools             5.8.3         hb03c661_0            conda-forge
  zipp                 4.1.0         pyhcf101f3_0          conda-forge
  zlib                 1.3.2         h25fd6f3_2            conda-forge
  zlib-ng              2.3.3         hceb46e0_1            conda-forge
  zstd                 1.5.7         hb78ec9c_6            conda-forge
```
</details>
</br>

Code repository: https://github.com/HKU-BAL/Clair3

Basic information on how to use this tool:
- executable: run_clair3.sh
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: A germline small variant caller for long-reads.

Additional information:

- This container includes the following models in `/clair3/models` and `/opt/models`
- This container has no GPU support!

List of models:
```
hifi
hifi_revio
hifi_sequel2
ilmn
ont
ont_guppy5
r1041_e82_400bps_hac_v410
r1041_e82_400bps_hac_v500
r1041_e82_400bps_hac_v520_with_mv
r1041_e82_400bps_hac_v600_with_mv
r1041_e82_400bps_hac_with_mv
r1041_e82_400bps_sup_v410
r1041_e82_400bps_sup_v430_bacteria_finetuned
r1041_e82_400bps_sup_v500
r1041_e82_400bps_sup_v520_with_mv
r1041_e82_400bps_sup_with_mv
r941_prom_hac_g360+g422
r941_prom_sup_g5014
```

Full documentation: https://github.com/HKU-BAL/Clair3

## Example Usage

```bash
run_clair3.sh \
  --bam_fn=${BAM} \
  --ref_fn=${REF} \
  --threads=${THREADS} \  		     
  --platform="ont" \               ## options: {ont,hifi,ilmn}
  --model_path=${MODEL_PREFIX} \   ## absolute model path prefix
  --output=${OUTPUT_DIR}           ## absolute output path prefix
## pileup output file: ${OUTPUT_DIR}/pileup.vcf.gz
## full-alignment output file: ${OUTPUT_DIR}/full_alignment.vcf.gz
## Clair3 final output file: ${OUTPUT_DIR}/merge_output.vcf.gz
```
