#you r given with a , separated natural numbers 1 to 10 print only even numbers
my_list=list(map(int,input().split(",")))
for i in range (1,len(my_list),2):
    print(my_list[i])

#7.2
#how many even numbers are there in the above qs
my_list=list(map(int,input().split(",")))
count=0
for i in range (1,len(my_list),2):
    count+=1
    print(count)
    
#7.3 you are given with a space separated integer list find no.of even elements 
#and no.of odd ele ments in a given list1
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)