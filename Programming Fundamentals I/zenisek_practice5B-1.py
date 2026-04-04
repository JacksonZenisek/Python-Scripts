# Import both random and math functions:
import random
import math

# Define the main fuinction of the program. Randomly selects a number between 1-100:
def main():
    radius = random.randint(1, 100)
    area = area_of_cir_cal(radius)

# Print the outcome of both the random assigned radius and the area of the circle:
    print(f"Radius: {radius:.2f}")
    print(f"Area: {area:.2f}")

# Define the calculation process of the area of the circle given the random integer for the program:
def area_of_cir_cal(radius):
    area = math.pi * radius ** 2
    return area

# Calls the main function:
main()