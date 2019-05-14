# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:20:22 2019

@author: Shubham
"""

import pandas as pd


d={'Name':pd.Series(['abc','xyz','pqr','lkj']),'Age':pd.Series([23,44,23,32]),'Ratings':pd.Series([2,5,4,3])}
df=pd.DataFrame(d)
print(df)
print(df.dtypes)
print("Following is dataframe \n",df)
print(df.sum())
print("the meamn is ",df.mean())
print(df.max())
print(df.count())
