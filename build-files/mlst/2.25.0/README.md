# mlst container

Main tool : [mlst](https://github.com/tseemann/mlst)

Additional tools:

- ncbi-blast+ 2.9.0
- perl 5.34.0
- any2fasta 0.4.2

Full documentation: [https://github.com/tseemann/mlst](https://github.com/tseemann/mlst)

Scan contig files against PubMLST typing schemes

## pubMLST databases

This docker image contains databases that were updated approximately in early December 2025 when version 2.25.0 of mlst was released.

Each subdirectory in `/mlst-2.25.0/db/pubmlst/<scheme-name>/` contains a file `database_version.txt` that indicates the date that the specific database was last updated.

Available schemes found here: [https://github.com/tseemann/mlst/tree/master/db/pubmlst](https://github.com/tseemann/mlst/tree/master/db/pubmlst)

The Providencia spp. scheme (last updated 2025-12-11) was manually added to this docker image since it is not included by default with mlst v2.25.0. The FASTA files were downloaded from pubMLST.org and added to mlst's pubmlst database files & scheme. Users can either provide the argument --scheme providencia or allow for the auto-detection feature to detect the scheme automatically when typing Providencia genomes.

```bash
# sorted list of available mlst schemes
$ mlst --list 2>/dev/null | tr ' ' '\n' | sort | tr '\n' ' ' | fold -s -w80
aactinomycetemcomitans abaumannii abaumannii_2 achromobacter aeromonas 
aparagallinarum aphagocytophilum arcobacter bbacilliformis bcc bcereus 
bfragilis bhenselae blicheniformis_14 bordetella_3 borrelia bpseudomallei 
brachyspira brachyspira_2 brachyspira_3 brachyspira_4 brachyspira_5 brucella 
bsubtilis bwashoensis campylobacter campylobacter_nonjejuni 
campylobacter_nonjejuni_2 campylobacter_nonjejuni_3 campylobacter_nonjejuni_4 
campylobacter_nonjejuni_5 campylobacter_nonjejuni_6 campylobacter_nonjejuni_7 
campylobacter_nonjejuni_8 campylobacter_nonjejuni_9 cbotulinum cdifficile 
cdiphtheriae cfreundii chlamydiales cmaltaromaticum cperfringens cronobacter 
csepticum diphtheria_3 dnodosus ecloacae ecoli ecoli_achtman_4 edwardsiella 
efaecalis efaecium fpsychrophilum gallibacterium geotrichum hcinaedi 
helicobacter hinfluenzae hparasuis hsuis kaerogenes kingella klebsiella 
koxytoca leptospira leptospira_2 leptospira_3 lgarvieae liberibacter listeria_2 
llactis_phage lsalivarius mabscessus magalactiae manserisalpingitidis mbovis 
mbovis_2 mcanis mcaseolyticus mcatarrhalis_achtman_6 mflocculare mgallisepticum 
mgallisepticum_2 mgenitalium mhaemolytica mhominis mhominis_3 mhyopneumoniae 
mhyorhinis mhyosynoviae miowae mplutonius mpneumoniae msciuri msynoviae 
mycobacteria_2 neisseria oralstrep orhinotracheale otsutsugamushi pacnes_3 
paeruginosa pdamselae pfluorescens pgingivalis plarvae pmultocida pmultocida_2 
ppentosaceus pputida proteus providencia psalmonis ranatipestifer rhodococcus 
sagalactiae saureus sbsec scanis schromogenes sdysgalactiae senterica_achtman_2 
sepidermidis serratia sgallolyticus shaemolyticus shewanella shominis siniae 
sinorhizobium smaltophilia smitis spneumoniae spseudintermedius spyogenes ssuis 
staphlugdunensis sthermophilus streptomyces streptothermophilus suberis 
szooepidemicus taylorella tenacibaculum tpallidum tvaginalis ureaplasma 
vcholerae vcholerae_2 vibrio vparahaemolyticus vtapetis vvulnificus wolbachia 
xfastidiosa ypseudotuberculosis_achtman_3 yruckeri
```

## Example Usage

```bash
mlst --nopath contigs.fasta > mlst-results.tsv
```
