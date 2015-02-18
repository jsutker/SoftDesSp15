# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: JOSEPH SUTKER

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from load import *

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """



    ORF_list = []

    def ORF_loop(thing,start_n):
        ORF_list = []
        this_ORF = ''
        in_ORF = False
        for i in range(start_n,len(thing)-2,3):
            if thing[i:i+3] == 'ATG':
                in_ORF = True
                this_ORF += 'ATG'
            elif thing[i:i+3] == 'TAA' or thing[i:i+3] == 'TAG' or thing[i:i+3] == 'TGA':
                if in_ORF:
                    ORF_list += [this_ORF]
                this_ORF = ''
                in_ORF = False
            elif in_ORF:
                this_ORF += thing[i:i+3]
                if i >= len(thing)-4:
                    ORF_list += [this_ORF]

        return ORF_list

            

    def rev_comp(thing):
        new_thing = ''
        for i in range(len(thing)):
            if thing[len(thing)-i-1] == 'A':
                new_thing += 'T'
            elif thing[len(thing)-i-1] == 'T':
                new_thing += 'A'
            elif thing[len(thing)-i-1] == 'G':
                new_thing += 'C'
            else:
                new_thing += 'G'
        return new_thing

    for i in range(3):
        ORF_list += ORF_loop(dna,i)
        ORF_list += ORF_loop(rev_comp(dna),i)
    return ORF_list


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """

    ORF_list = find_all_ORFs_both_strands(dna)
    longest_strand = ''
    for i in range(len(ORF_list)):
        if len(ORF_list[i]) > len(longest_strand):
            longest_strand = ORF_list[i]
    return longest_strand



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF
    """

    longest_length = 0
    for i in range(num_trials):
        ORF = longest_ORF(shuffle_string(dna))
        if len(ORF) > longest_length:
            longest_length = len(ORF)
    return longest_length



def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    prot = ''
    for thing in range(0,len(dna)-2,3):
        for i in range(len(aa)):
            for j in range(len(codons[i])):
                if codons[i][j] == dna[thing:thing+3]:
                    prot += aa[i]
    return prot


<<<<<<< HEAD
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that
        have an ORF larger than the specified threshold.
=======
def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
>>>>>>> 922a6e32441860ab0413630f74531e6e47a16a7c
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    long_ORFs = []
    ORFs = find_all_ORFs_both_strands(dna)
    for ORF in ORFs:
        if len(ORF) >= threshold:
            long_ORFs += [ORF]
    return long_ORFs

dna = load_seq("./data/X73525.fa")
dna_sal = load_salmonella_genome()
threshold = longest_ORF_noncoding(dna,1500)
print "Threshold: %d" % threshold
thingies = gene_finder(dna, threshold)
for i in range(len(thingies)):
    print "Protein #%d:" % (i+1), coding_strand_to_AA(thingies[i])

if __name__ == "__main__":
    import doctest
    doctest.testmod()