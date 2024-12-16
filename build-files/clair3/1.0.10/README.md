# Clair3 container

Main tool: [clair3](https://github.com/HKU-BAL/Clair3)
  
Code repository: https://github.com/HKU-BAL/Clair3

Basic information on how to use this tool:
- executable: run_clair3.sh
- help: -h, --help
- version: -v, --version
- description: <tool does something>

Additional information:

This container includes models in `/clair3/models`
  
Full documentation: https://github.com/HKU-BAL/Clair3

## Example Usage

```bash
run_clair3.sh \
  --bam_fn=${BAM} \
  --ref_fn=${REF} \
  --threads=${THREADS} \  		     
  --platform="ont" \               ## options: {ont,hifi,ilmn}
  --model_path=${MODEL_PREFIX} \   ## absolute model path prefix
  --output=${OUTPUT_DIR}           ## absolute output path prefix
## pileup output file: ${OUTPUT_DIR}/pileup.vcf.gz
## full-alignment output file: ${OUTPUT_DIR}/full_alignment.vcf.gz
## Clair3 final output file: ${OUTPUT_DIR}/merge_output.vcf.gz
```
