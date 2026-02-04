#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter #collections is part of python's standard library

#read DNA sequence from a FASTA file and convert it to uppercase
def read_fasta(file_path):
    with open (file_path, "r") as file:   #with automatically closes the file after statements are executed
        lines = file.readlines()
        sequence = "".join([line.strip().upper() for line in lines if not line.startswith(">")])  #if not line.startswith() ignores the FASTA header
        #.strip removes the whitespace/newline characters and .upper() capitalizes all letters
    return sequence

#calculate GC content
def gc_content(sequence):
    seq_array = np.array(list(sequence)) #converts sequence to NumPy array     #list(sequence) takes the string and breaks it into individual letters
    g_count = np.sum (seq_array == 'G')
    c_count = np.sum (seq_array == 'C')
    gc_percentage = (g_count + c_count) / len(seq_array) * 100
    return gc_percentage

#count nucleotides for plotting later on
def nucleotide_counts(sequence):
    seq_array = np.array(list(sequence))
    counts = { #we are creating a dictionary of nucleotide counts
        'A': np.sum(seq_array == 'A'),
        'T': np.sum(seq_array == 'T'),
        'G': np.sum(seq_array == 'G'),
        'C': np.sum(seq_array == 'C')
    }
    return counts

#find restriction enzyme sites
def find_restriction_sites(sequence, enzymes):
    results = {}
    for enzyme, site in enzymes.items():  #this creates the outer loop to pick an enzyme
        positions = []
        start = 0
        while True: #creates the inner loop to scan the DNA
            pos = sequence.find (site, start)  #.find(value, start, end) is used to locate location of specific substring
            if pos == -1:    #note: in python, if .find() can't find the pattern, it returns -1
                break #if the pattern isn't found, the while loop is stopped and code moves onto next enzyme
            positions.append (pos+1)  #if pattern was found, append the location to our list
            start = pos + 1 #updates starting point so we can look for the next occurrence of the same enzyme later in the string
            #position will reflect 1-based biological position instead of 0-based indexing

        results[enzyme] = positions #saves list of positions to our results dictionary under the enzyme's name
    return results

#create a bar chart to visualize nucleotide composition
def plot_nucleotide_composition(sequence):
    counts = nucleotide_counts(sequence)
    plt.bar (counts.keys(), counts.values(), color = ['green', 'red', 'yellow', 'blue']) #.keys() retrieves the names of the categories in the counts dictionary created earlier
    plt.title('Nucleotide Composition')
    plt.xlabel("Nucleotide")
    plt.ylabel('Count')
    plt.savefig("plots/nucleotide_composition.png") #saves plot to plots folder I created
    plt.show()

#find the reverse complement of the initial sequence
def reverse_complement(sequence):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} #creates dictionary that acts as a lookup table
    rev_comp = "".join([complement[base] for base in sequence[::-1]]) # #slicing here reads the string backwards
    #dictionary[key] is to look up a value from dict
    #list comprehension here creates a list of individual characters and .join() puts it back into a single string
    return rev_comp


#count the codons
def codon_count(sequence):
    codons = [sequence[i:i+3] for i in range(0, len(sequence)-2, 3)]
    return dict(Counter(codons))  #creating dict with codons and count of each


#main
def main():
    print("DNA Sequence Analyzer")
    print("---------------------")

    #ask user for FASTA File
    fasta_file = input("Enter path to FASTA file: ")
    sequence = read_fasta(fasta_file) #read_fasta function defined at start of code

    print("\nSequence Length:")
    print (len(sequence))

    #GC content
    gc = gc_content(sequence)
    print ("\nGC content (%):")
    print(round(gc, 2))

    #nucleotide counts
    counts = nucleotide_counts(sequence)
    print("\nNucleotide counts:")
    print("A:", counts["A"])
    print("T:", counts["T"])
    print("G:", counts["G"])
    print("C:", counts["C"])

    #define the restriction enzymes in a dict
    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT"
    }

    sites = find_restriction_sites(sequence, enzymes)
    print("\nRestriction enzyme sites:")

    for enzyme in sites:
        if len(sites[enzyme]) > 0:
            print(enzyme, "found at positions:", sites[enzyme])
        else:
            print(enzyme, "not found")

    #reverse complement
    rev_comp = reverse_complement(sequence)
    print("\nReverse complement:")
    print(rev_comp)

    #codon count
    codons = codon_count(sequence)
    print("\nCodon counts:")

    for codon in codons:
        print(codon, ":", codons[codon])

    #optional plot
    show_plot = input("\nDo you want to see a nucleotide composition plot? (y/n): ")
    if show_plot.lower() == "y":   #.lower() converts user response to lowercase
        plot_nucleotide_composition(sequence)


if __name__ == "__main__":
    main()




