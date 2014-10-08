#coding=utf8

__author__ = 'tony'

import sys
import configs
import polygon_mutation
import optimal_func
import image_build


class Simulation():
    def __init__(self, image):
        self.origin = image
        self.x, self.y = self.origin.size
        self.sim_image = polygon_mutation.get_random_simi((self.x, self.y))
        self.check_points = optimal_func.get_check_pixels(self.origin, configs.get_checks_count(self.origin))

    def start_mutate(self):
        sim_image = self.sim_image
        sim_image.img.show()
        max_diff = sim_image.get_diff(self.check_points)

        iterate_round = 0
        all_iterate_count = 0

        while True:
            all_iterate_count += 1
            clone_image = sim_image.clone()

            #是否需要局部优化
            need_local_optimization = False
            # if all_iterate_count - pre_effective_it > configs.LOCAL_OPTIMIZATION_IT:
            #     need_local_optimization = True



            sim_image.__do_mutate__(need_local_optimization)

            new_diff = sim_image.get_diff(self.check_points)
            if new_diff >= max_diff:
                del sim_image
                sim_image = clone_image
                continue

            pre_effective_it = all_iterate_count
            max_diff = new_diff
            iterate_round += 1
            if iterate_round > configs.MAX_ITERATE or max_diff < configs.MIN_OPTIMAL:
                break

            print "all iteratecount %d effective iterate %d optimal value :%d" % (
            all_iterate_count, iterate_round, max_diff)
            sys.stdout.flush()

            if iterate_round % 100 == 0:
                image_name = "simulation_images/image_%d.jpg" % iterate_round
                sim_image.img.save(image_name, "JPEG")

        image_name = "image_%d.jpg" % iterate_round
        sim_image.img.save(image_name, "JPEG")





if __name__ == "__main__":

    images = image_build.divide_image(configs.origin_image, configs.divide_size)
    simulation = Simulation(images[0].image)
    simulation.start_mutate()


