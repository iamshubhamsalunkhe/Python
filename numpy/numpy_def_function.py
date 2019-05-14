# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:11:32 2019

@author: Shubham
"""



'''
def funlist(list1):
    s=[]
    s=[i for i in list1 if (i%2)!=0]
    list1 = s
    print(list1)
l1=[1,2,3,4]
funlist(l1)
l2=[3,4,6,9]
funlist(l2)
 or
'''
'''
def funlist(list1):
    s=[]
    s=[i for i in list1 if (i%2)!=0]
    print("the list of add elements is ",s)
    print("First element of odd list is ",s[0])
    print("Second element of odd list is ",s[1])
l1=[1,2,3,4]
funlist(l1)
l2=[3,4,6,9]
funlist(l2)
'''
'''
def sumoddlist(list1):
    sumodd = 0
    for i in list1:
        if(i%2!=0):
            sumodd+=1
            
        else:
            return (0)

def sumevenlist(list1):
    sumeven = 0
    for i in list1:
        if(i%2==0):
            sumeven+=1
        else:
            return (0)
        
l1=[2,3,5,7]
sumoddlist(l1)
l2=[3,4,6,8,11]
sumevenlist(l2)       
'''
'''
def sum_odd_num(list1):
    s=[sum((i for i in list1 if i%2!=0),0)]
    return s
def sum_even_num(list1):
    s=[sum((i for i in list1 if i%2==0),0)]
    return s

mylist=[1,2,4,5,6,8,88,9,10]
print(sum_odd_num(mylist))
print(sum_even_num(mylist))
'''

import numpy as np
def funarray(arr):
    a=np.array([a for a in arr if np.mod(a,2)!=0])
    print("odd element array created from given list",a)
arr1=np.array([1,2,3,4])
funarray(arr1)













