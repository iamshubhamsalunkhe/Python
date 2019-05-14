# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:05:29 2019

@author: Shubham
"""

import nltk
import re
import numpy
import nltk.corpus


#creating bag of WORDS model

from sklearn.feature_extraction.text import CountVectorizer

all_sent =["Joe waited for the train,The train was late,Mary and Samantha took the bus,I looked for Mary and Samantha at the bus station,Mary and Samantha arrived at the bus station early but waited until noon for the bus"] 

def word_extraction(sentence):
    ignore = ["a","the","is"]
    words = re.sub("[^\w]","",sentence).split()
    print("words are :\n",words)
    cleaned_text=[w.lower for w in words if w not in ignore]
    print("cleaned text is ",cleaned_text)
    return cleaned_text
#word_extraction(all_sent)
    
def tokenize(sentences):
    words=[]
    for sentence in sentences:
        w=word_extraction(sentence)
        words.extend(w)
        words=sorted(list(set(words)))
        print("tokenize words are",words)
        return words
    
       
    
    
    
    
    
    
    
    
    
    
        