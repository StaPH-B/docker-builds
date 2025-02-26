# ShigaPass container

Main tool: [ShigaPass](https://github.com/imanyass/ShigaPass)
  
Code repository: https://github.com/imanyass/ShigaPass

Additional tools:

- ncbi-blast+ 2.12.0

Basic information on how to use this tool:

````
###### This tool is used to predict Shigella serotypes  #####
        Usage : ShigaPass.sh [options]
   
        options :
        -l	List of input file(s) (FASTA) with their path(s) (mandatory)
        -o	Output directory (mandatory)
        -p	Path to databases directory (mandatory)
        -t	Number of threads (optional, default: 2)
        -u	Call the makeblastdb utility for databases initialisation (optional, but required when running the script for the first time)
        -k	Do not remove subdirectories (optional)
       	-v	Display the version and exit
        -h	Display this help and exit
        Example: ShigaPass.sh -l list_of_fasta.txt -o ShigaPass_Results -p ShigaPass/ShigaPass_DataBases -t 4 -u -k
        Please note that the -u option should be used when running the script for the first time and after databases updates
````

> ShigaPass is a new in silico tool used to predict Shigella serotypes and to differentiate between Shigella, EIEC (Enteroinvasive E. coli), and non Shigella/EIEC using assembled whole genomes.

Additional information:

Full documentation: https://github.com/imanyass/ShigaPass

Included Database: Found at `/ShigaPass-${version}/SCRIPT/ShigaPass_DataBases/` so for v1.5.0 use `-p /ShigaPass-1.5.0/SCRIPT/ShigaPass_DataBases/`. This database has already been indexed so there is no need to pass `-u` with your command. If you do a permissions error will occur. 

## Example Usage

```bash
ShigaPass.sh -l ShigaPass_test.txt -o ShigaPass_Results -p /ShigaPass-1.5.0/SCRIPT/ShigaPass_DataBases/
```
