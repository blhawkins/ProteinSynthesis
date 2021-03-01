#Author: Benjamin Hawkins
#Date: 1 March 2021

#Importation of dependencies
from dataclasses import dataclass

#----------Definition of classes----------
class NucleicAcid:
    NUCLEIC_ACID_TYPES  = ("Template DNA", "Coding DNA", "mRNA")

    def __init__(self, type, sequence):
        if (not type in NucleicAcid.NUCLEIC_ACID_TYPES):
            raise ValueError(f"{type} is not a valid type of nucleic acid. Please import a section of Template DNA, Coding DNA, or mRNA.")
        else:
            self.__type = type
        self.__sequence = sequence
        self.__numOfBasePairs = len(sequence)
        self.__numOfCodons = int(self.__numOfBasePairs / 3)
        self.toMRNA()
    
    def toMRNA(self):
        if self.__type == "Template DNA":
            pass
        if self.__type == "Coding DNA":
            pass
        if self.__type == "mRNA":
            pass

@dataclass
class AminoAcid:
    __name : str
    __abbreviation : str
    __class : str
    __polarity : str
    __charge : str
    __molecular_mass : float
    __codons : []



    

#----------Implementation of Program----------

#Request user input for the type of nucleic acid and the base pair sequence to be operated on
nucleicAcidType = input("Is the entry a selection of [Template DNA], [Coding DNA], or [mRNA]? ")
print(nucleicAcidType)
basePairSequence = input(f"Please enter the sequence of {nucleicAcidType}: ")
print(basePairSequence)

#Instantiate 
nucleicAcidInput = NucleicAcid(nucleicAcidType, basePairSequence)
