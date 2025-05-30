import math

def circle_stats(radius):
    if radius < 0:
        raise ValueError("Radius can't be a negative value.")
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 3), round(circumference, 3)

try:
    a,c = circle_stats(-4)
    print("Area:", a, "Circumference:", c)
except ValueError as e:
    print("ERROR:",e)


# Key Concepts:
# try: Tests a block of code for errors.
# except: Handles errors if an exception occurs.
# raise: Manually triggers an exception.
# e: Holds the exception object, including the error message.

