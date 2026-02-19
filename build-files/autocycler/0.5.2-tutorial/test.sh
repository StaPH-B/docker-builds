# stolen from https://github.com/rrwick/Autocycler/wiki/Demo-dataset
threads="4"
genome_size="242000"

autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "$genome_size"

mkdir assemblies
for assembler in flye miniasm raven; do
    for i in 01 02 03 04; do
        "$assembler".sh subsampled_reads/sample_"$i".fastq assemblies/"$assembler"_"$i" "$threads" "$genome_size"
    done
done
rm subsampled_reads/*.fastq

autocycler compress -i assemblies -a autocycler_out

autocycler cluster -a autocycler_out

for c in autocycler_out/clustering/qc_pass/cluster_*; do
    autocycler trim -c "$c"
    autocycler resolve -c "$c"
done

autocycler combine -a autocycler_out -i autocycler_out/clustering/qc_pass/cluster_*/5_final.gfa
