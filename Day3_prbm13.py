#13
#replace the elements in an array with average of maximum and minimum 
my_list=list(map(int,input().split()))
a=my_list[0]
b=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>a):
        a=my_list[i]
    elif(my_list[i]<b):
        b=my_list[i]
avg=(a+b)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)

