# pangolin docker image

Main tool : [pangolin](https://github.com/cov-lineages/pangolin)

Full documentation: [https://cov-lineages.org/resources/pangolin.html](https://cov-lineages.org/resources/pangolin.html)

Phylogenetic Assignment of Named Global Outbreak LINeages

Additional tools:

- [pangolin-data](https://github.com/cov-lineages/pangolin-data) 1.20
- [pangolin-assignment](https://github.com/cov-lineages/pangolin-assignment)  1.20
- [minimap2](https://github.com/lh3/minimap2) 2.26-r1175
- [usher](https://github.com/yatisht/usher) 0.6.2
- [faToVcf](https://github.com/yatisht/usher) 426
- [scorpio](https://github.com/cov-lineages/scorpio) 0.3.17
- [constellations](https://github.com/cov-lineages/constellations) 0.1.10
- [gofasta](https://github.com/virus-evolution/gofasta) 1.2.0
- [mafft](https://mafft.cbrc.jp/alignment/software/) 7.520
- python 3.8.15

## pangoLEARN deprecation

As of pangolin version 4.3, pangoLEARN mode has been deprecated. [More info can be found here on the v4.3 release page.](https://github.com/cov-lineages/pangolin/releases/tag/v4.3)

> If `--analysis-mode fast` or `--analysis-mode pangolearn` is given, pangolin v4.3 will print out a warning and use UShER mode instead, unless `--datadir` is also given specifying a directory with pangoLEARN model files. The next release of pangolin-data (v1.20) will no longer include the model files which have not been updated since v1.18.

This docker image contains `pangolin-data` v1.20. The pangoLEARN model has not been updated since pangolin-data version 1.18. Only the the underlying UShER tree/protobuf file will be maintained for the forseeable future. 

**Please use the UShER mode of pangolin if you want to stay up-to-date with the most recent lineages.** [See pangolin-data release notes here for more details](https://github.com/cov-lineages/pangolin-data/releases/tag/v1.20)

## Example Usage

```bash
# run Pangolin in the default mode (usher). Can optionally supply --analysis-mode usher
$ pangolin /pangolin/pangolin/test/test_seqs.fasta  -o /data/test_seqs-output-pusher

# view the output CSV
$ column -t -s, /data/test_seqs-output-pusher/lineage_report.csv
taxon                                lineage     conflict  ambiguity_score  scorpio_call                  scorpio_support  scorpio_conflict  scorpio_notes                                                              version       pangolin_version  scorpio_version  constellation_version  is_designated  qc_status  qc_notes                note
India seq                            B.1.617.1   0.0                        B.1.617.1-like                1.0              0.0               scorpio call: Alt alleles 11; Ref alleles 0; Amb alleles 0; Oth alleles 0  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: B.1.617.1(1/1)
b117                                 B.1.1.7     0.0                        Alpha (B.1.1.7-like)          0.91             0.04              scorpio call: Alt alleles 21; Ref alleles 1; Amb alleles 1; Oth alleles 0  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: B.1.1.7(2/2)
outgroup_A                           A           0.0                                                                                                                                                                    PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.02  Usher placements: A(1/1)
issue_57_torsten_seq                 Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_has_6000_Ns_in_18000_bases  Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_has_no_seq                  Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
This_seq_is_too_short                Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       Ambiguous_content:0.9   
This_seq_has_lots_of_Ns              Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       Ambiguous_content:0.98  
This_seq_is_literally_just_N         Unassigned                                                                                                                                                                         PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          fail       failed to map           
Japan_seq                            B           0.0                                                                                                                                                                    PANGO-v1.16   4.1.3             0.3.17           v0.1.10                True           pass       Ambiguous_content:0.02  Assigned from designation hash.
USA_seq                              B.1.314     0.0                                                                                                                                                                    PANGO-v1.16   4.1.3             0.3.17           v0.1.10                True           pass       Ambiguous_content:0.02  Assigned from designation hash.
Unassigned_omicron_seq               BA.1        0.0                        Probable Omicron (BA.1-like)  0.71             0.08              scorpio call: Alt alleles 42; Ref alleles 5; Amb alleles 9; Oth alleles 3  PUSHER-v1.16  4.1.3             0.3.17           v0.1.10                False          pass       Ambiguous_content:0.03  Usher placements: BA.1(1/1)
```
