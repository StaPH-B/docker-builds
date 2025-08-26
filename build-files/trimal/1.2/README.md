# trimAl Container

## Main Tool
**trimAl**  
Repository: [https://github.com/inab/trimal](https://github.com/inab/trimal)  
Documentation: [https://vicfero.github.io/trimal/](https://vicfero.github.io/trimal/)

## Additional Tools
- `readAl`

## Description
> **trimAl** is a tool for the automated removal of spurious sequences or poorly aligned regions from a multiple sequence alignment.

This container provides the `trimal` executable along with `readAl` for alignment processing.

## Executables
- `trimal`
- `readAl`

## Usage
- Help: `trimal --help`
- Version: `trimal --version`

## Example
```bash
trimal -in input.fasta -out output.fasta

