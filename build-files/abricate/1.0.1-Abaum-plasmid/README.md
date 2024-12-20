# ABRicate docker image + AcinetobacterPlasmidTyping db

> ABRicate: Mass screening of contigs for antimicrobial resistance or virulence genes. It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF and VFDB.

Main tool : [ABRicate](https://github.com/tseemann/abricate)

Additional tools:

- any2fasta 0.4.2
- ncbi-blast+ 2.9.0
- perl 5.30.0
- bioperl 1.7.7-1

## Custom database info

The Acinetobacter Plasmid Typing database included in this docker build is v1.0.0 from [GitHub](https://github.com/MehradHamidian/AcinetobacterPlasmidTyping) and is described in a [preprint](https://www.biorxiv.org/content/10.1101/2022.08.26.505409v1). The database contains variants of the plasmid rep gene found in Acinetobacter baumannii, as described in the manuscript. When rep genes match with > 95 % identity, this represents a typing scheme for Acinetobacter baumannii plasmids.

The database (FASTA file) has been modified slightly to conform to ABRicate requirements. Lowercase nucleotide sequences `a,t,c,g` have been converted to uppercase `A,T,C,G` and FASTA headers were altered according to directions here: [https://github.com/tseemann/abricate#making-your-own-database](https://github.com/tseemann/abricate#making-your-own-database)

## Example Usage

```bash
# list out the available databases
$ abricate --list
DATABASE        SEQUENCES       DBTYPE  DATE
card    2631    nucl    2022-Oct-13
ncbi    5386    nucl    2022-Oct-13
vfdb    2597    nucl    2022-Oct-13
megares 6635    nucl    2022-Oct-13
ecoli_vf        2701    nucl    2022-Oct-13
argannot        2223    nucl    2022-Oct-13
ecoh    597     nucl    2022-Oct-13
plasmidfinder   460     nucl    2022-Oct-13
resfinder       3077    nucl    2022-Oct-13
AcinetobacterPlasmidTyping      152     nucl    2022-Oct-13

# run ABRicate on an A. baumannii assembly using custom database, saving results to file "a-baum-plasmid.abricate.tsv"
$ abricate SAMN19774594_contigs.fasta --db AcinetobacterPlasmidTyping | tee a-baum-plasmid.abricate.tsv
Using nucl database AcinetobacterPlasmidTyping:  152 sequences -  2022-Oct-13
Processing: SAMN19774594_contigs.fasta
#FILE   SEQUENCE        START   END     STRAND  GENE    COVERAGE        COVERAGE_MAP    GAPS    %COVERAGE       %IDENTITY       DATABASE        ACCESSIONPRODUCT  RESISTANCE
Found 2 genes in SAMN19774594_contigs.fasta
Tip: the --fofn option allows you to feed in a big list of files to run on.
Done.
SAMN19774594_contigs.fasta      contig00028     28950   30125   +       rP-T1   1-1176/1176     =============== 0/0     100.00  100.00  AcinetobacterPlasmidTyping        CP001922.1_ABKp1        rP-T1
SAMN19774594_contigs.fasta      contig00059     2896    3831    +       r3-T4   1-936/936       =============== 0/0     100.00  100.00  AcinetobacterPlasmidTyping        AY541809.1_pMAC r3-T4

# run ABRicate on an assembly supplied with ABRicate code, saving results to file "1.tab"
$ abricate /abricate*/test/assembly.fa | tee 1.tab
Using nucl database ncbi:  5386 sequences -  2022-Oct-13
Processing: /abricate-1.0.1/test/assembly.fa
#FILE   SEQUENCE        START   END     STRAND  GENE    COVERAGE        COVERAGE_MAP    GAPS    %COVERAGE       %IDENTITY       DATABASE        ACCESSIONPRODUCT  RESISTANCE
Found 5 genes in /abricate-1.0.1/test/assembly.fa
Tip: the --fofn option allows you to feed in a big list of files to run on.
Done.
/abricate-1.0.1/test/assembly.fa        LGJG01000038    62416   62796   -       blaI_of_Z       1-381/381       =============== 0/0     100.00  95.28   ncbi      NG_047499.1     penicillinase repressor BlaI    BETA-LACTAM
/abricate-1.0.1/test/assembly.fa        LGJG01000038    62786   64543   -       blaR1   1-1758/1758     =============== 0/0     100.00  92.83   ncbi    NG_047539.1       beta-lactam sensor/signal transducer BlaR1      BETA-LACTAM
/abricate-1.0.1/test/assembly.fa        LGJG01000038    64650   65495   +       blaZ    1-846/846       =============== 0/0     100.00  96.81   ncbi    NG_055999.1       penicillin-hydrolyzing class A beta-lactamase BlaZ      BETA-LACTAM
/abricate-1.0.1/test/assembly.fa        LGJG01000040    190796  191281  +       dfrC    1-486/486       =============== 0/0     100.00  99.59   ncbi    NG_047752.1       trimethoprim-resistant dihydrofolate reductase DfrC     TRIMETHOPRIM
/abricate-1.0.1/test/assembly.fa        LGJG01000041    35416   35844   -       fosB-251804940  1-429/429       =============== 0/0     100.00  100.00  ncbi      NG_047889.1     FosB family fosfomycin resistance bacillithiol transferase      FOSFOMYCIN

```
