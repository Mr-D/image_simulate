__author__ = 'tony'

import Image, ImageDraw
from configs import *


def build_img(polygons):
    img = Image.new("RGB", (x, y), "white")
    draw1 = ImageDraw.Draw(img, "RGBA")

    for polygon in polygons:
        color_tuple = (polygon.color[0], polygon.color[1], polygon.color[2], 128)
        draw1.polygon(polygon.coordinates, fill=color_tuple)

    return img