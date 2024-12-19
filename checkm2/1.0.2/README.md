# CheckM2

Main tool: [checkm2](https://github.com/chklovski/CheckM2)
  
Code repository: https://github.com/chklovski/CheckM2

Basic information on how to use this tool:
- executable: |

```
General usage:
    predict -> Predict the completeness and contamination of genome bins in a folder. Example usage:
        checkm2 predict --threads 30 --input <folder_with_bins> --output-directory <output_folder>

    testrun -> Runs Checkm2 on internal test genomes to ensure it runs without errors. 
    
Example usage:

    checkm2 testrun --threads 10
    database -> Download and set up required CheckM2 DIAMOND database for annotation

Use checkm2 <command> -h for command-specific help.
```

- help: `checkm2 --help`
- version: `checkm2 --version`
- description: | 
> Rapid assessment of genome bin quality using machine learning.

Full documentation: https://github.com/chklovski/CheckM2

CheckM2 relies on a external diamond database (~1.7 GB) for rapid annotation. the database can be downloaded via `checkm2 database --download` command or obtained directly from: https://zenodo.org/api/records/5571251/files/checkm2_database.tar.gz/content

## Testing checkm2 analysis
```
# Download database and set db in PATH
checkm2 database --download

# Run internal tests
checkm2 testrun

# Download positive and negative control test data
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa -O burk_wgs_pos_ctrl.fa
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_16S.fa -O burk_16S_neg_ctrl.fa

# Running CheckM2 on the test data
checkm2 predict --input burk_wgs_pos_ctrl.fa \
    burk_16S_neg_ctrl.fa \
    --output-directory tests_output/
```
