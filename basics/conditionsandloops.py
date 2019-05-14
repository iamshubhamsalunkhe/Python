# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:40:42 2019

@author: Shubham
"""
'''
#conditions and loops

a,b = eval(input("Enter two numbers"))

if a > b :
    print("a is greater " , a)
else :
    print("b is greater " , b)
    
'''
'''
#nested if

a,b,c = eval(input("Enter three numbers"))

if a > b :
    if a>c:
        print("a is greater " , a)
if b > a:
    if b>c:
        print("b is greater " , b)
if c>a :
    if c>b :
        print("c is greater ", c)
        
'''
'''
#elif

a,b,c = eval(input("Enter three numbers"))

if a>b and a>c :
    print("a is greater", a)
elif b>a and b>c :
    print("b is greater " , b)
else :
    print("c is greater " , c)

'''






















