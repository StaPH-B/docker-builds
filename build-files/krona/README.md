
# Krona container

Main tool: [Krona](https://github.com/marbl/Krona)
  
Code repository: <https://github.com/marbl/Krona/tree/master/KronaTools>

Additional tools:

- krona 2.8.1
- krakentools d4a2fbe
- pandas 2.2.3
- bioptyhon 1.84
- miniconda (latest)

Basic information on how to use this tool:
- executable: various perl scripts
- help: provide the tool name without any arguments to see the help message (`<toolname>`)
- version: Versioning information is available within the help message and can be retrieved with the following grep command `<toolname> | grep "KronaTools" | cut -d' ' -f3`
- description: "Krona allows hierarchical data to be explored with zooming, multi-layered pie charts... The interactive charts are self-contained and can be viewed with any modern web browser."

Additional information: This container also contains [KrakenTools](https://github.com/jenniferlu717/KrakenTools), which provides a way for Krona plots to be generated for viral data.
  
Full documentation: [https://github.com/marbl/Krona](https://github.com/marbl/Krona/wiki)

## Example Usage

```bash
# run Krona without preprocessing of the kraken output by Krakentools -- viral data will be considered "other root" but bacterial data will be visualized
ktImportTaxonomy MYSAMPLE.kraken_output_report -o MYSAMPLE.krona.hmtl -tax taxonomy

# run Krona with preprocessing of the kraken output by Krakentools in order to visualize viral data properly
python3 /KrakenTools/kreport2krona.py -r MYSAMPLE.kraken_output_report -o MYSAMPLE.krona 
ktImportText MYSAMPLE.krona -o MYSAMPLE.krona.html
```
