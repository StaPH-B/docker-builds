# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

You can find [additional information on the SARS-CoV-2 models used by VADR here](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation#sarscov2models). The models are downloaded from the [NCBI FTP server](https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/)

Additional tools:

- perl v5.22.1
- infernal v1.1.5
- ncbi-blast+ v2.15.0
- fasta v36.3.8h (the tool, not the file format)
- minimap2 v2.26

Available VADR models:

- influenza v1.6.3-2
  - More information on this model can be found in the publication describing the creation, testing, and validation here: [https://doi.org/10.1093/database/baae091](https://doi.org/10.1093/database/baae091)

### VADR Documentation

- [Full documentation](https://github.com/ncbi/vadr#vadr-documentation-)
- [Docs on Coronavirus annotation](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation)
- [Docs on Mpox annotation](https://github.com/ncbi/vadr/wiki/Mpox-virus-annotation)
- [Docs on Dengue and other Flaviviridae annotation](https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#dengue-virus-and-other-flaviviridae-refseq-vadr-models)
- [Docs on RSV annotation](https://github.com/ncbi/vadr/wiki/RSV-annotation)
- [Docs on flu annotation](https://github.com/ncbi/vadr/wiki/Influenza-annotation)

## Example Usage

```bash
# trim terminal Ns from my input genome (VADR requires this as the first step)
# for MPXV, adjust maxlen to 210000
/opt/vadr/vadr/miniscripts/fasta-trim-terminal-ambigs.pl \
    /data/SRR13957123.consensus.fa \
    --minlen 50 \
    --maxlen 30000 \
    > /data/SRR13957123.consensus.trimmed.fasta

# run v-annotate.pl using the sarscov2 model to annotate a trimmed input genome
v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
    --mkey sarscov2 --lowsim5seq 6 \
    --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
    /data/SRR13957123.consensus.trimmed.fasta \
    SRR13957123-vadr-outdir

# run v-annotate.pl using mpxv model to annotate a trimmed input genome
v-annotate.pl --split --cpu 8 --glsearch -s -r --nomisc --mkey mpxv \
    --r_lowsimok --r_lowsimxd 100 --r_lowsimxl 2000 --alt_pass discontn,dupregin \
    --minimap2 --s_overhang 150 \
    mpxv.consensus.trimmed.fasta \
    mpxv-vadr-1.5-test-output

# run v-annotate.pl using Flaviviridae model to annotate a Dengue viral genome
v-annotate.pl --split --cpu 1 --group Dengue --nomisc --noprotid \
    --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi \
    GCF_000862125.1_ViralProj15306_genomic.fna \
    dengue-test-outdir

# run v-annotate.pl using flu models to annotate input sequences in flu.fa
v-annotate.pl --split --cpu 8 -r --atgonly --xnocomp --nomisc \
    --alt_fail extrant5,extrant3 --mkey flu \
    flu.fa \
    flu-test-output

# run v-annotate.pl using HAV modesl to annotate an HAV FASTA file
# the "-mkey hav.vadr" option is required to specify the HAV model
 v-annotate.pl --split \
     -r \
     -xnocomp \
     -mkey hav.vadr \
     hav.trimmed.fasta \
     hav-vadr-test-output
```
