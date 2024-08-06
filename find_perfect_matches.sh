#!/usr/bin/bash

# usage: find_perfect_matches.sh <query file> <subjectfile> <output file>

blastn -query $1 -subject $2 -outfmt '6 std qlen' -task blastn-short | awk '$3==100 && $4==$13' > $3
wc -l $3
