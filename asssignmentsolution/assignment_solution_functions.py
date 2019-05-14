

## program 1
'''
def display_str(str):
    print("string is " ,str)
    
    
def lenght_func(str):
    count=0
    for letter in str:
        if letter != ' ':
            count=count+1
    return count
def concate_str(x,y):
    if type(x)!=str and type(y)!=str:
        print("Enter string to concatnate")
    else:
        return x+y
def reverse_str(str):
    return str[::-1]


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
        
        
def _func(str):
    count=0
    for letter in str:
        if letter == '_':
            count=count+1
    return count

def uppercase_func(str):
    return str.upper()



def input_func():
    choice = int(input("-1 for str display, -2 for length str,-3 to concatenate str,-4 to reverse,-5 vowel count,-6 for '_'count ,-7 for uppercase of string"))
    string = input("Enter string ")
    if choice==1:
        display_str(string)
    elif choice==2:
        print("lenght of string is",lenght_func(string))
    elif choice==3:
        string2=input("Enter a another string")
        print("Concatenation of two strings is ",concate_str(string,string2))
    elif choice==4:
        print("reverse of string is ",reverse_str(string))
    elif choice==5:
        vowel_func(string)
    elif choice==6:
        print("underscore count is ",_func(string))
    elif choice==7:
        print("uppercase of string is ",uppercase_func(string))

cont="yes"
while(cont=="yes"):
    input_func()
    cont=input("Do you wish to continue : yes/no")
print("thanks")
'''
'''
#program 2


def digi_count_display_digi(x):
    print("digit is ", x)
    count1 = 0
    while (x > 0):
        x = x //10
        count1 += 1
    print ("Total number of digits : ",count1)
    
    
    
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
        
def armstrong_func(num):
    sum = 0

# find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

# display the result
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

def input_func():
    choice=int(input("-1 for digi_count&display,-2 for reverse,-3 for palindrome,-4 armstrong number"))
    number=int(input("Enter a  number"))
    if choice==1:
        digi_count_display_digi(number)
    elif choice==2:
        print("The reverse of number is ",reverse_func(number))
    elif choice==3:
        palindrome_func(number)
    elif choice==4:
        armstrong_func(number)
    else:
        print("Enter correct choice ")
cont="yes"
while(cont=="yes"):
    input_func()
    cont=input("Do you wish to continue : yes/no")
print("thanks")
'''
'''
import cmath
def quadratic_func(x,y,z):
    d = (y**2) - (4*x*z)
    sol1 = (-y-cmath.sqrt(d))/(2*x)   ## cmath library is used i have tried it on math library but math domain error 
    sol2 = (-y+cmath.sqrt(d))/(2*x)  ##this code is referenced from internet
    return sol1,sol2
qaudratic = quadratic_func(5,4,3)
print("roots of quadratic  function is",qaudratic)
        
'''








