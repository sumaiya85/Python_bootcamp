#sort the elements first half ascending and second half #descending 



my_list=list(map(int,input().split()))
m=len(my_list)//2
a=my_list[:m]
b=my_list[m:]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]<b[j]:
            b[i],b[j]=b[j],b[i]
result=a+b
print(result)