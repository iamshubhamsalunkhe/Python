# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:09:14 2019

@author: Shubham
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize , word_tokenize


words = ["game","gaming","gamed","games","analytics"]

ps= PorterStemmer()

for word in words:
    print(ps.stem(word))