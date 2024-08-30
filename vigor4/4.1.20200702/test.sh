i=1
while read line
do
    tbl=$(echo   $line | cut -f 1 -d , )
    fasta=$(echo $line | cut -f 2 -d , )
    db=$(echo    $line | cut -f 3 -d , )
    vigor4 -i /VIGOR4/src/test/resources/$fasta -o test_${db}_${i} -d /VIGOR_DB/Reference_DBs/$db
    diff test_${db}_${i}.tbl /VIGOR4/src/test/resources/${tbl}
    i=$((i+1))
done < <(grep -v referenceType /VIGOR4/src/test/resources/config/RegressionTestConfig.csv)