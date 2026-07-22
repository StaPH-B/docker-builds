# Clair3 container

Main tool: [clair3](https://github.com/HKU-BAL/Clair3)


<details>
<summary>Additional tools installed via micromamba:</summary> 

```
List of packages in environment: "/opt/conda"

  Name                 Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────
  Jinja2               3.1.6         pypi_0                pypi       
  MarkupSafe           3.0.3         pypi_0                pypi       
  _openmp_mutex        4.5           20_gnu                conda-forge
  amply                0.1.7         pyhd8ed1ab_0          conda-forge
  backports.zstd       1.6.0         py311h6b1f9c4_0       conda-forge
  biopython            1.87          py311h49ec1c0_0       conda-forge
  boost-cpp            1.85.0        h3c6214e_4            conda-forge
  bzip2                1.0.8         hda65f42_9            conda-forge
  c-ares               1.34.8        hb03c661_0            conda-forge
  ca-certificates      2026.6.17     hbd8a1cb_0            conda-forge
  cffi                 2.1.0         pypi_0                pypi       
  coin-or-cbc          2.10.13       h4d16d09_1            conda-forge
  coin-or-cgl          0.60.10       hc46dffc_1            conda-forge
  coin-or-clp          1.17.11       hc03379b_1            conda-forge
  coin-or-osi          0.108.12      hf4fecb4_1            conda-forge
  coin-or-utils        2.11.13       hc93afbd_1            conda-forge
  docutils             0.23          pyhcf101f3_0          conda-forge
  filelock             3.29.0        pypi_0                pypi       
  fsspec               2026.4.0      pypi_0                pypi       
  h5py                 3.16.0        pypi_0                pypi       
  hdf5plugin           7.0.0         pypi_0                pypi       
  htslib               1.24          ha79157c_0            bioconda   
  icu                  75.1          he02047a_0            conda-forge
  importlib-metadata   9.0.0         pyhcf101f3_0          conda-forge
  isa-l                2.32.1        hb03c661_0            conda-forge
  keyutils             1.6.3         hb9d3cd8_0            conda-forge
  krb5                 1.22.2        hbde042b_1            conda-forge
  ld_impl_linux-64     2.46.1        default_hbd61a6d_102  conda-forge
  libblas              3.11.0        8_h4a7cf45_openblas   conda-forge
  libboost             1.85.0        h0ccab89_4            conda-forge
  libboost-devel       1.85.0        h00ab1b0_4            conda-forge
  libboost-headers     1.85.0        ha770c72_4            conda-forge
  libcblas             3.11.0        8_h0358290_openblas   conda-forge
  libcurl              8.21.0        hcf29cc6_1            conda-forge
  libdeflate           1.25          h17f619e_0            conda-forge
  libedit              3.1.20250104  pl5321h7949ede_0      conda-forge
  libev                4.33          hd590300_2            conda-forge
  libexpat             2.8.1         hecca717_1            conda-forge
  libffi               3.5.2         h3435931_0            conda-forge
  libgcc               15.2.0        he0feb66_19           conda-forge
  libgcc-ng            15.2.0        h69a702a_19           conda-forge
  libgfortran          15.2.0        h69a702a_19           conda-forge
  libgfortran5         15.2.0        h68bc16d_19           conda-forge
  libgomp              15.2.0        he0feb66_19           conda-forge
  liblapack            3.11.0        8_h47877c9_openblas   conda-forge
  liblapacke           3.11.0        8_h6ae95b6_openblas   conda-forge
  liblzma              5.8.3         hb03c661_0            conda-forge
  liblzma-devel        5.8.3         hb03c661_0            conda-forge
  libnghttp2           1.68.1        h877daf1_0            conda-forge
  libnsl               2.0.1         hb9d3cd8_1            conda-forge
  libopenblas          0.3.33        pthreads_h94d23a6_0   conda-forge
  libsqlite            3.53.3        h0c1763c_0            conda-forge
  libssh2              1.11.1        hcf80075_0            conda-forge
  libstdcxx            15.2.0        h934c35e_19           conda-forge
  libstdcxx-ng         15.2.0        hdf11a46_19           conda-forge
  libuuid              2.42.2        h5347b49_0            conda-forge
  libxcrypt            4.4.36        hd590300_1            conda-forge
  libzlib              1.3.2         h25fd6f3_2            conda-forge
  lightning-utilities  0.15.3        pypi_0                pypi       
  mpmath               1.3.0         pypi_0                pypi       
  ncurses              6.6           hdb14827_0            conda-forge
  networkx             3.6.1         pyhcf101f3_0          conda-forge
  numexpr              2.14.2        pypi_0                pypi       
  numpy                2.4.6         py311h2e04523_0       conda-forge
  openssl              3.6.3         h35e630c_0            conda-forge
  packaging            26.2          pyhc364b38_0          conda-forge
  parallel             20260722      hd8ed1ab_0            conda-forge
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
  python-zlib-ng       1.0.0         py311h15805fc_2       conda-forge
  python_abi           3.11          8_cp311               conda-forge
  pyvcf3               1.0.4         py311haab0aaa_0       bioconda   
  readline             8.3           h853b02a_0            conda-forge
  samtools             1.24          h9dcdb79_1            bioconda   
  scipy                1.17.1        py311hbe70eeb_1       conda-forge
  setuptools           83.0.0        pyh332efcf_0          conda-forge
  six                  1.17.0        pyhe01879c_1          conda-forge
  sympy                1.14.0        pypi_0                pypi       
  tk                   8.6.13        noxft_hd70dff1_3      conda-forge
  torch                2.13.0+cpu    pypi_0                pypi       
  torchmetrics         1.9.0         pypi_0                pypi       
  torchvision          0.28.0+cpu    pypi_0                pypi       
  tqdm                 4.69.0        pypi_0                pypi       
  typing_extensions    4.15.0        pypi_0                pypi       
  tzdata               2026c         h151e31d_0            conda-forge
  uv                   0.11.31       pypi_0                pypi       
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
