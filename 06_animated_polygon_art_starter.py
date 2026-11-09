"""EXERCISE: animate multiple polygons by moving existing objects.
First finish polygon_shape.py. Then change the motion, colors, sizes,
number of polygons, and frame count to create your own artwork.
"""
import turtle
import random
import math
import time
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("steelblue")
screen.tracer(0)  # The entire frame is displayed with screen.update().

rng = random.Random(12)
colors = ["cyan", "turquoise", "aqua", "lightyellow", "deepskyblue",
          "cornsilk", "plum", "mintcream", "lavender", "pink", "aliceblue", "powderblue"]

shapes = []
for _ in range(19):
    x = rng.randint(-290, 210)
    y = rng.randint(-225, 180)
    shape = Polygon(x, y, rng.randint(3, 7), rng.randint(35, 120),
                    rng.choice(colors), rng.randint(1, 7), rng.randint(0, 359))
    shape.draw()
    # Store the home position and motion phase, not a second copy of
    # the shape's current position.
    shapes.append((shape, x, y, rng.random() * 6.28))

for frame in range(100):
    for shape, home_x, home_y, phase in shapes:
        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        shape.move_to(x, y)  # Reuse the same object and its internal turtle.
    screen.update()
    time.sleep(0.045)  # A short delay makes motion visible.

screen.mainloop()
