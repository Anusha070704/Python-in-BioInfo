from DNAToolKit import *
import random
from utilities import *

#rndDNAStr = "ATTGCGTTA"
randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50
)])

DNAStr=validateSeq(randDNAStr)

print(colored(DNAStr))

print(countNucFrequency((DNAStr)))

print(colored(transcription((DNAStr))))

print(colored(DNAStr))
print(''.join(['|' for c in range(len(DNAStr))]))
print(colored(reverse_complement((DNAStr))))