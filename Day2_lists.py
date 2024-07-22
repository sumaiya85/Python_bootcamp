my_list=[1,2,3,4]#declaration of list,static declaration
print(my_list)

my_list=[1,2,3,4]#without brackets and ,
print(*my_list)

my_list.append(9999)#append
print(my_list)

my_list.insert(0,999)#insert
print(my_list)
my_list.insert(15,90)
print(my_list)

print(len(my_list))#length
my_list=[5,6,7,55,324,11,4,]

my_list.pop(3)#pop it will default pop the last element
print(*my_list)

my_list_2=[5,6,7,8]#concatination
new_list=my_list+my_list_2
print(*new_list)

cnt=my_list.count(6)#count
print(cnt)

my_list=[-12,-3,5,1,2,3,50,25]#sorting ascending order
my_list.sort()
print(*my_list)

#to take dynamic input
my_list=list(map(int,input().split()))
print(*my_list)


