class Animal: # Parent class (super class)
   location ="India"
   def __init__(self , name):
      self.name= name
   def speak (self):
      print("Speaking now.....") 
class Dog(Animal):  #This is how inheritance is done in Python
   def speak(self):
      super().speak()# We are using the speack funcction of the parent class
      print("Woof")
# a =  Animal("Meggie")
# a.speak()

d =Dog("dog")
d.speak()
# print(d.location)