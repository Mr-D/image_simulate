#coding=utf8
import random

__author__ = 'tony'

import configs, mutate_func
import image_build
import optimal_func
import polygon_mutation

class Polygon():
    def __init__(self, coordinates, color, type):
        self.coordinates = coordinates
        self.color = color
        self.dirty = False
        self.type = type

    def __do_mutate__(self):

        #单个坐标的移动
        for index in range(0, self.coordinates.__len__()):
            coordinate = self.coordinates[index]
            re_draw, xx = mutate_func.do_mutate(coordinate[0], 0, configs.x, configs.COORDINATOR_MUTATE_RATE)
            self.dirty = self.dirty | re_draw
            re_draw, yy = mutate_func.do_mutate(coordinate[1], 0, configs.y, configs.COORDINATOR_MUTATE_RATE)
            self.dirty = self.dirty | re_draw
            self.coordinates[index] = (xx, yy)

        for index in range(0, self.color.__len__()):
            re_draw, self.color[index] = mutate_func.do_mutate(self.color[index], 0, 255, configs.COLOR_MUTATE_RATE)
            self.dirty = self.dirty | re_draw

        #整个多边形一起移动
        x_coord_list = []
        y_coord_list = []
        for index in range(0, self.coordinates.__len__()):
            x_coord_list.append(self.coordinates[index][0])
            y_coord_list.append(self.coordinates[index][1])

        re_draw, x_coord_list = mutate_func.all_move(x_coord_list, 0, configs.x, configs.POLYGON_MOVE_MUTATE_RATE)
        self.dirty = self.dirty | re_draw
        re_draw, y_coord_list = mutate_func.all_move(y_coord_list, 0, configs.y, configs.POLYGON_MOVE_MUTATE_RATE)
        self.dirty = self.dirty | re_draw

        for index in range(0, self.coordinates.__len__()):
            self.coordinates[index] = (x_coord_list[index], y_coord_list[index])

    def clone(self):
        copy_coords = list(self.coordinates)
        copy_color = list(self.color)
        return Polygon(copy_coords, copy_color, self.type)

    def point_inward(self, coords):
        PA = (coords[0] - self.coordinates[0][0], coords[1] - self.coordinates[0][1])
        PB = (coords[0] - self.coordinates[1][0], coords[1] - self.coordinates[1][1])
        PC = (coords[0] - self.coordinates[2][0], coords[1] - self.coordinates[2][1])

        PA_PB = PA[0] * PB[1] - PA[1] * PB[0]
        PB_PC = PB[0] * PC[1] - PB[1] * PC[0]

        PC_PA = PC[0] * PA[1] - PC[1] * PA[0]


        if (PA_PB < 0 and PB_PC < 0 and PC_PA < 0) or (PA_PB > 0 and PB_PC > 0 and PC_PA > 0):
            return True
        return False


class SimImage():

    def __init__(self, polugons):
        self.polygons = polugons
        self.img = image_build.build_img(self.polygons)

    def __do_mutate__(self, need_local_optimization=False):
        redraw = False
        for polygon in self.polygons:
            polygon.__do_mutate__()
            redraw = redraw | polygon.dirty

        redraw = self.polygon_mutate() | redraw

        if need_local_optimization:
            self.local_optimize()
            redraw = True

        if redraw:
            self.img = image_build.build_img(self.polygons)

    def polygon_mutate(self):
        dirty = False
        drop_rand = random.randint(1, configs.POLYGON_DROP_RATE)
        if drop_rand == 1 and self.polygons.__len__() > configs.POLYGON_NUM_MIN:
            drop_index = random.randint(0, self.polygons.__len__() - 1)
            self.polygons.pop(drop_index)
            dirty = True

        new_polygon = random.randint(1, configs.POKYGON_NEW_RATE)
        if new_polygon == 1 and self.polygons.__len__() < configs.POLYGON_NUM_MAX:
            new_polygon = polygon_mutation.create_polygon()
            insert_pos = random.randint(0, self.polygons.__len__())
            self.polygons.insert(insert_pos, new_polygon)
            dirty = True
        return dirty

    def get_diff(self):
        return optimal_func.optimal_function(self.img)

    def clone(self):
        copy_polygon = []
        for polygon in self.polygons:
            copy_polygon.append(polygon.clone())
        return SimImage(copy_polygon)

    def local_optimize(self):
        replace_polygon = polygon_mutation.get_replace_polygon(self)
        replace = False
        for index in range(self.polygons.__len__() - 1, 0, -1):
            polygon = self.polygons[index]
            if polygon.type == configs.POLYGON_SMALL and (
                polygon.point_inward(replace_polygon.coordinates[0]) or polygon.point_inward(
                    replace_polygon.coordinates[1]) or polygon.point_inward(replace_polygon.coordinates[2])):
                self.polygons.remove(polygon)
                replace = True
                break
        if replace:
            print "local optimization coord:(%d  %d)" % (replace_polygon.coordinates[0][0], replace_polygon.coordinates[0][1])
            self.polygons.append(replace_polygon)



