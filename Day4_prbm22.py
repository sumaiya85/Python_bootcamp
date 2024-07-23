#GCD of 2 numbers
#euclidean Algorithm
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while b!=0:
    a,b=b,a%b  #a=b & b=a%b
print("GCD of two numbers is:",a)