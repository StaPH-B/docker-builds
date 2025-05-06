# colorid container

Main tool: [colorid](https://github.com/hcdenbakker/colorid/tree/master)
  
Code repository: https://github.com/hcdenbakker/colorid

Basic information on how to use this tool:
- executable: colorid
- help: --help
- version: --version
- description: |

Experiments with using BIGSI data structure for metagenomic and QC applications
  
Full documentation: https://github.com/hcdenbakker/colorid

## Example Usage

```bash
# create index
colorid build -r ref_file_example.txt -b test -k 31 -s 50000000 -n 4

# search
colorid search -b test.bxi -q SRR4098796_1.fastq.gz -r SRR4098796_2.fastq.gz
```
