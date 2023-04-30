Nucleotides = ["A", "C", "G", "T"]
import collections
#Check the sequence to make sure it is in a DNA String 
#we want to make sure we only get ACGT 
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False 
    return tmpseq 

#counts number of nucleotides 
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] +=1 
    return tmpFreqDict

    #4 lines of code can be replaced by a collection 
    # return dict(collections.Counter(seq))
