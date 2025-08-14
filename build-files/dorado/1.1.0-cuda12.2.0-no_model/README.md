# Dorado container

Main tool: [dorado](https://github.com/nanoporetech/dorado)

Code repository: https://github.com/nanoporetech/dorado

Basic information on how to use this tool:
- executable: dorado
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.

Additional information:

- This container does not contain any models. The models can be downloaded manually by `dorado download` command. If no specific model is provided, Dorado will automatically select and download the appropriate one using the model selection complex.
- Cuda drivers >= 12.2.0 are required for gpu support.
- Use **"--gpus all"** flag to activate gpu support in docker. E.g.
`docker run -it --gpus all staphb/dorado:1.1.0-cuda12.2.0-no_model bash`
- Support for Fast5 files and basecalling models for DNA R10.4.1 4kHz data, DNA R9.4.1, and RNA002 were removed after v0.9.6

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
