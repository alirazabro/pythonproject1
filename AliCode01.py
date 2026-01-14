# Program to calculate area of circle.square and rectangle
import math
def area_circle(radius):
    return math.pi * radius * radius
def area_square(side):
    return side * side
def area_rectangle(length, width):
    return length  * width
r = float(input("Enter radius of circle: "))
s = float(input("Enter side of square: "))
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

circle_area = area_circle(r)
square_area = area_square(s)
rectangle_area = area_rectangle(l,w)

print("Area of cirlce is:",circle_area)
print("Area of square is:",square_area)
print("Area of Rectangle:",rectangle_area)
