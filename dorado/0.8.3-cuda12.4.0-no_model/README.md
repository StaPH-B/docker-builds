# Dorada container

Main tool: [dorado](https://github.com/nanoporetech/dorado)
  
Code repository: https://github.com/nanoporetech/dorado

Basic information on how to use this tool:
- executable: dorado
- help: -h, --help
- version: -v, --version
- description: Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.

Additional information:

This container does not contain any models.</br>
Cuda dirivers >= 12.4.0 are required for gpu support.</br>
Use **"--gpus all"** flag to activate gpu support in docker. E.g.
`docker run -it --gpus all staphb/dorado:0.8.3-cuda12.4.0-no_model bash`

Full documentation: https://dorado-docs.readthedocs.io/en/latest/

## Example Usage
```bash
# list models
dorado download --list
# downlaod a single model
dorado download --model {model_name}
# download all models
dorado download
# basecaller
dorado basecaller {model} {data} > calls.bam
```

