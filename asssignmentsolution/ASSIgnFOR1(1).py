##1
sum5nd7 =0
sum3 = 0
sumeven = 0
sumodd = 0
count_pos = 0
count_neg = 0
count_even = 0
count_odd = 0
count_zero = 0
x=eval(input("Enter how  many no you want"))
for i in range(1,x+1,1):
    n=eval(input("Enter a no"))
    if(n%2==0):
        sumeven+=n
        count_even+=1
    if(n%2!=0):
        sumodd+=n
        count_odd+=1    
    
    if(n%3==0):
        sum3+=1
    
    if(n%5==0 & n%7==0):
        sum5nd7+=1
    if(n==0):
        count_zero+=1
    if(n>=0):
        count_pos+=1
    else:
        count_neg+=1
    
print("sum of even no is ",sumeven)
print("count of even no is ",count_even)
print("sum of odd no is ",sumodd)
print("count of odd no is ",count_odd)
print("count of positive no",count_pos)
print("count of negative no",count_neg)
print("count of zero",count_zero)
print("sum  of no divisible by 3",sum3)
print("sum of no divisible by 5 and 7",sum5nd7)


####2
fact = 1
sum = 0
n = int(input("Enter a number: "))

for i in range(1,n+1,1):
    fact = fact * i
    print(fact)
    sum += fact   

print("The sum of factorial of",n,"numbers is",sum)


###3
chance = 1

while(chance < 4):
    n = int(input("Please enter the number: "))
    if(n > 0):
        square = n*n
        print("square of",n,"is",square)
        chance = 1
        break
    else:
        print("Please enter a positive number.")
        chance += 1
        if(chance == 4):
            print("no attempts left ")
        continue

####4

bal = 200000
widrw_amt = 0
dep_amt = 0

while(True):
    user_input = input("please enter b for balance check, w for withdraw, d for deposit: ")
    if(user_input == 'b' or user_input == 'B'):
        print("your account balance is:",bal)
    elif(user_input == 'w' or user_input == 'W'):
        widrw_amt= int(input("please enter anount you want to withdraw: "))
        if(bal >= widrw_amt):
            bal = bal - widrw_amt
            print("the updated balance is:",bal)
        else:
            print("insufficient funds. You have",bal,"in your account")
    elif(user_input == 'd' or user_input == 'D'):
        dep_amt = int(input("please enter the amount you want to deposit."))
        bal = bal + dep_amt
        print("the updated balance is:", bal)
    elif(user_input == 'cancel'):
        break
    else:
        print("please select the correct option.")



####Assignment on LIST

#1.	How to create list
list1 = ['v','e','c','t','o','r']
list2 = [1,2,3,4,5,6,7,8,9]
print(list(list2)) 
#2.	How to create empty list
emptylist = []
#3.	Indexing of List elements in forward way from left to right
print(list1[1:])

#4.	Indexing of List elements in reverse way from right to left
print(list1[:-1])
#5.	What is default traversing direction of List? Can we traverse list from right to left
print(list2.reverse())
#6.	How to access or display First element of List
print(list1[0])
#7.	 How to access or display Last element of List if List consist of 9 elements, Answer by two ways
print(list2[9:])
print(list2[:-1])
#8.	How to Nested list elements are accessed with two elements in a list , first element is nested list of 3 elements
nest_list = ["hello",["h","o","w","a","r","e"],["you"]]
print("nested list element",nest_list[1][0:4])
#9.	How to display third last element with negative indexing
list2[:-3]
#10.	Slice list to display 3rd,4th and 5th element from List
list3 = list2[3:6]
print(list3)
#11.	Display List elements from start to 6th
print(list2[0:7])
#12.	Display elements from 2nd element to end
print(list2[1:9])
#13.	Display all elements of the list from beginning to end by using :
print(list2[1:])
#14.	Create List as odd = [2, 4, 6, 8], replace first element as 1
odd_list =[2,4,6,8]
odd_list[0]=1
print(odd_list)
#15.	Replace element 2nd to 4th with [3,5,7]
odd_list[1:4]=[3,5,7]
print(odd_list)
#16.	Display total number of elements in odd list'
print(len(odd_list))
#17.	Display occurance of 3 in odd list
print(odd_list.count(3))
#18.	Display sum of all elements of odd list
print(sum(odd_list))
#19.	Display maximum element from List
print(max(odd_list))


# 20.	Display minimum element from List
min(list1)

# 21.	Delete 3rd element from List by specifying index number
list1.pop(2)
list1

# 22.	Delete 3rd element whose value is 40 by specifying value
l2 = [34,12,40,54,30]
l2.remove(40)
l2

# 23.	Delete elements from 3rd to 6th from the list
del list1[2:6]
list1

# 24.	Pop element from List
list1.pop(4)

# 25.	Pop 5th element from List
list1.pop(4)

# 26.	Sort list and do not update original one
l3 = sorted(l2)
l2
l3

# 27.	Sort list by updating original one
l2.sort()
l2

# 28.	Sort list in a reverse order
l2.sort()
l2
l2.reverse()
l2

# 30.	Clear whole list
l3.clear()
l3

# 31.	Create list a=[1,2,3] b=[4,5,6] and concatenate both & display new list
a=[1,2,3]
b=[4,5,6]

c = a+b
c

# 32.	Repeat list a 5 times and store in d
d = a*5
d

# 33.	Repeat only first two elements of List a 6 times and store in new
e = a[0:2]*6
e

# 34.	Check 30 is available in list a
if 30 in a:
    print("List a contains 30")
else:
    print("List a does not contain 30")

# 35.	Check 2 is not available in list a
if 2 in a:
    print("List a contains 2")
else:
    print("List a does not contain 2")
# 36.	Append 6 element in list a
a = a + [5,6,7,8,9,10]
a
# 37.	Append any decimal number to a list
a.append(11.4)
a

# 38.	Create a temp list of 5 elements and extend a list by adding temp list
temp = [1,2,3,4,5]
a = a + temp
a

# 39.	Display index number of any specified element
a[11]

# 40.	Copy list a to newlist
b = a.copy()
b

# 41.	Using for loop to traverse through list newlist and print all elements of the List on a single line separated by comma
for i in b:
    print(i, end = ',')

# 42.	Within a for loop only assign list and traverse and display each element of list on separated line
for i in b:
    print(i)

# 43.	Create a list of natural numbers from 1 to 50 by using inbuilt function
e = list(range(1,51,1))
e
e[11]

# 44.	Create List of even numbers from 2 to 40 by using inbuit function
even = list(range(2,40,2))
even

# 45.	Create list of numbers in descecending order with specified interval
reve = list(reversed(range(1,10,1)))
reve

# 46.	Creating a list from negative integers to positive integers of a number (Hint -5 to 5)
f = list(range(-5,5,1))
f

# 47.	Creating a list with equally spaced numbers
e = list(range(1,51,1))

# 48.	Print datatype of newlist
type(f)

# 49.	Insert 5th element in newlist as 90
f.insert(5,90)
f

# 50.	Write difference between del,pop & remove
# pop deletes a particular value using indexing
# remove deletes a particular value using actual value
# del is similar to pop except it can delete sequence of values using indexing

# 51.	Write difference between sorted and sort
# sort will update the list you are working on
# sorted will not update the list, instead we can create another list and put the sorted values of the current list in the new list without changing the current list.

# 52.	Write difference between sort and reverse
# sort will sort the list in ascending order
# reverse will reverse the sequence of values. for eg the last value will be first, secondlast will be second and so on.

















