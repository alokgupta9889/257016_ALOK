class person:
    def __init__(self, name ,age):
        self.name=name
        self.__age=age #Private attribute
    
p1 = person("Alok",20)
print(p1.name)
print(p1._person__age) #This will cause an error

