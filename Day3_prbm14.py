#14
# find the missing number in an array

n=list(map(int,input().split(" ")))
sum=0
for i in range(1,len(n)+2):
        sum+=i
a=0        
for j in n:
    a+=j
miss=sum-a  
print(miss)

