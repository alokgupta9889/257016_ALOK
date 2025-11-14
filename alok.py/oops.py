# create class named as Reactangle 
# there is attributes in it length and width 
# there is method named as area which return area of reactangle 
# Get input from user for a and b 
# hint:
# area=length *width 
# return area 
# 1=float(input("Enter length:"))
# w=float(input("Enter width:"))

# area=Reactangle(1,w)

class Reactangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    

length  = float(input("Enter the length of the reactangle:"))
width = float(input("Enter the width of th reactangle:"))


rect = Reactangle(length, width)

print("Area of reactangle:", rect.area())


class Car:
    def __init__(self, brand ,color):
        self.brand = brand 
        self.color = color

    def drives(self):
        print(f"{self.color}{self.brand} is driving ")
    

car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")

car1.drive()
car2.drive()

