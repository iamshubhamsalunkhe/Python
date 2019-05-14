# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:34:52 2019

@author: Shubham
"""

import nltk
from nltk import RegexpParser
import textblob
from textblob import TextBlob


input_str ="Pickle refers to any type of pickled cucumber. Whereas a Gherkin is usually reserved for cucumbers between 1–3 inches in size. "

result =TextBlob(input_str)

print(result.tags)

reg_exp = "NP:{<DT>?<JJ>*<NN>}"
rp=nltk.RegexpParser(reg_exp)
result=rp.parse(result.tags)
print(result)