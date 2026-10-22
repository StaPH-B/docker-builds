# gambit container

Main tool : [gambit](github.com/jlumpe/gambit)

Full documentation: https://gambit-genomics.readthedocs.io/en/latest/

GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking) is a tool for rapid taxonomic identification of microbial pathogens. It uses an extremely efficient genomic distance metric along with a curated database of approximately 50,000 reference genomes (derived from NCBI RefSeq) to identify unknown bacterial genomes within seconds.

## Dependencies

GAMBIT is built using [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) with the following dependencies:

<details>
<summary>Dependencies</summary>
  
List of packages in environment: "/opt/conda"

	Name                Version       Build                    Channel
	──────────────────────────────────────────────────────────────────────────
	_openmp_mutex       4.5           20_gnu                   conda-forge
	alembic             1.19.1        pyhcf101f3_0             conda-forge
	attrs               26.1.0        pyhcf101f3_0             conda-forge
	aws-c-auth          0.10.4        h4610da3_2               conda-forge
	aws-c-cal           0.9.15        h6bbde05_1               conda-forge
	aws-c-common        0.14.3        hb03c661_0               conda-forge
	aws-c-compression   0.3.2         h01ee8f8_5               conda-forge
	aws-c-http          0.11.0        hbe094ff_5               conda-forge
	aws-c-io            0.27.5        h4f381ba_1               conda-forge
	aws-c-s3            0.13.1        h7508075_1               conda-forge
	aws-c-sdkutils      0.2.7         h01ee8f8_3               conda-forge
	aws-checksums       0.2.10        h01ee8f8_5               conda-forge
	biopython           1.88          py311h49ec1c0_0          conda-forge
	bzip2               1.0.8         hda65f42_10              conda-forge
	c-ares              1.34.8        h280c20c_1               conda-forge
	ca-certificates     2026.7.22     hbd8a1cb_0               conda-forge
	cached-property     1.5.2         hd8ed1ab_2               conda-forge
	cached_property     1.5.2         pyha770c72_2             conda-forge
	cattrs              26.1.0        pyhcf101f3_1             conda-forge
	click               8.4.2         pyhc90fa1f_0             conda-forge
	exceptiongroup      1.3.1         pyhd8ed1ab_0             conda-forge
	gambit              1.2.0         pypi_0                   pypi
	greenlet            3.5.5         py311hc665b79_0          conda-forge
	h5py                3.16.0        nompi_py311hfef529e_102  conda-forge
	hdf5                2.2.0         nompi_hc529623_100       conda-forge
	icu                 78.3          py310h44b86e0_2          conda-forge
	importlib-metadata  9.0.0         pyhcf101f3_0             conda-forge
	keyutils            1.6.3         hb9d3cd8_0               conda-forge
	krb5                1.22.2        hbde042b_1               conda-forge
	ld_impl_linux-64    2.46.1        default_hbd61a6d_102     conda-forge
	libaec              1.1.5         h088129d_0               conda-forge
	libblas             3.11.0        9_h4a7cf45_openblas      conda-forge
	libcblas            3.11.0        9_h0358290_openblas      conda-forge
	libcurl             8.21.0        heca4667_4               conda-forge
	libedit             3.1.20250104  pl5321h7949ede_0         conda-forge
	libev               4.33          h280c20c_3               conda-forge
	libffi              3.7.0         h3435931_0               conda-forge
	libgcc              16.1.0        ha9f2e26_1               conda-forge
	libgcc-ng           16.1.0        h69a702a_1               conda-forge
	libgfortran         16.1.0        h69a702a_1               conda-forge
	libgfortran5        16.1.0        h79bb938_1               conda-forge
	libgomp             16.1.0        he0feb66_1               conda-forge
	liblapack           3.11.0        9_h47877c9_openblas      conda-forge
	liblzma             5.8.3         hb03c661_1               conda-forge
	liblzma-devel       5.8.3         hb03c661_1               conda-forge
	libnghttp2          1.68.1        h877daf1_0               conda-forge
	libnsl              2.0.1         hb9d3cd8_1               conda-forge
	libopenblas         0.3.34        pthreads_h94d23a6_0      conda-forge
	libpsl              0.23.1        hf670292_0               conda-forge
	libsqlite           3.53.4        hf4e2dac_0               conda-forge
	libssh2             1.11.1        hcf80075_0               conda-forge
	libstdcxx           16.1.0        h934c35e_1               conda-forge
	libuuid             2.42.2        h5347b49_0               conda-forge
	libzlib             1.3.2         h25fd6f3_3               conda-forge
	mako                1.4.1         pyhcf101f3_0             conda-forge
	markupsafe          3.0.3         py311h3778330_1          conda-forge
	ncurses             6.6           hdb14827_1               conda-forge
	numpy               2.4.6         py311h2e04523_0          conda-forge
	openssl             3.6.3         h35e630c_1               conda-forge
	packaging           26.3          pyhc364b38_0             conda-forge
	pandas              3.0.5         py311h8032f78_1          conda-forge
	pip                 26.2.1        pyh8b19718_0             conda-forge
	python              3.11.0        he550d4f_1_cpython       conda-forge
	python-dateutil     2.9.0.post0   pyhe01879c_2             conda-forge
	python_abi          3.11          8_cp311                  conda-forge
	readline            8.3           h853b02a_0               conda-forge
	s2n                 1.7.6         h7e3ee7f_0               conda-forge
	scipy               1.17.1        py311hbe70eeb_1          conda-forge
	setuptools          84.0.0        pyh332efcf_0             conda-forge
	six                 1.17.0        pyhe01879c_1             conda-forge
	sqlalchemy          2.0.52        py311haee01d2_0          conda-forge
	tk                  8.6.13        noxft_hd70dff1_3         conda-forge
	tomli               2.4.1         pyhcf101f3_0             conda-forge
	typing-extensions   4.16.0        h69aa097_0               conda-forge
	typing_extensions   4.16.0        pyhcf101f3_0             conda-forge
	tzdata              2026c         h151e31d_0               conda-forge
	wheel               0.47.0        pyhd8ed1ab_0             conda-forge
	xz                  5.8.3         ha02ee65_1               conda-forge
	xz-gpl-tools        5.8.3         ha02ee65_1               conda-forge
	xz-tools            5.8.3         hb03c661_1               conda-forge
	zipp                4.1.0         pyhcf101f3_0             conda-forge
	zstd                1.5.7         hb78ec9c_6               conda-forge

</details>

## Example Usage

```bash
# run gambit on assembly 
gambit query GCF_000240185.1_ASM24018v2_genomic.fna
```
