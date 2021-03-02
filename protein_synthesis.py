#Author: Benjamin Hawkins
#Date: 1 March 2021

#Importation of dependencies
from dataclasses import dataclass
from abc import ABC, abstractmethod
from amino_acids import amino_acid_dict

#----------Definition of classes----------
class NucleicAcid(ABC):

    NUCLEIC_ACID_TYPES  = ("Template DNA", "Coding DNA", "mRNA")

    def __init__(self, type, sequence):
        if (not type in NucleicAcid.NUCLEIC_ACID_TYPES):
            raise ValueError(f"{type} is not a valid type of nucleic acid. Please import a section of Template DNA, Coding DNA, or mRNA.")
        else:
            self.__type = type
        self.sequence = sequence.upper()
        self.__num_of_base_pairs = len(sequence)
        self.__num_of_codons = int(self.__num_of_base_pairs / 3)
    
    @abstractmethod
    def to_mRNA(self):
        pass

class TemplateDNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
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

class CodingDNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
        self.mRNA_sequence = self.to_mRNA()
        
    def to_mRNA(self):
        #Convert T to A, A to U, C to G, and G to C to obtain the cooresponding mRNA strand
        translation = {84: 65, 65 : 85, 67 : 71, 71 : 67}
        cooresponding_mRNA = self.sequence.translate(translation)

        #Output and return the mRNA strand cooresponding to the original coding DNA strand
        print(f"{cooresponding_mRNA} is the cooresponding mRNA strand.")
        return cooresponding_mRNA


class mRNA(NucleicAcid):
    def __init__(self, type, sequence):
        super().__init__(type, sequence)
        self.mRNA_sequence = self.to_mRNA()
    
    def to_mRNA(self):
        #Since the input was an mRNA sequence, simply print and return the original sequence unchanged
        print(f"{self.sequence} remains the mRNA strand.")
        return self.sequence

@dataclass
class AminoAcid:
    __name : str
    __three_letter_abbreviation : str
    __one_letter_abbr : str
    __class : str
    __polarity : str
    __charge : str
    __hydropathy : float
    __molecular_mass : float
    __abundance : float
    __codons : []
    #I could incorporate elements of composition between the side chain and the amino acid itself

#----------Instantiation of Amino Acids----------
#Loop through the entries in the amino_acid_dict
#I want to prevent having to do this everytime the program is run, perhaps I could use more of a do loop so the user can perform the functional operation of the program as long as they want, while only having to instantiate these variables upon restarting the program
#for entry in amino_acid_dict:
#    print(entry['name'])
    #f"entry['name']" = AminoAcid(entry['name'])

#----------Implementation of Program----------

#Request user input for the type of nucleic acid and the base pair sequence to be operated on
#nucleic_acid_type = input("Is the entry a selection of [Template DNA], [Coding DNA], or [mRNA]? ")
#print(nucleic_acid_type)
#base_pair_sequence = input(f"Please enter the sequence of {nucleic_acid_type}: ")
#print(base_pair_sequence)

#Instantiate 
#nucleic_acid_input = TemplateDNA(nucleic_acid_type, base_pair_sequence)
nuclelic_acid_input = mRNA('Template DNA', 'aat')
