# Mykrobe (and genotyphi and sonneityping) docker image

Main tool : [Mykrobe](https://github.com/Mykrobe-tools/mykrobe)

Additional tools:

- [genotyphi](https://github.com/typhoidgenomics/genotyphi) 2.0
- [sonneityping](https://github.com/katholt/sonneityping) v20210201
- python 3.10.10
- biopython 1.81
- pandas 1.5.3

Full documentation: [https://github.com/Mykrobe-tools/mykrobe/wiki](https://github.com/Mykrobe-tools/mykrobe/wiki)

This docker image was created with the intention of running `genotyphi` on FASTQ files from Salmonella Typhi isolates using the Mykrobe implementation of `genotyphi`. However, this docker image contains the full (bio)conda environment for `mykrobe`, and thus can be used for other organisms as well (Mycobacterium tuberculosis, Staphylococcus aureus, Shigella sonnei)

The docker image was also created with the intention of running Mykrobe on Shigella sonnei FASTQ files, and therefore includes the python script from `sonneityping` which can be used to parse the outputs of `mykrobe`.

## Included Mykrobe databases (AKA panels)

The docker image for Mykrobe was built on 2023-04-17, and thus contains the most recent database that was available at the time.

```bash
### OUTPUT FROM mykrobe panels describe run on 2023-03-30: ###
$ mykrobe panels describe
# Species summary:

# Species Update_available        Installed_version       Installed_url   Latest_version  Latest_url
# sonnei  no      20210201        https://ndownloader.figshare.com/files/26274424 20210201        https://ndownloader.figshare.com/files/26274424
# staph   no      20201001        https://ndownloader.figshare.com/files/24914930 20201001        https://ndownloader.figshare.com/files/24914930
# tb      no      20220705        https://ndownloader.figshare.com/files/36197349 20220705        https://ndownloader.figshare.com/files/36197349
# typhi   no      20221208        https://ndownloader.figshare.com/files/38478086 20221208        https://ndownloader.figshare.com/files/38478086

# sonnei default panel: 20210201
# sonnei panels:
# Panel   Reference       Description
# 20201012        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
# 20210201        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)

# staph default panel: 20170217
# staph panels:
# Panel   Reference       Description
# 20170217        BX571856.1      AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)

# tb default panel: 202206
# tb panels:
# Panel   Reference       Description
# 201901  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
# 202010  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
# 202206  NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), and lineage scheme from Chiner-Oms 2020
# bradley-2015    NC_000962.3     AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
# walker-2015     NC_000962.3     AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202

# typhi default panel: 20221207
# typhi panels:
# Panel   Reference       Description
# 20210323        AL513382.1      GenoTyphi genotyping scheme and AMR calling using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766)
# 20221207        AL513382.1      v20220712 of GenoTyphi genotyping scheme and AMR calling for Salmonella Typhi, using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766), Sikorski et al 2022 (https://doi.org/10.1128/mbio.01920-22) and the technical report at https://doi.org/10.5281/zenodo.7407985.
```

## Example Usage

Following directions from here for running the `mykrobe` implementation of `genotyphi`: https://github.com/katholt/genotyphi#running-mykrobe

### Salmonella serovar Typhi/genotyphi example

```bash
# launch the container interactively
$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -it staphb/mykrobe:latest

# run genotyphi/mykrobe on Illumina reads from a Salmonella typhi isolate
$ mykrobe predict --sample SRR3277297 --species typhi --format json --out SRR3277297.genotyphi.json --seq SRR3277297_1.fastq.gz SRR3277297_2.fastq.gz

# parse mykrobe output with helper script from genotyphi; generate TSV
$ python /genotyphi/parse_typhi_mykrobe.py --jsons SRR3277297.genotyphi.json --prefix mykrobe_out
SRR3277297

# print out results TSV
$ column -t -s $'\t' mykrobe_out_predictResults.tsv
genome      species  spp_percent  final genotype  confidence  acrB_R717L  acrB_R717Q  num QRDR  lowest support for genotype marker  poorly supported markers  max support for additional markers  additional markers  node support                                                                                  parC_S80R  parC_S80I  parC_E84G  parC_E84K  gyrA_S83F  gyrA_S83Y  gyrA_D87G  gyrA_D87N  gyrA_D87V  gyrA_D87Y  gyrB_S464F  gyrB_S464Y  catA1  dfrA7  sul1  sul2  strA  strB  mphA  TEM1  qnrS1  ermB  CTXM15  tetB  tetA  dfrA5  dfrA15  IncFIAHI1  IncHI1A  IncHI1BR27  IncHI1_ST6  IncY  z66
SRR3277297  typhi    91.715       2.3.1           strong      0           0           1                                                                                                                               1 (1; 0/69); 2 (1; 0/102); 2.2 (1; 134/0); 2.3 (1; 110/0); 2.3.2 (1; 82/0); 2.3.1 (1; 106/0)  0          0          0          0          0          0          0          0          0          0          1           0           0      0      0     0     0     0     0     0     0      0     0       0     0     0      0       0          0        0           0           0     0
```

### Shigella sonnei/sonneityping example

```bash
# launch the container interactively
$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) -it staphb/mykrobe:0.12.1

# run genotyphi/mykrobe on Illumina reads from a Salmonella typhi isolate
$ mykrobe predict --sample Ssonnei --species sonnei --format json_and_csv --out Ssonnei --seq shigella_sonnei_R1.fastq.gz shigella_sonnei.fastq.gz

# parse mykrobe output JSON with helper script from sonneityping; must use alleles.txt file found inside docker container
# generate TSV output
$ python /sonneityping/parse_mykrobe_predict.py --jsons Ssonnei.json --alleles /sonneityping/alleles.txt --prefix sonneityping

# print out results TSV
$ column -t -s $'\t' sonneityping_predictResults.tsv
genome     species    final genotype  name       confidence  num QRDR  parC_S80I  gyrA_S83L  gyrA_S83A  gyrA_D87G  gyrA_D87N  gyrA_D87Y  lowest support for genotype marker  poorly supported markers  max support for additional markers  additional markers  node support
Ssonnei    S. sonnei  3.6.1.1.2       CipR.MSM5  strong      3         1          1          0          1          0          0                                                                                                                                lineage3 (1; 65/0); lineage3.6 (1; 94/0); lineage3.6.1 (1; 59/0); lineage3.6.1.1 (1; 74/0); lineage3.6.1.1.2 (1; 65/0)
```
