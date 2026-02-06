# 🧬 DNA Sequence Analyzer

Project Description: This program is designed to allow users/researchers to input DNA sequences in the form of FASTA files for analysis. 

## 🌟 Features

1. Nucleotide Statistics: Total length and automated counts for A, T, C, and G.

2. GC Content: Precise percentage calculation for stability analysis.

3. Restriction Mapping: Identifies EcoRI, BamHI, and HindIII sites.

4. Sequence Manipulation: Generate reverse complements instantly.

5. Visualization: Optional bar chart generation for nucleotide composition analysis.


## 🛠️ Getting Started / Usage
1. Ensure installation of libraries (pip install numpy matplotlib) and clone this repository.

2. Run the main script (main.py)

3. Enter the path to your FASTA file when prompted (for test case, enter: test_sequence.fasta)

4. Follow the prompts, and the program will output the following: sequence length, GC content (%), nucleotide counts, restriction enzyme sites, reverse complement, codon counts, and a nucleotide composition bar chart if "y" is typed when prompted.


## 📊 FASTA File Example
>test_sequence
ATGCGATACGCTTGAATTCGCGCGATAG

### Expected Output for Example:

Sequence Length: 28

GC content (%): 50.0

Nucleotide counts: A: 7 T: 7 G: 8 C: 6

Restriction enzyme sites: EcoRI found at positions: [14], BamHI not found, HindIII not found

Reverse complement: CTATCGCGCGAATTCAAGCGTATCGCT

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


  ## ⏭️ Future improvements/next steps
  1. Modify script to support multiple FASTA sequences in a single file instead of a single sequence.
  

  2. Add automatic FASTA file validation to catch user error (malformed headers, invalid characters, empty files).



  ## 💻 Libraries used
  1. NumPy for numerical operations
  2. Matplotlib for nucleotide composition bar chart
  3. collections (Python standard library) - specifically Counter for counting codons and nucleotides

