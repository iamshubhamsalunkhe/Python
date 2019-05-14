# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:36:43 2019

@author: Shubham
"""
'''
def square(x):
    if type(x)!= float and type(x)!=int:
        print("Invalid Input")
    else:
        return(x*x)
num = int(input("Enter a number"))
s = square(num)
print("The square of ",num ,"is",s)

'''

'''
def square(x):
    if type(x)!= float and type(x)!=int:
        print("invalid number")
    else:
        if(x<0):
            print("it is a negative num")
        else:
            return x*x
num = int(input("Enter a number"))
s = square(num)
print("The square of ",num ,"is",s)
'''

'''


def sqaure(x):
    s=x*x
    return s

def cube(x):
    square()
    c=s
    return s*x
'''
'''
def vowel_func(str):
    cw=0
    vowel_set=['a','e','i','o','u']
    for letter in str:
        if letter in vowel_set:
            print("This letter ",letter,"is a vowel")
            cw+=1
        else:
            print("This letter",letter,"is alphabet/constant")
        print("Number of vowel in ",str,"string is",cw)

def lenght_func(str):
    count=0
    for letter in str:
        if letter != ' ':
            count=count+1
    return count


def input_func():
    choice=int(input("Enter your choice- 1 for vowel , 2 for length of string"))
    mystring=input("Enter the string")
    if choice == 1:
        vowel_func(mystring)
    elif choice ==2:
        print("the length of the string is ",lenght_func(mystring))
    else:
        print("Not a valid choice")
        
cont="yes"
while(cont=="yes"):
    input_func()
    cont=input("Do you wish to continue : yes/no")
print("thanks")
        
'''

def reverse_func(num):
    reverse=0
    while num > 0:
        remainder = num%10
        reverse=(reverse*10)+remainder
        num = num//10
    return reverse

def palindrome_func(num):
    original = num
    rev =0
    while num!=0:
        rev=rev*10
        rev=rev+int(num%10)
        num=int(num/10)
    if original == rev :
        print("It is a palindrome")
    else:
        print("It is not palindrome")
        
def input_func():
    choice = int(input("Enter your choice -1 : reverse , 2 : palindrome :"))
    if choice == 1:
        x=int(input("Enter the number whose reverse is to  calculated:"))
        print("The reverse of the number is ",x,"is",reverse_func(x))
    elif choice ==2:
        x= int(input("enter the number for which you want to check if it is palindrome"))
        palindrome_func(x)
    else:
        print("Not a valid choice")
        
        
cont = "yes"
while(cont=="yes"):
    input_func()
    cont=input("Do you wish to continue yes/no")
print("Thanks")
    
    
    
    
    
    
    
    
        
        
        












        
        
        
        
        
        












    
    