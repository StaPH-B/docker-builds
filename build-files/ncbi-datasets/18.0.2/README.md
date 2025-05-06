# NCBI datasets and dataformat container

Main tool : [datasets](https://www.ncbi.nlm.nih.gov/datasets/docs/v1/download-and-install/#use-the-datasets-tool-to-download-biological-data) and [dataformat](https://www.ncbi.nlm.nih.gov/datasets/docs/v1/download-and-install/#use-the-dataformat-tool-to-convert-data-reports-to-other-formats)

Full documentation: [https://www.ncbi.nlm.nih.gov/datasets/docs/v1/how-tos/](https://www.ncbi.nlm.nih.gov/datasets/docs/v1/how-tos/)

> Use NCBI Datasets to gather metadata, download data packages, view reports and more

## Example Usage

```bash
# will download the fasta for ON924087.1 in a zipped directory
datasets download virus genome accession ON924087.1 --filename ON924087.1.zip

# unzipping the directory and the fasta file will be located at ncbi_dataset/data/genomic.fna
unzip ON924087.1.zip 

# copying the file into something with a better name
cp ncbi_dataset/data/genomic.fna ncbi_dataset/data/ON924087.1.genomic.fna
```
