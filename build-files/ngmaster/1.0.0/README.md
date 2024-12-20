# ngmaster 1.0.0 container

Main tool : [ngmaster](https://github.com/MDU-PHL/ngmaster)

In silico multi-antigen sequence typing for Neisseria gonorrhoeae (NG-MAST).

Additional tools:

- any2fasta 0.4.2
- mlst 2.23.0
- python 3.9.0
- biopython 1.80
- perl 5.32.1
- bioperl 1.7.9

## Example Usage

```bash
# test ngmaster with the test FASTA file included with ngmaster code
$ ngmaster /opt/conda/lib/python3.9/site-packages/ngmaster/test/test.fa
FILE    SCHEME  NG-MAST/NG-STAR porB_NG-MAST    tbpB    penA    mtrR    porB_NG-STAR    ponA    gyrA    parC    23S
/opt/conda/lib/python3.9/site-packages/ngmaster/test/test.fa    ngmaSTar        4186/231        2569    241     23      42      100     100     10      2100
```
