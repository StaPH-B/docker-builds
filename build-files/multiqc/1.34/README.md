# MultiQC container

Main tool : [MultiQC](https://multiqc.info/)

Aggregate results from bioinformatics analyses across many samples into a single report.

Full documentation: [Docs] (https://multiqc.info/docs/)

Notes: Starting with version 1.27, multiqc can use ai to assist with summaries. More information on how to set this up and use it can be found at https://docs.seqera.io/multiqc/ai.

# Example Usage

```
multiqc -f --cl_config "prokka_fn_snames: True"  .
```
