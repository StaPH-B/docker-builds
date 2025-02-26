# Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs (BUSCO) container

Main tool : [BUSCO](https://gitlab.com/ezlab/busco/)

Additional tools:
- BBTools 39.10
- HMMER 3.3
- Prodigal 2.6.3
- BLAST+ 2.16.0
- AUGUSTUS 3.3.3
- MetaEuk (Release 7-bba0d80)
- SEPP 4.5.5
- Python 3.8.10
- BioPython 1.83
- R 3.6.3
- Perl 5.30.0
- OpenJDK 1.8.0_392
- Miniprot 0.13

Full documentation: https://busco.ezlab.org/busco_userguide.html

This fully functional BUSCO docker image allows you to use all the program options. All additional tools were added to satisfy the requirements of those functions. This image does not contain any lineage dataset. BUSCO downloads the passed dataset name automatically while running. If a full path is given as lineage, this automated management will be disabled. The usage options are given below. Please refer to the BUSCO manual for further information.
## Example Usage
### Specific lineage
```bash
busco -i assembly.fasta -l bacteria_odb10 -o output -m genome
```
or
```bash
busco -i assembly.fasta -l /path/to/folder/bacteria_odb10 -o output -m genome
```
### Auto lineage selection:
```bash
busco -i assembly.fasta -o output -m genome --auto-lineage-prok
```
### Additional options:
```bash
  -i FASTA FILE, --in FASTA FILE
                        Input sequence file in FASTA format. Can be an assembled genome or transcriptome (DNA), or protein sequences from an annotated gene set.
  -o OUTPUT, --out OUTPUT
                        Give your analysis run a recognisable short name. Output folders and files will be labelled with this name. WARNING: do not provide a path
  -m MODE, --mode MODE  Specify which BUSCO analysis mode to run.
                        There are three valid modes:
                        - geno or genome, for genome assemblies (DNA)
                        - tran or transcriptome, for transcriptome assemblies (DNA)
                        - prot or proteins, for annotated gene sets (protein)
  -l LINEAGE, --lineage_dataset LINEAGE
                        Specify the name of the BUSCO lineage to be used.
  --auto-lineage        Run auto-lineage to find optimum lineage path
  --auto-lineage-prok   Run auto-lineage just on non-eukaryote trees to find optimum lineage path
  --auto-lineage-euk    Run auto-placement just on eukaryote tree to find optimum lineage path
  -c N, --cpu N         Specify the number (N=integer) of threads/cores to use.
  -f, --force           Force rewriting of existing files. Must be used when output files with the provided name already exist.
  -r, --restart         Continue a run that had already partially completed.
  -q, --quiet           Disable the info logs, displays only errors
  --out_path OUTPUT_PATH
                        Optional location for results folder, excluding results folder name. Default is current working directory.
  --download_path DOWNLOAD_PATH
                        Specify local filepath for storing BUSCO dataset downloads
  --datasets_version DATASETS_VERSION
                        Specify the version of BUSCO datasets, e.g. odb10
  --download_base_url DOWNLOAD_BASE_URL
                        Set the url to the remote BUSCO dataset location
  --update-data         Download and replace with last versions all lineages datasets and files necessary to their automated selection
  --offline             To indicate that BUSCO cannot attempt to download files
  --metaeuk_parameters METAEUK_PARAMETERS
                        Pass additional arguments to Metaeuk for the first run. All arguments should be contained within a single pair of quotation marks, separated by commas. E.g. "--param1=1,--param2=2"
  --metaeuk_rerun_parameters METAEUK_RERUN_PARAMETERS
                        Pass additional arguments to Metaeuk for the second run. All arguments should be contained within a single pair of quotation marks, separated by commas. E.g. "--param1=1,--param2=2"
  -e N, --evalue N      E-value cutoff for BLAST searches. Allowed formats, 0.001 or 1e-03 (Default: 1e-03)
  --limit REGION_LIMIT  How many candidate regions (contig or transcript) to consider per BUSCO (default: 3)
  --augustus            Use augustus gene predictor for eukaryote runs
  --augustus_parameters AUGUSTUS_PARAMETERS
                        Pass additional arguments to Augustus. All arguments should be contained within a single pair of quotation marks, separated by commas. E.g. "--param1=1,--param2=2"
  --augustus_species AUGUSTUS_SPECIES
                        Specify a species for Augustus training.
  --long                Optimization Augustus self-training mode (Default: Off); adds considerably to the run time, but can improve results for some non-model organisms
  --config CONFIG_FILE  Provide a config file
  -v, --version         Show this version and exit
  -h, --help            Show this help message and exit
  --list-datasets       Print the list of available BUSCO datasets
```
### Plot
Example usage of plotting script:
```bash
# collect short summaries
mkdir my_summaries
cp SPEC1/short_summary.generic.lineage1_odb10.SPEC1.txt my_summaries/.
cp SPEC2/short_summary.generic.lineage2_odb10.SPEC2.txt my_summaries/.
cp SPEC3/short_summary.specific.lineage2_odb10.SPEC3.txt my_summaries/.
cp SPEC4/short_summary.generic.lineage3_odb10.SPEC4.txt my_summaries/.
cp SPEC5/short_summary.generic.lineage4_odb10.SPEC5.txt my_summaries/.
# plot via script
python3 generate_plot.py –wd my_summaries
```
