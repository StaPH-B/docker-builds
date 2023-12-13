# geNomad container

Main tool: [geNomad](https://github.com/apcamargo/genomad/)
  
Code repository: https://github.com/apcamargo/genomad/

Additional tools:
- aragorn: 1.2.41
- mmseq2: 15-6f452

Basic information on how to use this tool:
- executable: genomad
- help: --help
- version: --version
- description: Identification of mobile genetic elements

Additional information:

The geNomad database version 1.6 is downloaded in /genomad_db.
  
Full documentation: https://portal.nersc.gov/genomad/

## Example Usage

```bash
# to download the database (database is already downloaded at /genomad_db)
genomad download-database .

# recommended usage
genomad end-to-end input.fna output /genomad_db

# subsections of genomad
genomad annotate metagenome.fna genomad_output /genomad_db
genomad find-proviruses metagenome.fna genomad_output /genomad_db
genomad marker-classification metagenome.fna genomad_output /genomad_db
genomad nn-classification metagenome.fna /genomad_output
genomad aggregated-classification metagenome.fna /genomad_output
genomad score-calibration metagenome.fna /genomad_output
genomad summary metagenome.fna /genomad_output
```
