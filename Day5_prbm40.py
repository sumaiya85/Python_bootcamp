#print lower triangular matrix
#print upper triangular matrix
#print rhombus
#print parallelogram
#    ***
#     ***
#        ***
#print number pyramid

#1
#lower triangular
for i in range(5):
    for j in range(5):
        if i==j or i<j:
            print("*",end=" ")
    print()

#Lower triangular(2)
for i in range(5):
    for j in range(5):
        if i==j or i>j:
            print("*",end=" ")
    print()

#2 upper triangular
for i in range(5):
    for j in range(5):
      if j >= i:
        print("*", end=" ")  
      else:
         print(" ", end=" ")
    print()

#3 Rhombus

n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
          print("*",end=" ")
    print() 
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(i,n-1):
          print("*",end=" ")
    print()

#4
n=int(input())   
for i in range(n+1):     
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(n):
          print("*",end=" ")
    print()

