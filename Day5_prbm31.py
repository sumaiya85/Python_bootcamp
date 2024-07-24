#31
#print the non repeating in a string orelse print uniquie characters in a string 

i=input()
inp=i.lower()
vowel="aeiou"
cons="bcdfghjklmnpqrstvwxyz"
ans=" "
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)