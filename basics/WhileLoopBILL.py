total = 0
choice = "yes"
while(choice=="yes"):
    rate = eval(input("Enter a rate :"))
    quantity = eval(input("Enter the quantity:"))
    total = (rate*quantity)+total
    choice=input("Wish to continue  - yes/no : ")
print("Your total Bill is",total)