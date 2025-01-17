
# Pavian container

Main tool: [Pavian](https://github.com/fbreitwieser/pavian)
  
Code repository: https://github.com/fbreitwieser/pavian

Additional tools:
- R: 4.1.0

Basic information on how to use this tool:

Pavian is a interactive browser application for analyzing and visualization metagenomics classification results from classifiers such as Kraken, KrakenUniq, Kraken 2, Centrifuge and MetaPhlAn. It also provides an alignment viewer for validation of matches to a particular genome.  

![image](https://cloud.githubusercontent.com/assets/516060/20188595/5c8b9808-a747-11e6-9235-296a2314659a.png)

Full documentation: https://github.com/fbreitwieser/pavian

## Example Usage
You should publish a container's port(s) to the host while running pavian.
```bash
# run as root
docker run --rm -p 3838:3838 staphb/pavian:1.2.1
# non-root
docker run --rm --user shiny -p 3838:3838 staphb/pavian:1.2.1
```
Pavian will then be available at http://127.0.0.1:3838 in your web browser
