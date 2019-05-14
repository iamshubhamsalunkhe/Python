# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:00:55 2019

@author: Shubham
"""
'''
count of adjectives JJ
input address from user consist of , name and location remove coma and dot after removal print name and location  
'''




import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

document = "Today the Netherlands celebrates King\'s Day. "
sentences = nltk.sent_tokenize(document)

data = []
for sent in sentences:
    p = nltk.pos_tag(nltk.word_tokenize(sent))
    print(p)
    data = data + p
for word in data:
    if 'NNP' in word:
        print(word[0])
        
        