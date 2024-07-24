#29
#print how many consonants are there in strings
vowel="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
count=0
cons=0
i="hello world"
inp=i.lower() # to avoid again checking for consonants
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in abc):
        cons+=1
print(cons)