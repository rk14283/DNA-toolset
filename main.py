#place to test all of our functions

from DNAToolkit import * 
import random 
randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(20)])


#validate sequence                
DNAStr= (validateSeq(randDNAStr))
#counts number of nucleotides 
print (countNucFrequency(DNAStr))