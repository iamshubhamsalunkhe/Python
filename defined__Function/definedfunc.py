####defined function 

'''
def sum(x,y):  ##this are formal parameters 
    s=x+y
    return(s)
a=4
b=5
s=sum(a.b) ##this is actual paramters  
print(s)


def square(x):
    s = x*x
    return(s)
def cube(x):
    s = x*square(x) ##nested fuction should have return 
    print("the cube of ",x,"is",s)
cube(3)

def avg(x,y,z):
    a =(x+y+z)/3
    return(a)
a,b,c = eval(input("Enter three elements"))
s =avg(a,b,c)
print("Average of 3 numbers is " , s)


def sum(x,y,z):
    sum1 =x+y+z
    return(sum1)
a,b,c = eval(input("Enter three no "))
sum1=sum(a,b,c)
print("sum od 3 no is ",sum1)
'''
'''
def sumavg(x,y,z):
    s=x+y+z
    avg = s/3
    return s,avg
a,b,c = eval(input("Enter  three no"))
s1,a = sumavg(a,b,c)
print("the sum is",s1 )
print("avg of sum is ",a)
'''
'''
###Area of circle

import math

def area_circum(r):

    a =math.pi * r * r
    c = 2 * math.pi * r
    return (a,c)

radius = eval(input("Enter the radius "))
a1,c1=area_circum(radius)
print("area of circle is ",a1)
print("circum of circle is ",c1)

'''
'''

import math
def square():
    side = int(input("enter side of square"))
    print("The area of square is " , side*side)

def circle():
    rad = int(input("Enter the radius"))
    print("the are of circle is ", math.pi*rad*rad)
def rectangle():
    l,b = int(input("enter l and b"))
    print("area of rectangle is " , l*b)

def traingle():
    a,b,c=eval(input("enter sides of triangle "))
    
    

'''
'''
def even(x):
    if(x%2 == 0):
        print(x," is a even no")
    else:
        print(x," is a odd no")
n=int(input("ENter the no"))
even(n)

'''

'''

def fact(x):
    f=1
    for i in range(1,x+1,1):
        f=f*i
    return f
n =  int(input("ENter nummber for which u need to calculate factorail"))
f1 = fact(n)
print("the factorial of num is " , f1)

'''
















































