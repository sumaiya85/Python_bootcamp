
#9
#find the  element present in k+n index
#k is given by user k=3 &  n=2 the input parameters are
#3 6 8 4 61 2 output:2
#k=3 & n=4
#80 70 54 36 72 op:error

my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
for i in range(0,len(my_list)):
        print(my_list[k+n])
        break
if k+n > len(my_list):
       print("Error")
