from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Radius Must be an non negative real no")
    if r < 0:
        raise ValueError("Radius must be positive")
    return pi*(r**2)
