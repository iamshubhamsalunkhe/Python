# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:56:29 2019

@author: Shubham
"""
'''
class Myclass:
    x=5
p1=Myclass()
print("p1 object value of x is :",p1.x)
print("the value of x instance varaible is ",p1.x)
p1.x=10
print("changed value of x for p1 is ",p1.x)
p2=Myclass()
print("p2 object x value is ",p2.x)
p2.x=15
print("changed value of x for p1 is ",p2.x)

'''
'''
class person:
    x=5
    y=6
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello how are you :",self.name)
    def sum(self,x,y):
        return(self.x+self.y)
    def sum1(self,x,y):
        self.x=x
        self.y=y
        return(self.x+self.y)
p1=person("abc","70")
print("name is ",p1.name)
print("age is ",p1.age)
p1.myfunc()
p2=person("xyz","40")
print("name is ",p2.name)
print("age is ",p2.age)
p2.myfunc()
s=p1.sum(3,4)
s1=p1.sum1(3,4)
print("the sum is ",s)
print("the sum of objects is",s1)
'''
'''
#write a python program class employee with empno,name,salary,
#accept details through paratmetried getdata() method
#provide calculate method to add 10% bonus to and update salary
#display all details through display method
#getdata(self,en,nm,sal)


class employee:
    def getdata(self,empno,name,salary):
        self.empno=empno
        self.name=name
        self.salary=salary
    def cal(self):
        self.salary+=self.salary*0.1
        
    def dispaly(self):
        print(self.empno)
        print(self.name)
        print(self.salary)

p1=employee()
p1.getdata(122,"abc",2000)
p1.cal()
p1.dispaly()
'''
'''
class message:
    def __init__(self,msg):
        self.msg=msg
    def sizemsg(self):
        print("size of message is ",len(self.msg))
    def dispmsg(self):
        print("Message entered at run time is ",self.msg)
m=message("hello")
m.sizemsg()
m.dispmsg()
'''
class Addition:
    def sum(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.s=self.x+self.y+self.z
        
        
        
#python does not support method overloading
        












