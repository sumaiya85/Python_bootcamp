#given an space separated integer list find the avg of  even elements present in the given index
my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list)
for i in range(n):
     if(i%2==0):
      sum+=my_list[i] 
      count+=1
print(sum/count)