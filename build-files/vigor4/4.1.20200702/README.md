# VIGOR4 container

Main tool: [vigor4](https://github.com/JCVenterInstitute/VIGOR4)
  
Code repository: https://github.com/JCVenterInstitute/VIGOR4

Additional tools:
- exonerate: 2.4.0

Basic information on how to use this tool:
- executable: vigor4
- help: -h
- version: --version
- description: |
> VIGOR4 (Viral Genome ORF Reader) is a Java application to predict protein sequences encoded in viral genomes.
> VIGOR4 determines the protein coding sequences by sequence similarity searching against curated viral protein databases.

Additional information:

All databases in VIGOR4_DB have been downloaded to /VIGOR_DB and can be found at /VIGOR_DB/Reference_DBs.

Currently included databases:
```bash
antennavirus_txid2560091_db
bandavirus_txid2733256_db
beidivirus_txid2501981_db
cicadellivirus_txid2948664_db
coguvirus_txid2560118_db
dengue_GP_mp
dengue_txid12637_db
embe_db
embe_orf1a_mp
embe_orf1ab_mp
entovirus_txid2733257_db
feravirus_txid2501995_db
flua_db
flua_ha_mp
flub_db
fluc_db
goukovirus_txid1980420_db
hantaviridae_db
hartmanivirus_txid2169607_db
hibeco_db
hibeco_orf1a_mp
hibeco_orf1ab_mp
horwuvirus_txid2501976_db
hudivirus_txid2501977_db
hudovirus_txid2501978_db
inshuvirus_txid2501996_db
ixovirus_txid2733258_db
jonvirus_txid2501997_db
lassa_db
laulavirus_txid2560166_db
lentinuvirus_txid2733259_db
merbe_db
merbe_orf1a_mp
merbe_orf1ab_mp
mobuvirus_txid2501979_db
monkeypox_db
nairoviridae_db
nobeco_db
nobeco_orf1a_mp
nobeco_orf1ab_mp
orthophasmavirus_txid1980538_db
peribunyaviridae_db
phasivirus_txid1980421_db
phlebovirus_txid11584_db
pidchovirus_txid2501975_db
reptarenavirus_txid1653395_db
rsv_db
rtva_db
rtvb_db
rtvc_db
rtvf_db
rtvg_db
rubodvirus_txid2733260_db
sapo_db
sapo_mp
sarbe_db
sarbe_orf1a_mp
sarbe_orf1ab_mp
sarscov2_db
sarscov2_orf1a_mp
sarscov2_orf1ab_mp
sawastrivirus_txid2560224_db
tenuivirus_txid12329_db
uukuvirus_txid2734594_db
veev_db
veev_nsp_mp
veev_sp_mp
wenrivirus_txid2560254_db
wnvII_db
wnvI_db
wnv_GP1_mp
wnv_GP2_mp
wnv_GP3_mp
wuhivirus_txid2501998_db
zikv_db
zikv_mp
```

VIGOR4_DB is up-to-date with commit [390582955049b9ddc989510672fbde90cf3387c7](https://github.com/JCVenterInstitute/VIGOR_DB/commits/master/) on Dec 1, 2022.
  
Full documentation: [https://github.com/JCVenterInstitute/VIGOR4](https://github.com/JCVenterInstitute/VIGOR4)

## Example Usage

```bash
vigor4 -i entovirus.fasta -o entovirus -d /VIGOR_DB/Reference_DBs/entovirus_txid2733257_db
```
