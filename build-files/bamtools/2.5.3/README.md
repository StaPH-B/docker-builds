# bamtools container

Main tool: [bamtools](https://github.com/pezmaster31/bamtools)
  
Code repository: https://github.com/pezmaster31/bamtools

Additional tools:
- none

Basic information on how to use this tool:
- executable: `bamtools`
- help: `--help`, `-h`
- version: `--version`, `-v`
- description: A command-line toolkit for reading, writing, and manipulating BAM files

Additional information: https://github.com/pezmaster31/bamtools/wiki/Tutorial_Toolkit_BamTools-1.0.pdf

  
Full documentation: https://github.com/pezmaster31/bamtools/wiki

## Example Usage

```bash
usage: bamtools COMMAND [ARGS]

Available bamtools commands:
        convert         Converts between BAM and a number of other formats
        count           Prints number of alignments in BAM file(s)
        coverage        Prints coverage statistics from the input BAM file
        filter          Filters BAM file(s) by user-specified criteria
        header          Prints BAM header information
        index           Generates index for BAM file
        merge           Merge multiple BAM files into single file
        random          Select random alignments from existing BAM file(s), intended more as a testing tool.
        resolve         Resolves paired-end reads (marking the IsProperPair flag as needed)
        revert          Removes duplicate marks and restores original base qualities
        sort            Sorts the BAM file according to some criteria
        split           Splits a BAM file on user-specified property, creating a new BAM output file for each value found
        stats           Prints some basic statistics from input BAM file(s)
```

