# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:45:41 2019

@author: Shubham
"""
import numpy as np
#create combining arrays

x= np.random.random(10)
y= np.random.random(10)
z= np.random.random(10)

data = np.array(zip(x,y,z))
print("zip array x,y and z is",data)

#adding a new column
a=np.array([[1,2,3],[4,5,6]])
print("The array a is ",a)
z=np.zeros((2,1),dtype="int32")
print("the z matrix is\n",z)

a=np.append(a,z,axis=1)
print("\nThe array a after adding one column of zeros\n",a)

z1=np.zeros((2,2),dtype="int32")
print("\nthe z matrix of zeros of two columns is\n",z1)

a=np.append(a,z1,axis=1)
print("\nThe array a after adding two column of zeros\n",a)

z2=np.zeros((2,6),dtype="int32")
a=np.append(a,z2,axis=0)
print("\n The array a after adding two rows of zeros\n",a)









