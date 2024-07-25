 #creation of a class
class Myclass:
    def add(a,b):
        return a+b

obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.add(12,5))

#
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b): 
        return a%b

obj1=Myclass
print(obj1.add(2,5))
print(obj1.sub(2,5))
print(obj1.mul(2,5))
print(obj1.mod(2,5))
print(obj1.div(2,5))
