import math
import random

__author__ = 'tony'


def get_random_nonrepeate_coord(x_max, y_max, count):
    check_coords = set([])
    while True:
        x = random.randint(0, x_max - 1)
        y = random.randint(0, y_max - 1)
        coord = (x, y)
        if check_coords.__contains__(coord):
            continue
        check_coords.add(coord)
        if check_coords.__len__() >= count:
            break

    return check_coords


class CheckPixel():
    def __init__(self, image, coordinator):
        self.__coord = coordinator
        self.__pixel = image.getpixel(self.__coord)

    def diff(self, image):
        image_pixel = image.getpixel(self.__coord)
        value = 0
        for i in range(0, 3):
            value += abs(image_pixel[i] - self.__pixel[i])
        return value


def get_check_pixels(image, count):
    x, y = image.size
    check_pixels = []
    random_coords = get_random_nonrepeate_coord(x, y, count)

    for coord in random_coords:
        check_pixels.append(CheckPixel(image, coord))

    return check_pixels


# check_pixels = get_check_pixels()


def optimal_function(image1, checks):
    diff_v = 0
    for pixel in checks:
        diff_v += pixel.diff(image1)
    return diff_v



####   test #####
if __name__ == "__main__":
    cc = get_random_nonrepeate_coord(10, 10, 100)
    for a in cc:
        print a






