# NCBI AMRFinderPlus docker image

Main tool : [NCBI AMRFinderPlus](https://github.com/ncbi/amr)

Additional tools:

- hmmer v3.3.2
- ncbi-blast+ v2.12.0

## Database information

The database included at time of docker image build is **`2022-10-11.2`**. More information can be found in the changes.txt on [NCBI's FTP](https://ftp.ncbi.nlm.nih.gov/pathogen/Antimicrobial_resistance/Data/2022-10-11.2/changes.txt).

Full documentation: [https://github.com/ncbi/amr/wiki](https://github.com/ncbi/amr/wiki)

## Example Usage

```bash
# list out the available organisms for the -O/--organism flag
$ amrfinder -l
Running: amrfinder -l
Software directory: '/amrfinder/'
Software version: 3.10.42
Database directory: '/amrfinder/data/2022-10-11.2'
Database version: 2022-10-11.2

Available --organism options: Acinetobacter_baumannii, Burkholderia_cepacia, Burkholderia_pseudomallei, Campylobacter, Clostridioides_difficile, Enterococcus_faecalis, Enterococcus_faecium, Escherichia, Klebsiella, Neisseria, Pseudomonas_aeruginosa, Salmonella, Staphylococcus_aureus, Staphylococcus_pseudintermedius, Streptococcus_agalactiae, Streptococcus_pneumoniae, Streptococcus_pyogenes, Vibrio_cholerae

# run amrfinder with an genome assembly (FASTA/FNA) as input (nucleotide mode)
$ amrfinder --plus --name GCA_011245895.1 -n GCA_011245895.1_PDT000672941.1_genomic.fna -O Salmonella -o GCA_011245895.1-amrfinder.tsv

# part of output TSV
Name             Protein identifier  Contig id          Start   Stop    Strand  Gene symbol  Sequence name                                                      Scope  Element type  Element subtype  Class                Subclass                     Method   Target length  Reference sequence length  % Coverage of reference sequence  % Identity to reference sequence  Alignment length  Accession of closest sequence  Name of closest sequence                                           HMM id  HMM description
GCA_011245895.1  NA                  AAPPHT010000001.1  373875  376130  -       parC_S80I    Salmonella quinolone resistant ParC                                core   AMR           POINT            QUINOLONE            QUINOLONE                    POINTX   752            752                        100.00                            99.60                             752               WP_001281910.1                 DNA topoisomerase IV subunit A ParC                                NA      NA
GCA_011245895.1  NA                  AAPPHT010000003.1  338394  338855  -       golS         Au(I) sensor transcriptional regulator GolS                        plus   STRESS        METAL            GOLD                 GOLD                         BLASTX   154            154                        100.00                            99.35                             154               AAL19308.1                     Au(I) sensor transcriptional regulator GolS                        NA      NA
GCA_011245895.1  NA                  AAPPHT010000003.1  338870  341155  -       golT         gold/copper-translocating P-type ATPase GolT                       plus   STRESS        METAL            COPPER/GOLD          COPPER/GOLD                  BLASTX   762            762                        100.00                            99.48                             762               AAL19307.1                     gold/copper-translocating P-type ATPase GolT                       NA      NA
GCA_011245895.1  NA                  AAPPHT010000003.1  341432  342655  +       mdsA         multidrug efflux RND transporter periplasmic adaptor subunit MdsA  plus   AMR           AMR              EFFLUX               EFFLUX                       BLASTX   408            408                        100.00                            98.28                             408               AAL19306.1                     multidrug efflux RND transporter periplasmic adaptor subunit MdsA  NA      NA
GCA_011245895.1  NA                  AAPPHT010000003.1  342655  345819  +       mdsB         multidrug efflux RND transporter permease subunit MdsB             plus   AMR           AMR              EFFLUX               EFFLUX                       BLASTX   1055           1055                       100.00                            99.53                             1055              AAL19305.1                     multidrug efflux RND transporter permease subunit MdsB             NA      NA
GCA_011245895.1  NA                  AAPPHT010000009.1  96940   99129   +       sinH         intimin-like inverse autotransporter SinH                          plus   VIRULENCE     VIRULENCE        NA                   NA                           BLASTX   730            730                        100.00                            98.77                             730               AAL21411.1                     intimin-like inverse autotransporter SinH                          NA      NA
GCA_011245895.1  NA                  AAPPHT010000010.1  173540  176173  +       gyrA_D87G    Salmonella quinolone/triclosan resistant GyrA                      core   AMR           POINT            QUINOLONE/TRICLOSAN  QUINOLONE/TRICLOSAN          POINTX   878            878                        100.00                            99.77                             878               WP_001281271.1                 DNA gyrase subunit A GyrA                                          NA      NA
GCA_011245895.1  NA                  AAPPHT010000010.1  173540  176173  +       gyrA_S83F    Salmonella quinolone/triclosan resistant GyrA                      core   AMR           POINT            QUINOLONE/TRICLOSAN  QUINOLONE/TRICLOSAN          POINTX   878            878                        100.00                            99.77                             878               WP_001281271.1                 DNA gyrase subunit A GyrA                                          NA      NA
GCA_011245895.1  NA                  AAPPHT010000014.1  51361   52473   +       iroB         salmochelin biosynthesis C-glycosyltransferase IroB                plus   VIRULENCE     VIRULENCE        NA                   NA                           BLASTX   371            371                        100.00                            86.52                             371               EOW04219.1                     salmochelin biosynthesis C-glycosyltransferase IroB                NA      NA
GCA_011245895.1  NA                  AAPPHT010000014.1  52557   56183   +       iroC         salmochelin/enterobactin export ABC transporter IroC               plus   VIRULENCE     VIRULENCE        NA                   NA                           BLASTX   1209           1219                       98.85                             80.18                             1211              AUH19662.1                     salmochelin/enterobactin export ABC transporter IroC               NA      NA
```
