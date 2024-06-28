
# pango_aliasor container

Main tool: [pango_aliasor](https://github.com/corneliusroemer/pango_aliasor)
  
Code repository: https://github.com/corneliusroemer/pango_aliasor

Basic information on how to use this tool:
- executable: NA
- help: NA
- version: NA
- description: pango_aliasor is a python library for determining parent pangolin lineages

Additional information:
- Although not an official use by any means, `aliasor.py` is included in this image. This python script was written by [@erinyoung](https://github.com/erinyoung) for some quick use cases of finding parent lineages from pangolin results. Usage is below.
- A alias key is found at `/key/alias_key.json` in the containers spun from this image. When used, pango_aliasor does not download the latest key from github, which is useful for some cloud infrastructures.

Full documentation: [https://github.com/corneliusroemer/pango_aliasor](https://github.com/corneliusroemer/pango_aliasor)

## Example Usage

```python
import pandas as pd
from pango_aliasor.aliasor import Aliasor
import argparse


def add_unaliased_column(tsv_file_path, pango_column='pango_lineage', unaliased_column='pango_lineage_unaliased'):
    aliasor = Aliasor()
    def uncompress_lineage(lineage):
        if not lineage or pd.isna(lineage):
            return "?"
        return aliasor.uncompress(lineage)

    df = pd.read_csv(tsv_file_path, sep='\t')
    df[unaliased_column] = df[pango_column].apply(uncompress_lineage)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add unaliased Pango lineage column to a TSV file.')
    parser.add_argument('--input-tsv', required=True, help='Path to the input TSV file.')
    parser.add_argument('--pango-column', default='pango_lineage', help='Name of the Pango lineage column in the input file.')
    parser.add_argument('--unaliased-column', default='pango_lineage_unaliased', help='Name of the column to use for the unaliased Pango lineage column in output.')
    args = parser.parse_args()
    df = add_unaliased_column(args.input_tsv, args.pango_column, args.unaliased_column)
    print(df.to_csv(sep='\t', index=False))
```

## Example Usage of aliasor.py

The help message
```bash
usage: aliasor.py [-h] --input INPUT [--output OUTPUT] [--pango-column PANGO_COLUMN] [--unaliased-column UNALIASED_COLUMN] [--alias-key ALIAS_KEY]

Add unaliased Pango lineage column to a TSV file.

options:
  -h, --help            show this help message and exit
  --input INPUT         Path to the input file (should end in tsv or csv for best results).
  --output OUTPUT       Name of tab-delimited output file
  --pango-column PANGO_COLUMN
                        Name of the Pango lineage column in the input file.
  --unaliased-column UNALIASED_COLUMN
                        Name of the column to use for the unaliased Pango lineage column in output.
  --alias-key ALIAS_KEY
                        Alias Key as json file. If none provided, will download the latest version from github.
```

Examples for using aliasor.py with the lineage_report.csv file generated via pangolin (lineage_report.csv)
```bash
# downloading the latest alias key from github
aliasor.py --input lineage_report.csv --output unaliased_lineage_report.tsv

# using included alias key
aliasor.py --input lineage_report.csv --output unaliased_lineage_report.tsv --alias-key /key/alias_key.json
```
The unaliased column will be the last column in the output file.