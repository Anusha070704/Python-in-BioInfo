# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:29:59 2025

@author: Anusha07
"""
def countNucFrequency(seq):
    tmpFreqDict={"A":0,"C":0,"G":0,"T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

DNAString="GTTTACTGCCTTCGTGAATGTGGCGAAAGATACCGATAGTATTTATCCCACCCTATTATGAGGTGGGGGTCCGTTAAACAGGTATGTTTTCCGAAGAGATACGCTCCCGCTGAGTTGCCAATTCCATGTAGTACTCACTACGCCAGTCTAAACAAACTCGGCTCGATTAGGTCAAAGACCTTCTTCGGCTATTTAGGTTTAGCTTTGTACCGACACTAGAAGGTTCCACACTCCGCGATCGATCCTGATTGCCTAAGCGGCTGTTTAGTATGACACAAGCGCACAGCCAGAAACTGCGACTGTAGGAGAACGAATTCGCCAAGGGAATGAGGGGCAGCCAAAGGTGCGATACTAAAACCAGGTTTCGCAGCATTAGCATATTGCACGAGGTTAGCAAATTTTGGAAATGAATTGCTACTAATCCGTAGCTCTACAGAATCCAACCTGGCTCAGCCAGTTGAAGGCGGGGGTGCTACTGGGCTATCTAACTGGCCACGTAAACGCCCCAAGGTTTATCCCCACATCCCCCCATCACGACGTATGATCGGTTTAACTCATGAACCTAAATCCCTGAACGCGACGGAAGACAATAAAAACCATGATAAACTCCAGCCTCATGTACTTCCAGTACAGCGGGCAACCCGTGTCTGACTCCAGATCATGACTTATGAAAATAACGCGCGAACAGGGTAGGTCGTTATATACCAGGTGGCTGCGCGGACGTATATGAGAACCATTGTCCCGGGTCTTTATCACAAACCCTGGCTAGAGCCTGGAATAGGACAGTTGGCGATTACGATAGCTCGGGCTGGGCCCTGGCACATAGCACATTCGAATGTATCTCGTCGTACAATAGCCGGAGGTGCCTTCGGTTTACAGGAGCACGTGGGGACAATGCAATTGCAATAGACAGATAAACCAGGCATGTGACAGTGCACCTTAGAATTTATCGGC"
result=countNucFrequency(DNAString)
print(' '.join([str(val) for key, val in result.items()]))
