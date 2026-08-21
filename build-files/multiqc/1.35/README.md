# MultiQC container

Main tool : [MultiQC](https://multiqc.info/)

Aggregate results from bioinformatics analyses across many samples into a single report.

Full documentation: [Docs] (https://multiqc.info/docs/)

Notes: Starting with version 1.27, multiqc can use ai to assist with summaries. More information on how to set this up and use it can be found at https://docs.seqera.io/multiqc/ai.

<details>
<summary>
Additional tools installed via pip:
</summary>

```
	Package                   Version
	------------------------- -----------
	annotated-types           0.7.0
	attrs                     26.1.0
	boto3                     1.43.36
	botocore                  1.43.36
	certifi                   2026.6.17
	charset-normalizer        3.4.7
	click                     8.4.2
	coloredlogs               15.0.1
	colormath2                3.0.3
	humanfriendly             10.0
	humanize                  4.15.0
	idna                      3.18
	importlib_metadata        9.0.0
	Jinja2                    3.1.6
	jmespath                  1.1.0
	jsonschema                4.26.0
	jsonschema-specifications 2025.9.1
	kaleido                   0.2.1
	Markdown                  3.10.2
	markdown-it-py            4.2.0
	MarkupSafe                3.0.3
	mdurl                     0.1.2
	multiqc                   1.35
	narwhals                  2.22.1
	natsort                   8.4.0
	networkx                  3.6.1
	numpy                     2.5.0
	packaging                 26.2
	pillow                    12.2.0
	pip                       24.0
	plotly                    6.8.0
	polars                    1.42.0
	polars-runtime-32         1.42.0
	polars-runtime-compat     1.42.0
	pyarrow                   24.0.0
	pydantic                  2.13.4
	pydantic_core             2.46.4
	Pygments                  2.20.0
	python-dateutil           2.9.0.post0
	python-dotenv             1.2.2
	PyYAML                    6.0.3
	referencing               0.37.0
	regex                     2026.5.9
	requests                  2.34.2
	rich                      15.0.0
	rich-click                1.9.8
	rpds-py                   2026.5.1
	s3transfer                0.19.0
	setuptools                68.1.2
	six                       1.17.0
	spectra                   0.1.0
	tiktoken                  0.13.0
	tqdm                      4.68.3
	typeguard                 4.5.2
	typing_extensions         4.15.0
	typing-inspection         0.4.2
	urllib3                   2.7.0
	wheel                     0.42.0
	zipp                      4.1.0
```
</details>


# Example Usage

```
multiqc -f --cl_config "prokka_fn_snames: True"  .
```
