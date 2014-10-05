#coding=utf8
__author__ = 'tony'

import configs
import random
import draw_elements as drawing
import mutate_func
import optimal_func


def get_small_polygon_by_coord(_x, _y):
    coords_set = set([])
    for i in range(0, configs.POLYGON_POINTS):
        while True:
            coord_x = mutate_func.norm_mutate(_x, 0, configs.x)
            coord_y = mutate_func.norm_mutate(_y, 0, configs.y)
            if 0 <= coord_x < configs.x and 0 <= coord_y < configs.y:
                coord = (coord_x, coord_y)
                if not coords_set.__contains__(coord):
                    break

        coords_set.add(coord)
    color = list(configs.origin_image.getpixel(coord))

    return drawing.Polygon(list(coords_set), color, configs.POLYGON_SMALL)


def get_small_polygon():
    _x = random.randint(0, configs.x - 1)
    _y = random.randint(0, configs.y - 1)

    return get_small_polygon_by_coord(_x, _y)


def get_random_polygon():
    coords = []
    for j in range(0, configs.POLYGON_POINTS):
        c1 = (random.randint(1, configs.x) - 1, random.randint(1, configs.y) - 1)
        coords.append(c1)

    color = list(configs.origin_image.getpixel(c1))
    return drawing.Polygon(coords, color, configs.POLYGON_BIG)


def create_polygon():
    polygon_type_rand = random.randint(0, 100)
    # 小尺寸的多边形
    if polygon_type_rand < configs.SMALL_POLYGON_PERCENT:
        return get_small_polygon()
    else:
        return get_random_polygon()


def get_random_simi():
    polygons = []
    for i in range(0, configs.POLYGON_NUM_MIN):
        polygons.append(create_polygon())
    return drawing.SimImage(polygons)


def get_dismatch_location(sim):

    max_diff_x = -1
    max_diff_y = -1
    max_diff = 0

    for i in range(0, 100):
        x = random.randint(0, configs.x - 1)
        y = random.randint(0, configs.y - 1)

        diff_value = 0
        for j in range(0, 10):
            norm_x = mutate_func.norm_mutate(x, 0, configs.x)
            norm_y = mutate_func.norm_mutate(y, 0, configs.y)
            if 0 <= norm_x < configs.x and 0 <= norm_y < configs.y:
                pixel = optimal_func.CheckPixel((norm_x, norm_y))
                diff_value += pixel.diff(sim.img)

        if diff_value > max_diff:
            max_diff_x = x
            max_diff_y = y
            max_diff = diff_value

    return max_diff_x, max_diff_y

