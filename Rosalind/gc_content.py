import os

def readFile(filePath):
    with open(filePath,'r') as f:
        return [l.strip() for l in f.readlines()]
    
def gc_content(seq):
    return round(((seq.count('C')+seq.count('G'))/len(seq))*100,6)

FASTAFile=readFile("c:/Users/Anusha07/Desktop/Placements/Python in BioInfo/BioInfo/Rosalind/test_data/gc_content.txt")
FASTADict={}
FASTALabel=""

print(FASTAFile)

for line in FASTAFile:
    if '>' in line:
        FASTALabel=line
        FASTADict[FASTALabel]=""
    else:
        FASTADict[FASTALabel]+=line

print(FASTADict)

RESULTDict={key:gc_content(value) for (key,value) in FASTADict.items()}

print(RESULTDict)

MaxGCKey=max(RESULTDict, key=RESULTDict.get)
print(f'{MaxGCKey.lstrip(">")}\n{RESULTDict[MaxGCKey]}')
