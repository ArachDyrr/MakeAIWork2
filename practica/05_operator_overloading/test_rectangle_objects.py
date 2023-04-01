#!/usr/bin/env python

from rectangle_objects import Box, Circle, Rectangle, Triangle

rectangle = Rectangle(4, 5)
area = rectangle.getArea()
print(f"The color of rectangle is {rectangle.getColor()}")
print(f"The area of the rectangle is : {rectangle.getArea()}")

rectangleForStephan = Rectangle(10, 12, "red")
print(f"The color of rectangle for Stephan is {rectangleForStephan.getColor()}")

box = Box(4, 4, 2)
area = box.getArea()
print(f"The area of the box is : {area}")

box_area = box.getArea()
box_mass = box.getMass()
print(f"The area of the box is : {box_area} dm its mass is : {box_mass} kg.")

triangle = Triangle(4, 4, "red")
triangle_area = triangle.getArea()
triangle_color = triangle.getColor()
print(f"The area of the triangle is : {area} Its color is {triangle_color}")

circle = Circle(10)
circle_area = circle.getArea()
circle_color = circle.setColor("Green")
print(f"The area of the triangle is : {area} Its color is {circle_color}")


