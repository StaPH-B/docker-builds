# TBProfiler Container
Main tool: [TBProfiler](https://github.com/jodyphelan/TBProfiler)

The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database. We also predict the number of reads supporting drug resistance variants as an insight into hetero-resistance.

## Database
This tool relys on a database to run. The database that is included in the docker image is ```4738132```. This is from the Git repository https://github.com/jodyphelan/tbdb. This can be confirmed in the json file:``` ./TBProfiler-${TBPROFILER_VER}/db/tbdb.version.json ```:
```
{"name": "tbdb", "commit": "4738132", "Merge": "47daa08 0fd1e98", "Author": "Jody Phelan <jody.phelan@lshtm.ac.uk>", "Date": "Thu Jul 21 16:19:40 2022 +0100"}
```

# Example Usage
Run whole pipeline:
```
tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 4 -p ERR1664619 --txt
```
Make alternative database:
```
tb-profiler create_db --prefix <new_library_name>
tb-profiler load_library --prefix <new_library_name>
```


Better documentation can be found [here.](https://jodyphelan.gitbook.io/tb-profiler/)
