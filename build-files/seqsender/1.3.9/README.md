# SeqSender 1.3.9 container

Main tool: [SeqSender](https://github.com/CDCgov/seqsender)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name                Version       Build                Channel    
──────────────────────────────────────────────────────────────────────
  Cerberus            1.3.5         pypi_0               pypi       
  _libgcc_mutex       0.1           conda_forge          conda-forge
  _openmp_mutex       4.5           2_gnu                conda-forge
  annotated-types     0.6.0         pyhd8ed1ab_0         conda-forge
  biopython           1.83          py38h01eb140_0       conda-forge
  brotli-python       1.1.0         py38h17151c0_1       conda-forge
  bzip2               1.0.8         hd590300_5           conda-forge
  ca-certificates     2024.2.2      hbcca054_0           conda-forge
  certifi             2024.2.2      pyhd8ed1ab_0         conda-forge
  charset-normalizer  3.3.2         pyhd8ed1ab_0         conda-forge
  icu                 73.2          h59595ed_0           conda-forge
  idna                3.6           pyhd8ed1ab_0         conda-forge
  importlib-metadata  7.1.0         pyha770c72_0         conda-forge
  importlib_metadata  7.1.0         hd8ed1ab_0           conda-forge
  ld_impl_linux-64    2.40          h41732ed_0           conda-forge
  libblas             3.9.0         21_linux64_openblas  conda-forge
  libcblas            3.9.0         21_linux64_openblas  conda-forge
  libffi              3.4.2         h7f98852_5           conda-forge
  libgcc-ng           13.2.0        h807b86a_5           conda-forge
  libgfortran-ng      13.2.0        h69a702a_5           conda-forge
  libgfortran5        13.2.0        ha4646dd_5           conda-forge
  libgomp             13.2.0        h807b86a_5           conda-forge
  libiconv            1.17          hd590300_2           conda-forge
  liblapack           3.9.0         21_linux64_openblas  conda-forge
  libnsl              2.0.1         hd590300_0           conda-forge
  libopenblas         0.3.26        pthreads_h413a1c8_0  conda-forge
  libsqlite           3.45.2        h2797004_0           conda-forge
  libstdcxx-ng        13.2.0        h7e041cc_5           conda-forge
  libuuid             2.38.1        h0b41bf4_0           conda-forge
  libxcrypt           4.4.36        hd590300_1           conda-forge
  libxml2             2.12.6        h232c23b_1           conda-forge
  libxslt             1.1.39        h76b75d6_0           conda-forge
  libzlib             1.2.13        hd590300_5           conda-forge
  lxml                5.1.0         py38h32ae189_0       conda-forge
  multimethod         1.9.1         pyhd8ed1ab_0         conda-forge
  mypy_extensions     1.0.0         pyha770c72_0         conda-forge
  nameparser          1.1.3         pypi_0               pypi       
  ncurses             6.4.20240210  h59595ed_0           conda-forge
  numpy               1.24.4        py38h59b608b_0       conda-forge
  openssl             3.2.1         hd590300_1           conda-forge
  packaging           24.0          pyhd8ed1ab_0         conda-forge
  pandas              2.0.3         py38h01efb38_1       conda-forge
  pandera             0.18.3        hd8ed1ab_0           conda-forge
  pandera-base        0.18.3        pyhd8ed1ab_0         conda-forge
  pip                 24.0          pyhd8ed1ab_0         conda-forge
  pydantic            2.6.4         pyhd8ed1ab_0         conda-forge
  pydantic-core       2.16.3        py38h0cc4f7c_0       conda-forge
  pysocks             1.7.1         pyha2e5f31_6         conda-forge
  python              3.8.19        hd12c33a_0_cpython   conda-forge
  python-dateutil     2.9.0         pyhd8ed1ab_0         conda-forge
  python-tzdata       2024.1        pyhd8ed1ab_0         conda-forge
  python_abi          3.8           4_cp38               conda-forge
  pytz                2024.1        pyhd8ed1ab_0         conda-forge
  pyyaml              6.0.1         py38h01eb140_1       conda-forge
  readline            8.2           h8228510_1           conda-forge
  requests            2.31.0        pyhd8ed1ab_0         conda-forge
  setuptools          69.2.0        pyhd8ed1ab_0         conda-forge
  six                 1.16.0        pyh6c4a22f_0         conda-forge
  tk                  8.6.13        noxft_h4845f30_101   conda-forge
  typeguard           4.2.1         pyhd8ed1ab_0         conda-forge
  typing-extensions   4.10.0        hd8ed1ab_0           conda-forge
  typing_extensions   4.10.0        pyha770c72_0         conda-forge
  typing_inspect      0.9.0         pyhd8ed1ab_0         conda-forge
  urllib3             2.2.1         pyhd8ed1ab_0         conda-forge
  wheel               0.43.0        pyhd8ed1ab_1         conda-forge
  wrapt               1.16.0        py38h01eb140_0       conda-forge
  xmltodict           0.13.0        pyhd8ed1ab_0         conda-forge
  xz                  5.2.6         h166bdaf_0           conda-forge
  yaml                0.2.5         h7f98852_2           conda-forge
  zipp                3.17.0        pyhd8ed1ab_0         conda-forge
```

</details>

Documentation: [https://cdcgov.github.io/seqsender](https://cdcgov.github.io/seqsender)

SeqSender is a public database submission pipeline by the CDC.

## Example Usage

```bash
# Create test submission files with supplied Influenza data
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py test_data -bsng --organism FLU --submission_dir test_dir

# Create test submission files with supplied SARS-CoV-2 data
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py test_data -bsng --organism COV --submission_dir test_dir
```

View full `seqsender` help options: `docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py --help`
