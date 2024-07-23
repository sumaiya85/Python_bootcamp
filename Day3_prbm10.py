#print the element in a particular index
#cyclic method
my_list=list(map(int,input().split()))
k=int(input())
len=len(my_list)
a=k%len
print(my_list[a])

