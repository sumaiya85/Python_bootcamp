#5.1 
# using for loop print 1 to 100 numbers
for i in range(1,101):
   print(i,end=" ") 

#5.2
# using for loop append 1 to 100 numbers in an empty list
n=[]
for i in range(1,101):
    n.append(i)
print(n)

#5.3 
# sum of all the numbers in a list by using for loop
my_list=list(map(int,input().split()))
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
print(sum) 