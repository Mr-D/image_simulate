from decimal import Decimal
from math import floor
import random
import math

__author__ = 'tony'

import Image
import ImageDraw

from configs import *


def get_diff(sim, checks):
    value = 0.0
    for check in checks:
        check_coord = check.coord
        check_color = check.color

        image_color = sim.img.getpixel(check_coord)
        for i in range(0, 3):
            value = value + math.fabs(check_color[i] - image_color[i])
    return value


class CheckPoint():
    def __init__(self, coordinate, color):
        self.coord = coordinate
        self.color = color

##        mutate  function   ##


def mutate(value, min, max, factor):
    mutate_value = random.randint(0, 100)
    if mutate_value > (factor * 100):
        return value

    while True:
        # v = random.randint(min, max - 1)
        random_offset = random.randint(min, max) * mutate_factor
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
            xx = mutate(coordinate[0], 0, x, mutate_rate)
            yy = mutate(coordinate[1], 0, y, mutate_rate)
            coordinates.append((xx, yy))
        self.coordinates = coordinates

        color = []
        for v in self.color:
            color.append(mutate(v, 0, 255, mutate_rate))
        self.color = color


def draw_triangular(triangular):
    im = Image.new("RGBA", (x, y), "white")

    draw1 = ImageDraw.Draw(im)


    # draw1.polygon([(x1,y1), (x2, y2), (x3, y3)],
    #               fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128))
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


def get_norepeate_pairs(size, pair_size):
    pair_set = set()

    for i in range(0, pair_size):
        while True:
            x = random.randint(0, size - 1)
            while True:
                y = random.randint(0, size - 1)
                if x != y:
                    break

            pair = (x, y)
            reverse_pair = (y, x)

            if not pair_set.__contains__(pair) and not pair_set.__contains__(reverse_pair):
                pair_set.add(pair)
                break
    return pair_set






