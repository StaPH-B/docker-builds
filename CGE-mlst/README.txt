Hello - this dockerfile is set up to point to the mlst database.
You don't need to provide the -p path to the database.

Example docker run command:
$ docker run -v /Users/mokaze:/data docker.io/mokaze/cge-mlst:2.19.0 \
mlst.py -i /data/GCF_000021205.1_ASM2120v1_genomic.fna -o /data/output \
-s bcereus -x 
