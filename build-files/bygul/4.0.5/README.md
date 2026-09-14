# Bygul container

Main tool: [Bygul](https://github.com/andersen-lab/Bygul)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/bygul-env"

  Name              Version      Build                 Channel    
────────────────────────────────────────────────────────────────────
  _openmp_mutex     4.5          20_gnu                conda-forge
  art               2016.06.05   h0704011_13           bioconda   
  biopython         1.88         py314h89acca1_1       conda-forge
  bygul             4.0.5        pyhdfd78af_0          bioconda   
  bzip2             1.0.8        hda65f42_10           conda-forge
  ca-certificates   2026.7.22    hbd8a1cb_0            conda-forge
  click             8.5.0        pyh5ded981_0          conda-forge
  gsl               2.7          he838d99_0            conda-forge
  icu               78.3         py310h44b86e0_2       conda-forge
  ld_impl_linux-64  2.46.1       default_hbd61a6d_102  conda-forge
  libblas           3.11.0       11_h4a7cf45_openblas  conda-forge
  libcblas          3.11.0       11_h0358290_openblas  conda-forge
  libexpat          2.8.1        hecca717_1            conda-forge
  libffi            3.7.0        h81df57d_1            conda-forge
  libgcc            16.2.0       ha9f2e26_4            conda-forge
  libgcc-ng         16.2.0       h69a702a_4            conda-forge
  libgfortran       16.2.0       h69a702a_4            conda-forge
  libgfortran5      16.2.0       h6b99dfc_4            conda-forge
  libgomp           16.2.0       he0feb66_4            conda-forge
  liblapack         3.11.0       11_h47877c9_openblas  conda-forge
  liblzma           5.8.3        hb03c661_1            conda-forge
  libmpdec          4.0.0        hb03c661_2            conda-forge
  libopenblas       0.3.34       pthreads_hf13c14d_2   conda-forge
  libpython         3.14.7       hdc7f604_106_cp314    conda-forge
  libsqlite         3.53.4       h13e7031_1            conda-forge
  libstdcxx         16.2.0       h934c35e_4            conda-forge
  libuuid           2.42.3       hcfc3c73_0            conda-forge
  libxcrypt         4.4.38       h280c20c_0            conda-forge
  libzlib           1.3.2        h25fd6f3_3            conda-forge
  mason             2.0.13       h7f3286b_0            bioconda   
  ncurses           6.6          hdb14827_1            conda-forge
  numpy             2.5.3        py314hd3a7d6b_0       conda-forge
  openssl           3.6.4        h781a0a9_0            conda-forge
  pandas            3.0.5        py314hb4ffadd_1       conda-forge
  perl              5.32.1       9_h7cc23a3_perl5      conda-forge
  pip               26.2.1       pyh145f28c_0          conda-forge
  python            3.14.7       hcd007b5_106_cp314    conda-forge
  python-dateutil   2.9.0.post0  pyhe01879c_2          conda-forge
  python_abi        3.14         9_cp314               conda-forge
  readline          8.3          hd6e31c0_1            conda-forge
  regex             2026.9.10    py314h89acca1_0       conda-forge
  six               1.17.0       pyhe01879c_1          conda-forge
  tk                8.6.13       noxft_h1df4ec4_4      conda-forge
  tqdm              4.70.1       pyhfa0c392_0          conda-forge
  tzdata            2026c        h151e31d_0            conda-forge
  wgsim             1.0          h577a1d6_10           bioconda   
  zstd              1.5.7        hb78ec9c_7            conda-forge
```

</details>

Full documentation: https://github.com/andersen-lab/Bygul

Bygul is a Python 3 tool designed for simulating sequencing reads in wastewater surveillance and other metagenomic applications. It allows users to simulate complex multi-sample datasets with customizable proportions using industry-standard backends like `wgsim` and `mason` and `art`.

## Example Usage

```bash
bygul simulate-proportions --genomes [SAMPLE1.fasta,SAMPLE2.fasta] --primers [primer.bed] --proportions [0.8,0.2] --outdir [output_dir]
```

### Advanced Examples
* **Random Proportions & Mismatches:**
    Simulate with random proportions and allow up to 2 SNPs in primer regions.
    ```bash
    bygul simulate-proportions --genomes sample1.fasta,sample2.fasta --primers primer.bed --reference reference.fasta --outdir results/ --maxmismatch 2
    ```
* **Switching Simulators:**
    Use `mason` instead of the default `wgsim`.
    ```bash
    bygul simulate-proportions --genomes sample1.fasta,sample2.fasta --primers primer.bed --simulator mason
    ```
* **Custom Error Rates & Lengths:**
    Pass simulator-specific parameters (e.g. indel fraction `-R`) directly.
    ```bash
    bygul simulate-proportions --genomes sample1.fasta,sample2.fasta --primers primer.bed -R 0.01
    ```
* **Using a csv file and all samples in a multi-fasta file:**
    ```bash
    bygul simulate-proportions --csv samples.csv --multifasta samples.fasta
    ```
