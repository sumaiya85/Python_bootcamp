#arithemetic operation
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)#removes the decimal
print(a**b)#power operator

#logical operators:
#and,or,not
age=int(input())
if(age>=18 and  age<24):
    print("allowed to drive only 2 wheeler")
elif(age>=24 and age<45):
    print("allowed for 2 and 4 wheeler")
else:
    print("all")

