# NCBI AMRFinderPlus docker image

Main tool : [NCBI AMRFinderPlus](https://github.com/ncbi/amr)

Additional tools:

- hmmer v3.3.2
- ncbi-blast+ v2.15.0

## Database information

The database included at time of docker image build is **`2024-05-02.2`**. More information can be found in the [changelog.txt on NCBI's FTP](https://ftp.ncbi.nlm.nih.gov/pathogen/Antimicrobial_resistance/AMRFinderPlus/database/3.12/2024-05-02.2/changelog.txt).

Full documentation: [https://github.com/ncbi/amr/wiki](https://github.com/ncbi/amr/wiki)

## Docker Image Tags

Beginning with AMRFinderPlus v3.11.2, we will include the version of AMRFinderPlus followed by the database version in the docker image tag so that it is more informative to users. The format is as follows:

```bash
# general format
staphb/ncbi-amrfinderplus:<amrfinderplus-version>-<database-version>

# example
staphb/ncbi-amrfinderplus:3.11.14-2023-04-17.1
```

You can view all available docker images on [dockerhub](https://hub.docker.com/r/staphb/ncbi-amrfinderplus/tags) and [quay.io](https://quay.io/repository/staphb/ncbi-amrfinderplus?tab=tags)

## Example Usage

```bash
# list out the available organisms for the -O/--organism flag
$ amrfinder -l
Running: amrfinder -l
Software directory: '/amrfinder/'
Software version: 3.12.8
Database directory: '/amrfinder/data/2024-01-31.1'
Database version: 2024-01-31.1

Available --organism options: Acinetobacter_baumannii, Burkholderia_cepacia, Burkholderia_pseudomallei, Campylobacter, 
Citrobacter_freundii, Clostridioides_difficile, Enterobacter_asburiae, Enterobacter_cloacae, Enterococcus_faecalis, 
Enterococcus_faecium, Escherichia, Klebsiella_oxytoca, Klebsiella_pneumoniae, Neisseria_gonorrhoeae, 
Neisseria_meningitidis, Pseudomonas_aeruginosa, Salmonella, Serratia_marcescens, Staphylococcus_aureus, 
Staphylococcus_pseudintermedius, Streptococcus_agalactiae, Streptococcus_pneumoniae, Streptococcus_pyogenes, 
Vibrio_cholerae, Vibrio_parahaemolyticus, Vibrio_vulnificus

# download Klebsiella oxytoca genome FASTA/FNA to use as a test
$ wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/812/925/GCA_003812925.1_ASM381292v1/GCA_003812925.1_ASM381292v1_genomic.fna.gz" 

# uncompress the FNA file
$ gzip -d GCA_003812925.1_ASM381292v1_genomic.fna.gz  

# run amrfinder (nucleotide mode) on the uncompressed FNA file
$ amrfinder --plus --name GCA_003812925.1 -n GCA_003812925.1_ASM381292v1_genomic.fna -O Klebsiella_oxytoca -o GCA_003812925.1-amrfinder.tsv

# view output TSV
$ column -t -s $'\t' -n GCA_003812925.1-amrfinder.tsv
Name             Protein identifier  Contig id   Start    Stop     Strand  Gene symbol  Sequence name                                                      Scope  Element type  Element subtype  Class               Subclass                         Method   Target length  Reference sequence length  % Coverage of reference sequence  % Identity to reference sequence  Alignment length  Accession of closest sequence  Name of closest sequence                                           HMM id  HMM description
GCA_003812925.1  NA                  CP033844.1  369234   370406   +       oqxA         multidrug efflux RND transporter periplasmic adaptor subunit OqxA  core   AMR           AMR              PHENICOL/QUINOLONE  PHENICOL/QUINOLONE               BLASTX   391            391                        100.00                            90.79                             391               WP_002914189.1                 multidrug efflux RND transporter periplasmic adaptor subunit OqxA  NA      NA
GCA_003812925.1  NA                  CP033844.1  370433   373582   +       oqxB         multidrug efflux RND transporter permease subunit OqxB             core   AMR           AMR              PHENICOL/QUINOLONE  PHENICOL/QUINOLONE               BLASTX   1050           1050                       100.00                            96.86                             1050              WP_023323140.1                 multidrug efflux RND transporter permease subunit OqxB15           NA      NA
GCA_003812925.1  NA                  CP033844.1  636118   637917   -       ybtQ         yersiniabactin ABC transporter ATP-binding/permease protein YbtQ   plus   VIRULENCE     VIRULENCE        NA                  NA                               BLASTX   600            600                        100.00                            89.17                             600               AAC69584.1                     yersiniabactin ABC transporter ATP-binding/permease protein YbtQ   NA      NA
GCA_003812925.1  NA                  CP033844.1  637913   639706   -       ybtP         yersiniabactin ABC transporter ATP-binding/permease protein YbtP   plus   VIRULENCE     VIRULENCE        NA                  NA                               BLASTX   598            600                        99.67                             89.30                             598               CAA21388.1                     yersiniabactin ABC transporter ATP-binding/permease protein YbtP   NA      NA
GCA_003812925.1  NA                  CP033844.1  3473617  3474798  +       emrD         multidrug efflux MFS transporter EmrD                              plus   AMR           AMR              EFFLUX              EFFLUX                           BLASTX   394            394                        100.00                            94.16                             394               ACN65732.1                     multidrug efflux MFS transporter EmrD                              NA      NA
GCA_003812925.1  NA                  CP033844.1  5085488  5086357  -       blaOXY-2-1   extended-spectrum class A beta-lactamase OXY-2-1                   core   AMR           AMR              BETA-LACTAM         CEPHALOSPORIN                    ALLELEX  290            290                        100.00                            100.00                            290               WP_032727905.1                 extended-spectrum class A beta-lactamase OXY-2-1                   NA      NA
GCA_003812925.1  NA                  CP033845.1  5102     5632     -       ant(2'')-Ia  aminoglycoside nucleotidyltransferase ANT(2'')-Ia                  core   AMR           AMR              AMINOGLYCOSIDE      GENTAMICIN/KANAMYCIN/TOBRAMYCIN  BLASTX   177            177                        100.00                            98.31                             177               WP_000381803.1                 aminoglycoside nucleotidyltransferase ANT(2'')-Ia                  NA      NA
GCA_003812925.1  NA                  CP033846.1  748      1932     -       tet(39)      tetracycline efflux MFS transporter Tet(39)                        core   AMR           AMR              TETRACYCLINE        TETRACYCLINE                     EXACTX   395            395                        100.00                            100.00                            395               WP_004856455.1                 tetracycline efflux MFS transporter Tet(39)
```
