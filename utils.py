from decimal import Decimal
from math import floor
import random

__author__ = 'tony'

import Image
import ImageDraw

from configs import *


image = Image.open("07.jpg", "r")




def mutate(value, min, max, factor):

    while True:
        random_offset = random.randint(min, max) * factor
        negative_random = random.randint(-1 , 2)
        if negative_random > 0:
            random_offset = random_offset * -1
        v = int(value + random_offset)
        if max > v >= min:
            return v


class Triangular():
    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color

    def __do_mutate__(self):
        coordinates = []
        for coordinate in self.coordinates:
            xx = mutate(coordinate[0], 0, x, mutate_fac)
            yy = mutate(coordinate[1], 0, y, mutate_fac)
            coordinates.append((xx, yy))
        self.coordinates = coordinates

        color = []
        for v in self.color:
            color.append(mutate(v, 0, 255, mutate_fac))
        self.color = color


def draw_triangular(triangular):
    im = Image.new("RGBA", (x, y), "white")

    draw1 = ImageDraw.Draw(im)


    # draw1.polygon([(x1,y1), (x2, y2), (x3, y3)],
    #               fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128))
    print triangular.coordinates
    print triangular.color
    draw1.polygon(triangular.coordinates, fill=tuple(triangular.color))

    return im



def splits_rand_parts(i, a_size):
    all = range(0, i)

    a = []
    b = []

    a_all = 0
    while True:
        v = random.randint(0, i) - 1
        if all[v] > 0:
            a.append(all[v])
            all[v] = -1
            a_all += 1
            if a_all >= a_size:
                break

    for v in all:
        if v >= 0:
            b.append(v)

    return a, b







