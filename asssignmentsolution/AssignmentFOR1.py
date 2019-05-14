#1.	Write a python program to accept n different numbers from user & print following data
#a.	sum of even numbers from n different nos
#b.	sum of odd numbers from n different nos
#c.	sum of numbers which are divisible by 3 from n different numbers
#d.	sum of numbers which are divisible by 5 and 7 both
#e.	count how many are even numbers
#f.	count how many are odd numbers
#g.	count how many are positive numbers
#h.	count how many are negative numbers
#i.	count how many are zeros

sum = 0
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
        sumeven += n
    else:
        sumodd += n
print("the sum of even",x,"is",sumeven)
print("the sum of odd",x,"is",sumodd)
    
    if(n%3==0):
        sum+=n
    elif(n%5==0 and n%7==0):
        sum+=n
    else:
        print("the no are not divisible by 3,5,7")

    for  i in n:
        if(n%2==0):
            count_even+=1

        else:
        count_odd+=1
print("count of even number is ",count_even)
print("count of odd number is ",count_odd)
    
    for i in n :
        if(n>=0):
            count_pos+=1
        else:
            count_neg+=1
print("count of postive no is ",count_pos)
print("count of negative no is ",count_neg)


     for i in n:
         if(n==0):
             count_zero+=1
     print("count of number zero is",count_zero)
    
          else:
              print("there is no zero number is entered")









