# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:24:42 2019

@author: Shubham
"""


'''
#create a two dimensional array with two rows four columns as x
import numpy as np
x=np.reshape(np.arange(8),(2,4))
print(x)

##type of array
print("type of array is ",type(x))
print("type of array is ",x.__class__)

#dimension of array
print("Dimension of array is ",x.ndim)

#size of array and in terms rows and columns
print("size of array",x.shape) 

#display datatype of 2d array created
print("datatype of 2d array is ",x.dtype)

#append 4 zeros row wise and store it in n1
#n1=np.zeros(x)
#print(n1)
n1 = np.append(x,[[0,0,0,0]],axis = 0)
print(n1)
#Create a matrix of zeros with 5 rows and 5 columns
n2=np.zeros((5,5))
print(n2)

#Concatenate n1 and n2 to n3 and display n3

n3 = np.append(n1,x,axis = 0)
n3
##rows and columns of both arrays should be same for concatenation


#Create array of 50 elements with values from 0 to 49 and reshape it into rows and cols
c=np.arange(50).reshape(5,10)
print(c)

#Replace 7 to 11 element of array to 15

c[0,6:10]=15
print(c)
'''
'''
#Create a array a1 of 3 rows with 5 elements in each row
import numpy as np

a1=np.arange(15).reshape(3,5)
print(a1)


#Display 3rd row

print(a1[2])
print("The numpy array created is ",a1)
print("The type of a1 is ",type(a1))
print("Dimension of array a1 is ",a1.ndim)
print("number of rows and cols of a1 is ",a1.shape)
print("Data within a1 is ",a1.dtype)
print("printing 1st and 2nd column of a1",a1[:,0:2])
print("printing last three cols of a1 ",a1[:,2:])
print("printing first two element from first row are ",a1[0:1,0:2])
print("printing first column ",a1[:,0])
print("printing 3rd column ",a1[:,2])
print("first and second row with two column",a1[0:2,0:2])
print("transpose of array matrix is\n",a1.T)
arr = np.random.randn(6,3)+9
print("Random array created is\n",arr)
prod=np.dot(arr.T,arr)
print("prod\n",prod)
sq1 = np.sqrt(a1)
print("square root of matrix a1 is ",sq1)
ex = np.exp(a1)
print("exponential of matrix a1 is ",ex)
sm = np.sum(a1)
print("sum of matrix a1 is ",sm)
sd = np.std(a1)
print("standard deviation of matrix is ",sd)
mn=np.mean(a1)
print("mean of matrix a1 is ",mn)
ab=np.abs(arr)
print("absolute of matrix a1 is ",ab)
squ=np.square(a1)
print("square of each element is ",squ)
lg=np.log(a1)
print("log of matrix a1 is ",lg)
sn=np.sin(a1)
print("sin of matrix a1 is ",sn)
lg10=np.log10(a1)
print("log10 of matrix a1 is ",lg10)
mx=np.max(a1)
print("max of a1 is ",mx)


'''
'''

import numpy as np
x=np.arange(8).reshape(2,4)
x1=np.arange(8).reshape(2,4)
data=[9,10,11,12,13,14,15,16]
x2=np.array(data)
print("/nx matrix is /n",x)
print("/nx1 atrix is /n",x1)
print("/nx2 matrix is /n",x2)
add1 = np.add(x,x1)
print("/n",x,"+",x1,"=/n",add1)

print("/nx matrix is /n",x)
print("/nx1 matrix is /n",x1)
sub1=np.subtract(x,x1)
print("/n",x,"-",x1,"=/n",sub1)


print("/nx matrix is /n",x)
print("/nx1 matrix is /n",x1)
mul1=np.multiply(x,x1)
print("/n")


##


'''

































































































































































