#in python polymorphism is not possible
#method over riding
class Animal:
    def Speak():
        return " speaking......"
class Dog(Animal):
    def Speak():
        return " Dog is speaking....."
class puppy(Dog):
    def Speak():
        return " puppy is speaking....."
obj3=puppy
print(obj3.Speak())

#method overloading
class cal:
    def add(self,*args):
        #return sum(args)
        sum=0
        for i in args:
            sum+=i
            return(sum)
#take inputs
obj1=cal()
print(obj1.add(1,2,))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))
print(obj1.add(1,2,3,4,5))