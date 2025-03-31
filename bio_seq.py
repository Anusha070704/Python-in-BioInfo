from bio_struc import *
import random
from collections import Counter

"__ before any function converts from public to private"

class bio_seq:
    def __init__(self, dna_seq="ATCG", dna_seq_type="DNA", label="No Label"):
        self.dna_seq=dna_seq.upper()
        self.label=label
        self.dna_seq_type=dna_seq_type
        self.is_valid=self.validate()
        assert self.is_valid, f"Provided data does not seem to be correct {self.dna_seq_type} sequence"

    def validate(self):
        return set(Nucleotides[self.dna_seq_type]).issuperset(self.dna_seq)
    
    def get_seq_biotype(self):
        return self.dna_seq_type

    def get_seq_info(self):
        return f"[Label]: {self.label}\n[Sequence]: {self.dna_seq}\n[BioType]: {self.dna_seq_type}\n[Length]: {len(self.dna_seq)}"
    
    def generate_rnd_seq(self, length=10, dna_seq_type="DNA"):
        dna_seq=''.join([random.choice(Nucleotides[dna_seq_type]) for x in range(length)])
        self.__init__(dna_seq, dna_seq_type, "Randomly generated sequence")

    def nucleotide_frequency(self):
        return dict(Counter(self.dna_seq))
    
    def transcription(self):
        if self.dna_seq_type == "DNA":
            return self.dna_seq.replace("T", "U")
        return "Not a DNA sequence"
    
    def reverse_complement(self):
        if self.dna_seq_type == "DNA":
            mapping=str.maketrans('ATGC','TAGC')
        else:
            mapping=str.maketrans('AUCG', 'UAGC')
        return self.dna_seq.translate(mapping)[::-1]
    
    def gc_content(self):
        return round((self.dna_seq.count('C')+self.dna_seq.count('G')/len(self.dna_seq)*100))
    
    def gc_content_subsec(self,k=20):
        res=[]
        for i in range(0,len(self.dna_seq)-k+1,k):
            subseq=self.dna_seq[i:i+k]
            res.append(round((subseq.count('C')+subseq.count('G')/len(subseq)*100)))
        return res
    
    def translate_seq(self, init_pos=0):
        if self.dna_seq_type == "DNA":
            return[DNA_Codons[self.dna_seq[pos:pos+3]]for pos in range(init_pos, len(self.dna_seq) - 2,3)]
        elif self.dna_seq_type == "RNA":
            return[RNA_Codons[self.dna_seq[pos:pos+3]]for pos in range(init_pos, len(self.dna_seq) - 2,3)]

    
    def codon_usage(self, aminoacid):
        tmplist=[]
        if self.dna_seq_type == "DNA":
            for i in range(0,len(self.dna_seq)-2,3):
                if DNA_Codons[self.dna_seq[i:i+3]]==aminoacid:
                    tmplist.append(self.dna_seq[i:i+3])
        elif self.dna_seq_type == "RNA":
            for i in range(0,len(self.dna_seq)-2,3):
                if RNA_Codons[self.dna_seq[i:i+3]]==aminoacid:
                    tmplist.append(self.dna_seq[i:i+3])

        freqDict=dict(Counter(tmplist))
        totalWeight=sum(freqDict.values())
        for self.dna_seq in freqDict:
            freqDict[self.dna_seq]=round(freqDict[self.dna_seq]/totalWeight,2)
        return freqDict
    
    def gen_reading_frames(self):
        frames=[]
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        tmp_seq=bio_seq(self.reverse_complement(),self.dna_seq_type)
        frames.append(tmp_seq.translate_seq(0))
        frames.append(tmp_seq.translate_seq(1))
        frames.append(tmp_seq.translate_seq(2))
        return frames 
    
    def proteins_from_rf(self, aa_seq):
        current_prot=[]
        proteins=[]
        for aa in aa_seq:
            if aa=="_":
                if current_prot:
                    for p in current_prot:
                        proteins.append(p)
                    current_prot=[]
            else:
                if aa=="M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i]+=aa
        return proteins
    
    def all_proteins_from_orfs(self,startReadPos=0,endReadPos=0,ordered=False):
        if endReadPos>startReadPos:
            tmp_seq=bio_seq(self.dna_seq[startReadPos:endReadPos], self.dna_seq_type)
            rfs=tmp_seq.gen_reading_frames
        else:
            rfs=self.gen_reading_frames()

        res=[]
        for rf in rfs:
            prots=self.proteins_from_rf(rf)
            for p in prots:
                res.append(p)

        if ordered:
            return sorted(res,key=len,reverse=True)
        return res


