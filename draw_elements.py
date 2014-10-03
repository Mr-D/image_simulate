#coding=utf8
__author__ = 'tony'

import configs, mutate_func
import image_build
import optimal_func

class Polygon():
    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color
        self.dirty = False

    def __do_mutate__(self):

        #单个坐标的移动
        for index in range(0, self.coordinates.__len__()):
            coordinate = self.coordinates[index]
            re_draw, xx = mutate_func.do_mutate(coordinate[0], 0, configs.x, configs.coordinator_mutate_rate)
            self.dirty = self.dirty | re_draw
            re_draw, yy = mutate_func.do_mutate(coordinate[1], 0, configs.y, configs.coordinator_mutate_rate)
            self.dirty = self.dirty | re_draw
            self.coordinates[index] = (xx, yy)

        for index in range(0, self.color.__len__()):
            re_draw, self.color[index] = mutate_func.do_mutate(self.color[index], 0, 255, configs.color_mutate_rate)
            self.dirty = self.dirty | re_draw

        #整个多边形一起移动
        x_coord_list = []
        y_coord_list = []
        for index in range(0, self.coordinates.__len__()):
            x_coord_list.append(self.coordinates[index][0])
            y_coord_list.append(self.coordinates[index][1])

        re_draw, x_coord_list = mutate_func.all_move(x_coord_list, 0, configs.x, configs.all_coordinator_mutate_rate)
        self.dirty = self.dirty | re_draw
        re_draw, y_coord_list = mutate_func.all_move(y_coord_list, 0, configs.y, configs.all_coordinator_mutate_rate)
        self.dirty = self.dirty | re_draw

        for index in range(0, self.coordinates.__len__()):
            self.coordinates[index] = (x_coord_list[index], y_coord_list[index])

    def clone(self):
        copy_coords = list(self.coordinates)
        copy_color = list(self.color)
        return Polygon(copy_coords, copy_color)


class SimImage():

    def __init__(self, polugons):
        self.polygons = polugons
        self.img = image_build.build_img(self.polygons)
        self.dirty = False

    def __do_mutate__(self):
        redraw = False
        for polygon in self.polygons:
            polygon.__do_mutate__()
            redraw = redraw | polygon.dirty

        if redraw:
            self.img = image_build.build_img(self.polygons)

    def get_diff(self):
        return optimal_func.optimal_function(self.img)

    def clone(self):
        copy_polygon = []
        for polygon in self.polygons:
            copy_polygon.append(polygon.clone())
        return SimImage(copy_polygon)


    # def make(sim1, sim2):
    #     a, b = splits_rand_parts(tria_size, tria_size / 2)
    #
    #     triangulars = range(0, tria_size)
    #     for index in a:
    #         triangulars[index] = sim1.triangulars[index]
    #     for index in b:
    #         triangulars[index] = sim2.triangulars[index]
    #
    #     return Simi(triangulars)