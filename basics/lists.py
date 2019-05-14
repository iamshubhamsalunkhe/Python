m = ['w','e','l','c','o','m','e']
n=['happy',['b','i','r','t','h','d','a','y']]
print("First element of list m",m[0])
print("Last element is ",m[-1])
print("First three elements are",m[0:3])
print("last four element",m[3:8])
print("Element from 2nd to 5th are",m[1:5])
print("7th element is ",m[6])
print("app from nested list",n[0][1:4])
print("print birth",n[1][0:5])
print("print day from nested list",)

t = ['a','b','c','d']
item = t.pop(1)
print("The element which is poped",item)
print("list after deletion",t)

t.remove('a')
print("First element is removed with remove method")
print("list after deletion is:",t)
t1 =['a','b','c','d','e','f']
del t1[0]
print("list t1 after deleting first element ", t1)
del t1[2:5]
print("List t1 after deleting 3rd , 4th  and 5th element ", t1)
t1.remove(t1[0])
print(t1)
t1.clear()
print(t1)

t1 = ['a','b','c','d','e','f']
print("Length of list is :",len(t1))
a=[1,2,3]
b=[4,5,6]
c=a+b
print("List",c)
d=a*3
print(d)
d1=['a','b','c','d']*2
print(d1)
print('a' in t1)
print('a' not in t1)
for i in [1,2,3,4]:
    print(i)
for i in t1:
    print(i)

##append
d1.append('e')    
print(d1)

t1.append('p')
print("t1 after append is ", t1)

t1.append(9.0)
print("t1 after append is ", t1)


print(t1.index('b'))

t3=[1,2,3,4,5]
print("occurence of 2 in t3 list",t3.count(2))
print("orignal list of t3",t3)
print(t3)
print(t3.sort())
print(t3.reverse())
t4=sorted(t3)
print(t4)

newlist = t3.copy()
print("new list is ",newlist)
##copying returns reverse of orginal list
templist = list([1,2,3,4])
t=[5,6,7,8]
t.extend(templist) ##extend add multiple objects not like append which can add single object
print(t)
t.insert(5,9)
print(t)
del t[5]
print(t)
t5 = [1,2,3,4,5,6,7,8,9]
print(t5)
t5[2:5]=['a','b',89.9]
print(t5)
t5[4:4]=['x','y','z']
print(t5)






































