#!/usr/bin/env python3

"""
Report generating script for C-BIRD workflow
Created on Thu Aug  4 13:43:46 2022
@author: Kutluhan Incekara
email: kutluhan.incekara@ct.gov
"""
import argparse
import pandas as pd
from datetime import date

def main(args):
    samplename = args.samplename
    fastp_report = args.fastp_report
    bracken_report = args.bracken_report
    quast_report = args.quast_report
    checkm2_report = args.checkm2_report
    version = args.version
    phiX_ratio = args.phiX_ratio
    sequencing_depth = args.sequencing_depth
    genome_ratio = args.genome_ratio

    # get sequencing depth & genome ratio
    with open(sequencing_depth) as f:
        seq_depth = f.read()

    with open(genome_ratio) as f:
        gen_ratio = f.read()

    # get fastp report
    with open(fastp_report) as f:
        df_list=pd.read_html(f)
        f0 = df_list[0].drop(index=0)
        f0.columns = ["General", ""]
        f1 = df_list[1]
        f1.columns = (["", "Before"])
        f2 = df_list[2]
        f2.columns = (["", "After"])
        f1_f2 = pd.merge(f1, f2, on="")
        f3 = df_list[3]
        f3.columns = ["Quality Filtering", ""]
        f4 = df_list[5]
        f4.columns = ["Adapter or bad ligation of read1", ""]
        f5 = df_list[6]
        f5.columns = ["Adapter or bad ligation of read2", ""]

    # get bracken report
    br_df = pd.read_csv(bracken_report, sep = '\t')
    br_df = br_df.sort_values(by=['fraction_total_reads'], ascending=False)

    # get quast report
    q_df = pd.read_csv(quast_report, sep = '\t')

    # get checkm2 report
    with open(checkm2_report) as f:
        ckm_df = pd.read_csv(checkm2_report, sep = '\t')
        completeness = ckm_df.iat[0, 1]
        contamination = ckm_df.iat[0, 2]

    ## Report template ##
    page_title = samplename
    title = "QC Summary"
    stitle1 = "Sample Information"
    stitle2 = "Sequencing Statistics"
    stitle3 = "Quality Trimming & Filtering"
    stitle4 = "Taxonomy Report"
    stitle5 = "Assembly Statistics"
    stitle6 = "Assembly Assesment"
    today = date.today()

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
            
            table.custom tr:nth-child(odd) {{background-color: #f2f2f2;}}
            
            table.custom th {{
            background-color: #1e5c85;
            color: white;
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
        <table class="custom">
        <tr>
            <td>Report date:</td>
            <td>{today}</td>
        </tr>
        <tr>
            <td>Laboratory ID:</td>
            <td>{samplename}</td>
        </tr>
        <tr>
            <td>Pipeline:</td>
            <td>{version}</td>
        </tr>
        </table>
        <h2>{stitle2}</h2>

        <table class="custom">
        <tr>
        <td>Sequencing depth:</td>
        <td>{seq_depth}</td>
        </tr>
        <tr>
        <td>PhiX ratio:</td>
        <td>{phiX_ratio}</td>
        </tr>
        <tr>
        <td>Assembly completeness:</td>
        <td>{completeness}</td>
        </tr>
        <tr>
        <td>Assembly contamination:</td>
        <td>{contamination}</td>
        </tr>
        <tr>
        <td>Estimated genome ratio:</td>
        <td>{gen_ratio}</td>
        </tr>
        </table>
        <h2>{stitle3}</h2>
        {f0.to_html(index=False, justify="left")}
        <p></p>
        {f1_f2.to_html(index=False, justify="left")}
        <p></p>
        {f3.to_html(index=False, justify="left")}
        <p></p>
        {f4.to_html(index=False, justify="left")}
        <p></p>
        {f5.to_html(index=False, justify="left")}
        <p></p>
        <h2>{stitle4}</h2>
        {br_df.to_html(index=False, justify="left")}
        <h2>{stitle5}</h2>
        {q_df.to_html(index=False, justify="left")}
        <p></p>
        </article>
        <hr>
        <footer>
        <p><i>This QC summary is created by <a href="https://github.com/Kincekara/C-BIRD">{version}</a> bioinformatics pipeline.</i></p>
        </footer>
    </body>
    </html>
    '''

    with open(samplename+"_QC_summary.html", "w") as f:
        f.write(html)
        print(samplename + "_QC_summary.html was created!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='QC report generating script for C-BIRD workflow')

    parser.add_argument('samplename', type=str, help='Sample name' )
    parser.add_argument('fastp_report', type=str, help='FastP report file')
    parser.add_argument('bracken_report', type=str, help='Bracken report file')
    parser.add_argument('quast_report', type=str, help='Quast report file')
    parser.add_argument('checkm2_report', type=str, help='CheckM2 report file')
    parser.add_argument('version', type=str, help='C-BIRD version')
    parser.add_argument('phiX_ratio', type=str, help='PhiX_ratio')
    parser.add_argument('sequencing_depth', type=str, help='COVERAGE file generated by est_coverage script')
    parser.add_argument('genome_ratio', type=str, help='GENOME_RATIO file generated by est_coverage script')
    
    args = parser.parse_args()

    main(args)