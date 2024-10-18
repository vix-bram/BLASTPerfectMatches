# isPCR and Global Alignment of Amplicons

This repo contains the files needed to perform in-silico polymerase chain reaction (isPCRp=  and then perform global alignment of the amplicons produced.
Execute the amplicon_align.py file on the command line to perform both the PCR and amplicon alignment. Here is the usage:

python amplicon_align.py -1 <path_to_assembly1> -2 <path_to_assembly2> -p <path_to_primers> -m <max_amplicon_size> --match <match_score> --mismatch <mismatch_penalty> --gap <gap_penalty>

The primer file contains primers which define which regions of the DNA (in the assembly file) should be amplified. The best amplicon alignment along with the alignment score will be printed to the terminal after executing the file. There are some sample files in data-magnusopus that this code can be run on. The Pseudomonas_ tiles are bacterial DNA assemblies, and rpoD.fna is the DNA primer file.  
