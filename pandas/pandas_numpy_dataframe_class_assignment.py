# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:48:03 2019

@author: Shubham
"""

#create first dataframe with three rows and 3 columns contents are empno , name and salary by 

import numpy as np
import pandas as pd
empno=[102,120,285]
names=['xyz','abc','pqr']
salary=[20222,55525,54545]

mydict={'empno':empno,'names':names,'salary':salary}

edf=pd.DataFrame(mydict)
print(edf)
#2. Create second dataframe with three rows and 3 columns, contents are empno,name and salary
d={'empno':pd.Series([107,722,333]),'names':pd.Series(['asd','asf','kik']),'salary':pd.Series([20266,55215,12456])}
edf1=pd.DataFrame(d)
print(edf1)
#by passing data through series of dataframe
#3. Append data of second frame into first dataframe &amp; print First dataframe after updation.
edf=edf.append(edf1)
print(edf)

#4. Display dimension of dataframe
print("dimension of dataframe is :\n",edf.shape)
#5. Display size of Dataframe in terms of row and column
print("Size of dataframe is :\n",edf.size)

#6. Display data type of dataframe
print("data type of dataframe is :\n",type(edf),edf.dtypes)
#7. Append 4 columns to first data frame with some values &amp; Display dataframe after updation also
#display dimension also
edf['location']=['yst','iuu','loa','uaay','ayay','iaua']
edf['depart']=[1,2,3,5,8,7]
edf['des']=['lead','jr','sr','sr','m','am']
edf['jd']=[2003,2018,2010,2009,2008,2011]
print(edf)
#8. Create a even number series through pandas &amp; display series
even=pd.Series(2,4,5,6)
print(even)
#9. Create a matrix of ones with 5 rows and 5 columns and convert that into pandas dataframe &amp;
#display it
ones=np.repeat(1,25).reshape(5,5)
print(ones)
df1=pd.DataFrame(ones)
print(df1)
#10. Display empnames of all employees
edf['names']
#11. Display details of employee of name kiran
edf[edf['names']=='xyz']
#12. Display records with salary between 10,000 to 90,000
betwn=[np.logical_and]

#13. Display records of First five employees
#14. Display 3 rd row to 6 th row
#15. Display first row to 7 th row
#16. Display First two columns
#17. Print standard deviation of array dataframe
#18. Print sum of dataframe
#19. Print min value from dataframe
#20. Print max value from dataframe
#21. Print count of dataframe
#22. Describe dataframe with full summary information
#23. Create a four random arrays of 15 elements convert it into dataframe &amp; display it