__author__ = 'tony'

import Image, ImageDraw
from configs import *


def build_img(triangulars):
    img = Image.new("RGB", (x, y), "white")
    draw1 = ImageDraw.Draw(img, "RGBA")

    for triangular in triangulars:
        color_tuple = (triangular.color[0], triangular.color[1], triangular.color[2], 128)
        draw1.polygon(triangular.coordinates, fill=color_tuple)

    return img