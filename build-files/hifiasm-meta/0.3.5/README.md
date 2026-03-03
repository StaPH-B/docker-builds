# hifiasm-meta container

Main tool: [hifiasm-meta](https://github.com/xfengnefx/hifiasm-meta/)
  
Code repository: https://github.com/xfengnefx/hifiasm-meta

Additional tools:
- none

Basic information on how to use this tool:
- executable: `hifiasm_meta`
- help: `-h`
- version: `--version`
- description: A hifiasm fork for metagenome assembly using Hifi reads.

Additional information:

Feng, X., Cheng, H., Portik, D., & Li, H. (2022). Metagenome assembly of high-fidelity long reads with hifiasm-meta. Nature Methods, 19(6), 671–674. https://doi.org/10.1038/s41592-022-01478-3

‌  
Full documentation: https://github.com/xfengnefx/hifiasm-meta

## Example Usage

```bash
hifiasm_meta -t32 -o asm reads.fq.gz 2>asm.log

# if the dataset has high redundancy
hifiasm_meta -t32 --force-rs -o asm reads.fq.gz 2>asm.log  
```
