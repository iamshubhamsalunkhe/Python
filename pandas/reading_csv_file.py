# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:12:38 2019

@author: Shubham
"""
'''
import pandas as pd 
df=pd.read_csv("job.csv")
print(df)
print(type(df))
'''
'''
import numpy as np
import pandas as pd 
df=pd.read_csv("job.csv",dtype={'income':np.float64})
print(df)
print(type(df))
'''
'''
import numpy as np 
import pandas as pd 
df=pd.read_csv("job.csv",names=['a','b','c','d'])
print(df)
print(type(df))
'''
'''
import numpy as np 
import pandas as pd 
df=pd.read_csv("job.csv",skiprows=1)
print(df)
print(type(df))
'''
    