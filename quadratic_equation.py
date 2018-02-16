from math import sqrt


def _root1(a, b, discriminant):
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    return root1


def _root2(a, b, discriminant):
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root2


def get_roots(a, b, c):
    discriminant = b ** 2 - (4 * a * c)
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return _root1(a, b, discriminant), None
    else:
        return _root1(a, b, discriminant), _root2(a, b, discriminant)
