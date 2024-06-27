#!/usr/bin/env python3

#####
# Mostly stolen from https://github.com/corneliusroemer/pango_aliasor?tab=readme-ov-file#convenience-script
# and https://github.com/UPHL-BioNGS/Wastewater-genomic-analysis/blob/pooja-dev/utils/freyja_custom_lin_processing.py
#####

import pandas as pd
from pango_aliasor.aliasor import Aliasor
import argparse

def add_unaliased_column(tsv_file_path, pango_column='lineage', unaliased_column='unaliased_lineage', alias_key = ''):
    if alias_key:
        aliasor = Aliasor(alias_key)
    else:
        aliasor = Aliasor()

    def uncompress_lineage(lineage):
        if not lineage or pd.isna(lineage):
            return "?"
        return aliasor.uncompress(lineage)

    df = pd.DataFrame()

    if tsv_file_path.endswith('.tsv'):
        df = pd.read_csv(tsv_file_path, sep='\t')
    elif tsv_file_path.endswith('.csv'):
        df = pd.read_csv(tsv_file_path, sep=',')
    else:
        df = pd.read_csv(tsv_file_path, sep='\t')

    df[unaliased_column] = df[pango_column].apply(uncompress_lineage)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add unaliased Pango lineage column to a TSV file.')
    parser.add_argument('--input', required=True, help='Path to the input file (should end in tsv or csv for best results).')
    parser.add_argument('--output', default='unaliased_lineage_report.tsv', help='Name of tab-delimited output file' )
    parser.add_argument('--pango-column', default='lineage', help='Name of the Pango lineage column in the input file.')
    parser.add_argument('--unaliased-column', default='unaliased_lineage', help='Name of the column to use for the unaliased Pango lineage column in output.')
    parser.add_argument('--alias-key', default='', help="Alias Key as json file. If none provided, will download the latest version from github.")
    args = parser.parse_args()
    
    df = add_unaliased_column(args.input, args.pango_column, args.unaliased_column, args.alias_key)
    df.to_csv(args.output, sep='\t', index=False)