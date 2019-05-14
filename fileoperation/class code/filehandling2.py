# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:24:03 2019

@author: Shubham
"""

'''
import sys

f=input("Enter filename with extension which u want to open")
fr=open(f,"r")
print("opening  file",fr.name,"for reading")
for line in fr:
    sys.stdout.write(line)
fr.close()
print("\n File ",f,"sucessfully reading completed")
'''



'''
import sys
f = input("Enter filename with extenion which you want to open : ")
fr = open(f,"r")
print("Opening file",fr.name,"for reading")
line = fr.readline()
while(line != ""):
    sys.stdout.write(line)
    line = fr.readline()
fr.close()
print("\nFile",f,"successfully reading completed")

'''
'''
fr = open("job.txt","r")
print("opening file",fr.name,"for reading")
print("current position of file on following character",fr.tell())
line=fr.readline()
print("information ",line)
print("current position of file on following character",fr.tell())
for line in fr:
    print(line)
    name,job,income=line.split(",")
    last,first=name.split()
    income=int(income)
    income=income+1000
    print("firstname",first)
    print("lastaname",last)
    print("incremented income is ",income)
fr.close()    
'''
'''
#incrementing income and updating it 

fr = open("job.txt","r")
fw=open("job2.txt","w")
print("opening file",fr.name,"for reading")
print("current position of file on following character",fr.tell())
line=fr.readline()
print("information ",line)
fw.write(line+"\n")
fw.close()
print("current position of file on following character",fr.tell())
for line in fr:
    print(line)
    name,job,income=line.split(",")
    last,first=name.split()
    income=int(income)
    income=income+1000
    print("firstname",first)
    print("lastaname",last)
    
    print("incremented income is ",income)
    fw=open("job2.txt","a")
    s=name+","+job+","+str(income)+"\n"
    fw.write(s)
    print()
fr.close()    
fw.close()
fw=open("job2.txt","r")
r=fw.read()
print(r)


'''
'''
#count number of character in file and line in file


f=open("job.txt","r")
txt=f.read()
print("contents of job.txt are:\n",txt)
print("Number of characters in a file is ",len(txt))
fobj=open("job.txt","r")
count=0
for i in fobj :
    count+=1
print("number of lines in a file",count)
'''


























