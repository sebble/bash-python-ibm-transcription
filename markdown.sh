#!/bin/bash

FILENAME="$1"

for PART in $(ls "$FILENAME"*.json); do
    echo "#### $PART"
    echo
    cat "$PART"|jq -r '.results[].alternatives[0].transcript'|sed 's/$/\n/'
    echo
done
