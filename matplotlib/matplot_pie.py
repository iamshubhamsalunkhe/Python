# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:01:05 2019

@author: Shubham
"""

import matplotlib.pyplot as plt

labels = 'FROGS' , 'HOGS' , 'DOGS' , 'LOGS'

sizes = [15,30,45,10]

explode=(0,0.1,0,0)

fig1 , ax1 = plt.subplots()

ax1.pie(sizes , explode = explode , labels=labels , autopct = '%1.1f%%',
        shadow=True,startangle=90)

ax1.axis('equal')
plt.show()

