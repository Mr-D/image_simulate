import math

__author__ = 'tony'

import ImageDraw
from configs import *

class DivideImage():
    def __init__(self, image, location):
        self.image = image
        self.location = location


def build_img(sim):
    img = Image.new("RGB", sim.size, "white")
    draw1 = ImageDraw.Draw(img, "RGBA")

    for polygon in sim.polygons:
        color_tuple = (polygon.color[0], polygon.color[1], polygon.color[2], 128)
        draw1.polygon(polygon.coordinates, fill=color_tuple)

    return img


def divide_image(image, (width, length)):
    x, y = image.size

    width_c = int(math.floor(x / width))

    length_c = int(math.floor(y / length))

    divides = []

    for i in range(0, width_c):
        if i == width_c - 1:
            x_max = x
        else:
            x_max = (i+1) * width

        for j in range(0, length_c):
            if j == length_c - 1:
                y_max = y
            else:
                y_max = (j + 1) * length

            location = (i * width, j * length)
            im = image.crop((location[0], location[1], x_max, y_max))
            dim = DivideImage(im, location)
            divides.append(dim)

        # location = ((i + 1) * width, (j + 1) * length)
        # im = image.crop((location[0], location[1], x, y))
        # # im = image.crop(((i + 1) * width, (j + 1) * length, x - (i + 1) * width, y - (j + 1) * length))
        # dim = DivideImage(im, location)
        # divides.append(dim)


    return divides


def compose(divide_images):
    image = Image.new("RGB", origin_image.size, "white")
    for divide in divide_images:
        image.paste(divide.image, box = divide.location)
    return image

