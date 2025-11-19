# Kleborate container

Main tool : [Kleborate](https://github.com/klebgenomics/Kleborate)

:warning: **Note:** Kleborate v3 is different from v2, please see here for the differences: https://kleborate.readthedocs.io/en/latest/index.html#changes-from-v2

Additional tools:

- [amrfinderplus](https://github.com/ncbi/amr) 4.0.23 with database version 2025-07-16.1
- biopython 1.85
- [dna-features-viewer](https://edinburgh-genome-foundry.github.io/DnaFeaturesViewer/) 3.1.5
- [ectyper](https://github.com/phac-nml/ecoli_serotyping) 2.0.0
- [ezclermont](https://github.com/nickp60/EzClermont) 0.7.0
- [mash](https://github.com/marbl/Mash) 2.3
- matplotlib 3.9.4
- [minimap2](https://github.com/lh3/minimap2) 2.30
- numpy 2.0.2
- python 3.9.23
- [kaptive](https://github.com/klebgenomics/Kaptive) 3.1.0
- [stxtyper](https://github.com/ncbi/stxtyper/) 1.0.42

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                     Version       Build                 Channel    
#13 7.659 ────────────────────────────────────────────────────────────────────────────
#13 7.659   _libgcc_mutex            0.1           conda_forge           conda-forge
#13 7.659   _openmp_mutex            4.5           2_gnu                 conda-forge
#13 7.659   bcftools                 1.22          h3a4d415_1            bioconda   
#13 7.659   biopython                1.85          py39h8cd3c5a_1        conda-forge
#13 7.659   blast                    2.17.0        h66d330f_0            bioconda   
#13 7.659   bowtie2                  2.5.4         he96a11b_6            bioconda   
#13 7.659   brotli-python            1.1.0         py39hf88036b_3        conda-forge
#13 7.659   bzip2                    1.0.8         hda65f42_8            conda-forge
#13 7.659   c-ares                   1.34.5        hb9d3cd8_0            conda-forge
#13 7.659   ca-certificates          2025.10.5     hbd8a1cb_0            conda-forge
#13 7.659   capnproto                1.0.2         h766bdaa_3            conda-forge
#13 7.659   certifi                  2025.8.3      pyhd8ed1ab_0          conda-forge
#13 7.659   cffi                     1.17.1        py39h15c3d72_0        conda-forge
#13 7.659   charset-normalizer       3.4.3         pyhd8ed1ab_0          conda-forge
#13 7.659   colorama                 0.4.6         pyhd8ed1ab_1          conda-forge
#13 7.659   contourpy                1.3.0         pypi_0                pypi       
#13 7.659   coverage                 7.10.4        py39heb7d2ae_0        conda-forge
#13 7.659   curl                     8.17.0        h4e3cde8_0            conda-forge
#13 7.659   cycler                   0.12.1        pypi_0                pypi       
#13 7.659   dna_features_viewer      3.1.5         pypi_0                pypi       
#13 7.659   ectyper                  2.0.0         pyhdfd78af_4          bioconda   
#13 7.659   entrez-direct            24.0          he881be0_0            bioconda   
#13 7.659   exceptiongroup           1.3.0         pyhd8ed1ab_0          conda-forge
#13 7.659   ezclermont               0.7.0         pyhdfd78af_0          bioconda   
#13 7.659   fonttools                4.60.1        pypi_0                pypi       
#13 7.659   gsl                      2.7           he838d99_0            conda-forge
#13 7.659   h2                       4.2.0         pyhd8ed1ab_0          conda-forge
#13 7.659   hmmer                    3.4           hb6cb901_4            bioconda   
#13 7.659   hpack                    4.1.0         pyhd8ed1ab_0          conda-forge
#13 7.659   htslib                   1.22.1        h566b1c6_0            bioconda   
#13 7.659   hyperframe               6.1.0         pyhd8ed1ab_0          conda-forge
#13 7.659   icu                      75.1          he02047a_0            conda-forge
#13 7.659   idna                     3.10          pyhd8ed1ab_1          conda-forge
#13 7.659   importlib_resources      6.5.2         pypi_0                pypi       
#13 7.659   iniconfig                2.0.0         pyhd8ed1ab_1          conda-forge
#13 7.659   k8                       1.2           he8db53b_6            bioconda   
#13 7.659   kaptive                  3.1.0         pypi_0                pypi       
#13 7.659   kernel-headers_linux-64  5.14.0        he073ed8_2            conda-forge
#13 7.659   keyutils                 1.6.3         hb9d3cd8_0            conda-forge
#13 7.659   kiwisolver               1.4.7         pypi_0                pypi       
#13 7.659   kleborate                3.2.4         pypi_0                pypi       
#13 7.659   krb5                     1.21.3        h659f571_0            conda-forge
#13 7.659   ld_impl_linux-64         2.44          h1aa0949_5            conda-forge
#13 7.659   libblas                  3.9.0         38_h4a7cf45_openblas  conda-forge
#13 7.659   libcblas                 3.9.0         38_h0358290_openblas  conda-forge
#13 7.659   libcurl                  8.17.0        h4e3cde8_0            conda-forge
#13 7.659   libdeflate               1.25          h17f619e_0            conda-forge
#13 7.659   libedit                  3.1.20250104  pl5321h7949ede_0      conda-forge
#13 7.659   libev                    4.33          hd590300_2            conda-forge
#13 7.659   libexpat                 2.7.1         hecca717_0            conda-forge
#13 7.659   libffi                   3.5.2         h9ec8514_0            conda-forge
#13 7.659   libgcc                   15.2.0        h767d61c_7            conda-forge
#13 7.659   libgcc-ng                15.2.0        h69a702a_7            conda-forge
#13 7.659   libgfortran              15.2.0        h69a702a_7            conda-forge
#13 7.659   libgfortran-ng           15.2.0        h69a702a_7            conda-forge
#13 7.659   libgfortran5             15.2.0        hcd61629_7            conda-forge
#13 7.659   libgomp                  15.2.0        h767d61c_7            conda-forge
#13 7.659   libidn2                  2.3.8         hfac485b_1            conda-forge
#13 7.659   liblapack                3.9.0         38_h47877c9_openblas  conda-forge
#13 7.659   liblzma                  5.8.1         hb9d3cd8_2            conda-forge
#13 7.659   libnghttp2               1.67.0        had1ee68_0            conda-forge
#13 7.659   libnsl                   2.0.1         hb9d3cd8_1            conda-forge
#13 7.659   libopenblas              0.3.30        pthreads_h94d23a6_3   conda-forge
#13 7.659   libsqlite                3.51.0        hee844dc_0            conda-forge
#13 7.659   libssh2                  1.11.1        hcf80075_0            conda-forge
#13 7.659   libstdcxx                15.2.0        h8f9b012_7            conda-forge
#13 7.659   libstdcxx-ng             15.2.0        h4852527_7            conda-forge
#13 7.659   libunistring             0.9.10        h7f98852_0            conda-forge
#13 7.659   libuuid                  2.41.2        he9a06e4_0            conda-forge
#13 7.659   libxcrypt                4.4.36        hd590300_1            conda-forge
#13 7.659   libzlib                  1.3.1         hb9d3cd8_2            conda-forge
#13 7.659   mash                     2.3           hb105d93_9            bioconda   
#13 7.659   matplotlib               3.9.4         pypi_0                pypi       
#13 7.659   minimap2                 2.30          h577a1d6_0            bioconda   
#13 7.659   mpi                      1.0           openmpi               conda-forge
#13 7.659   ncbi-amrfinderplus       4.0.23        hf69ffd2_0            bioconda   
#13 7.659   ncbi-vdb                 3.2.1         h9948957_0            bioconda   
#13 7.659   ncurses                  6.5           h2d0b736_3            conda-forge
#13 7.659   numpy                    2.0.2         py39h9cb892a_1        conda-forge
#13 7.659   openmpi                  4.1.6         hc5af2df_101          conda-forge
#13 7.659   openssl                  3.6.0         h26f9b46_0            conda-forge
#13 7.659   packaging                25.0          pyh29332c3_1          conda-forge
#13 7.659   pandas                   2.3.1         py39h1b6b32d_0        conda-forge
#13 7.659   pcre2                    10.45         hc749103_0            conda-forge
#13 7.659   perl                     5.32.1        7_hd590300_perl5      conda-forge
#13 7.659   perl-archive-tar         3.04          pl5321hdfd78af_0      bioconda   
#13 7.659   perl-carp                1.50          pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-common-sense        3.75          pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-compress-raw-bzip2  2.214         pl5321hda65f42_0      conda-forge
#13 7.659   perl-compress-raw-zlib   2.214         pl5321h4dac143_0      conda-forge
#13 7.659   perl-encode              3.21          pl5321hb9d3cd8_1      conda-forge
#13 7.659   perl-exporter            5.74          pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-exporter-tiny       1.002002      pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-extutils-makemaker  7.70          pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-io-compress         2.213         pl5321h503566f_0      bioconda   
#13 7.659   perl-io-zlib             1.15          pl5321hdfd78af_1      bioconda   
#13 7.659   perl-json                4.10          pl5321hdfd78af_1      bioconda   
#13 7.659   perl-json-xs             4.04          pl5321h9948957_0      bioconda   
#13 7.659   perl-list-moreutils      0.430         pl5321hdfd78af_0      bioconda   
#13 7.659   perl-list-moreutils-xs   0.430         pl5321h7b50bb2_5      bioconda   
#13 7.659   perl-parent              0.243         pl5321hd8ed1ab_0      conda-forge
#13 7.659   perl-pathtools           3.75          pl5321hb9d3cd8_2      conda-forge
#13 7.659   perl-scalar-list-utils   1.70          pl5321hb03c661_0      conda-forge
#13 7.659   perl-storable            3.15          pl5321hb9d3cd8_2      conda-forge
#13 7.659   perl-types-serialiser    1.01          pl5321hdfd78af_0      bioconda   
#13 7.659   pillow                   11.3.0        pypi_0                pypi       
#13 7.659   pip                      25.2          pyh8b19718_0          conda-forge
#13 7.659   pluggy                   1.6.0         pyhd8ed1ab_0          conda-forge
#13 7.659   pycparser                2.22          pyh29332c3_1          conda-forge
#13 7.659   pygments                 2.19.2        pyhd8ed1ab_0          conda-forge
#13 7.659   pyparsing                3.2.5         pypi_0                pypi       
#13 7.659   pysocks                  1.7.1         pyha55dd90_7          conda-forge
#13 7.659   pytest                   8.4.1         pyhd8ed1ab_0          conda-forge
#13 7.659   python                   3.9.23        hc30ae73_0_cpython    conda-forge
#13 7.659   python-dateutil          2.9.0.post0   pyhe01879c_2          conda-forge
#13 7.659   python-tzdata            2025.2        pyhd8ed1ab_0          conda-forge
#13 7.659   python_abi               3.9           8_cp39                conda-forge
#13 7.659   pytz                     2025.2        pyhd8ed1ab_0          conda-forge
#13 7.659   readline                 8.2           h8c095d6_2            conda-forge
#13 7.659   requests                 2.32.5        pyhd8ed1ab_0          conda-forge
#13 7.659   samtools                 1.22.1        h96c455f_0            bioconda   
#13 7.659   seqtk                    1.5           h577a1d6_1            bioconda   
#13 7.659   setuptools               80.9.0        pyhff2d567_0          conda-forge
#13 7.659   six                      1.17.0        pyhe01879c_1          conda-forge
#13 7.659   sysroot_linux-64         2.34          h087de78_2            conda-forge
#13 7.659   tk                       8.6.13        noxft_hd72426e_102    conda-forge
#13 7.659   tomli                    2.2.1         pyhe01879c_2          conda-forge
#13 7.659   typing_extensions        4.14.1        pyhe01879c_0          conda-forge
#13 7.659   tzdata                   2025b         h78e105d_0            conda-forge
#13 7.659   urllib3                  2.5.0         pyhd8ed1ab_0          conda-forge
#13 7.659   wget                     1.25.0        hc2d8bac_0            conda-forge
#13 7.659   wheel                    0.45.1        pyhd8ed1ab_1          conda-forge
#13 7.659   zipp                     3.23.0        pypi_0                pypi       
#13 7.659   zlib                     1.3.1         hb9d3cd8_2            conda-forge
#13 7.659   zstandard                0.23.0        py39hd399759_3        conda-forge
#13 7.659   zstd                     1.5.7         hb8e6e7a_2            conda-forge
```
</details>

Full documentation: [https://kleborate.readthedocs.io/en/latest/index.html](https://kleborate.readthedocs.io/en/latest/index.html)

Description:
> Kleborate is a tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC) for:
> 
> - MLST sequence type
> - species (e.g. K. pneumoniae, K. quasipneumoniae, K. variicola, etc.)
> - ICEKp associated virulence loci: yersiniabactin (ybt), colibactin (clb), salmochelin (iro), hypermucoidy (rmpA)
> - virulence plasmid associated loci: salmochelin (iro), aerobactin (iuc), hypermucoidy (rmpA, rmpA2)
> - antimicrobial resistance determinants: acquired genes, SNPs, gene truncations and intrinsic β-lactamases
> - K (capsule) and O antigen (LPS) serotype prediction, via wzi alleles and Kaptive

## Included models

Kleborate has modules for both Klebsiella and Escherichia species. The available presets and modules are listed below.

Available presets: kpsc, kosc, escherichia

```
Available modules for Kleborate
-------------------------------
enterobacterales__species: Mash-based species detection for enterobacterales species

escherichia__mlst_achtman: chromosomal MLST for Escherichia coli using the Achtman scheme

escherichia__mlst_pasteur: chromosomal MLST for Escherichia coli using the Pasteur scheme

general__contig_stats: basic stats on the assembly's contigs

klebsiella__abst: MLST on the KpSC aerobactin locus (iuc genes)

klebsiella__cbst: MLST on the KpSC colibactin locus (clb genes)

klebsiella__rmpa2: typing for the rmpA2 gene

klebsiella__rmst: MLST on the KpSC Rmp locus (rmp genes)

klebsiella__smst: MLST on the KpSC salmochelin locus (iro genes)

klebsiella__ybst: MLST on the KpSC yersiniabactin locus (ybt and irp genes)

klebsiella_oxytoca_complex__mlst: chromosomal MLST for the Klebsiella oxytoca species complex

klebsiella_pneumo_complex__amr: Genotyping acquired genes and mutations for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__kaptive: In silico serotyping of K and L locus for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__mlst: chromosomal MLST for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__resistance_class_count: Resistance gene classes count, excluding the Bla_chr class which is intrinsicresults of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__resistance_gene_count: Resistance genes counts, excluding the Bla class which is intrinsicresults of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__resistance_score: resistance score (0-3) for the Klebsiella pneumoniae species complex, based on the results of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__virulence_score: virulence score (0-5) for the Klebsiella pneumoniae species complex, based on the results of the abst, cbst
and ybst modules

klebsiella_pneumo_complex__wzi: WZI typing for K antigen prediction
```

## Example Usage

```bash
kleborate -a sample.fasta -o outdir -p preset
```
