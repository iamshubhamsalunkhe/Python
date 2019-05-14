# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:03:09 2019

@author: Shubham
"""

fname=input("Enter filename with extension")
try: 
    fobj=open(fname,"r")
    for i in fobj:
        print(i)
except:
    print("File not found or can not be opened",fname)
