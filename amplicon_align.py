#!/usr/bin/env python3
import argparse
import sys
from magnumopus.ispcr import *
from magnumopus.nw import *

def parse_args():
    parser = argparse.ArgumentParser(
        description="Perform in-silico PCR on two assemblies and align the amplicons"
    )
    parser.add_argument("-1", "--assembly1", help="Path to the first assembly file", required=True)
    parser.add_argument("-2", "--assembly2", help="Path to the second assembly file", required=True)
    parser.add_argument("-p", "--primers", help="Path to the primer file", required=True)
    parser.add_argument("-m", "--max_amplicon_size", type=int, help="Maximum amplicon size for isPCR", required=True)
    parser.add_argument("--match", type=int, help="Match score to use in alignment", required=True)
    parser.add_argument("--mismatch", type=int, help="Mismatch penalty to use in alignment", required=True)
    parser.add_argument("--gap", type=int, help="Gap penalty to use in alignment", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    # Getting the amplicons
    amplicon1 = ispcr(args.primers, args.assembly1, args.max_amplicon_size)
    amplicon2 = ispcr(args.primers, args.assembly2, args.max_amplicon_size)

    # Aligning the amplicons
    alignment, score = needleman_wunsch(amplicon1, amplicon2, args.match, args.mismatch, args.gap)

    # Formatting th output and printing it
    alignmentSplit1 = alignment[0].split('\n')
    alignmentSplit2 = alignment[1].split('\n')

    toPrint1 = alignmentSplit1[1]
    toPrint2 = alignmentSplit2[1]

    print(toPrint1)
    print(toPrint2)
    print(score)


if __name__ == "__main__":
    main()
