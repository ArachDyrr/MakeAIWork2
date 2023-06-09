# let's create a button class

# -----------------------------------------------------------------------
from Shape import Shape


# -----------------------------------------------------------------------


class Button:

    def __init__(self, bg_color, txt):  # __init__ is a constructor.

        self.backgroundColor = bg_color
        self.text = txt

        self.shape = Shape()

    def click(self):
        print(f"Button {self.text}")


# -----------------------------------------------------------------------
# Create a button
btn1 = Button(0, "Black")

btn1.shape.width = 100
btn1.shape.height = 100

# Add another
btn2 = Button(255, "White")

btn2.shape.width = 100
btn2.shape.height = 100

btn1.click()
btn2.click()

print("")
# -----------------------------------------------------------------------


#     def shape (shape):
#         pass
#
#     def backgroundColor(self):
#         pass
#
#     def text (self):
#         pass
#
#     def click (self):
#         pass
#
