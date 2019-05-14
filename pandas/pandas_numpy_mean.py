# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:05:56 2019

@author: Shubham
"""

import pandas as pd
import numpy as np




df=pd.DataFrame(np.random.randn(5,3).reshape(5,3),columns={'col1','col2','col3a'})
print(df)
d=df.apply(np.mean)
print(d)