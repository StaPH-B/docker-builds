# bindashtree container

Main tool: [bindashtree](https://github.com/jianshu93/bindashtree)
  
Code repository: https://github.com/jianshu93/bindashtree

Additional tools:
- diamond: 2.0.4
- prodigal 2.6.3

Basic information on how to use this tool:
- executable: checkm2
- help: -h, --help
- version: --version
- description: Rapid assessment of genome bin quality using machine learning.

Additional information:

CheckM2 relies on a external diamond database (~1.7 GB) for rapid annotation. the database can be downloaded via `checkm2 database --download` command or obtained directly from: https://zenodo.org/api/records/5571251/files/checkm2_database.tar.gz/content

  
Full documentation: https://github.com/jianshu93/bindashtree

## Example Usage

```bash
checkm2 predict --threads 8 fasta --input ./input_folder --output-directory ./output_folder --database_path /path/to/database/CheckM2_database/uniref100.KO.1.dmnd
```