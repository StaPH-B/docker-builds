# EMBOSS Container

## Main Tool
**EMBOSS**  
Website: [http://emboss.sourceforge.net](http://emboss.sourceforge.net)  
Code Repository: [http://emboss.sourceforge.net](http://emboss.sourceforge.net)  
Documentation: [https://emboss.sourceforge.net///what/#Uses](https://emboss.sourceforge.net///what/#Uses)

## Description
> **EMBOSS** (The European Molecular Biology Open Software Suite) is a free Open Source software analysis package specially developed for the needs of the molecular biology user community. It supports numerous file formats, offers transparent web-based sequence retrieval, and provides a development platform with integrated libraries. EMBOSS consolidates a wide range of bioinformatics tools into a cohesive suite and promotes open scientific software development.

## Executables

EMBOSS includes **hundreds of bioinformatics applications**, with support for diverse analyses such as:

- Sequence alignment
- Pattern-based database searching
- Protein motif identification
- CpG island and repeat analysis
- Codon usage statistics
- Profile scanning and sequence pattern analysis
- Sequence visualization and presentation

### Notable Applications

| Application     | Description                                                        |
|----------------|--------------------------------------------------------------------|
| `prophet`       | Gapped alignment for profiles                                      |
| `infoseq`       | Displays simple information about sequences                        |
| `water`         | Smith-Waterman local alignment                                     |
| `pepstats`      | Computes protein statistics                                        |
| `showfeat`      | Displays sequence features                                         |
| `palindrome`    | Detects inverted repeats in nucleotide sequences                   |
| `eprimer3`      | Picks PCR primers and hybridization oligos                         |
| `profit`        | Scans a sequence with a matrix or profile                          |
| `extractseq`    | Extracts regions from a sequence                                   |
| `marscan`       | Finds MAR/SAR sites in nucleotide sequences                        |
| `tfscan`        | Scans DNA sequences for transcription factors                      |
| `patmatmotifs`  | Compares proteins to the PROSITE motif database                    |
| `showdb`        | Displays available database info                                   |
| `wossname`      | Searches programs by keywords in their documentation               |
| `abiview`       | Displays ABI chromatogram trace files                              |
| `tranalign`     | Aligns nucleotide coding regions based on aligned proteins         |

## Usage

- Help: Most programs support the `-help` flag  
- Version: Use application --version, for example: `water --version` to check suite version

## Example Usage
```bash
# Perform local alignment between two sequences using the Smith-Waterman algorithm
water -asequence X01753.1.fa -bsequence X01755.1.fa -gapopen 10 -gapextend 0.5 -outfile alignment.water
