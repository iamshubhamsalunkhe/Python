####
d1=dict()
print(d1)
print(type(d1))
d2={'name':'Shubham Salunkhe','age':21,'job':'Scientist'}
print(d2)
print(d2['name'])
my_dict = {'name':'John', 1: [2,4,3]}
print(my_dict)
print(my_dict[1])
print(my_dict['name'])
print(d2)
d2
d2['age']=24
print(d2)
d2['address']='koperkhairane'
print(d2)
for  k in d2.keys():
    print(k)
for i in d2.items():
    print(i)
    
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares.pop(3))
print(squares)
print(squares.popitem())
print(squares)


dict1 = {"rollno":39,"name":"Shubham"}
d2={"marks":600,"per":90}
dict1.update(d2)
print(dict1)
