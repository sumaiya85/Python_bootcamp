#find lcm of 2 numbers

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while b!=0:
    a,b=b,a%b 
    
print("Lcm of 2 numbers is:",a)