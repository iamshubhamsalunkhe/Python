# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:53:25 2019

@author: Shubham
"""

import pandas as pd

#creating a ddtaframe 

mydf1=pd.DataFrame([[1,2,3,4],[11,22,33,44]],columns=list('ABCD'))
print("The first data frame is :\n",mydf1)

print("The dimension of the first data frame is ",mydf1.shape)

print("The size of the first data frame is :",mydf1.size)

print("The name of the columns are:",mydf1.keys())