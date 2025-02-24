# mlst container

Main tool : [mlst](https://github.com/tseemann/mlst)

Additional tools:

- ncbi-blast+ 2.9.0
- perl 5.30.0
- any2fasta 0.4.2

Full documentation: [https://github.com/tseemann/mlst](https://github.com/tseemann/mlst)

Scan contig files against PubMLST typing schemes

## pubMLST databases

This docker image contains data that was submitted on or prior to 2024-12-31.

Available schemes found here: [https://github.com/tseemann/mlst/tree/master/db/pubmlst](https://github.com/tseemann/mlst/tree/master/db/pubmlst)

__NOTE:__ This specific docker image also has 2 additional schemes that were not available in previous docker images:

- Serratia spp. https://pubmlst.org/organisms/serratia-spp
- Providencia spp. https://pubmlst.org/organisms/providencia-spp

These schemes can optionally be accessed using the `mlst --scheme` option with either `serratia` or `providencia`. `mlst` also has the ability to auto detect the scheme so it's not necessary to specify the scheme at runtime.

```bash
# sorted list of available mlst schemes
$ mlst --list 2>/dev/null | tr ' ' '\n' | sort | tr '\n' ' ' | fold -s -w80
aactinomycetemcomitans abaumannii abaumannii_2 achromobacter aeromonas 
aphagocytophilum arcobacter bbacilliformis bcc bcereus bfragilis bhenselae 
blicheniformis_14 bordetella_3 borrelia bpseudomallei brachyspira brachyspira_2 
brachyspira_3 brachyspira_4 brachyspira_5 brucella bsubtilis bwashoensis 
campylobacter campylobacter_nonjejuni campylobacter_nonjejuni_2 
campylobacter_nonjejuni_3 campylobacter_nonjejuni_4 campylobacter_nonjejuni_5 
campylobacter_nonjejuni_6 campylobacter_nonjejuni_7 campylobacter_nonjejuni_8 
campylobacter_nonjejuni_9 cbotulinum cdifficile cfreundii chlamydiales 
cmaltaromaticum cperfringens cronobacter csepticum diphtheria_3 dnodosus 
ecloacae ecoli ecoli_achtman_4 edwardsiella efaecalis efaecium fpsychrophilum 
gallibacterium geotrichum hcinaedi helicobacter hinfluenzae hparasuis hsuis 
kaerogenes kingella klebsiella koxytoca leptospira leptospira_2 leptospira_3 
liberibacter listeria_2 llactis_phage lsalivarius mabscessus magalactiae 
manserisalpingitidis mbovis_2 mcanis mcaseolyticus mcatarrhalis_achtman_6 
mflocculare mgallisepticum mgallisepticum_2 mhaemolytica mhominis_3 
mhyopneumoniae mhyorhinis miowae mplutonius mpneumoniae msciuri msynoviae 
mycobacteria_2 neisseria oralstrep orhinotracheale otsutsugamushi pacnes_3 
paeruginosa pdamselae pfluorescens pgingivalis plarvae pmultocida pmultocida_2 
ppentosaceus pputida providencia psalmonis ranatipestifer rhodococcus 
sagalactiae saureus sbsec scanis schromogenes sdysgalactiae senterica_achtman_2 
sepidermidis serratia sgallolyticus shaemolyticus shewanella shominis 
sinorhizobium smaltophilia spneumoniae spseudintermedius spyogenes ssuis 
staphlugdunensis sthermophilus streptomyces streptothermophilus suberis 
szooepidemicus taylorella tenacibaculum tpallidum ureaplasma vcholerae 
vcholerae_2 vibrio vparahaemolyticus vtapetis vvulnificus wolbachia xfastidiosa
```

## Example Usage

```bash
mlst --nopath contigs.fasta > mlst-results.tsv
```
