#Basics
#print stmts used to give output
print("hello swec")
#by default python prints in new line
#printing formats:
#1.using print stmts
print("good morning")
#2.to print hello,name(for this we need to store the name)
var1="python"
print("good morning,var1")

#to take input values in the o/p
name=input("enter your name")
print("hello",name)


#to take input values in the o/p in next line
name=input("enter your name\n")
print("hello",name)

#format string(fstring):used to write multiple data type
name=input("name")
age=input("age")
print(f"hello{name} Im {age}years old")

#take user name,take marks of 3 subjects and print total marks
#and avg of marks
name=input()
s1=int(input())
s2=int(input())
s3=int(input())
print(f"your marks are{s1+s2+s3},and avg is{(s1+s2+s3)/300}")
