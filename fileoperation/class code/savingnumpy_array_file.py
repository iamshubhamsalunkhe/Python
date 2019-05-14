# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:37:59 2019

@author: Shubham
"""
'''
import numpy as np
a=np.array([1,2,3,4])

np.save('outfile',a)
f=open("outfile.npy","r")
r=f.read()
print(r)
'''
'''
import numpy as np
a=np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b=np.load("outfile.npy")
print(b)
'''
'''
import numpy as np
a=np.array([1,2,3,4,5])
np.save('outfile',a)
b=np.load("outfile.npy")
print(b)

'''



































