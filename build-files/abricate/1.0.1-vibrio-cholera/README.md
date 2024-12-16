# ABRicate v1.0.1 docker image + Vibrio cholerae db

> ABRicate: Mass screening of contigs for antimicrobial resistance or virulence genes. It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF and VFDB.

Main tool : [ABRicate](https://github.com/tseemann/abricate)

Additional tools:

- any2fasta 0.4.2
- ncbi-blast+ 2.9.0
- perl 5.30.0
- bioperl 1.7.7-1

## Custom *Vibrio cholerae* database info

This docker image includes a *Vibrio cholerae-specific* database of gene targets (traditionally used in PCR methods) for detecting O1 & O139 serotypes, toxin-production markers, and Biotype markers within the O1 serogroup ("El Tor" or "Classical" biotypes). These sequences were shared via personal communication with Dr. Christine Lee, of the National Listeria, Yersinia, Vibrio and Enterobacterales Reference Laboratory within the Enteric Diseases Laboratory Branch at CDC.

The genes included (and their purpose) included in the database are as follows:

- `ctxA` - Cholera toxin, an indication of toxigenic cholerae
- `ompW` - outer membrane protein, a *V. cholerae* species marker (presence of any allele of this gene distinguishes *V. cholerae* from *V. parahaemolyticus* and *V. vulnificus*)
- `tcpA` - toxin co-pilus A, used to infer Biotype, either "El Tor" or "Clasical"
  - database includes an allele for each Biotype. `tcpA_classical` and `tcpA_ElTor`
- `toxR` - transcriptional activator (controls cholera toxin, pilus, and outer-membrane protein expression) - Species marker (allele distinguishes *V. cholerae* from *V. parahaemolyticus* and *V. vulnificus*)
- `wbeN` - O antigen encoding region - used to identify the O1 serogroup
- `wbfR` - O antigen encoding region - used to identify the O139 serogroup

:warning: The database's FASTA file & index files are located within `/abricate-$1.0.1/db/vibrio/sequences` in the container's file system and can be utilized via the example command below.

:warning: This database is identical in nucleotide sequence content to the `vibrio_230224.fasta` database included in the SRST2 container (located at `srst2/0.2.0-vibrio-230224/vibrio_230224.fasta`), but the FASTA headers were formatted for use with ABRicate.

## Example Usage

```bash
# list out the available databases
$ abricate --list
DATABASE        SEQUENCES       DBTYPE  DATE
card    2631    nucl    2024-Apr-30
ncbi    5386    nucl    2024-Apr-30
vfdb    2597    nucl    2024-Apr-30
megares 6635    nucl    2024-Apr-30
ecoli_vf        2701    nucl    2024-Apr-30
argannot        2223    nucl    2024-Apr-30
ecoh    597     nucl    2024-Apr-30
plasmidfinder   460     nucl    2024-Apr-30
resfinder       3077    nucl    2024-Apr-30
vibrio  8       nucl    2024-Apr-30

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
