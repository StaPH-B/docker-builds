# pangolin container

Main tool : [pangolin](https://github.com/cov-lineages/pangolin)

Full documentation: https://cov-lineages.org/resources/pangolin.html

Phylogenetic Assignment of Named Global Outbreak LINeages

# Example Usage

```bash
# run Pangolin in the default mode (usher). Can optionally supply --analysis-mode usher
pangolin /pangolin/pangolin/test/test_seqs.fasta  -o /data/test_seqs-output-pusher

# run Pangolin in the fast/pangolearn mode. Can use either --analysis-mode fast or --analysis-mode pangolearn
pangolin /pangolin/pangolin/test/test_seqs.fasta --analysis-mode pangolearn -o /data/test_seqs-output-plearn
```
