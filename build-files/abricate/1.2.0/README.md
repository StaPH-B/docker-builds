# ABRicate

> ABRicate: Mass screening of contigs for antimicrobial resistance or virulence genes. It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF and VFDB.

Main tool : [ABRicate](https://github.com/tseemann/abricate)

Additional tools:

- any2fasta 0.8.1
- ncbi-blast+ 2.12.0
- perl 5.38.2
- bioperl 1.7.8

Additional information:

This image uses the most up-to-date databases at the time of building. This image is rebuilt every month on Dockerhub and Quay.io with the tag `${abricate version}-${data image was deployed}` as well as `latest`.


## Example Usage

```bash
# list out the available databases
$ abricate --list
DATABASE        SEQUENCES       DBTYPE  DATE
victors 4545    nucl    2025-Dec-30
resfinder       3206    nucl    2025-Dec-30
card    6052    nucl    2025-Dec-30
megares 6635    nucl    2025-Dec-30
ecoli_vf        2701    nucl    2025-Dec-30
vfdb    4592    nucl    2025-Dec-30
ecoh    597     nucl    2025-Dec-30
bacmet2 746     prot    2025-Dec-30
argannot        2224    nucl    2025-Dec-30
plasmidfinder   488     nucl    2025-Dec-30
ncbi    8035    nucl    2025-Dec-30

# run ABRicate on an Vibrio cholerae assembly using custom database, saving results to file "/data/abricate_vibrio.tsv"
$ abricate --db vibrio /data/GCA_018083565.2_PDT000793508.2_genomic.fna | tee /data/abricate_vibrio.tsv
abricate --nopath --db vibrio /data/GCA_018083565.2_PDT000793508.2_genomic.fna | tee /data/abricate_vibrio.tsv
Using nucl database vibrio:  8 sequences -  2024-Apr-30
Processing: /data/GCA_018083565.2_PDT000793508.2_genomic.fna
#FILE   SEQUENCE        START   END     STRAND  GENE    COVERAGE        COVERAGE_MAP    GAPS    %COVERAGE       %IDENTITY       DATABASE        ACCESSION       PRODUCT RESISTANCE
Found 5 genes in /data/GCA_018083565.2_PDT000793508.2_genomic.fna
Tip: did you know? abricate was named after 'A'nti 'B'acterial 'R'esistiance
Done.
GCA_018083565.2_PDT000793508.2_genomic.fna      DADXRP020000001.1       3562    4338    +       ctxA    1-777/777       =============== 0/0     100.00  100.00  Vibriov1.0.0    CP000627.1      ctxA_O395       cholera_toxin_gene
GCA_018083565.2_PDT000793508.2_genomic.fna      DADXRP020000001.1       520818  521702  +       toxR    1-885/885       =============== 0/0     100.00  98.42   Vibriov1.0.0    CP000627.1      toxR_O395       Vcholerae_species_marker
GCA_018083565.2_PDT000793508.2_genomic.fna      DADXRP020000002.1       439805  440458  +       ompW    1-654/654       =============== 0/0     100.00  99.08   Vibriov1.0.0    CP000626.1      ompW_O395       Vcholerae_species_marker
GCA_018083565.2_PDT000793508.2_genomic.fna      DADXRP020000008.1       101343  103820  +       wbeN_O1 1-2478/2478     =============== 0/0     100.00  100.00  Vibriov1.0.0    NA      wbeN_O1_INDRE   O1_serotype_marker
GCA_018083565.2_PDT000793508.2_genomic.fna      DADXRP020000033.1       3271    3945    -       tcpA_ElTor      1-675/675       =============== 0/0     100.00  100.00  Vibriov1.0.0    CP064350.1      tcpA_ElTor_C6706        ElTor_biotype

```
