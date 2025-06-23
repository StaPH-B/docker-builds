#!/usr/bin/env python3
"""
Report generating script for C-BIRD workflow
2025-01-09
@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
from datetime import date
import argparse
import pandas as pd
import numpy as np

# Define functions
def read_bracken_report(taxon_report):
    # get bracken report
    df = pd.read_csv(taxon_report, sep = '\t')
    df = df.sort_values(by=['fraction_total_reads'], ascending=False)

    # find top tax id & write
    with open("taxid.txt", "w") as f:
        taxid = df["taxonomy_id"][0]
        f.write(str(taxid))

    # Species
    df2 = df.loc[:, ["name", "fraction_total_reads" ]].copy()
    df2['fraction_total_reads'] = df2['fraction_total_reads'].apply(lambda x: round(x*100, 2))
    df2 = df2.rename(columns={"name": "Microorganism", "fraction_total_reads": "Abundance(%)"})
    return df2

def read_mlst_report(mlst_report):
    df = pd.read_csv(mlst_report, sep="\t", skiprows=1, header=None)
    df = df.drop(columns=0)
    columns = ['Scheme','Type (ST)','Alleles']
    if len(df.columns) < 3:
        df = pd.DataFrame(columns=columns)
    else:
        for i in range(3,len(df.columns)):
            columns.append('')
        df.columns = columns    
    return df

def read_amr_report(amr_report):

    df =  pd.read_csv(amr_report, sep = '\t')    
    df2 = df.loc[:, ['Element symbol','Element name','Scope','Subclass','% Coverage of reference','% Identity to reference', 'Type', 'Subtype','Method']].copy()
    df2 = df2.rename(columns={'Element symbol':'Gene','Element name':'Description',
                                    'Subclass':'Resistance / Mechanism','% Coverage of reference':'Coverage(%)',
                                    '% Identity to reference':'Identity(%)'})

    conditions = [
        (df2['Method'].str.contains('ALLELE')),
        (df2['Method'].str.contains('BLAST')),
        (df2['Method'].str.contains('EXACT')),
        (df2['Method'].str.contains('HMM')),
        (df2['Method'].str.contains('INTERNAL_STOP')),
        (df2['Method'].str.contains('PARTIALX')),
        (df2['Method'].str.contains('PARTIALP')),
        (df2['Method'].str.contains('POINT')),
        (df2['Method'].str.contains('PARTIAL_CONTIG_END')),
        ]
    values = ['Very High', 'High', 'Very High', 'Low (HMM)', 'Low (Int. Stop)', 'Low (Partial)', 'Low (Partial)', 'Very High', 'Moderate (Contig End)']
    df2['Confidence'] = np.select(conditions, values, default='Uncertain')
    df2 = df2.drop(columns=['Method'])

    amr_df = df2.loc[df2['Subtype'] == "AMR"].copy()
    amr_df.loc[amr_df['Scope']=='plus', 'Confidence'] = 'Uncertain'
    amr_df = amr_df.drop(columns={'Type', 'Subtype', 'Scope'})
    amr_df = amr_df.sort_values(by=['Resistance / Mechanism'], ascending=True)

    point_df = df2.loc[df2['Subtype'] == "POINT"].copy()
    point_df = point_df.drop(columns={'Type', 'Subtype','Scope'})
    point_df = point_df.sort_values(by=['Resistance / Mechanism'], ascending=True)

    stress_df = df2.loc[df2['Type'] == "STRESS"].copy()
    stress_df.loc[stress_df['Scope']=='plus', 'Confidence'] = 'Uncertain'
    stress_df = stress_df.drop(columns={'Type', 'Subtype','Scope'})
    stress_df = stress_df.sort_values(by=['Resistance / Mechanism'], ascending=True)
    stress_df = stress_df.fillna("")

    vir_df = df2.loc[df2['Type'] == "VIRULENCE"].copy()
    vir_df.loc[vir_df['Scope']=='plus', 'Confidence'] = 'Uncertain'
    vir_df = vir_df.drop(columns={'Type', 'Subtype','Scope', 'Resistance / Mechanism'})

    df_list = [amr_df, point_df, stress_df, vir_df]
    return df_list

def read_plasmidfinder_report(plasmid_report):
    df = pd.read_csv(plasmid_report, sep = '\t')
    df2 = df.loc[:, ['Plasmid','Identity','Query / Template length','Accession number']].copy()
    df2 = df2.sort_values(by=['Identity','Plasmid'], ascending=False)
    df2 = df2.rename(columns={'Identity':'Identity(%)'})
    return df2 

def read_mash_report(mash_report):
    df = pd.read_csv(mash_report, sep = '\t', header=None)
    df.columns = ['Microorganism', 'Identity(%)']
    return df

def read_blast_report(blast_report):
    df = pd.read_csv(blast_report, sep = '\t')
    if not df.empty:
        df['Coverage(%)'] = df['length'] / df['qlen'] * 100
        df.drop(columns=['sseqid', 'mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore'], inplace=True)
        df.rename(columns={'qseqid':'Gene','pident':'Identity(%)','length':'Length'}, inplace=True)
        df=df[['Gene','Length','Coverage(%)','Identity(%)']].round(2)
    else:
        df=pd.DataFrame(columns=['Gene','Length','Coverage(%)','Identity(%)'])
    return df

def basic_report(samplename, mash, amr, point, version, footer):
    m = mash.copy()
    m['Microorganism'] = m['Microorganism'].apply(lambda x: x.split()[0]+" "+x.split()[1])

    # report
    page_title = samplename
    title = "Whole Genome Sequencing Analysis Report"
    stitle1 = "Sample Information"
    stitle2 = "Predicted Organism"
    stitle3 = "Resistance Genes"
    stitle4 = "Point Mutations"
    today = date.today()
    # HTML #
    html = f'''
    <!DOCTYPE html>
    <html lang="en-us">
        <head>
            <meta charset="UTF-8">
            <title>{page_title}</title>
            <style>
            h1 {{
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.5em;
            text-align: center;
            color: #1e5c85
            }}

            h2 {{
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1em;
            margin-top: 1em;
            margin-bottom: 0.4em;
            text-align: left;
            color: #D6672E 
            }}

            table {{
            border-collapse: collapse;
            border: none;
            }}
            
            th, td {{
            text-align: left;
            padding-left: 5px;
            padding-right: 5px;
            padding-top: 1px;
            padding-bottom: 1px;
            border: none;
            }}
            
            table.dataframe tr:nth-child(even) {{background-color: #f2f2f2;}}
            
            table.dataframe th {{
            background-color: #1e5c85;
            color: white;
            
            }}
            footer {{
                    font-size: 0.8em
                }}      
            </style>
        </head>
        <body>
        <header>
        <h1>{title}</h1>
        </header>
        <hr>
        <article>
        <h2>{stitle1}</h2>
        <table>
        <tr>
        <td>Report date:</td>
        <td>{today}</td>
        </tr>
        <tr>
        <td>Laboratory ID:</td>
        <td>{samplename}</td>
        </tr>
        </table>
        <h2>{stitle2}</h2>
        {m.to_html(index=False, justify="left")}
        <h2>{stitle3}</h2>
        {amr.to_html(index=False, justify="left")}
        <h2>{stitle4}</h2>
        {point.to_html(index=False, justify="left")}
        <p></p>
        </article>
        <hr>
        <footer>
        <p><i>This report is created by <a href="https://github.com/Kincekara/C-BIRD">{version}</a> bioinformatics pipeline.</br>
        {footer}</i></p>
        </footer>
    </body>
    </html>
    '''
    # write html file
    with open(samplename + "_basic_report.html", "w") as f:
        f.write(html)
    print(samplename + "_basic_report.html was created!")

def extended_report(samplename, bracken, mlst, amr, point, stress, virulence, plasmid, blast, mash, version):
    page_title = samplename
    title = "Whole Genome Sequencing Analysis Report"
    stitle1 = "Sample Information"
    stitle2 = "Taxonomic Profile of Reads"
    stitle3 = "Predicted Organism"
    stitle4 = "MLST Typing"
    stitle5 = "Resistance Genes"
    stitle6 = "Point Mutations"
    stitle7 = "Stress Genes"
    stitle8 = "Hypervirulance Genes"
    stitle9 = "Target Gene Search"
    stitle10 = "Plasmids Detected"    
    today = date.today()
    footer = "Research use only."
    
    # HTML #
    html = f'''
    <!DOCTYPE html>
    <html lang="en-us">
        <head>
            <meta charset="UTF-8">
            <title>{page_title}</title>
            <style>
            h1 {{
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1.5em;
            text-align: center;
            color: #1e5c85
            }}

            h2 {{
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1em;
            margin-top: 1em;
            margin-bottom: 0.4em;
            text-align: left;
            color: #D6672E 
            }}

            table {{
            border-collapse: collapse;
            border: none;
            }}
            
            th, td {{
            text-align: left;
            padding-left: 5px;
            padding-right: 5px;
            padding-top: 1px;
            padding-bottom: 1px;
            border: none;
            }}
            
            table.dataframe tr:nth-child(even) {{background-color: #f2f2f2;}}
            
            table.dataframe th {{
            background-color: #1e5c85;
            color: white;
            
            }}
            footer {{
                    font-size: 0.8em
                }}      
            </style>
        </head>
        <body>
        <header>
        <h1>{title}</h1>
        </header>
        <hr>
        <article>
        <h2>{stitle1}</h2>
        <table>
        <tr>
        <td>Report date:</td>
        <td>{today}</td>
        </tr>
        <tr>
        <td>Laboratory ID:</td>
        <td>{samplename}</td>
        </tr>
        </table>
        <h2>{stitle2}</h2>
        {bracken.to_html(index=False, justify="left")}
        <h2>{stitle3}</h2>
        {mash.to_html(index=False, justify="left")}
        <h2>{stitle4}</h2>
        {mlst.to_html(index=False, justify="left")}
        <p></p>
        <hr>
        <h2>{stitle5}</h2>
        {amr.to_html(index=False, justify="left")}
        <h2>{stitle6}</h2>
        {point.to_html(index=False, justify="left")}
        <p></p>
        <hr>
        <h2>{stitle7}</h2>
        {stress.to_html(index=False, justify="left")}
        <h2>{stitle8}</h2>
        {virulence.to_html(index=False, justify="left")}
        <h2>{stitle9}</h2>
        {blast.to_html(index=False, justify="left")}
        <h2>{stitle10}</h2>
        {plasmid.to_html(index=False, justify="left")}
        <p></p>
        </article>
        <hr>
        <footer>
        <p><i>This report is created by <a href="https://github.com/Kincekara/C-BIRD">{version}</a> bioinformatics pipeline.</br>
        {footer}</i></p>
        </footer>
    </body>
    </html>
    '''
    # write html file
    with open(samplename + "_extended_report.html", "w") as f:
        f.write(html)     
    print(samplename + "_extended_report.html was created!")

# Main #
def main(args):
    samplename = args.samplename
    taxon_report = args.taxon_report
    mlst_report = args.mlst_report
    amr_report = args.amr_report
    plasmid_report = args.plasmid_report
    mash_report = args.mash_report
    version = args.cbird_version
    footer = args.footer_note
    blast_report = args.blast_report

    # read reports
    bracken = read_bracken_report(taxon_report)
    mlst = read_mlst_report(mlst_report)
    amr = read_amr_report(amr_report)[0]
    point = read_amr_report(amr_report)[1]
    stress = read_amr_report(amr_report)[2]
    virulence = read_amr_report(amr_report)[3]    
    plasmid = read_plasmidfinder_report(plasmid_report)
    if blast_report is not None:
        blast = read_blast_report(blast_report)
    else:
        # create empty dataframe
        blast = pd.DataFrame(columns=['Gene','Length','Identity(%)', 'Coverage(%)'])
    
    if mash_report is not None:
        mash = read_mash_report(mash_report)
        # write clia report
        basic_report(samplename, mash, amr, point, version, footer)
    else:
        print("No mash result. Basic report won't be created!")
        # create empty dataframe
        mash = pd.DataFrame(columns=['Microorganism', 'Identity(%)'])
        
    # write summary report    
    extended_report(samplename, bracken, mlst, amr, point, stress, virulence, plasmid, blast, mash, version)       
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summary report generating script for C-BIRD workflow')

    parser.add_argument('-s', '--samplename', type=str, help='Sample name', required=True)
    parser.add_argument('-t', '--taxon_report', type=str, help='Bracken report file', required=True)
    parser.add_argument('-st', '--mlst_report', type=str, help='MLST report file', required=True)
    parser.add_argument('-a', '--amr_report',  type=str, help='AMRFinderPlus report file', required=True)
    parser.add_argument('-p', '--plasmid_report', type=str, help='PlasmidFinder report file', required=True)    
    parser.add_argument('-c', '--cbird_version',  type=str, help='C-BIRD version', required=True)    
    parser.add_argument('-m', '--mash_report',  type=str, help='MASH report file')
    parser.add_argument('-b', '--blast_report', type=str, help='Blast report file')
    parser.add_argument('-f', '--footer_note',  type=str, help='Disclaimer text', default="")
    args = parser.parse_args()

    main(args)