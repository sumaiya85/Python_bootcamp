#1. person x goes to market, buy 10 apples , 2 dozen bananas & 8 oranges
# the cost of each apple is 15/-, 1 banana =  4/-, 1 orange = 5/-, 
# mother of X is mrs Y, she gave x 700/- to x. she said some amount will be left over with x
# if x is left with money then fruit vendor cannot fooled the kid

apple=int(input())
banana=int(input())
orange=int(input())
cost=apple*15+banana*4+orange*5
if(cost<700):
  print("x is not cheated")
else:
  print(" x is cheated")
