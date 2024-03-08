#!/bin/bash

DATA_DIRECTORY=$1
TOTAL_COUNT=0

#touch ./data/results/trim_counts.csv
echo "id,trim_count" > ./data/results/trim_counts.csv;
#echo "FILE COUNT"
for FILE in "$DATA_DIRECTORY"/*.trim; 
do
    trim_COUNT=$(wc -l < "$FILE")
    trim_COUNT=$((trim_COUNT/4))
    ID=$(basename "$FILE" .trim)
    ID=$(basename "$ID" .dedup)
    #echo "$ID: $trim_COUNT "
    OUT=$ID","$trim_COUNT
    echo $OUT >> ./data/results/trim_counts.csv; 
    TOTAL_COUNT=$((TOTAL_COUNT + trim_COUNT))
done

TOTAL_COUNT=$((TOTAL_COUNT/4))

echo "Total trimmed reads: $TOTAL_COUNT"
