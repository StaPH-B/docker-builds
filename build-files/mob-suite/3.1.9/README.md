# MOB-suite container

Main tool: [mob_suite](https://github.com/phac-nml/mob-suite)
  
Code repository: https://github.com/phac-nml/mob-suite

Additional tools:
- blast+ : 2.12.0+
- mash : 2.3

Basic information on how to use this tool:
- executable: `mob_init`, `mob_cluster`, `mob_recon`, `mob_typer`
- help: `-h`, `--help` 
- version: `-V`, `--version` 
- description: Software tools for clustering, reconstruction and typing of plasmids from draft assemblies

Additional information:

The MOB-suite depends on a series of databases which is not included in the container. They can be downloaded and updated by running `mob_init` or can be manually downloaded from [here](https://zenodo.org/records/10304948/files/data.tar.gz?download=1).
  
Full documentation:

Robertson, J., & John. (2018). MOB-suite: software tools for clustering, reconstruction and typing of plasmids from draft assemblies. Microbial Genomics, 4(8). https://doi.org/10.1099/mgen.0.000206
‌

## Example Usage

### Using MOB-typer to perform replicon and relaxase typing of complete plasmids and predict mobility
```bash
# Single plasmid
mob_typer --infile assembly.fasta --out_file sample_mobtyper_results.txt

# Multiple independant plasmids
% mob_typer --multi --infile assembly.fasta --out_file sample_mobtyper_results.txt
```
### Using MOB-recon to reconstruct plasmids from draft assemblies
```bash
# Basic Mode
mob_recon --infile assembly.fasta --outdir my_out_dir

# User sequence mask
mob_recon --infile assembly.fasta --outdir my_out_dir --filter_db filter.fasta

# Autodetected close genome filter
mob_recon --infile assembly.fasta --outdir my_out_dir -g 2019-11-NCBI-Enterobacteriacea-Chromosomes.fasta
```
### Using MOB-cluster
```bash
# Build a new database
mob_cluster --mode build -f new_plasmids.fasta -p new_plasmids_mobtyper_report.txt -t new_plasmids_host_taxonomy.txt --outdir output_directory

# Add a sequence to an existing database
mob_cluster --mode update -f new_plasmids.fasta -p new_plasmids_mobtyper_report.txt -t new_plasmids_host_taxonomy.txt --outdir output_directory -c existing_clusters.txt -r existing_sequences.fasta

# Update MOB-suite plasmid databases
cp output_directory/clusters.txt
mv output_directory/updated.fasta mob_db_path/ncbi_plasmid_full_seqs.fas
makeblastdb -in mob_db_path/ncbi_plasmid_full_seqs.fas -dbtype nucl
mash sketch -i mob_db_path/ncbi_plasmid_full_seqs.fas 
```