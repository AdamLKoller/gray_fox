#!/bin/bash

DATA_DIRECTORY=$1
TOTAL_COUNT=0

for FILE in "$DATA_DIRECTORY"/*.fastq; 
do
    COUNT=$(wc -l < "$FILE")
    TOTAL_COUNT=$((TOTAL_COUNT + COUNT))
done
TOTAL_COUNT=$((TOTAL_COUNT/4))

echo "Total raw reads: $TOTAL_COUNT"