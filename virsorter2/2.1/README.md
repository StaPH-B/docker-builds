# Virsorter 2 container

Main tool : [VirSorter2](https://github.com/jiarong/VirSorter2)

Additional tools:
- list

Full documentation: https://github.com/jiarong/VirSorter2

> VirSorter2 applies a multi-classifier, expert-guided approach to detect diverse DNA and RNA virus genomes.

# Example Usage

From github page

```
virsorter setup -d db -j 4
tar -xzf db.tgz
virsorter config --init-source --db-dir=./db
virsorter run -w test.out -i test.fa --min-length 1500 -j 4 all
```

From Joachim
```
virsorter config --init-source --db-dir=./db
virsorter run -w virsorter2.test.out -i test.fa -j 1
```
