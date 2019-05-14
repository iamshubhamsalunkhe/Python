# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:14:29 2019

@author: Shubham
"""

import pandas as pd

#creating a ddtaframe 

mydf1=pd.DataFrame([[1,2,3,4],[11,22,33,44]],columns=list('ABCD'))
print("The first data frame is :\n",mydf1)

mydf2=pd.DataFrame([[5,6,7,8],[55,66,77,88]],columns=list('ABCD'))

print("The second data frame is :\n",mydf2)
print("The dimension of the second dataframe is ",mydf2.shape)

mydf3=mydf1.append(mydf2)
print("The new data frame is :\n",mydf3)


print("the dimension of new dataframe is :",mydf3.shape)

mydf3["X"]=[100,200,300,400]

mydf3["Y"]=[500,600,700,800]

mydf3["Z"]=[444,555,666,777]

print("The new dataframe after adding three column is :\n",mydf3)

print("the size of new dataframe is:",mydf3.size)
#deleting single column
del mydf3['Z']
print(mydf3)
#for deleting multiple columns
mydf3=mydf3.drop(columns=['X','Y'])
print(mydf3)
#to drop rows index wise 
mydf3=mydf3.drop(index=[0])
print(mydf3)

mydf3=mydf3.drop()

#adding a new column

mydf3["new1"]=list(range(33,31,-1))
print("Final mydf3",mydf3)
print("mydf3",mydf3)


mydf3new=mydf3.copy()
print(mydf3new)
print(mydf3.info())
print(mydf3.describe())
print(mydf3.describe)










