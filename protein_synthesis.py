#Author: Benjamin Hawkins
#Date: 1 March 2021

#----------Definition of classes----------
class NucleicAcid:
    NUCLEIC_ACID_TYPES  = ("Template DNA", "Coding DNA", "mRNA")

    def __init__(self, type, sequence):
        if (not type in NucleicAcid.NUCLEIC_ACID_TYPES):
            raise ValueError(f"{type} is not a valid type of nucleic acid. Please import a section of Template DNA, Coding DNA, or mRNA.")
        else:
            self.__type = type
        self.__sequence = sequence
    
    def toMRNA(self):
        if self.__type == "Template DNA":
            pass
        if self.__type == "Coding DNA":
            pass
        if self.__type == "mRNA":
            pass

#----------Implementation of Program----------

#Re
nucleicAcidType = input("Is the entry a selection of [Template DNA], [Coding DNA], or [mRNA]? ")
print(nucleicAcidType)
entrySequence = input(f"Please enter the sequence of {nucleicAcidType}: ")
print(entrySequence)

nucleicAcidInput = NucleicAcid(nucleicAcidType, entrySequence)
