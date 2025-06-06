# SeqSender 1.3.3 container

Main tool: [SeqSender](https://github.com/CDCgov/seqsender)

Documentation: [https://cdcgov.github.io/seqsender](https://cdcgov.github.io/seqsender)

SeqSender is a public database submission pipeline by the CDC.

## Example Usage

```bash
# Create test submission files with supplied Influenza data
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py test_data -bsng --organism FLU --submission_dir test_dir

# Create test submission files with supplied SARS-CoV-2 data
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py test_data -bsng --organism COV --submission_dir test_dir
```

View full `seqsender` help options: `docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data seqsender:1.3.3 seqsender.py --help`
