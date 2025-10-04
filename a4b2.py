#Write python script using package to calculate area and
#volume of cylinder and cuboids.
import math

def cylinder_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cuboid_area(l, w, h):
    return 2 * (l*w + w*h + l*h)

def cuboid_volume(l, w, h):
    return l * w * h

    print("Cylinder Area:", cylinder_area(3, 5))
    print("Cylinder Volume:", cylinder_volume(3, 5))

    print("Cuboid Area:", cuboid_area(2, 3, 4))
    print("Cuboid Volume:", cuboid_volume(2, 3, 4))
