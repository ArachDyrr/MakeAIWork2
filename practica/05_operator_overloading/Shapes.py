from abc import ABC, abstractmethod
import math


# Abstraction: Abstract Superclass
class Shape(ABC):
    # Constructor method with Arguments/Parameters
    def __init__(self, width, height=1, depth=0, density=1, colorArg="black"):
        # Attributes
        self.width = width
        self.height = height
        self.depth = depth
        self.area = self.width * self.height
        self.density = density

        if colorArg is not None:
            self.setColor(colorArg)

    def setColor(self, colorArg):
        self.color = colorArg

    def getArea(self):
        return self.area

    def getColor(self):
        return self.color

    def getMass(self):
        return self.mass

    def getSide(self):
        return side

    def getTop(self):
        return top

    def getFront(self):
        return front


# Constructor
# Starts with Double Underscore -> dunder methods
class Rectangle(Shape):
    # Indent
    # DocString to document the purpose
    """
    This class can be used to generate Rectangle Objects
    with arguments
    width and height
    """

    # Default arguments always last
    def __init__(self, widthArg, heightArg, colorArg="blue"):
        """_summary_"""
        # Attributes
        # Encapsulated in object
        self.width = widthArg
        self.height = heightArg
        self.area = round(self.width * self.height)
        self.color = colorArg


# Each class inherits from Rectangle
class Box(Shape):
    def __init__(self, widthArg, heightArg, depthArg):
        super().__init__(widthArg, heightArg, depthArg)
        self.top = round(self.width * self.height)
        self.front = round(self.width * self.width)
        self.side = round(self.height * self.depth)
        self.area = 2 * self.top + 2 * self.front + 2 * self.side
        self.contents = round(self.front * self.side * self.top)
        self.mass = self.density * self.contents




class Triangle(Shape):
    def __init__(self, widthArg, heightArg):
        super().__init__(widthArg, heightArg)
        self.area = self.width * self.height * 0.5

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#         self.area = self.base * self.height * 0.5

class Circle(Shape):
    def __init__(self, radiusArg):
        super().__init__(radiusArg)
        self.radius = radiusArg
        self.area = round((self.radius) * 0.5 * math.pi,2)
