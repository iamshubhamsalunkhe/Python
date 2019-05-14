# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:47:16 2019

@author: Shubham
"""

#program for creating a series using series() function of pandas list
#importing a list

import pandas as pd

list1=[1,2,3,4,5]
#creating a series
myseries= pd.Series(list1,index=['a','b','c','d','e'])

print(myseries)
print(type(myseries))