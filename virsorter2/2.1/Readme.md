# Virsorter 2 container

Main tool :https://github.com/jiarong/VirSorter2  v.2.1


# Before doing anything, 
You need to configure the associated database, download it from https://github.com/jiarong/VirSorter2 


```
tar xvf db.tgz
```

# Example Usage
```
virsorter config --init-source --db-dir=./db
virsorter run -w virsorter2.test.out -i test.fa -j 1 
```

