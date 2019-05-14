# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:16:52 2019

@author: Shubham
"""

from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

print(len(stopWords))

print(stopWords)