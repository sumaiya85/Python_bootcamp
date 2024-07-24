#30
#print all the vowels followed by consonants
i=input()
inp=i.lower()
vowel="aeiou"
conso="bcdfghjklmnpqrstvwxyz"
ans=" "
for i in inp:
    if(i in vowel):
      ans+=i
for i in inp:
    if(i in conso):
        ans+=i
print(ans)
        