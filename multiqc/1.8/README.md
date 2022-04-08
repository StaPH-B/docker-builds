# MultiQC container

Main tool : [MultiQC](https://multiqc.info/)

Additional tools:
- pandoc

Full documentation: https://multiqc.info/

Aggregate results from bioinformatic analyses across many samples into a single report.

# Example Usage

```
multiqc -f --cl_config "prokka_fn_snames: True"  .
```
