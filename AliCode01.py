# Program to calculate area of circle.square and traingle
import math
#circle ka area
def area_circle(radius):
    return math.pi * radius * radius
#Square ka area
def area_square(side):
    return side * side
#Traingle ka area
def area_traingle(base, height):
    return 0.5 * base * height
#========User Input========
r = float(input("Enter radius of circle: "))
s = float(input("Enter side of square: "))
b = float(input("Enter base of traingle: "))
h = float(input("Enter height of traingle: "))
#=======calculation======
circle_area = area_circle(r)
square_area = area_square(s)
traingle_area = area_traingle(b, h)
#=======Output=======
print("Area of cirlce is:",circle_area)
print("Area of square is:",square_area)
print("Area of traingle is:",traingle_area)



