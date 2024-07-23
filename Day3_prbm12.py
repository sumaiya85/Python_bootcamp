#write a program for minimum element
#12 23 36 44 45 57

my_list=list(map(int,input().split()))
mini=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
print(mini)
