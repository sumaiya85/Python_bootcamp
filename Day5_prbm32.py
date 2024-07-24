#32
#inp:hello 123
#op:sum

str=input()
inp=str.lower()
vowel="aeiou"
cons="bcdfghjklmnpqrstvwxyz"
num="0123456789"
ans=0
for i in str:
    if(i in num):
        ans+=int(i)
print(ans) 