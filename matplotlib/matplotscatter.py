# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:57:07 2019

@author: Shubham
"""

import matplotlib.pyplot as plt
import matplotlib.style as s 



x=[5,8,10]
y=[12,161,6]
x1=[6,9,11]
y1=[6,15,7]
plt.scatter(x,y,color='g')
plt.scatter(x1,y1,color='r')
plt.xlabel('x series')
plt.ylabel('y series')

plt.title('Simple line graph')
plt.grid(True,color='y')
plt.show()