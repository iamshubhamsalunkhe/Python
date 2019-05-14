##While loop


number = 0 
sum =  0

print("Enter numbers to add ; negative to end")

while True :
    number = eval(input("Enter a number :"))
    if number < 0 :
        break
    sum += number
print("The total is ",sum)