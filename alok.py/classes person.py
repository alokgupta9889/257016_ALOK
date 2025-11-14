class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is {self.name} and i am {self.age} years old.")
result=person("rachit", 23)
result.greet()