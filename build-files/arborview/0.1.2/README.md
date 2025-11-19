# ArborView container

Main tool: [ArborView](https://github.com/phac-nml/ArborView)
  
Code repository: https://github.com/phac-nml/ArborView

Additional tools:


Basic information on how to use this tool:
- executable: inline_arborview.py
- help: `-h`, `--help`
- version:
- description: ArborView visualize newick trees with associated sample metadata. `inline_arborview.py` embeds the newick file and tabular data directly into the html file eliminating the need for user data upload.

Additional information:

- Web server: https://phac-nml.github.io/ArborView/main/index.html

- metadata format

| sample_id  | serovar  | mlst_st  | earliest_date  | state_province | source_type | source_site | age | sex | reported_id | national_outbreak_code |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S1 | Enteritidis | 11.0  | 2021-06-19  | ON  | Human  | Stool  | 20 | F | Salmonella | None |
| S2 | Enteritidis | 11.0  | 2006-01-03  | QC  | Animal  | Chicken  | 52 | M | Salmonella | None |
  
  
Full documentation: https://github.com/phac-nml/ArborView

## Example Usage

```bash
inline_arborview.py -d metadata.tsv -n tree.nwk -o output.html
```
