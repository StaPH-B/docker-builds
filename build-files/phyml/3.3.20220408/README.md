# Phyml Container

## Documentation and Overview

Main Tool: [Phyml 3.0 paper](http://www.atgc-montpellier.fr/download/papers/phyml_2010.pdf)

Full documentation: http://www.atgc-montpellier.fr/phyml/versions.php

"PhyML is a software package that uses modern statistical approaches to analyse alignments of nucleotide or amino acid sequences in a phylogenetic framework. The main tool in this package builds phylogenies under the maximum likelihood criterion. It implements a large number of substitution models coupled to efficient options to search the space of phylogenetic tree topologies."

```
NAME
        - PhyML 3.3.20220408 -

        ''A simple, fast, and accurate algorithm to estimate
        large phylogenies by maximum likelihood''

        Stephane Guindon and Olivier Gascuel,
        Systematic Biology 52(5):696-704, 2003.

        Please cite this paper if you use this software in your publications.

SYNOPSIS:

        phyml [command args]

        All the options below are optional (except '-i' if you want to use the command-line interface).


Command options:

        -i (or --input) seq_file_name
                seq_file_name is the name of the nucleotide or amino-acid sequence file in PHYLIP format.


        -d (or --datatype) data_type
                data_type is 'nt' for nucleotide (default), 'aa' for amino-acid sequences, or 'generic',
                (use NEXUS file format and the 'symbols' parameter here).


        -q (or --sequential)
                Changes interleaved format (default) to sequential format.


        -n (or --multiple) nb_data_sets
                nb_data_sets is an integer corresponding to the number of data sets to analyse.


        -p (or --pars)
                Use a minimum parsimony starting tree. This option is taken into account when the '-u' option
                is absent and when tree topology modifications are to be done.


        -b (or --bootstrap) int
                int >  0: int is the number of bootstrap replicates.
                int =  0: neither approximate likelihood ratio test nor bootstrap values are computed.
                int = -1: approximate likelihood ratio test returning aLRT statistics.
                int = -2: approximate likelihood ratio test returning Chi2-based parametric branch supports.
                int = -4: SH-like branch supports alone.
                int = -5: (default) approximate Bayes branch supports.


        --tbe
                Computes TBE instead of FBP (standard) bootstrap support
                Has no effect with -b <= 0

        -m (or --model) model
                model : substitution model name.
                - Nucleotide-based models : HKY85 (default) | JC69 | K80 | F81 | F84
                 TN93 | GTR | custom (*)
                (*) : for the custom option, a string of six digits identifies the model. For instance, 000000
                 corresponds to F81 (or JC69 provided the distribution of nucleotide frequencies is uniform).
                 012345 corresponds to GTR. This option can be used for encoding any model that is a nested within GTR.

                - Amino-acid based models : LG (default) | WAG | JTT | MtREV | Dayhoff | DCMut
                 RtREV | CpREV | VT | AB | Blosum62 | MtMam | MtArt
                 HIVw |  HIVb | custom


        --aa_rate_file filename
                filename is the name of the file that provides the amino acid substitution rate matrix in PAML format.
                It is compulsory to use this option when analysing amino acid sequences with the `custom' model.


        -f e, m, o or fA,fC,fG,fT
                e : the character frequencies are determined by counting the number of amino-acids
                 or nucleotides from the sequence alignment.

                m : the character frequencies are determined as follows :
                - Nucleotide sequences: the equilibrium base frequencies are optimized using maximum likelihood.
                - Amino-acid sequences: the equilibrium amino-acid frequencies are estimated using
                 the frequencies defined by the substitution model.

                o : the character frequencies (amino-acids or nucleotides) are optimized using maximum likelihood

                fA,fC,fG,fT : only valid for nucleotide-based models. fA, fC, fG and fT are floating numbers that
                 correspond to the frequencies of A, C, G and T respectively (WARNING: do not use any blank space between
                 your values of nucleotide frequencies, only commas!)


        -t (or --ts/tv) ts/tv_ratio
                ts/tv_ratio : transition/transversion ratio. DNA sequences only.
                Can be a fixed positive value (ex:4.0) or e to get the maximum likelihood estimate.


        -v (or --pinv) prop_invar
                prop_invar : proportion of invariable sites.
                Can be a fixed value in the [0,1] range or e to get the maximum likelihood estimate.


        -c (or --nclasses) nb_subst_cat
                nb_subst_cat : number of relative substitution rate categories. Default : nb_subst_cat=4.
                Must be a positive integer.


        --freerates (or --free_rates or --freerate or --free_rate)
                 FreeRate model of substitution rate variation across sites.


        -a (or --alpha) gamma
                gamma : distribution of the gamma distribution shape parameter.
                Can be a fixed positive value or e to get the maximum likelihood estimate.


        -s (or --search) move
                 Deprecated option.
                Tree topology search operation option.
                Can be either NNI (default, fast) or SPR (a bit slower than NNI) or BEST (best of NNI and SPR search).


        -u (or --inputtree) user_tree_file
                user_tree_file : starting tree filename. The tree must be in Newick format.


        -o params
                This option focuses on specific parameter optimisation.
                params=tlr : tree topology (t), branch length (l) and rate parameters (r) are optimised.
                params=tl  : tree topology and branch length are optimised.
                params=lr  : branch length and rate parameters are optimised.
                params=l   : branch length are optimised.
                params=r   : rate parameters are optimised.
                params=n   : no parameter is optimised.


        --rand_start
                This option sets the initial tree to random.
                It is only valid if SPR searches are to be performed.


        --n_rand_starts num
                num is the number of initial random trees to be used.
                It is only valid if SPR searches are to be performed.


        --r_seed num
                num is the seed used to initiate the random number generator.
                Must be an integer.


        --print_site_lnl
                Print the likelihood for each site in file *_phyml_lk.txt.


        --print_trace
                Print each phylogeny explored during the tree search process
                in file *_phyml_trace.txt.


        --run_id ID_string
                Append the string ID_string at the end of each PhyML output file.
                This option may be useful when running simulations involving PhyML.


        --quiet
                No interactive question (for running in batch mode) and quiet output.


        --no_memory_check
                No interactive question for memory usage (for running in batch mode). Normal output otherwise.


        --leave_duplicates
                PhyML removes duplicate sequences by default. Use this option to leave them in.


        --alias_subpatt
                Site aliasing is generalized at the subtree level. Sometimes lead to faster calculations.
                See Kosakovsky Pond SL, Muse SV, Sytematic Biology (2004) for an example.


        --boot_progress_display num (default=20)
                num is the frequency at which the bootstrap progress bar will be updated.
                Must be an integer.

PHYLIP-LIKE INTERFACE

        You can also use PhyML with no argument, in this case change the value of
        a parameter by typing its corresponding character as shown on screen.

EXAMPLES

        DNA interleaved sequence file, default parameters :   ./phyml -i seqs1
        AA interleaved sequence file, default parameters :    ./phyml -i seqs2 -d aa
        AA sequential sequence file, with customization :     ./phyml -i seqs3 -q -d aa -m JTT -c 4 -a e
```

## Example Usage

```
phyml -i snvAlignment.phy --datatype nt --model GTR -v 0.0 -s BEST --ts/tv e --nclasses 4 --alpha e --bootstrap -4 --quiet
```
