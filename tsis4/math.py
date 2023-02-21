import math


def deg_rad(degree):
    return degree*math.pi/180


def trapezoid_area(base1, base2, height):
    return (base1+base2)/2*height


def polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan (math.pi / sides))


def parallelog_area(base, height):
    return base*height

