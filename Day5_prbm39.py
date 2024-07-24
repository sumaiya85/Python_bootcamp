#patterns
#*****
#*****
#*****
#*****
#*****
#print square
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
    
#print only diagonal
for i in range(5):
    for j in range(5):
        if i==j:
            print("%",end=" ")
        else:
          print("*",end=" ")
    print()

#print upper triangular matrix
#print lower triangular matrix
#print rhombus
#print parallelogram
#    ***
#     ***
#        ***
#print number pyramid