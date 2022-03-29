from math import pi


def circle_area(radius: float):
    """Create a funtion to compute the area of the circle
    """
    if type(radius) not in [int, float]:
        raise TypeError('The radius must be a non-negative real number.')

    if radius < 0:
        raise ValueError("the radious cannot be negative")

    return pi * (radius**2)


def run():
    # test function circle circle_area
    radius_values = [2, 0, -3, 2 + 5j, True, 'radius', '']
    message = "Area of the circles with r {radius} is {area}"

    for r in radius_values:
        area = circle_area(r)
        print(message.format(radius=r, area=area))


if __name__ == '__main__':
    run()
