# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:58:45 2019

@author: Shubham
"""
import numpy as np 
import matplotlib.pyplot as plt
# using function to plot

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.figure(1)
# Subplot definition : subplot(nrows, ncols, index, **kwargs)
plt.subplot(311)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(312)
plt.plot(t2,f(t2),'r--')

plt.subplot(313)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()