#2. take input from user and check whether the given number is
# positive and even, positive and odd, negative and even, negative and odd

a=int(input())
if(a>=0 and a%2==0):
  print("positive even number")
elif(a>=0 and a%2!=0):
  print("positive odd number")
elif(a<0 and a%2==0):
  print("negative even number")
else:
  print("negative odd number")




