# Panaroo Container

Main tool : [Panaroo](https://github.com/gtonkinhill/panaroo)

Full documentation: https://gtonkinhill.github.io/panaroo/#/

Panaroo is an updated pipeline for pangenome investigation.

[Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, Gladstone RA, Lo S, Beaudoin C, Floto RA, Frost SDW, Corander J, Bentley SD, Parkhill J. 2020. Producing polished prokaryotic pangenomes with the Panaroo pipeline. Genome Biol 21:180.](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02090-4)


## Example Usage

```bash
# Using GFFs in the same format as output by Prokka run:
mkdir results
panaroo -i *.gff -o results --clean-mode strict
```
