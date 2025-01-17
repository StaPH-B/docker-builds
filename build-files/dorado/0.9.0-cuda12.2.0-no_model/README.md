# Dorado container

Main tool: [dorado](https://github.com/nanoporetech/dorado)

Code repository: https://github.com/nanoporetech/dorado

Basic information on how to use this tool:
- executable: dorado
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.

Additional information:

- This container does not contain any models. They must be downloaded at runtime.
- Cuda drivers >= 12.2.0 are required for gpu support.
- Use **"--gpus all"** flag to activate gpu support in docker. E.g.
`docker run -it --gpus all staphb/dorado:0.9.0-cuda12.2.0-no_model bash`

Full documentation: https://dorado-docs.readthedocs.io/en/latest/

## Example Usage
```bash
# list models
dorado download --list
# download a single model
dorado download --model {model_name}
# download all models
dorado download
# basecaller
dorado basecaller {model} {data} > calls.bam
```
