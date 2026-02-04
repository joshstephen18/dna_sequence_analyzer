DNA Sequence Analyzer 

Project Description: This program is designed to allow users/researchers to input DNA sequences in the form of FASTA files for analysis. It allows users to calculate nucleotide statistics, calculate GC content, identify restriction enzyme sites, generate reverse complements, and count codons. Furthermore, an optional features includes plotting nucleotide composition for visual analysis.

Usage:
-run the program (main.py)
-enter the path to your FASTA file when prompted (for test case, enter: test_sequence.fasta
-follow the prompts, and the program will output the following: sequence length, GC content (%), nucleotide counts, restriction enzyme sites, reverse complement, codon counts, and an nucleotide composition bar chart if "y" is typed when prompted.

FASTA File Example
>test_sequence
ATGCGATACGCTTGAATTCGCGCGATAG

Expected Output for Example:

Sequence Length:
28

GC content (%):
50.0

Nucleotide counts:
A: 7
T: 7
G: 8
C: 6

Restriction enzyme sites:
EcoRI found at positions: [14]
, BamHI not found
, HindIII not found

Reverse complement:
CTATCGCGCGAATTCAAGCGTATCGCAT

Codon counts:
ATG : 1
CGA : 1
TAC : 1
GCT : 1
TGA : 1
ATT : 1
CGC : 1
GCG : 1
ATA : 1

Do you want to see a nucleotide composition plot? (y/n): y

-Plot saved to:
  plots/nucleotide_composition.png

