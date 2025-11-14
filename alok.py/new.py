import person

person.greet("Alok")

import random

print("Random number between 1-15:", random.randint(1, 15))
colors = ["yelow","black","orange","green"]
print("Random color:",random.choice(colors))

import datetime

today = datetime.date.today()
print("Today's date:",today)

now = datetime.datetime.now()
print("current time:",now)

import sys

print("python version:",sys.version)
print("platforms:", sys.platform)



# import math
# print("power of 2'3",pow(2,3))
# print("square root of 25:", math.sqrt(25))
# print("value of pi:", math.pi)
# print("floor of 4.8:", math.floor(4.8))
# print("ceil of 4.3:", math.ceil(4.3))

import math 
print("power of 5'6",pow(5,6))
print("square root of 625:", math.sqrt(625))
print("value of radian:", math.radians)
print("ceil of 6.6:", math.ceil(6.6))
print("floor of 5.5:", math.floor(5.5))


#Task
# create a function take random value using random module 
# check of the value is positive or negative and print it
# check if the value is divisible with 5 or not and print it
# check if the number is even or odd 

print("Enter any number:")
num=int(input())
if num>0:
    print("number is positive")
else:
    print("number is negative")


if num%5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")

    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
        
    

