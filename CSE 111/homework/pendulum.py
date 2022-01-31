# Pendulum


# t is the time in seconds,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# h is the length of the pendulum in meters.

import math

length = input("Length of pendulum (meters): ")
h = float(length)

t = 2 * math.pi * math.sqrt(h/9.81)

print(f"Time (seconds):{t:.2f}")
