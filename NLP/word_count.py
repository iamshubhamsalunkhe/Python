# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:20:58 2019

@author: Shubham
"""
#print count of word in sentence but  using tokenize and for loop

import nltk
from nltk.tokenize import sent_tokenize , word_tokenize 


h1="hey there how are you shubham yeah I am fine viraj so shubham what are you upto anything new  nothing man hey viraj how's you're hotel management course is going on"
 
wt = word_tokenize(h1)
count = 0
for word in wt:
    if word == "shubham":
        count+=1
    else:
        pass
print(count)