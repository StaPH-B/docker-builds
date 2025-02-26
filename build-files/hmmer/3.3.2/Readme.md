# Hmmmer container

Main tool : [HMMER3](http://hmmer.org/) 

HMMER: biosequence analysis using profile hidden Markov models
(http://eddylab.org/software/hmmer)

# Example commands 

```bash
# Test hmmscan with help options
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/hmmer:3.3.2 hmmscan -h
``` 


```bash 
# Test hmmsearch with help options
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/hmmer:3.3.2 hmmsearch -h
```


