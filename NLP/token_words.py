# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:10:21 2019

@author: Shubham
"""

#Tokenizing words

import nltk

from nltk.tokenize import sent_tokenize , word_tokenize 

data = "All work and no play makes a dull boy, all and no play"
tw=  word_tokenize(data)
print(tw)
print(type(tw))
print("First word of tw:",tw[0])
print("last word of  tw:",tw[-1]
