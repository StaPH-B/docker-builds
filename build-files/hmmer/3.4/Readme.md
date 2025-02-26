# HMMER container

Main tool : [HMMER](http://hmmer.org/)

Code repository: https://github.com/EddyRivasLab/hmmer

Basic information on how to use this tool:
- executables:
    - alimask
    - hmmalign
    - hmmbuild
    - hmmconvert
    - hmmemit
    - hmmfetch
    - hmmlogo
    - hmmpgmd
    - hmmpgmd_shard
    - hmmpress
    - hmmscan
    - hmmsearch
    - hmmsim
    - hmmstat
    - jackhmmer
    - makehmmerdb
    - nhmmer
    - nhmmscan
    - phmmer

- help: -h
- version: -v
- description:
>HMMER searches biological sequence databases for homologous sequences, using either single sequences or multiple sequence alignments as queries. HMMER implements a technology called "profile hidden Markov models" (profile HMMs).

Full documentation: http://eddylab.org/software/hmmer/Userguide.pdf

# Example commands 

```bash
# build a profile from an alignment
hmmbuild hmm_file msa_file

# search profile against a sequence database
hmmsearch hmm_file seqs.fa
```
