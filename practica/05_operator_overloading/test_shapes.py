#!/usr/bin/env python

from Shapes import Box, Circle, Rectangle, Triangle

rectangle = Rectangle(4, 5, "red")
print(f"The color of rectangle is {rectangle.getColor()}")
print(f"The area of the rectangle is : {rectangle.getArea()}")

box = Box(4, 4, 2)
area = box.getArea()
mass = box.getMass()
print(f"The area of the box is : {area}")
print(f"The color of the box is {box.getColor()}")
print(f'The mass of the box is {mass}')


triangle = Triangle(5, 6)
print(f"The area of the triangle is : {triangle.getArea()}")

circle = Circle(10)
circle.getArea()
circle.setColor("Green")
print(f"The area of the circle is : {circle.getArea()}")
print(f"The color of the triangle is {circle.getColor()}")
