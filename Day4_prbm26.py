#prime or not
a=int(input())
r=a**0.5
count=0
if a==1:
 print("not a prime number")
for i in range(2,int(r+1)):
    if a%1==0:
        count=1
        break
if count==0:
    print("prime")
else:
    print("not a prime number" )
    