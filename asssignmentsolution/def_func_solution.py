### write a program to print area and perimeter of program
''''
def rect_area_perimeter(x,y):
    a = x*y
    p = 2*(x+y)
    return(a,p)
a1,p1 = eval(input("Enter lenght,width"))
area,perimeter = rect_area_perimeter(a1,p1)
print("Area of rectangle is:",area)
print("Perimeter of rectangle is :",perimeter)
'''

###Write a program which has sum,sub,mul and division function with two parameters
'''

def cal(x,y):
    s = x+y
    sb = x-y
    ml=  x*y
    dv = x/y
    return(s,sb,ml,dv)
sum1,sub,mul,div = cal(10,2) 
print("sum is ",sum1,"subtraction is ",sub,"multiplication is ",mul,"division is ",div) 
'''
'''
###Write a program to print area of rectangle,area of circle  volume of sphere , perimeter
###of rectangle circumference of circle area of triangle with seperate function of in one program
import math
choice=int(input("Enter choice"))
def area_rectangle():
    l,b = eval(input("Enter lenght and breadth"))
    print("area of rectangle is " , l*b)
def area_circle():
    radius=eval(input("Enter radius"))
    print("Area of circle is " ,math.pi * radius *radius)
def vol_sphere():
    radius=eval(input("Enter radius"))
    print("Volume of sphere is ",4/3*math.pi*radius*radius*radius)
def per_rectangle():
    l,b=eval(input("Enter length and breadth"))
    print("Perimeter of rectangle is ", 2*(l+b))
def circum_circle():
    radius = eval(input("Enter radius"))
    print("Circumfernce of circle is ",2*math.pi*radius)
def area_triangle():
    b,h =eval(input("Enter base and height "))
    print("area of traingle is ",0.5*b*h)
    
if(choice==1):
    area_rectangle()
    
elif(choice==2):
    area_circle()
elif(choice==3):
    vol_sphere()
elif(choice==4):
    per_rectangle()
elif(choice==5):
    circum_circle()
elif(choice==6):
    area_triangle()

else:
    print("Enter correct choice")
    
'''    
'''
##write a program to print simple interest and compound interest for you should define two function in one program


def simple_int(x,y,z):
    si = (x*y*z)/100
    return si

def comp_int(x,y,z):
     ci = x * (pow((1 +y / 100), z)) 
     return ci

p,r,t= eval(input("Enter principal , rate and Time"))
simple_interest = simple_int(p,r,t)
compound_interest = comp_int(p,r,t)
print("Simple interest is " , simple_interest)
print("Compound interest is ",compound_interest)
'''
###Write s function to print number is divisible by 5 and 7 both or not

'''
def div5n7 (x):
    if(x%5==0 & x%7==0):
        return(x)
    else:
        print("the number is not divisible by 5 and 7")
num=int(input("Enter a number"))
divof5n7 = div5n7(num)
print("num is by divisib",num)        
''' 
'''
##Write a program to print table of  a number through function
def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
number = int(input("Enter a number "))
table(number)
'''
'''
###Write a program to print sum of even number from 1 to n

def sum_even(x,y):
    count = 0
    for i in range(x,y,1):
        if(i%2==0):
            count+=i

    return count
start = int(input("Enter a  Start"))
end = int(input("Enter limit"))
number = sum_even(start,end)
print("Sum of even number is ",number) 
####THE start and end is not calculated just the numbers between them are calculated
'''
'''
#wrtie a program with function print whether the number is even or odd or not

def even_odd(x):
    if(x%2==0):
        print("The num is even")
    else:
        print("The is odd")
num=int(input("Enter a number"))
even_odd(num)
'''

'''
# 9 Write a fun to accept number of subjects value through function, accept n subjects marks from user 
# calculate total and percentage and accordignly grade and print the same

n=int(input("Enter number of subjects"))
while(n>0):
    def sub_marks():
        for i in range(1,n+1):
            total=sum(n)
            per = (total/n*100)*100
            return total,per
per
if(per>80):
    print("A grade")
elif(per>70):
    print("B grade")
elif(per>60):
    print()
        
having problem with this program 
'''





'''

# 10 Create divide function which will have divisor and divident 2 params, 
# it should return quotient and remainder and print both, 
# by checking remainder print whether both numbers are divisible or not
import math
    
def divide():
    dividend = eval(input("Please enter the dividedend : "))
    divisor  = eval(input("Please enter the divisor: "))
    quotient = math.floor(dividend/divisor)
    remainder = dividend%divisor
    print("The division of",dividend,"and",divisor,"resulted in quotient of",quotient,"and remainder of",remainder)
    
    if(remainder == 0):
        print("Both numbers are divisible")
    else:
        print("Both numbers are not divisible")

divide()


'''








