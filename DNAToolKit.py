# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:42:33 2025

@author: Anusha07
"""
import collections
from sequencesused import *

def validateSeq(dna_seq):
    tmpSeq=dna_seq.upper()
    for nuc in tmpSeq:
        if nuc not in Nucleotides:
            return False
    return tmpSeq

def countNucFrequency(seq):
    tmpFreqDict={"A":0,"C":0,"T":0,"G":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

    #optimised counting way
    #return dict(collections.Counter(seq))

def transcription(seq):
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

