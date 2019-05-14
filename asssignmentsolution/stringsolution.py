#SHUBHAM SALUNKHE 

#1.	Create first as string

first = "Shubham "
print("first name is ", first)

#2.	Create middle as string
middle = "Vilas "
print("middle name is",middle)

#3.	Create last as string
last = "Salunkhe"
print("last name is ",last)
#4.	Combine first, middle and last in name string
name = first + middle + last
print("full name is ",name)
#5.	Display First character of name string
firstchar = name[0]
print("firstchar is ",firstchar)

#6.	Display last character of name string by two methods (+ve and –ve indexing)
print("last three character by +ve indexing",name[19:22])
print("last three character by -ve indexing",name[-4:-1])
#7.	Display First three characters of name string
firstthreechar = name[1:4]
print("the first three character are ",firstthreechar)

#8.	Display 3rd to 6th character of the string name
thrdtosixth = name[3:7]
print("third to sixth character in string name is ",thrdtosixth)
#9.	Display last three characters of the string name by using negative indexing
print("negative indexing of last three character is ",name[-5:-1])
#10.	Display length of name string
lenstring = len(name)
print("length of string name is ",lenstring)
#11.	Display type of name string
typename = type(name)
print("the type of variable name is ", typename) 
#12.	Display id of name var
idname = id(name)
print("id of variable name is ",idname)
#13.	Display name string in small case
smallcasename = name.lower()
print("lower case of string name is ",smallcasename)
#14.	Display name string in upper case
uppercasename = name.upper()
print("upper case of string name is ",uppercasename)
#15.	Display name string in capital or proper or title case
capitalizename = name.capitalize()
print("captilizing string in proper returns ",capitalizename)
titlename = name.title()
print("returing string in title format returns ",titlename)
#16.	Repeat last string 5 times and store into new variable
replast5 = last*5
print("repeating last ",replast5)
#17.	Find length of new variable
replastlen = len(replast5)
print("length of variable replast5",replastlen)
#18.	Combine name and new into name1 var, Display name1
name1 = name+replast5
print("new variable is ", name1)
#19.	Replace last string word with abc in name1 var
replcelast = name1.replace("Salunkhe","abc")
print("after replacing new string word is ",replcelast)
#20.	Print index number of any character & print its index value

print("index of character is ",name1.index('a'))
#21.	Display occurrence of k character in name1
counta = name1.count('a')
print("occurence of character a is ",counta)
#22.	Split name string & display each splited value by List method
splitname =  name.split()
print("splitting string returns " , splitname)
#23.	Split name string by assigning three var & print each varaible
s,s2,s3 = name.split(' ')
print(s)
print(s2)
print(s3)
#24.	Create a string with leading blank spaces and trailing blank spaces
newvar = "   newvariable  "

#25.	Remove leading and trailing blank spaces of the string & print string (hint strip function)
print("removing blank spaces of string returns",newvar.strip())
#26.	Check whether name string is in upper case or not ( hint isupper)
print(name.isupper())
#27.	Check whether name string is in lower case or not ( hint islower)
print(name.islower())
#28.	Check whether name string is in proper case or not ( hint istitle)
print(name.istitle())
#29.	Join hello string to each character of last string ( hint join)
h= "hello" 
hellojoin= h.join(last)
print("joining hello to last string returns",hellojoin)
#30.	Display help of join function of string (hint help(str.capitalize))
print(help(str.capitalize))
#31.	Display All methods which can be used with string variable ( Hint on python prompt dir(name))
#>>>dir(name)