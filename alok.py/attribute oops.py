#Class
class car:
    def __init__(self, brand ,color):
        self.brand = brand #attribute
        self.color = color #attribute

    def drive(self): #method
        print(f"{self.color} {self.brand} is driving 🚗")
    
#object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
car1=car("BMW","Black")
car2=car("Tesla","White")

car1.drive()
car2.drive()


