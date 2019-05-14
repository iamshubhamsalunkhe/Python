#
'''
sum = 0
for i in range(1,11,1):
    n= int(input("Enter a number"))
    sum = sum+n
print("the sum 0f 10 digit number is ",sum)
'''

'''
sum = 0
for i in range(1,11,1):
    n= int(input("Enter %d number" %i))
    sum = sum+n
print("the sum 0f 10 digit number is ",sum)
'''
'''
sum = 0
n=int(input("Enter how many no you want:"))
for i in range(1,n+1,1):
    x= int(input("Enter a numer"))
    sum = sum+x
print("the sum ",n ," digit number is ",sum)
'''
'''
#sum of even no entered by user

sumeven = 0
x =int(input("Enter how many nos you want"))
for i in range(1,x+1,1):
    n=int(input("Enter a no"))
    if(n%2==0):
        sumeven = sumeven+n
print("The Sum of ",x,"no is" , sumeven)

'''
'''
##odd and even

sumeven=0
sumodd =0
x=int(input("Enter how many no want"))

for i in range(1,x+1,1):
    n=int(input("ENter a no"))
    if(n%2==0):
        sumeven=sumeven+n
    else:
        sumodd=sumodd+n

print("sum of even",x,"is ",sumeven)
print("sum of odd",x,"is",sumodd)

'''












































