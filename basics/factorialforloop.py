###
fact = 1
n=int(input("Enter a no"))
for i in range(1,n+1,1):
    fact = fact*i
print("The factorial of ",n,"is",fact)