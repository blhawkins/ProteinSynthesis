#Author: Benjamin Hawkins
#Date: 1 March 2021

#Importation of dependencies
from dataclasses import dataclass
from abc import ABC, abstractmethod
from amino_acids import amino_acid_dict

#----------Definition of classes----------#
class NucleicAcid(ABC):

    NUCLEIC_ACID_TYPES = ("Template DNA", "Coding DNA", "mRNA")

    def __init__(self, type, sequence):
        if (not type in NucleicAcid.NUCLEIC_ACID_TYPES):
            raise ValueError(f"{type} is not a valid type of nucleic acid. Please import a section of Template DNA, Coding DNA, or mRNA.")
        else:
            self.type = type
        self.sequence = sequence.upper()
        self.num_of_base_pairs = len(sequence)
        self.num_of_codons = int(self.num_of_base_pairs / 3)
    
    @abstractmethod
    def to_mRNA(self):
        pass

    @abstractmethod
    def validate_sequence(self):
        pass

class TemplateDNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
        self.validate_sequence()
        self.mRNA_sequence = self.to_mRNA()

    #Define the toMRNA function that converts the Template DNA strand into the cooresponding mRNA strand
    #---Perhaps this should be inside of a polymerase object instead of being a method.
    def to_mRNA(self):

        #Reverse the order of the sequence to obtain the coding_dna strand
        coding_dna = self.sequence[::-1]

        #Convert T to A, A to U, C to G, and G to C to obtain the cooresponding mRNA strand
        translation = {84: 65, 65 : 85, 67 : 71, 71 : 67}
        cooresponding_mRNA = coding_dna.translate(translation)

        #Output and return the mRNA strand cooresponding to the original template DNA strand
        print(f"{cooresponding_mRNA} is the cooresponding mRNA strand.")
        return cooresponding_mRNA
    
    def validate_sequence(self):
        if any (base_pair not in 'ATGC' for base_pair in self.sequence):
            raise ValueError(f"A {self.type} sequence must only contain Arginine (A), Thymine (T), Cytosine (C), or Guanine (G).")

class CodingDNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
        self.validate_sequence()
        self.mRNA_sequence = self.to_mRNA()
        
    def to_mRNA(self):
        #Convert T to A, A to U, C to G, and G to C to obtain the cooresponding mRNA strand
        translation = {84: 65, 65 : 85, 67 : 71, 71 : 67}
        cooresponding_mRNA = self.sequence.translate(translation)

        #Output and return the mRNA strand cooresponding to the original coding DNA strand
        print(f"{cooresponding_mRNA} is the cooresponding mRNA strand.")
        return cooresponding_mRNA
    
    def validate_sequence(self):
        if any (base_pair not in 'ATGC' for base_pair in self.sequence):
            raise ValueError(f"A {self.type} sequence must only contain Arginine (A), Thymine (T), Cytosine (C), or Guanine (G).")


class mRNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
        self.validate_sequence()
        self.mRNA_sequence = self.to_mRNA()
        Ribosome(self.mRNA_sequence, self.num_of_base_pairs)
    
    def to_mRNA(self):
        #Since the input was an mRNA sequence, simply print and return the original sequence unchanged
        print(f"{self.sequence} remains the mRNA strand.")
        return self.sequence

    def validate_sequence(self):
        if any (base_pair not in 'AUGC' for base_pair in self.sequence):
            raise ValueError(f"A {self.type} sequence must only contain Arginine (A), Uracil (U), Cytosine (C), or Guanine (G).")

class Ribosome:
    def __init__(self, mRNA_sequence, num_of_base_pairs):
        self.mRNA_sequence = mRNA_sequence
        self.num_of_base_pairs = num_of_base_pairs
        self.codon_sequence = self.creating_codons()
        self.amino_acid_sequence = self.appending_amino_acids()
    
    def creating_codons(self):
        #Split the mRNA_sequence into triplet codons
        codons = []
        n = 3
        num_of_valid_base_pairs = self.num_of_base_pairs - self.num_of_base_pairs % 3
        for index in range(0, num_of_valid_base_pairs, n):
            codons.append(self.mRNA_sequence[index : index + n])
        
        #Print the resulting triplet codons
        print(codons)
        return codons
    
    def appending_amino_acids(self):
        amino_acids = []
        for codon in self.codon_sequence:
            print(codon)
            print(tRNA(codon).amino_acid)

class tRNA:

    PHENYLALANINE_CODONS = 8

    def __init__(self, codon):
        self.codon = codon
        self.amino_acid = self.amino_acid_translation()
    def amino_acid_translation(self):
        if self.codon[0] == 'U':
            if self.codon[1] == 'U':
                if self.codon[2] in 'UC':
                    return 'Phe'
                elif self.codon[2] in 'AG':
                    return 'Leu'
            elif self.codon[1] == 'C':
                return 'Ser'
            elif self.codon[1] == 'A':
                if self.codon[2] in 'UC':
                    return 'Tyr'
                elif self.codon[2] in 'AG':
                    return 'Stop'
            elif self.codon[1] == 'G':
                if self.codon[2] in 'UC':
                    return 'Cys'
                elif self.codon[2] == 'A':
                    return 'Stop'
                elif self.codon[2] == 'G':
                    return 'Trp'
        
        elif self.codon[0] == 'C':
            if self.codon[1] == 'U':
                return 'Leu'
            elif self.codon[1] == 'C':
                return 'Pro'
            elif self.codon[1] == 'A':
                if self.codon[2] in 'UC':
                    return 'His'
                elif self.codon[2] in 'AG':
                    return 'Gln'
            elif self.codon[1] == 'G':
                return 'Arg'
        
        #A start
        elif self.codon[0] == 'A':
            if self.codon[1] == 'U':
                if self.codon[2] in 'UCA':
                    return 'Ile'
                elif self.codon[2] == 'G':
                    return 'Met'
            elif self.codon[1] == 'C':
                return 'Thr'
            elif self.codon[1] == 'A':
                if self.codon[2] in 'UC':
                    return 'Asn'
                elif self.codon[2] in 'AG':
                    return 'Lys'
            elif self.codon[1] == 'G':
                if self.codon[2] in 'UC':
                    return 'Ser'
                elif self.codon[2] in 'AG':
                    return 'Arg'

        #G start
        elif self.codon[0] == 'G':
            if self.codon[1] == 'U':
                return 'Val'
            elif self.codon[1] == 'C':
                return 'Ala'
            elif self.codon[1] == 'A':
                if self.codon[2] in 'UC':
                    return 'Asp'
                elif self.codon[2] in 'AG':
                    return 'Glu'
            elif self.codon[1] == 'G':
                return 'Gly'

# class AminoAcid:
#     def __init__(self):
#         self.return_name()
#     def return_name:
#         return 


# @dataclass
# class AminoAcid:
#     __name : str
#     __three_letter_abbreviation : str
#     __one_letter_abbr : str
#     __class : str
#     __polarity : str
#     __charge : str
#     __hydropathy : float
#     __molecular_mass : float
#     __abundance : float
#     __codons : []
    #I could incorporate elements of composition between the side chain and the amino acid itself

#----------Instantiation of Amino Acids----------#
#Loop through the entries in the amino_acid_dict
#I want to prevent having to do this everytime the program is run, perhaps I could use more of a do loop so the user can perform the functional operation of the program as long as they want, while only having to instantiate these variables upon restarting the program
#for entry in amino_acid_dict:
#    print(entry['name'])
    #f"entry['name']" = AminoAcid(entry['name'])

#----------Implementation of Program----------#

#Request user input for the type of nucleic acid and the base pair sequence to be operated on
#nucleic_acid_type = input("Is the entry a selection of [Template DNA], [Coding DNA], or [mRNA]? ")
#print(nucleic_acid_type)
#base_pair_sequence = input(f"Please enter the sequence of {nucleic_acid_type}: ")
#print(base_pair_sequence)

#Instantiate 
#nucleic_acid_input = TemplateDNA(nucleic_acid_type, base_pair_sequence)
nuclelic_acid_input = mRNA('Coding DNA', 'UUGGGUACUGUCCCGAGGCUGGCUGAAUAGAAGGAGCGAUCCUUGGAGCUGAGUGCAGAGCUCGUUCGACAGAAAUAGACUUCCCUACAUGCGAUAAGAC')
