__author__ = 'tony'

import configs, mutate_func
import image_build
import optimal_func

class Triangular():
    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color

    def __do_mutate__(self):
        for index in range(0, self.coordinates.__len__()):
            coordinate = self.coordinates[index]
            xx = mutate_func.do_mutate(coordinate[0], 0, configs.x, configs.coordinator_mutate_rate)
            yy = mutate_func.do_mutate(coordinate[1], 0, configs.y, configs.coordinator_mutate_rate)
            self.coordinates[index] = (xx, yy)

        for index in range(0, self.color.__len__()):
            self.color[index] = mutate_func.do_mutate(self.color[index], 0, 255, configs.color_mutate_rate)

    def clone(self):
        copy_coords = list(self.coordinates)
        copy_color = list(self.color)
        return Triangular(copy_coords, copy_color)


class SimImage():

    def __init__(self, triangulars):
        self.triangulars = triangulars
        self.img = image_build.build_img(self.triangulars)

    def __do_mutate__(self):
        for triangular in self.triangulars:
            triangular.__do_mutate__()
            self.img = image_build.build_img(self.triangulars)

    def get_diff(self):
        return optimal_func.optimal_function(self.img)

    def clone(self):
        copy_triangulars = []
        for triangular in self.triangulars:
            copy_triangulars.append(triangular.clone())
        return SimImage(copy_triangulars)


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