# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

You can find [additional information on the SARS-CoV-2 models used by VADR here](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation#sarscov2models). The models are downloaded from the [NCBI FTP server](https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/)

Additional tools:

- perl v5.22.1
- infernal v1.1.4
- hmmer v3.3.2
- ncbi-blast+ v2.12.0
- fasta v36.3.8h (the tool, not the file format)

Available VADR models:

- sarscov2 v1.3-2
- mpxv (MonkeyPox) v1.4.2-1
- Norovirus and other Caliciviridae
- Dengue virus and other Flaviviridae

Full documentation: https://github.com/ncbi/vadr#vadr-documentation-

Docs on Coronavirus annotation: https://github.com/ncbi/vadr/wiki/Coronavirus-annotation

Docs on MPXV annotation: https://github.com/ncbi/vadr/wiki/Monkeypox-virus-annotation

**Note:** Support for MonkeyPox genome annotation was just added in the VADR software (July 2022) and is under active development. Things may change quickly. See the above documentation ^ to see the latest information on the state of MPXV annotation with VADR.

Also be aware that some sequences may take up to **30 minutes** to annotate, depending on how divergent it is from the RefSeq NC_063383 sequence. Some sequences may only take a minute or so.

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
        mpxv.consensus.trimmed.fasta \
        mpxv-vadr-1.4.2-test-output
```
