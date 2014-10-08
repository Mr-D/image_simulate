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
        for j in range(0, length_c):
            location = (i * width, j * length)
            im = image.crop((location[0], location[1], (i+1) * width, (j+1)*length))
            dim = DivideImage(im, location)
            divides.append(dim)

        location = ((i + 1) * width, (j + 1) * length)
        im = image.crop((location[0], location[1], x, y))
        # im = image.crop(((i + 1) * width, (j + 1) * length, x - (i + 1) * width, y - (j + 1) * length))
        dim = DivideImage(im, location)
        divides.append(dim)

    return divides

