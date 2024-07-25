#sinle inheritance
'''class Animal:
    def speak():
        return "animal is speaking"
class Dog(Animal):
    def Bark():
        return"bow..."
class puppy(Dog):

    obj1=Animal
    obj2=Dog
    print(obj2.speak())
    print(obj2.Bark())'''
   
#Write a code to demonstrate single,multiple and multi level
class Father:
    def Father_speak():
        return "father class"
class Mother:
    def Mother_speak():
        return "mother class"
class kid(Father,Mother):
    def kid_speak():
        return " Im kid im having properties"
obj1=kid
print(obj1.Father_speak())
print(obj1.Mother_speak())
print(obj1.kid_speak())


