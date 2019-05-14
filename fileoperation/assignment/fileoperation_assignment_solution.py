# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:24:34 2019

@author: Shubham
"""
'''
#define a function with filename as parameter to read contents contents of file line  by line

wobj = open("Shubham.txt","w")
print("name of file",wobj.name)
lines=["hello this is assignment file for file operations and creation","Hope you will understand it","Thank you"]
wobj.writelines(lines)
wobj.close()
def filename():
    fobj=open("Shubham.txt","r")
    t1=fobj.read()
    print("the readed line are ",t1)
    fobj.close()
filename()

'''
'''
def file_read():
    fobj=open("Shubham.txt","r")
    r1=fobj.read()
    print("the content of file is ",r1)
    
file_read()
'''
'''
# crete two files and append them

file1=open("f1.txt","w")
file1.write("this is file1 ")
file1.write("filename is f1 ")
file1.close()
file2=open("f2.txt","w")
file2.write("this is file2 ")
file2.write("filename is f2 ")
file2.write("f2 will be appended to f1 ")
file2.close()
robj=open("f2.txt","r")
data=robj.read()
robj.close()
aobj=open("f1.txt","a")
aobj.write(data)
aobj.close()
file1=open("f1.txt","r")
f=file1.read()
print("after appending f1 to f2 contents are",f)
'''
'''
#write python program to read the file content from file  and store into a list and print it from list 
# using for loop


fobj= open("Shubham.txt","r")
read = fobj.read()
for i in read:
    print(list(i))
fobj.close()
'''
'''
#write a program to read content line by line and store it into numpy array
import numpy as np

fobj= open("Shubham.txt","r").readlines()
lines = np.array([str(i) for i in fobj])
print(lines)
print(type(lines))
'''
'''
#write a program to count no of lines in file

fobj=open("Shubham.txt","r")
lines=len(fobj.readlines())
print("number of lines in file is ",lines)
fobj.close()
'''
'''
#count  of '-' in file 
count=0
fobj=open("Shubham.txt","r")
r = fobj.read()
for i in r:
    if i == "-":
        count+=1
    else:
        pass ## syntactically else required statement is required 
print("number of - in file is:",count)  ## pass is used for null operation   
fobj.close()
'''
'''
#copy one file to another file
f1= open("f1.txt")
f2=open("f2","a")
for i in f1.readlines():
    f2.write(i)
f1.close()
f2.close() 
f=open("f2.txt","r")
r=f.read()
print("after copying ",r)

'''


















 