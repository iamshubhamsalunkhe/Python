# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:01:01 2019

@author: Shubham
"""
import numpy as np
import matplotlib.pyplot as plt

x,y=np.loadtxt('C:/Users/Shubham/Desktop/values.txt',unpack=True,delimiter=',')
plt.plot(x,y)
plt.xlabel("x series")
plt.ylabel("y series")
plt.title("simple graph")
plt.grid(True,color='y')
plt.show()