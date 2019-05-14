# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:17:08 2019

@author: Shubham
"""

from nltk.tokenize import sent_tokenize , word_tokenize


data = "All work and no play makes jack dull boy . All work and no play."

ts= sent_tokenize(data)
print(type(ts))
print(ts)
print("first sent is :",ts[0])

for lines in ts :
    print(lines)