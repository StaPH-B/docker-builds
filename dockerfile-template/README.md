<!-- 
Please edit this readme with some basic information about the tool and how to use this container. 
- Include information about databases and additional files that are included.
- Keep it short - don't recreate the documentation from the creators.
- Do not just copy and paste the readme or help for the tool. 
-->

# <program> container

Main tool: [<program>](link to program)
  
Code repository:

Additional tools:
- list: version

<details>
<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda"

  Name                     Version       Build                 Channel    
────────────────────────────────────────────────────────────────────────────
  _openmp_mutex            4.5           20_gnu                conda-forge
  about-time               4.2.1         pyhd
```
</details>

<details>
<summary>Additional tools installed via pip:</summary>

```
Package                Version
---------------------- -----------
annotated-types        0.7.0
Brotli                 1.2.0
certifi                2025.11.12
charset-normalizer     3.4.4
colorama               0.4.6
h2                     4.3.0
hpack                  4.1.0
hyperframe             6.1.0
idna                   3.11
ncbi-datasets-pyclient 18.13.0
numpy                  2.4.0
pandas                 2.3.3
pip                    25.3
pydantic               2.12.5
pydantic_core          2.41.5
PySocks                1.7.1
python-dateutil        2.9.0.post0
pytz                   2025.2
requests               2.32.5
six                    1.17.0
spestimator            0.1.0.232
tqdm                   4.67.1
typing_extensions      4.15.0
typing-inspection      0.4.2
tzdata                 2025.3
urllib3                2.6.2
```

</details>

Basic information on how to use this tool:
- executable: <tool>
- help: <-h>
- version: <-v>
- description: <tool does something>

Additional information:

<Container contains X database at Y>
  
Full documentation: link to documentation or wiki

## Example Usage

```bash
<how creator of the dockerfile uses it>
```

  
<!-- Example README
# pasty container

Main tool: [pasty](https://github.com/rpetit3/pasty)

Code repository: https://github.com/rpetit3/pasty

Additional tools:
- ncbi-blast+: 2.12.0
- python: 3.10.6

Basic information on how to use this tool:
- executable: pasty
- help: --help
- version: --version
- description: "A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies"

Additional information:  
  
Full documentation: [https://github.com/rpetit3/pasty](https://github.com/rpetit3/pasty)

## Example Usage

```bash
pasty --assembly /pasty-1.0.2/test/O1-GCF_000504045.fna.gz --prefix O1-GCF_000504045
``` 
-->
