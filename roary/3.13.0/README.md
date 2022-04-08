# Roary container

Main tool : [Roary](https://github.com/sanger-pathogens/Roary)

Additional tools:
- Jellyfish
- cpanm for a million perl libraries
- Kraken

Full documentation: https://github.com/sanger-pathogens/Roary

Rapid large-scale prokaryotic pan genome analysis

# Example Usage

```
# aligning all gff files created from prokka
roary -p 16 -f roary -e -n *.gff
```

* Note : be sure to check the `summary_statistics.txt` file created at the end to determine how useful the alignment is going to be for you.
