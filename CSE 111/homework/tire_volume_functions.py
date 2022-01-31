import math


# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# calculate values
v = math.pi * w**2 * a * (w * a + 2540 * d) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

# Import datetime
from datetime import datetime

current_date_and_time = datetime.now(tz=None)

# Open file to store data
f = open('volumes.txt', mode="rt")

# Calculatte price per tire and total price(depends on the quantitty)
price_per_volumne = 1.25
tire_price = float(price_per_volumne) * v
print()
print(f"Your price per tire is: {tire_price:.2f} (including taxes)")

quantity = int(input("How many tires do you need? "))
total_price = quantity * tire_price
print(f"Your total price is : {total_price:.2f}")

# Ask the client if he want to buy this articles
answer = input("Do you want to buy this articles? (Y/N) ")

# If statement to have two different result (Y/N)
if answer.lower() == "y":

    with open('volumes.txt', "at") as volumes_file:

        print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {tire_price:.2f}, {quantity}, {total_price:.2f}", file=volumes_file)
    print("Thanks for buying with us." )

else:   

    with open('volumes.txt', "at") as volumes_file:

        print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}", file=volumes_file)
    print("Thanks for trust in us." )
