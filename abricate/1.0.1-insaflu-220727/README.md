# ABRicate docker image + insaflu db

> ABRicate: Mass screening of contigs for antimicrobial resistance or virulence genes. It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF and VFDB.

Main tool : [ABRicate](https://github.com/tseemann/abricate)

Additional tools:

- any2fasta 0.4.2
- ncbi-blast+ 2.9.0
- perl 5.30.0
- bioperl 1.7.7-1

## Custom database info

The InsaFlu_220727 database included in this docker build is from [GitHub](https://github.com/epi2me-labs/wf-flu/tree/prerelease/data/primer_schemes/V1/blastdb/insaflu) and is described in the [epi2me-labs/wf-flu repo](https://github.com/epi2me-labs/wf-flu#typing). 

## Example Usage

```bash
# list out the available databases
$ abricate --list
DATABASE        SEQUENCES       DBTYPE  DATE
megares 6635    nucl    2022-Nov-16
ecoh    597     nucl    2022-Nov-16
plasmidfinder   460     nucl    2022-Nov-16
resfinder       3077    nucl    2022-Nov-16
ecoli_vf        2701    nucl    2022-Nov-16
ncbi    5386    nucl    2022-Nov-16
card    2631    nucl    2022-Nov-16
argannot        2223    nucl    2022-Nov-16
vfdb    2597    nucl    2022-Nov-16
insaflu 34      nucl    2022-Nov-16

# run ABRicate on an influenza assembly using custom database, saving results to file "irma.abricate.tsv"
$ abricate sample_01.fasta --db insaflu | tee insaflu.abricate.tsv
Using nucl database insaflu:  34 sequences -  2022-Nov-16
Processing: sample_01.fasta
#FILE   SEQUENCE        START   END     STRAND  GENECOVERAGE        COVERAGE_MAP    GAPS    %COVERAGE  %IDENTITY        DATABASE        ACCESSION       PRODUCT     RESISTANCE
Found 2 genes in sample_01.fasta
Tip: the abricate manual is at https://github.com/tseemann/abricate/blob/master/README.md
Done.
sample_01.fasta SRR10013255_4   23      1868    +  HA       1-1843/1843     ========/====== 1/3     100.00      94.80   insaflu CY018765        CY018765.1 Influenza B virus (B/Yamagata/16/1988) segment 4 complete sequence   Yamagata
sample_01.fasta SRR10013255_7   31      1171    +  M1       1-1141/1141     =============== 0/0     100.00      96.67   insaflu AF100378        AF100378.1 Influenza B virus B/Yamagata/16/88 segment 7 M1 matrix protein (M) and BM2 protein (BM2) genes complete cds      Type_B

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
