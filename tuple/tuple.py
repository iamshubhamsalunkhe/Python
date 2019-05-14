my_tuple = ()
print(type(my_tuple))
m=(1,2,3,4)
print(type(m))
print(m)
m1=(1,2,7.8,9.8,'kk','pp')
print(type(m1))
print(m1)
m2=("mouse",[8,4,6],(1,2,3))
print(m2)
a,b,c = m2
print(a)
print(b)
print(c)
t=2,3
print(type(t))
print(t)
m3=m+m1
print(m3)
print(m)
print(m[-1])
print(m[1:3])
print(m2[0][2])
print(m2[0][2:])
print(m2[1][1])
print(m2[2][1:3])
l=[1,2,3,'pp',78.9]
t2=tuple(l)
print(t2)
for i in t2:
    print(i)
print(l in t2)
print(t2)
print(t2.count(2))
print(sum(m))
print(min(m))
print(max(m))
print(len(m))
t=(5,6,3,8)
print(sorted(t))
t1 = t*2
print(t1)
s












