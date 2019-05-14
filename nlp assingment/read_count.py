# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:30:20 2019

@author: Shubham
"""

'''read csv file and tokenize it and count tokenize word'''
import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize

dataset = pd.read_csv('legends.csv',delimiter ='\t')
for i in range(0,1000):
    abct = re.sub("[^a-zA-Z]"," ",dataset["Review"][i])
print(abct)


