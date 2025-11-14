class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal): # Dog inherits Animal
    def speak(sellf):
        print("Dog barks 🦮")

dog = Dog()
dog.speak()



class Cat:
    def sound(self):
        return "meow 🐈" 
        
class Dog:
    def sound(self):
        return "Woof 🐶"
    
    #polymorphism in action
for animal in [Cat(),Dog()]:
     print(animal.sound())
 