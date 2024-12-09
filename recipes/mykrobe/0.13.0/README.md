# Mykrobe docker image

Main tool : [Mykrobe](https://github.com/Mykrobe-tools/mykrobe)

Full documentation: [https://github.com/Mykrobe-tools/mykrobe/wiki](https://github.com/Mykrobe-tools/mykrobe/wiki)

This docker image was created with the intention of analyses involved with _Mycobacterium tuberculosis_ and other similar Mycobacterium species, so genotyphi and sonneityping are not included in this image.

## Included Mykrobe databases (AKA panels)

The docker image for Mykrobe was built on 2023-11-08, and thus contains the most recent database that was available at the time.

```bash
### OUTPUT FROM mykrobe panels describe run on 2023-11-08: ###
$ mykrobe panels describe
#0 12.57 Gathering data from /usr/local/lib/python3.9/site-packages/mykrobe/data
#0 12.57
#0 12.57 Species summary:
#0 12.57
#0 12.57 Species        Update_available        Installed_version       Installed_url   Latest_version  Latest_url
#0 12.57 sonnei no      20210201        https://ndownloader.figshare.com/files/26274424 20210201        https://ndownloader.figshare.com/files/26274424
#0 12.57 staph  no      20201001        https://ndownloader.figshare.com/files/24914930 20201001        https://ndownloader.figshare.com/files/24914930
#0 12.57 tb     no      20230928        https://figshare.com/ndownloader/files/42494211 20230928        https://figshare.com/ndownloader/files/42494211
#0 12.57 typhi  no      20221208        https://ndownloader.figshare.com/files/38478086 20221208        https://ndownloader.figshare.com/files/38478086
#0 12.57
#0 12.57 sonnei default panel: 20210201
#0 12.57 sonnei panels:
#0 12.57 Panel  Reference       Description
#0 12.57 20201012       NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
#0 12.57 20210201       NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)
#0 12.57
#0 12.57 staph default panel: 20170217
#0 12.57 staph panels:
#0 12.57 Panel  Reference       Description
#0 12.57 20170217       BX571856.1      AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
#0 12.57
#0 12.57 tb default panel: 202309
#0 12.57 tb panels:
#0 12.57 Panel  Reference       Description
#0 12.57 201901 NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
#0 12.57 202010 NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
#0 12.57 202206 NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), and lineage scheme from Chiner-Oms 2020
#0 12.57 202309 NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), lineage scheme from Chiner-Oms 2020, and updated species based on GTDB r214 (doi:10.1093/nar/gkab776)
#0 12.57 bradley-2015   NC_000962.3     AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
#0 12.57 walker-2015    NC_000962.3     AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202
```

## Example Usage
```bash
mykrobe predict -s SAMPLE -S tb -o out.json --format json -i test_reads.fq.gz
```