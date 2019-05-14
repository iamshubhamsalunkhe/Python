#
'''
camels =42 
s = "I have spotted %d camels" %camels
print(s)
'''

c = 0 


m1,m2,m3,m4,m5 = eval(input("Enter 5 subjects marks"))
c=0
if(m1 < 40):
    c=c+1
if(m2 < 40):
    c+=1
if(m3 < 40):
    c=c+1
if(m4 < 40):
    c = c+1
if(m5 < 40):
    c+=1




tot = m1+m2+m3+m4+m5
per = tot/5

print("total marks are" , tot)
print("percentage is " , per)

if(c==0):
    if(per > 75):
    print("Distinction")
    if(per > 60 ) & (per<75):
    print("First  Class")
    if(per>50) & (per<60):
    print("Second Class")
    if(per>40)&(per<50):
    print("Pass")
    elif(c<=2):
    print("ATKT")
elif(per<40):
    print("Fail")






