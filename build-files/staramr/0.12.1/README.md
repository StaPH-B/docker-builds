# staramr container

Main tool : [staramr](https://github.com/phac-nml/staramr)

Additional tools:

- mlst 2.32.2
- ncbi-blast+ 2.16.0+
- any2fasta 0.8.1
- Databases for PlasmidFinder, PointFinder, ResFinder

Database version information:

```
##### staramr db information at time of docker image build #####
resfinder_db_dir              = /usr/local/lib/python3.12/site-packages/staramr/databases/data/update/resfinder
resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
resfinder_db_commit           = eecf0aa207594fe6d51badf808473de62b28cb06
resfinder_db_date             = Mon, 26 Jan 2026 09:41
pointfinder_db_dir            = /usr/local/lib/python3.12/site-packages/staramr/databases/data/update/pointfinder
pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
pointfinder_db_commit         = 44ce624a806c6d2b70f7e39841a5f9cb4d9010aa
pointfinder_db_date           = Wed, 05 Nov 2025 09:17
pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
pointfinder_organisms_valid   = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, salmonella
plasmidfinder_db_dir          = /usr/local/lib/python3.12/site-packages/staramr/databases/data/update/plasmidfinder
plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
plasmidfinder_db_commit       = 07648fddc4c6cf0330c9fc041dd6f52b4a69f8d6
plasmidfinder_db_date         = Thu, 27 Nov 2025 09:52
mlst_version                  = 2.32.2
pointfinder_gene_drug_version = 032525
resfinder_gene_drug_version   = 032525
```

STARAMR uses several databases that it does not maintain. As such, this image is re-built twice a year for the latest of these databases {latest-version}={date of rebuilding}.


Full documentation: https://github.com/phac-nml/staramr

staramr scans bacterial genome contigs for AMR genes and plasmids

## Example Usage

```bash
# run "staramr search" on a genome assembly (broken into multiple lines for readability)
staramr search -o /data/staramrtest-Salmonella \
  --pointfinder-organism salmonella \
  --plasmidfinder-database-type enterobacteriales \
  /data/salmonella_enterica_assembly.fasta

# to get database information
staramr db info
```
