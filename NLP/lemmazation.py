# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:14:14 2019

@author: Shubham
"""
'''Lemmatization usually refers to doing things properly 
with the use of a vocabulary and morphological analysis of words,
normally aiming to remove inflectional
endings only and to return the base or dictionary form of a word'''


'''
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
input_str = "been had done languages cities mice"
input_str = word_tokenize(input_str)
for word in input_str:
    print(lemmatizer.lemmatize(word))
'''

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
input_str = "been had done languages cities mice"
input_str = word_tokenize(input_str)
for word in input_str:
    print(stemmer.stem(word))