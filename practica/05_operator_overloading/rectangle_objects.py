# Constructor
# Starts with Double Underscore -> dunder methods
class Shape:
    # Indent
    # DocString to document the purpose
    """
    This class can be used to generate Rectangle Objects
    with arguments
    width and height
    """

    # Class variable / Static variable with a value for ALL objects
    color = "black"

    # Default arguments always last
    def __init__(self, widthArg, heightArg, depthArg=0, densityArg=1, colorArg="black"):
        """_summary_"""
        # Attributes
        # Encapsulated in object
        self.width = int(widthArg)
        self.height = int(heightArg)
        self.depth = int(depthArg)
        self.area = round(self.width * self.height)
        self.contents = round(self.width * self.height * self.depth)
        self.density = densityArg
        self.color = colorArg
        self.mass = round(self.contents * self.density)



    # Method
    def getArea(self):
        return self.area

    def getColor(self):
        return self.color

    def getContents(self):
        return self.contents

    def getMass(self):
        return self.mass

    def setColor (colorArg):
        pass



# ------------------------
class Rectangle(Shape):
    # Indent
    # DocString to document the purpose
    """
    This class can be used to generate Rectangle Objects
    with arguments
    width and height
    """
    def __init__(self, widthArg, heightArg):
        super().__init__(widthArg, heightArg, colorArg="black")
        self.area = round(self.width * self.height)

# class Rectangle(Shape):
#     # Indent
#     # DocString to document the purpose
#     """
#     This class can be used to generate Rectangle Objects
#     with arguments
#     width and height
#     """
#     def __init__(self, widthArg, heightArg, colorArg="black"):
#         super().__init__(widthArg, heightArg, colorArg)
#         self.area = round(self.width * self.height)
# ------------------------
# Each class inherits from Rectangle
class Box(Shape):
    """This class can be used to generate Box Objects
    with arguments
    width, height, depth and density. """
    def __init__(self, widthArg, heightArg, depthArg):
        super().__init__(widthArg, heightArg, depthArg, colorArg="black")
        self.mass = round(self.width * self.height * self.depth * self.density)
        self.top = round(self.width * self.height)
        self.front = round(self.width * self.depth)
        self.side = round(self.height * self.depth)
        self.area = 2 * self.top + 2 * self.front + 2 * self.side



class Triangle(Shape):
    """
    This class can be used to generate Triangle Objects
    with arguments
    width and height
    """
    def __init__(self, widthArg, heightArg):
        super().__init__(widthArg, heightArg, colorArg="black")
        self.area = round(0.5 * self.width * self.height)



class Circle(Shape):
    def __init__(self):
        pass



