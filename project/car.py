# A test car file

dt = 0.01
t = 0

# define our car
f_motor = 750
mass = 1200
accelleration = f_motor/mass

running = True
velocity = 0
distance = 0

x = []
y = []

while running:
    t = t + dt
    dVelocity = accelleration * dt
    velocity += dVelocity

    dDistancex = velocity * dVelocity
    distance += dDistancex

    x.append(t)
    y.append(distance)



    if distance >100:
    # if t > 3:
        break

print(f'time: {t}, speed: {velocity}, distance: {distance}')

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# # make data
# x = t
# y = v

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 30), xticks=np.arange(1, 30),
       ylim=(0, 100), yticks=np.arange(1, 100))

plt.show()