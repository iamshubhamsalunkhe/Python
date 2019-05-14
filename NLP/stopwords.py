# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:33:08 2019

@author: Shubham
"""
newlist=[]
from nltk.corpus import stopwords 
en_stops = set(stopwords.words('english'))

all_words = ['There','is','a','tree','near','the','river']

for word in all_words:
    if word not in en_stops:
        newlist.append(word)
        print(word)
print(newlist)  