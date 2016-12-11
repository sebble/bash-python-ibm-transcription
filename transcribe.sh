#!/bin/bash

LENGTH=115
OVERLAP=3
FILENAME="$1"
IFS='
'
PART=0
DURATION=$(avprobe $FILENAME 2>&1|grep Duration|awk '{print $2}'|sed s/,//)
echo "Splitting file $FILENAME..."
date
for SPLIT in $(./splits.py $DURATION $LENGTH $OVERLAP); do
    START=$(echo $SPLIT|cut -d\  -f1)
    END=$(echo $SPLIT|cut -d\  -f2)
    PARTF=$(printf "%04d" $PART)
    echo "Part $PARTF from $START to $END"
    date
    PARTFILE="${FILENAME}_${PARTF}_${START}_${END}.wav"
    test -f $PARTFILE && {
        echo "$PARTFILE already exists. Skipping conversion."
    } || {
        avconv -i $FILENAME -ss $START -t $LENGTH $PARTFILE
    }
    (
        echo "Transcribing $PARTFILE..."
        echo "$PARTF START @ $(date)"
        ./sr.py $PARTFILE
        echo "$PARTF END @ $(date)"
    ) &
    ((PART++))
done

echo "Done!"
date
