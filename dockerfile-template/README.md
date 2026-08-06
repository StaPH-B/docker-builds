<!-- 
Please edit this readme with some basic information about the tool and how to use this container. 
- Include information about databases and additional files that are included.
- Keep it short - don't recreate the documentation from the creators.
- Do not just copy and paste the readme or help for the tool. 
-->

# <program> container

This images is part of the StaPH-B/docker-builds project. More information can be found at https://github.com/StaPH-B/docker-builds.

Main tool: [<program>](link to program)

Code repository:

Additional tools:
- list: version

<!-- 
Please add dependencies installed via micromamba. 
-->

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

<!-- 
Please add dependencies installed via pip. 
-->

<details>
<summary>Additional tools installed via pip:</summary>

```
Package                Version
---------------------- -----------
annotated-types        0.7.0
Brotli                 1.2.0
certifi                2025.11.12
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
