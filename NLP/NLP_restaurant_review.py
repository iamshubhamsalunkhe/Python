# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:49:04 2019

@author: Shubham
"""

import re
from nltk.tokenize import word_tokenize,sent_tokenize
import pandas as pd
import numpy as np 

dataset = pd.read_csv("C:/Users/Shubham/Desktop/pythoncodes/datasets/restaurant_reviews.tsv",delimiter='\t')
#ts=word_tokenize(dataset)
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]', " ",dataset['Review'][i])
    review=review.lower()
#print("data type",type(ts))
print(review)

#print(ts)
 


