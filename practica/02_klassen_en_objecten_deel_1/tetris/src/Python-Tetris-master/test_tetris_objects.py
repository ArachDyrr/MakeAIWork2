#!/usr/bin/env python

from tetris_objects import Figure
from random import randrange
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, filename="log.txt")
logging.info("Loglevel is info")

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

# Block
shape = np.array([(0, -1), (-1, -1), (-1, 0), (0, 0)])

# Create block object from class Figure
block = Figure(shape, color)

logging.debug(f"block color : {block.getColor()}")
logging.debug(f"block shape :  {block.getShape()}")

# iShape

# Shape of i-shape
shape = np.array([(-1, 0), (-2, 0), (0, 0), (1, 0)])

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

iShape = Figure(shape, color)

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

logging.debug("Rotate counterclockwise")
iShape.rotate()

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

shape = np.array(
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
)
zShape = Figure(shape, color)
# zShape.rotate()


# # rotate shape
# Define the 90-degree rotation matrix
rotation_matrix = np.array([[0, -1], [1, 0]])

# Apply the rotation matrix to the shape array
shape = np.dot(shape, rotation_matrix)



import matplotlib.pyplot as plt


# Create a plot and set its limits
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Plot the Tetris block shape
ax.scatter(shape[:,0], shape[:,1], color='blue')

# Show the plot
plt.show()