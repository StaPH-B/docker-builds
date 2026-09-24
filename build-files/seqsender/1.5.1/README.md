# SeqSender 1.3.93 container

Main tool: [SeqSender](https://github.com/CDCgov/seqsender)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name                Version       Build                 Channel    
───────────────────────────────────────────────────────────────────────
  Cerberus            1.3.8         pypi_0                pypi       
  _libgcc_mutex       0.1           conda_forge           conda-forge
  _openmp_mutex       4.5           20_gnu                conda-forge
  annotated-types     0.8.0         pyhd8ed1ab_0          conda-forge
  backports.zstd      1.7.0         py310hff74037_0       conda-forge
  beartype            0.22.9        pyhd8ed1ab_0          conda-forge
  biopython           1.88          py310h7c4b9e2_0       conda-forge
  brotli-python       1.2.0         py310h25d4438_3       conda-forge
  bzip2               1.0.8         hda65f42_10           conda-forge
  ca-certificates     2026.7.22     hbd8a1cb_0            conda-forge
  certifi             2026.7.22     pyhd8ed1ab_0          conda-forge
  cffi                2.1.1         py310hd4ea0ea_2       conda-forge
  charset-normalizer  3.5.1         pyhd8ed1ab_0          conda-forge
  cryptography        50.0.0        py310h20b05aa_1       conda-forge
  h2                  4.4.1         pyhcf101f3_0          conda-forge
  hpack               4.2.0         pyhd8ed1ab_0          conda-forge
  hyperframe          6.1.0         pyhd8ed1ab_0          conda-forge
  icu                 78.3          py310h44b86e0_2       conda-forge
  idna                3.19          pyhcf101f3_0          conda-forge
  importlib-metadata  9.0.1         pyhcf101f3_0          conda-forge
  importlib_metadata  9.0.1         ha21a7b4_0            conda-forge
  ld_impl_linux-64    2.46.1        default_hbd61a6d_102  conda-forge
  libblas             3.11.0        11_h4a7cf45_openblas  conda-forge
  libcblas            3.11.0        11_h0358290_openblas  conda-forge
  libexpat            2.8.1         hecca717_1            conda-forge
  libffi              3.7.0         h81df57d_1            conda-forge
  libgcc              16.2.0        ha9f2e26_5            conda-forge
  libgcc-ng           16.2.0        h69a702a_5            conda-forge
  libgfortran         16.2.0        h69a702a_5            conda-forge
  libgfortran-ng      16.2.0        h69a702a_5            conda-forge
  libgfortran5        16.2.0        h6b99dfc_5            conda-forge
  libgomp             16.2.0        he0feb66_5            conda-forge
  libiconv            1.18          h0cb94f2_3            conda-forge
  liblapack           3.11.0        11_h47877c9_openblas  conda-forge
  liblzma             5.8.3         hb03c661_1            conda-forge
  liblzma-devel       5.8.3         hb03c661_1            conda-forge
  libnsl              2.0.1         hb9d3cd8_1            conda-forge
  libopenblas         0.3.34        pthreads_hf13c14d_2   conda-forge
  libsqlite           3.53.4        h13e7031_1            conda-forge
  libstdcxx           16.2.0        h934c35e_5            conda-forge
  libstdcxx-ng        16.2.0        hdf11a46_5            conda-forge
  libuuid             2.42.3        hcfc3c73_0            conda-forge
  libxcrypt           4.4.38        h280c20c_0            conda-forge
  libxml2             2.15.4        h7df9aa5_0            conda-forge
  libxml2-16          2.15.4        hf3af7cc_0            conda-forge
  libxslt             1.1.45        h8e12856_1            conda-forge
  libzlib             1.3.2         h25fd6f3_3            conda-forge
  lxml                6.1.2         py310h04e47aa_0       conda-forge
  multimethod         1.9.1         pyhd8ed1ab_0          conda-forge
  mypy_extensions     1.1.0         pyha770c72_0          conda-forge
  nameparser          1.4.0         pypi_0                pypi       
  ncurses             6.6           hdb14827_1            conda-forge
  numpy               1.26.4        py310hb13e2d6_0       conda-forge
  openssl             3.6.4         h781a0a9_0            conda-forge
  packaging           26.3          pyhc364b38_0          conda-forge
  pandas              2.3.3         py310h0158d43_2       conda-forge
  pandera             0.18.3        hd8ed1ab_0            conda-forge
  pandera-base        0.18.3        pyhd8ed1ab_0          conda-forge
  pip                 26.2.1        pyh8b19718_0          conda-forge
  pycparser           3.0           pyhcf101f3_0          conda-forge
  pydantic            2.13.5        pyhcf101f3_0          conda-forge
  pydantic-core       2.46.5        py310hbfe5df0_1       conda-forge
  pysocks             1.7.1         pyha55dd90_7          conda-forge
  python              3.10.21       h267e890_0_cpython    conda-forge
  python-dateutil     2.9.0.post0   pyhe01879c_2          conda-forge
  python-tzdata       2026.3        pyhd8ed1ab_0          conda-forge
  python_abi          3.10          9_cp310               conda-forge
  pytz                2026.3.post1  pyhcf101f3_0          conda-forge
  pyyaml              6.0.3         py310h3406613_1       conda-forge
  readline            8.3           hd6e31c0_1            conda-forge
  requests            2.34.2        pyhcf101f3_0          conda-forge
  setuptools          84.0.0        pyh332efcf_0          conda-forge
  six                 1.17.0        pyhe01879c_1          conda-forge
  tk                  8.6.13        noxft_h1df4ec4_4      conda-forge
  typeguard           4.6.0         pyhcf101f3_0          conda-forge
  typing-extensions   4.16.0        h69aa097_0            conda-forge
  typing-inspection   0.4.4         pyhcf101f3_0          conda-forge
  typing_extensions   4.16.0        pyhcf101f3_0          conda-forge
  typing_inspect      0.9.0         pyhd8ed1ab_1          conda-forge
  tzdata              2026c         h151e31d_0            conda-forge
  urllib3             2.7.0         pyhd8ed1ab_0          conda-forge
  wheel               0.48.0        pyhd8ed1ab_0          conda-forge
  wrapt               2.4.0         py310h83e8816_0       conda-forge
  xmltodict           1.0.4         pyhcf101f3_0          conda-forge
  xz                  5.8.3         ha02ee65_1            conda-forge
  xz-gpl-tools        5.8.3         ha02ee65_1            conda-forge
  xz-tools            5.8.3         hb03c661_1            conda-forge
  yaml                0.2.5         hebe6cf0_3            conda-forge
  zipp                4.1.0         pyhcf101f3_0          conda-forge
  zstd                1.5.7         hb78ec9c_7            conda-forge
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
