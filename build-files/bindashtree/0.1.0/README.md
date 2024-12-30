# bindashtree container

Main tool: [bindashtree](https://github.com/jianshu93/bindashtree)
  
Code repository: https://github.com/jianshu93/bindashtree

Basic information on how to use this tool:
- executable: |

```
Binwise Densified MinHash and Rapid Neighbor-joining Tree Construction

Usage: bindashtree [OPTIONS] --input <INPUT_LIST_FILE> --output_tree <OUTPUT_TREE_FILE>

Options:
  -i, --input <INPUT_LIST_FILE>
          Genome list file (one FASTA/FNA file per line), gz supported
  -k, --kmer_size <KMER_SIZE>
          K-mer size [default: 16]
  -s, --sketch_size <SKETCH_SIZE>
          MinHash sketch size [default: 10240]
  -d, --densification <DENS_OPT>
          Densification strategy: 0=Optimal Densification, 1=Reverse Optimal Densification/faster Densification [default: 0]
  -t, --threads <THREADS>
          Number of threads to use in parallel [default: 1]
      --tree <TREE_METHOD>
          Tree construction method: naive, rapidnj, hybrid [default: rapidnj]
      --chunk_size <chunk_size>
          Chunk size for RapidNJ/Hybrid methods [default: 30]
      --naive_percentage <naive_percentage>
          Percentage of steps naive for hybrid method [default: 90]
      --output_matrix <OUTPUT_MATRIX_FILE>
          Output the phylip distance matrix to a file
      --output_tree <OUTPUT_TREE_FILE>
          Output the resulting tree in Newick format to a file
  -h, --help
          Print help
  -V, --version
          Print version
```

Additional information:
One Permutation Hashing with Optimal Densification can be use for genomic distance estimation (1-ANI) and then we can perform rapid neighbor-joining based on the genomic distance. We also provided a new densification strategy called faster densification (or reverse optimal densification), which is more accurate and faster for large sketch size.

  
Full documentation: https://github.com/jianshu93/bindashtree

## Testing for bindashtree

```
# Download test files
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/587/385/GCA_002587385.1_ASM258738v1/GCA_002587385.1_ASM258738v1_genomic.fna.gz && \
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/596/765/GCA_002596765.1_ASM259676v1/GCA_002596765.1_ASM259676v1_genomic.fna.gz && \
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/598/005/GCA_002598005.1_ASM259800v1/GCA_002598005.1_ASM259800v1_genomic.fna.gz

ls /data/test/*.fna.gz > name.txt

bindashtree -i name.txt -k 16 -s 10240 -d 1 -t 8 --output_tree try.nwk
```