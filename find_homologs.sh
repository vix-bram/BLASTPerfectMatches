#!/usr/bin/bash

# usage: find_perfect_matches.sh <query file> <subjectfile> <output file>

tblastn -query $1 -subject $2 -outfmt '6 std qlen' -task tblastn | awk '$3>=30 && $4>=($13)*0.9' > $3

wc -l $3


