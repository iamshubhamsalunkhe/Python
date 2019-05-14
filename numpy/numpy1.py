# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:09:59 2019

@author: Shubham
"""




import numpy as np
data1 = [[1,2,3,4],[5,6,7,8]]
print("data1 =",data1)
print("the data type of data is ",type(data1))
a=np.array(data1)
print("NP array is",a)
print("The data type of np array a is ",type(a))
print("The data type of data1 is ",data1.__class__)
print("The data type of numpy a is ",a.__class__)
print("Dimension of numpy array ",a.ndim)
print("number of cols and rows  ",a.shape)
print("data type of data of np array is ",a.dtype)

a1=np.arange(15).reshape(3,5)
print("The numpy array created is ",a1)
print("the type of a1 is ",type(a1))
print("Dimension os array a1 is",a1.ndim)
print("number of rows and cols in a1",a1.shape)
print("Data within a1 is",a1.dtype)
z=np.zeros((3,6))
print("the 3x6 matrix filled with zeros created aas z",z)
print("first row is ",a[0])
print("secod row is",a[1])
print("the second row  is onwards",a1[1:])


'''
#single dimension array

import numpy as np
a = np.arange(10)
print("Single dimension array created by numpy as a",a)
print(a.ndim)
print("First element of a",a[0])
print("Last element of a is ",a[9])
print("First three element",a[0:3])
print("last three element ",a[4:8])
print("display all the element from 3rd element onwards",a[2:])
print("dispaly all element from start to end ",a[:])
print("last three element ",a[-3:])
a[2:5]=15
print("updated np arrray is ",a)

'''









