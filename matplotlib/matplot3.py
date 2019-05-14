# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:41:52 2019

@author: Shubham
"""

import matplotlib.pyplot as plt
import matplotlib.style as s 

s.use ='ggplot'

x=[5,8,10]
y=[12,161,6]
x1=[6,9,11]
y1=[6,15,7]

plt.bar(x,y,color='g')
plt.bar(x1,y1,color='r',align='center')
plt.xlabel('x series')
plt.ylabel('y series')
plt.title('Simple line graph')
plt.grid(True,color='y')
plt.show()