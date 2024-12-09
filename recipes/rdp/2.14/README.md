# RDP Classifier 

Main tool: [RDP Classifier](https://sourceforge.net/projects/rdp-classifier/)
  
Code repository: https://github.com/rdpstaff/classifier

Basic information on how to use this tool:
- executable: |
```
	classify      - classify one or multiple samples
	crossvalidate - cross validate accuracy testing
	libcompare    - compare two samples
	loot          - leave one (sequence or taxon) out accuracy testing
	merge-detail  - merge classification detail result files to create a taxon assignment counts file
	merge-count   - merge multiple taxon assignment count files to into one count file
	random-sample - random select a subset or subregion of sequences
	rm-dupseq     - remove identical or any sequence contained by another sequence
	rm-partialseq - remove partial sequences
	taxa-sim      - calculate and plot the similarities within taxa
	train         - retrain classifier
```

- help: classify # with no flags
- version: NA
- description: | 
> The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data.

  
Full documentation: https://sourceforge.net/projects/rdp-classifier/


## Example analysis
Get test data:
```
# Download test data
wget -nv https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/rdp/2.14/16S_rRNA_gene.Burkholderia_pseudomallei.2002721184.AY305776.1.fasta -O 16S_test.fa
wget -nv https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/rdp/2.14/18S_rRNA_gene.Homo_sapiens.T2T-CHM13v2.0.Chromosome13.fasta -O 18S_test.fa
```

Use RDP Classifier to get taxonomic assignments for bacterial and archaeal 16S rRNA sequences:
```
classifier classify -o taxa_16S_test.txt 16S_test.fa
classifier classify -o taxa_18S_test.txt 18S_test.fa
```

## Output
```
head -2 taxa_16S_test.txt

AY305776.1		Root	rootrank	1.0	Bacteria	domain	1.0	Pseudomonadota	phylum	1.0	Betaproteobacteria	class	1.0	Burkholderiales	order	1.0	Burkholderiaceae	family	1.0	Burkholderia	genus	1.0
```


