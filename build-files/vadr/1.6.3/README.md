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

- sarscov2 v1.3-2
- Mpox (AKA MPXV, formerly known as "Monkeypox") v1.4.2-1
- Norovirus and other Caliciviridae
- Dengue virus and other Flaviviridae
- RSV v1.5.1-2
- influenza v1.6.3-1

## FYI

- Mpox FYIs
  - **Note:** Support for MonkeyPox genome annotation was added to the VADR software (July 2022) and is under active development. Things may change quickly. See the above documentation ^ to see the latest information on the state of MPXV annotation with VADR.
  - Also be aware that some Mpox sequences may take up to **30 minutes** to annotate, depending on how divergent it is from the RefSeq NC_063383 sequence. Some sequences may only take a minute or so.
- Most of the VADR model files are located at `/opt/vadr/vadr-models` in the container filesystem and this path is stored in the globally accessible bash variable `$VADRMODELDIR`. For most applications, there is no need to specify `v-annotate.pl --mdir /path/to/model/files` since `$VADRMODELDIR` is set in the environment.
  - The exception is that Dengue and other Flaviviridae model files are located at `/opt/vadr/vadr-models-flavi/` within the container filesystem. To use these models, please specify the 2 options: `v-annotate.pl --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi`. A full example command can be found below.

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

```
