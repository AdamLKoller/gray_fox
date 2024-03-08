#!/bin/bash

DATA_DIRECTORY=$1
TOTAL_COUNT=0

#touch ./data/results/dedup_counts.csv
echo "id,dedup_count" > ./data/results/dedup_counts.csv;
#echo "FILE COUNT"
for FILE in "$DATA_DIRECTORY"/*.dedup; 
do
    DEDUP_COUNT=$(wc -l < "$FILE")
    DEDUP_COUNT=$((DEDUP_COUNT/4))
    ID=$(basename "$FILE" .dedup)
#    echo "$FILE: $DEDUP_COUNT "
    OUT=$ID","$DEDUP_COUNT
    echo $OUT >> ./data/results/dedup_counts.csv; 
    TOTAL_COUNT=$((TOTAL_COUNT + DEDUP_COUNT))
done

TOTAL_COUNT=$((TOTAL_COUNT/4))

echo "Total deduped reads: $TOTAL_COUNT"
