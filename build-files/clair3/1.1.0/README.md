# Clair3 container

Main tool: [clair3](https://github.com/HKU-BAL/Clair3)


<details>
<summary>Additional tools installed via micromamba:</summary> 

```
  Name                     Version       Build                   Channel    
──────────────────────────────────────────────────────────────────────────────
  _libgcc_mutex            0.1           conda_forge             conda-forge
  _openmp_mutex            4.5           2_gnu                   conda-forge
  abseil-cpp               20210324.2    h9c3ff4c_0              conda-forge
  absl-py                  2.2.0         pyhd8ed1ab_0            conda-forge
  aiohappyeyeballs         2.6.1         pyhd8ed1ab_0            conda-forge
  aiohttp                  3.11.18       py39h9399b63_0          conda-forge
  aiosignal                1.3.2         pyhd8ed1ab_0            conda-forge
  amply                    0.1.6         pyhd8ed1ab_1            conda-forge
  astunparse               1.6.3         pyhd8ed1ab_3            conda-forge
  async-timeout            5.0.1         pyhd8ed1ab_1            conda-forge
  attrs                    25.3.0        pyh71513ae_0            conda-forge
  biopython                1.85          py39h8cd3c5a_1          conda-forge
  blinker                  1.9.0         pyhff2d567_0            conda-forge
  blosc                    1.21.5        h0f2a231_0              conda-forge
  brotli-python            1.1.0         py39hf88036b_2          conda-forge
  bzip2                    1.0.8         h4bc722e_7              conda-forge
  c-ares                   1.34.5        hb9d3cd8_0              conda-forge
  c-blosc2                 2.12.0        hb4ffafa_0              conda-forge
  ca-certificates          2025.4.26     hbd8a1cb_0              conda-forge
  cached-property          1.5.2         hd8ed1ab_1              conda-forge
  cached_property          1.5.2         pyha770c72_1            conda-forge
  cachetools               5.5.2         pyhd8ed1ab_0            conda-forge
  certifi                  2025.1.31     pyhd8ed1ab_0            conda-forge
  cffi                     1.14.4        py39he88106c_0          conda-forge
  charset-normalizer       3.4.2         pyhd8ed1ab_0            conda-forge
  click                    8.1.8         pyh707e725_0            conda-forge
  coin-or-cbc              2.10.12       h8b142ea_1              conda-forge
  coin-or-cgl              0.60.7        h516709c_0              conda-forge
  coin-or-clp              1.17.8        h1ee7a9c_0              conda-forge
  coin-or-osi              0.108.10      haf5fa05_0              conda-forge
  coin-or-utils            2.11.11       hee58242_0              conda-forge
  coincbc                  2.10.12       2_metapackage           conda-forge
  cryptography             39.0.0        py39hd598818_0          conda-forge
  docutils                 0.21.2        pyhd8ed1ab_1            conda-forge
  expat                    2.7.0         h5888daf_0              conda-forge
  frozenlist               1.5.0         py39h9399b63_1          conda-forge
  gast                     0.6.0         pyhd8ed1ab_0            conda-forge
  gdbm                     1.18          h0a1914f_2              conda-forge
  giflib                   5.2.2         hd590300_0              conda-forge
  google-auth              2.40.0        pyhd8ed1ab_0            conda-forge
  google-auth-oauthlib     0.4.6         pyhd8ed1ab_0            conda-forge
  google-pasta             0.2.0         pyhd8ed1ab_2            conda-forge
  grpc-cpp                 1.43.2        h9e046d8_3              conda-forge
  grpcio                   1.43.0        py39hff7568b_0          conda-forge
  h2                       4.2.0         pyhd8ed1ab_0            conda-forge
  h5py                     3.9.0         nompi_py39h4dfffb9_100  conda-forge
  hdf5                     1.14.0        nompi_h5231ba7_103      conda-forge
  hpack                    4.1.0         pyhd8ed1ab_0            conda-forge
  htslib                   1.17          h6bc39ce_1              bioconda   
  hyperframe               6.1.0         pyhd8ed1ab_0            conda-forge
  icu                      70.1          h27087fc_0              conda-forge
  idna                     3.10          pyhd8ed1ab_1            conda-forge
  importlib-metadata       8.6.1         pyha770c72_0            conda-forge
  isa-l                    2.31.1        hb9d3cd8_1              conda-forge
  jpeg                     9e            h0b41bf4_3              conda-forge
  keras                    2.8.0         pyhd8ed1ab_0            conda-forge
  keras-preprocessing      1.1.2         pyhd8ed1ab_1            conda-forge
  keyutils                 1.6.1         h166bdaf_0              conda-forge
  krb5                     1.20.1        hf9c8cef_0              conda-forge
  ld_impl_linux-64         2.43          h712a8e2_4              conda-forge
  libaec                   1.1.3         h59595ed_0              conda-forge
  libblas                  3.9.0         31_h59b9bed_openblas    conda-forge
  libcblas                 3.9.0         31_he106b2a_openblas    conda-forge
  libcurl                  7.87.0        h6312ad2_0              conda-forge
  libdeflate               1.23          h86f0d12_0              conda-forge
  libedit                  3.1.20250104  pl5321h7949ede_0        conda-forge
  libev                    4.33          hd590300_2              conda-forge
  libexpat                 2.7.0         h5888daf_0              conda-forge
  libffi                   3.2.1         he1b5a44_1007           conda-forge
  libgcc                   14.2.0        h767d61c_2              conda-forge
  libgcc-ng                14.2.0        h69a702a_2              conda-forge
  libgfortran              14.2.0        h69a702a_2              conda-forge
  libgfortran-ng           14.2.0        h69a702a_2              conda-forge
  libgfortran5             14.2.0        hf1ad2bd_2              conda-forge
  libgomp                  14.2.0        h767d61c_2              conda-forge
  liblapack                3.9.0         31_h7ac8fdf_openblas    conda-forge
  liblapacke               3.9.0         31_he2f377e_openblas    conda-forge
  libnghttp2               1.51.0        hdcd2b5c_0              conda-forge
  libopenblas              0.3.29        pthreads_h94d23a6_0     conda-forge
  libpng                   1.6.43        h2797004_0              conda-forge
  libprotobuf              3.19.6        h3eb15da_0              conda-forge
  libsqlite                3.46.0        hde9e2c9_0              conda-forge
  libssh2                  1.10.0        haa6b8db_3              conda-forge
  libstdcxx                14.2.0        h8f9b012_2              conda-forge
  libstdcxx-ng             14.2.0        h4852527_2              conda-forge
  libxcrypt                4.4.36        hd590300_1              conda-forge
  libzlib                  1.2.13        h4ab18f5_6              conda-forge
  lz4-c                    1.9.4         hcb278e6_0              conda-forge
  lzo                      2.10          hd590300_1001           conda-forge
  markdown                 3.8           pyhd8ed1ab_0            conda-forge
  markupsafe               3.0.2         py39h9399b63_1          conda-forge
  multidict                6.4.3         py39h9399b63_0          conda-forge
  ncurses                  6.5           h2d0b736_3              conda-forge
  networkx                 3.2.1         pyhd8ed1ab_0            conda-forge
  nomkl                    1.0           h5ca1d4c_0              conda-forge
  numexpr                  2.10.2        py39h0a7e20a_100        conda-forge
  numpy                    1.24.3        py39h6183b62_0          conda-forge
  oauthlib                 3.2.2         pyhd8ed1ab_1            conda-forge
  openssl                  1.1.1w        hd590300_0              conda-forge
  opt_einsum               3.4.0         pyhd8ed1ab_1            conda-forge
  packaging                25.0          pyh29332c3_1            conda-forge
  parallel                 20191122      0                       conda-forge
  pbzip2                   1.1.13        h1fcc475_2              conda-forge
  perl                     5.32.1        7_hd590300_perl5        conda-forge
  pigz                     2.8           h2797004_0              conda-forge
  pip                      25.1.1        pyh8b19718_0            conda-forge
  propcache                0.3.1         py39h9399b63_0          conda-forge
  protobuf                 3.19.6        py39h227be39_0          conda-forge
  pulp                     2.8.0         py39hf3d152e_0          conda-forge
  py-cpuinfo               9.0.0         pyhd8ed1ab_1            conda-forge
  pyasn1                   0.6.1         pyhd8ed1ab_2            conda-forge
  pyasn1-modules           0.4.2         pyhd8ed1ab_0            conda-forge
  pycparser                2.22          pyh29332c3_1            conda-forge
  pyfaidx                  0.8.1.4       pyhdfd78af_0            bioconda   
  pyjwt                    2.10.1        pyhd8ed1ab_0            conda-forge
  pyopenssl                23.2.0        pyhd8ed1ab_1            conda-forge
  pyparsing                3.2.3         pyhd8ed1ab_1            conda-forge
  pypy3.6                  7.3.2         h45e8706_2              conda-forge
  pysam                    0.21.0        py39h9abd093_0          bioconda   
  pysocks                  1.7.1         pyha55dd90_7            conda-forge
  pytables                 3.8.0         py39hac3db9e_1          conda-forge
  python                   3.9.0         h2a148a8_4_cpython      conda-forge
  python-flatbuffers       25.2.10       pyhbc23db3_0            conda-forge
  python-isal              1.7.2         py39h8cd3c5a_0          conda-forge
  python-zlib-ng           0.4.3         py39h520f041_0          conda-forge
  python_abi               3.9           7_cp39                  conda-forge
  pyu2f                    0.1.5         pyhd8ed1ab_1            conda-forge
  pyvcf3                   1.0.3         pyhdfd78af_0            bioconda   
  re2                      2022.02.01    h9c3ff4c_0              conda-forge
  readline                 8.2           h8c095d6_2              conda-forge
  requests                 2.32.3        pyhd8ed1ab_1            conda-forge
  requests-oauthlib        2.0.0         pyhd8ed1ab_1            conda-forge
  rsa                      4.9.1         pyhd8ed1ab_0            conda-forge
  samtools                 1.15.1        h6899075_1              bioconda   
  scipy                    1.13.1        py39haf93ffa_0          conda-forge
  setuptools               80.1.0        pyhff2d567_0            conda-forge
  six                      1.17.0        pyhd8ed1ab_0            conda-forge
  snappy                   1.1.10        hdb0a2a9_1              conda-forge
  sqlite                   3.46.0        h6d4b2fc_0              conda-forge
  tensorboard              2.8.0         pyhd8ed1ab_1            conda-forge
  tensorboard-data-server  0.6.1         py39hd97740a_4          conda-forge
  tensorboard-plugin-wit   1.8.1         pyhd8ed1ab_0            conda-forge
  tensorflow               2.8.0         cpu_py39h4655687_0      conda-forge
  tensorflow-addons        0.23.0        pypi_0                  pypi       
  tensorflow-base          2.8.0         cpu_py39h7e02d9e_0      conda-forge
  tensorflow-cpu           2.8.0         cpu_py39h718b53a_0      conda-forge
  tensorflow-estimator     2.8.0         cpu_py39heaff504_0      conda-forge
  termcolor                3.1.0         pyhd8ed1ab_0            conda-forge
  tk                       8.6.13        noxft_h4845f30_101      conda-forge
  typing-extensions        4.13.2        h0e9735f_0              conda-forge
  typing_extensions        4.13.2        pyh29332c3_0            conda-forge
  tzdata                   2025b         h78e105d_0              conda-forge
  urllib3                  2.4.0         pyhd8ed1ab_0            conda-forge
  werkzeug                 3.1.3         pyhd8ed1ab_1            conda-forge
  whatshap                 1.7           py39h1f90b4d_1          bioconda   
  wheel                    0.45.1        pyhd8ed1ab_1            conda-forge
  wrapt                    1.17.2        py39h8cd3c5a_0          conda-forge
  xopen                    2.0.2         pyh707e725_2            conda-forge
  xz                       5.2.6         h166bdaf_0              conda-forge
  yarl                     1.20.0        py39h9399b63_0          conda-forge
  zipp                     3.21.0        pyhd8ed1ab_1            conda-forge
  zlib                     1.2.13        h4ab18f5_6              conda-forge
  zlib-ng                  2.0.7         h0b41bf4_0              conda-forge
  zstandard                0.23.0        py39h8cd3c5a_2          conda-forge
  zstd                     1.5.6         ha6fb4c9_0              conda-forge
```
</details>
</br>

Code repository: https://github.com/HKU-BAL/Clair3

Basic information on how to use this tool:
- executable: run_clair3.sh
- help: -h, --help
- version: -v, --version
- description: 

Additional information:

This container includes the following models in `/clair3/models`

```
hifi
hifi_revio
hifi_sequel2
ilmn
ont
ont_guppy2
ont_guppy5
r941_prom_hac_g238
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
