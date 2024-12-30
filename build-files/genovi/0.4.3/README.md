# genovi container

Main tool: [GenoVi](https://github.com/robotoD/GenoVi)
  
Code repository: https://github.com/robotoD/GenoVi

Additional tools:
- circos
- python: 3.7

Basic information on how to use this tool:
- executable: genovi
- help: --help
- version: --version
- description: GenoVi generates circular genome representations.

> GenoVi generates circular genome representations for complete, draft, and multiple bacterial and archaeal genomes. GenoVi pipeline combines several python scripts to automatically generate all needed files for Circos to generate circular plots, including customisable options for colour palettes, fonts, font format, background colour and scaling options for genomes comprising more than 1 replicon. 
  
Full documentation: https://github.com/robotoD/GenoVi

## Example Usage

```bash
genovi -i <input>.gbk -s complete -o out
```

