# Auspice 2.68.0 container

Main tool: [Auspice](https://github.com/nextstrain/auspice)
  
Code repository: https://github.com/nextstrain/auspice

> Auspice is an open-source interactive web app for visualizing phylogenomic data. It may be used in tandem with nextstrain's bioinformatics toolkit augur or on its own. Auspice may be used to explore datasets locally or run as a server to share results.

Basic information on how to use this tool:
- Executable: `auspice`
- Help: `auspice --help`
- Version: `auspice --version`

Additional information:
Full documentation: https://github.com/nextstrain/auspice/tree/master/docs

## Example Usage
**View datasets from a directory:**
```bash
auspice view --datasetDir /data
```

**View datasets and narratives:**
```bash
auspice view --datasetDir /data --narrativeDir /narratives
```

**Run with Docker:**
```bash
docker run -p 4000:4000 -v $(pwd)/data:/data auspice
```
