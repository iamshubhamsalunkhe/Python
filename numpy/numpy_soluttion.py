# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:41:43 2019

@author: Shubham
"""

import numpy as np


x1=[4,2,1]

x2=[2,2,2]


print("/nx1=/n",x1)
print("/nx2=/n",x2)
result=np.greater_equal(x1,x2)
print("/nResult of greater_equal is:/n",result)

print("/nx1=/n",x1)
print("/nx2=/n",x2)
result=np.greater(x1,x2)
print("/n Result of greater is :/n",result)


a1=True,False,True,False
a2=True,True,False,False
a3=np.logical_and(a1,a2)
print("/n Result of logical and is: /n",a3)



a1=True,False,True,False
a2=True,True,False,False
a3=np.logical_and(a1,a2)
print("/n Result of logical and is: /n",a3)

a1=True,False,True,False
a2=True,True,False,False
a3=np.less(a1,a2)
print("/n Result of logical and is: /n",a3)

a1=True,False,True,False
a2=True,True,False,False
a3=np.less_equal(a1,a2)
print("/n Result of logical and is: /n",a3)


a1=True,False,True,False
a2=True,True,False,False
a3=np.not_equal(a1,a2)
print("/n Result of logical and is: /n",a3)


a1=True,False,True,False
a2=True,True,False,False
a3=np.logical_or(a1,a2)
print("/n Result of logical and is: /n",a3)

a1=True,False,True,False
a2=True,True,False,False
a3=np.logical_xor(a1,a2)
print("/n Result of logical and is: /n",a3)


















