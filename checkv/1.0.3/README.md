# CheckV container

Main tool: [checkv](https://jgi.doe.gov/data-and-tools/software-tools/checkv/)
  
Code repository: https://bitbucket.org/berkeleylab/checkv/

Additional tools:
- diamond: 2.1.8
- prodigal-gv: 2.11.0
- hmmer: 3.3.2
- blast: 2.12.0+

Basic information on how to use this tool:
- executable: checkv
- help: -h
- version:
- description: 
>CheckV is the first fully automated, command-line tool for assessing the quality of metagenome-assembled viral genomes

Additional information:

This container does not include any database. You can use `checkv download_database` command or https://portal.nersc.gov/CheckV/ address to download it manually

Full documentation: https://bitbucket.org/berkeleylab/checkv/src/master/

## Example Usage

```bash
# Using a single command to run the full pipeline (recommended)
checkv end_to_end input_file.fna output_directory -t 16

# Using individual commands for each step in the pipeline
checkv contamination input_file.fna output_directory -t 16
checkv completeness input_file.fna output_directory -t 16
checkv complete_genomes input_file.fna output_directory
checkv quality_summary input_file.fna output_directory
```

