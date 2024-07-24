#28
#check how many vowels are there in a string

check=['a','e','i','o','u']
count=0
i="hello world"
inp=i.lower() # to avoid again checking for consonants
for i in inp:
    if(i in check):
        count+=1
print(count)



