# MultiQC container

Main tool : [MultiQC](https://multiqc.info/) 1.17

Additional tools:
- python 3.8.2

Aggregate results from bioinformatics analyses across many samples into a single report.

Full documentation: [Docs] (https://multiqc.info/docs/)

# Example Usage

```
multiqc -f --cl_config "prokka_fn_snames: True"  .
```