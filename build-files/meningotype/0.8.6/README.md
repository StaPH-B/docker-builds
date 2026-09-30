# meningotype container

Main tool: [meningotype](https://github.com/MDU-PHL/meningotype)
  
Code repository: https://github.com/MDU-PHL/meningotype

Additional tools:
- blast: 2.12.0+
- isPCR: 33
- mlst: 2.23.0
- any2fasta: 0.4.2

Basic information on how to use this tool:
- executable: meningotype
- help: --help
- version: --version
- description: In silico typing for Neisseria meningitidis

Additional information: Documentation sometimes shows `meningotype.py` usage, but this is not in PATH. Please use `meningotype`.
  
Full documentation: https://github.com/MDU-PHL/meningotype

## Example Usage

```bash
meningotype --finetype *fasta > results.txt
```
