#19
# reverse of a number(important)
n=123
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))
