# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:46:42 2019

@author: Shubham
"""
import nltk
from nltk.corpus import state_union
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize , word_tokenize


h2 ="Shubham Salunkhe lives in INDIA."
data =[]
wt =nltk.word_tokenize(h2)
pt = nltk.pos_tag(wt)
for word in pt:
    if 'NNP' in pt:
        print(data.append())
    else:
        pass
print(data)   