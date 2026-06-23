# Mykrobe docker image

Main tool : [Mykrobe](https://github.com/Mykrobe-tools/mykrobe)

Full documentation: [https://github.com/Mykrobe-tools/mykrobe/wiki](https://github.com/Mykrobe-tools/mykrobe/wiki)

<details>

<summary>Additional tools installed via micromamba:</summary>

```
List of packages in environment: "/opt/conda/envs/mykrobe"

  Name                Version       Build                 Channel    
───────────────────────────────────────────────────────────────────────
  _openmp_mutex       4.5           20_gnu                conda-forge
  anytree             2.13.0        pyhcf101f3_1          conda-forge
  backports.zstd      1.6.0         py312h90b7ffd_0       conda-forge
  biopython           1.86          py312h47b2149_0       pkgs/main  
  blas                2.308         openblas              conda-forge
  blas-devel          3.11.0        8_h1ea3ea9_openblas   conda-forge
  brotli-python       1.2.0         py312h3dd09e2_0       pkgs/main  
  bzip2               1.0.8         hda65f42_9            conda-forge
  c-ares              1.34.6        hb03c661_0            conda-forge
  ca-certificates     2026.6.17     hbd8a1cb_0            conda-forge
  certifi             2026.6.17     pyhd8ed1ab_0          conda-forge
  charset-normalizer  3.4.7         pyhd8ed1ab_0          conda-forge
  dnspython           2.8.0         pyhcf101f3_0          conda-forge
  h2                  4.3.0         pyhcf101f3_0          conda-forge
  hpack               4.1.0         pyhd8ed1ab_0          conda-forge
  hyperframe          6.1.0         pyhd8ed1ab_0          conda-forge
  icu                 75.1          he02047a_0            conda-forge
  idna                3.18          pyhcf101f3_0          conda-forge
  keyutils            1.6.3         hb9d3cd8_0            conda-forge
  krb5                1.22.2        hbde042b_1            conda-forge
  ld_impl_linux-64    2.45.1        default_hbd61a6d_102  conda-forge
  libblas             3.11.0        8_h4a7cf45_openblas   conda-forge
  libboost            1.88.0        hed09d94_6            conda-forge
  libcblas            3.11.0        8_h0358290_openblas   conda-forge
  libcurl             8.20.0        hcf29cc6_0            conda-forge
  libedit             3.1.20250104  pl5321h7949ede_0      conda-forge
  libev               4.33          hd590300_2            conda-forge
  libexpat            2.8.1         hecca717_1            conda-forge
  libffi              3.5.2         h3435931_0            conda-forge
  libgcc              15.2.0        he0feb66_19           conda-forge
  libgcc-ng           15.2.0        h69a702a_19           conda-forge
  libgfortran         15.2.0        h69a702a_19           conda-forge
  libgfortran5        15.2.0        h68bc16d_19           conda-forge
  libgomp             15.2.0        he0feb66_19           conda-forge
  liblapack           3.11.0        8_h47877c9_openblas   conda-forge
  liblapacke          3.11.0        8_h6ae95b6_openblas   conda-forge
  liblzma             5.8.3         hb03c661_0            conda-forge
  libnghttp2          1.68.1        h877daf1_0            conda-forge
  libnsl              2.0.1         hb9d3cd8_1            conda-forge
  libopenblas         0.3.33        pthreads_h94d23a6_0   conda-forge
  libsqlite           3.53.2        h0c1763c_0            conda-forge
  libssh2             1.11.1        hcf80075_0            conda-forge
  libstdcxx           15.2.0        h934c35e_19           conda-forge
  libstdcxx-ng        15.2.0        hdf11a46_19           conda-forge
  libuuid             2.42.2        h5347b49_0            conda-forge
  libxcrypt           4.4.36        hd590300_1            conda-forge
  libzlib             1.3.2         h25fd6f3_2            conda-forge
  mongodb             7.0.34        he2e579a_0            conda-forge
  mongoengine         0.29.3        pyhcf101f3_0          conda-forge
  mykrobe             0.13.0        py312h20b014d_5       bioconda   
  ncurses             6.6           hdb14827_0            conda-forge
  numpy               1.26.4        py312hc213724_1       pkgs/main  
  numpy-base          1.26.4        py312hf387b04_1       pkgs/main  
  openblas            0.3.33        pthreads_h6ec200e_0   conda-forge
  openssl             3.6.3         h35e630c_0            conda-forge
  packaging           26.2          pyhc364b38_0          conda-forge
  pandas              3.0.3         py312h8ecdadd_0       conda-forge
  pcre2               10.47         haa7fec5_0            conda-forge
  pip                 24.2          pyhd8ed1ab_0          conda-forge
  pymongo             4.17.0        py312h47b2149_0       pkgs/main  
  pysocks             1.7.1         pyha55dd90_7          conda-forge
  python              3.12.13       hd63d673_0_cpython    conda-forge
  python-dateutil     2.9.0.post0   pyhe01879c_2          conda-forge
  python_abi          3.12          8_cp312               conda-forge
  pyvcf3              1.0.4         py312h0fa9677_0       bioconda   
  readline            8.3           h853b02a_0            conda-forge
  requests            2.34.2        pyhcf101f3_0          conda-forge
  setuptools          80.10.2       pyh332efcf_0          conda-forge
  six                 1.17.0        pyhe01879c_1          conda-forge
  snappy              1.2.2         h03e3b7b_1            conda-forge
  sniffio             1.3.1         pyhd8ed1ab_2          conda-forge
  tk                  8.6.13        noxft_h366c992_103    conda-forge
  tzdata              2025c         hc9c84f9_1            conda-forge
  urllib3             2.7.0         pyhd8ed1ab_0          conda-forge
  wheel               0.47.0        pyhd8ed1ab_0          conda-forge
  yaml-cpp            0.8.0         h3f2d84a_0            conda-forge
  zstd                1.5.7         hb78ec9c_6            conda-forge
```

</details>


### Additional Information:

This docker image was created with the intention of analyses involved with _Mycobacterium tuberculosis_ and other similar Mycobacterium species, so genotyphi and sonneityping are not included in this image.

Citations:

Hunt M, Bradley P, Lapierre SG et al. Antibiotic resistance prediction for Mycobacterium tuberculosis from genome sequence data with Mykrobe [version 1; peer review: 2 approved, 1 approved with reservations]. Wellcome Open Res 2019, 4:191 (https://doi.org/10.12688/wellcomeopenres.15603.1)

Ingle, D. J., Hawkey, J., Hunt, M., Iqbal, Z., Keane, J. A., Afolayan, A. O., Ahmed, N., Andleeb, S., Ashton, P. M., Bogoch, I. I., Carey, M. E., Chattaway, M. A., Crump, J. A., Guevara, P. D., Howden, B. P., Izumiya, H., Jacob, J. J., Judd, L. M., Kapil, A., … Global Typhoid Genomics Consortium. (2024). Typhi Mykrobe: Fast and accurate lineage identification and antimicrobial resistance genotyping directly from sequence reads for the typhoid fever agent <em>Salmonella</em> Typhi. bioRxiv, 2024.09.30.613582. https://doi.org/10.1101/2024.09.30.613582


Zoe A Dyson, Kathryn E Holt, Five Years of GenoTyphi: Updates to the Global Salmonella Typhi Genotyping Framework, The Journal of Infectious Diseases, Volume 224, Issue Supplement_7, 15 December 2021, Pages S775–S780, https://doi.org/10.1093/infdis/jiab414

Kat Holt, Zoe Anne Dyson, Jane Hawkey, & flashton2003. (2024). typhoidgenomics/genotyphi: v2.1 (v2.1). Zenodo. https://doi.org/10.5281/zenodo.13859721

### Included Mykrobe databases (AKA panels)

The docker image for Mykrobe was built on 2026-06-08, and thus contains the most recent database that was available at the time.

```bash
$ mykrobe panels describe
### OUTPUT FROM mykrobe panels describe run on 2026-06-08: ###
# Species summary:
	
# 	Species	Update_available	Installed_version	Installed_url	Latest_version	Latest_url
# 	flexneri	no	20250902	https://ndownloader.figshare.com/files/63190870	20250902	https://ndownloader.figshare.com/files/63190870
# 	paratyphiB	no	20230627	https://figshare.com/ndownloader/files/43870968	20230627	https://figshare.com/ndownloader/files/43870968
# 	sonnei	no	20210201	https://ndownloader.figshare.com/files/26274424	20210201	https://ndownloader.figshare.com/files/26274424
# 	staph	no	20201001	https://ndownloader.figshare.com/files/24914930	20201001	https://ndownloader.figshare.com/files/24914930
# 	tb	no	20230928	https://figshare.com/ndownloader/files/42494211	20230928	https://figshare.com/ndownloader/files/42494211
# 	typhi	no	20240407	https://figshare.com/ndownloader/files/49527246	20240407	https://figshare.com/ndownloader/files/49527246
	
# 	flexneri default panel: 20250902
# 	flexneri panels:
# 	Panel	Reference	Description
# 	20250902	AE005674	Genotyping panel for Shigella flexneri, including lineage and panel for variants in the quinolone resistance determining region. Described in Hawkey et al 2026.
	
# 	paratyphiB default panel: 20230627
# 	paratyphiB panels:
# 	Panel	Reference	Description
# 	20230627	CIP54_115	Genotyping scheme for Salmonella enterica serovar Paratphi B PG1
	
# 	sonnei default panel: 20210201
# 	sonnei panels:
# 	Panel	Reference	Description
# 	20201012	NC_016822.1	Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
# 	20210201	NC_016822.1	Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)
	
# 	staph default panel: 20170217
# 	staph panels:
# 	Panel	Reference	Description
# 	20170217	BX571856.1	AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
	
# 	tb default panel: 202309
# 	tb panels:
# 	Panel	Reference	Description
# 	201901	NC_000962.3	AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
# 	202010	NC_000962.3	AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
# 	202206	NC_000962.3	AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), and lineage scheme from Chiner-Oms 2020
# 	202309	NC_000962.3	AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), lineage scheme from Chiner-Oms 2020, and updated species based on GTDB r214 (doi:10.1093/nar/gkab776)
# 	bradley-2015	NC_000962.3	AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
# 	walker-2015	NC_000962.3	AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202
	
# 	typhi default panel: 20240407
# 	typhi panels:
# 	Panel	Reference	Description
# 	20210323	AL513382.1	GenoTyphi genotyping scheme and AMR calling using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766)
# 	20221207	AL513382.1	v20220712 of GenoTyphi genotyping scheme and AMR calling for Salmonella Typhi, using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766), Sikorski et al 2022 (https://doi.org/10.1128/mbio.01920-22) and the technical report at https://doi.org/10.5281/zenodo.7407985.
# 	20240407	AL513382.1	v20240407 of GenoTyphi genotyping scheme and AMR calling for Salmonella Typhi, using markers described in Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766), Sikorski et al 2022 (https://doi.org/10.1128/mbio.01920-22) and the technical report at https://doi.org/10.5281/zenodo.7407985. Includes additional probes for the carbapenemase genes KPC-2, NDM-5, VIM-1, IMP-27, OXA-48, and plasmid replicons IncX3 and p0111 as described in Ingle et al 2024 (https://doi.org/10.1101/2024.09.30.613582). Probes for resistance genes AmpC1 and OXA-134 have been removed.
```

## Example Usage
```bash
mykrobe predict -s SAMPLE -S tb -o out.json --format json -i test_reads.fq.gz
```
