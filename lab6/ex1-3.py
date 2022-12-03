# Excercise 06.1.3
# Geometric solids

#  Functions for computing the volume and surface area of spheres, cylinders
#  and cones.
#
from math import pi, sqrt


def main():
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))

    print("A sphere has volume:", sphere_volume(r))
    print("A sphere has surface area:", sphere_surface(r))
    print("A cylinder has volume:", cylinder_volume(r, h))
    print("A cylinder has surface area:", cylinder_surface(r, h))
    print("A cone has volume:", cone_volume(r, h))
    print("A cone has surface area:", cone_surface(r, h))


def sphere_volume(r):
    """
    Compute the volume of a sphere
    :param r: the radius of the sphere
    :return: the volume of the sphere
    """
    return 4 / 3 * pi * r ** 3


def sphere_surface(r):
    """
    Compute the surface area of a sphere
    :param r: the radius of the sphere
    :return: the surface area of the sphere
    """
    return 4 * pi * r ** 2


def cylinder_volume(r, h):
    """
    Compute the volume of a cylinder
    :param r: the radius of the cylinder
    :param h: the height of the cylinder
    :return: the volume of the cylinder
    """
    return pi * r ** 2 * h


def cylinder_surface(r, h):
    """
    Compute the surface area of a cylinder
    :param r: the radius of the cylinder
    :param h: the height of the cylinder
    :return: the surface area of the cylinder
    """
    return 2 * (pi * r ** 2 + pi * r * h)


def cone_volume(r, h):
    """
    Compute the volume of a cone
    :param r: the radius of the cone
    :param h: the height of the cone
    :return: the volume of the cone
    """
    return 1 / 3 * pi * r * r * h


def cone_surface(r, h):
    """
    Compute the surface area of a cone
    :param r: the radius of the cone
    :param h: the height of the cone
    :return: the surface area of the cone
    """
    s = sqrt(h * h + r * r)
    return pi * r * s + pi * r * r


# Call the main function.
main()
