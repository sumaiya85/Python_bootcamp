#find the maximum element in a given list 
#test case:0
#12 23 36 44 45 57
my_list=list(map(int,input().split()))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)
