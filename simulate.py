#coding=utf8
import threading

__author__ = 'tony'

import sys
import configs
import polygon_mutation
import optimal_func
import image_build


class Simulation(threading.Thread):
    def __init__(self, thread_num, divide_image, cond, image_arr):
        threading.Thread.__init__(self)
        self.__thread_num = thread_num
        self.__cond = cond
        self.image_arr = image_arr
        self.origin = divide_image.image
        self.divide = divide_image
        self.x, self.y = self.origin.size
        self.sim_image = polygon_mutation.get_random_simi((self.x, self.y))
        self.check_points = optimal_func.get_check_pixels(self.origin, configs.get_checks_count(self.origin))

    def run(self):
        self.start_mutate()

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

            print "[thread %d] all iteratecount %d effective iterate %d optimal value :%d" % (
            self.__thread_num, all_iterate_count, iterate_round, max_diff)
            sys.stdout.flush()

            if iterate_round % 100 == 0:
                # image_name = "simulation_images/image_%d.jpg" % iterate_round
                # sim_image.img.save(image_name, "JPEG")
                self.image_arr.append(image_build.DivideImage(sim_image.img, self.divide.location))
                self.__cond.acquire()
                self.__cond.notify()
                self.__cond.release()

        # image_name = "image_%d.jpg" % iterate_round
        # sim_image.img.save(image_name, "JPEG")


if __name__ == "__main__":

    images = image_build.divide_image(configs.origin_image, configs.divide_size)

    cond = threading.Condition()
    image_arr_list = []

    for i in range(0, images.__len__()):
        image_arr = []
        image_arr_list.append(image_arr)
        simulation = Simulation(i, images[i], cond, image_arr)
        simulation.start()

    compose_num = 0
    while True:
        cond.acquire()
        cond.wait()
        cond.release()

        divides = []
        for arr in image_arr_list:
            try:
                divides.append(arr[compose_num])
            except IndexError, e:
                break

        if divides.__len__() == images.__len__():
            compose_num += 1
            image = image_build.compose(divides)
            image.show()
            image_name = "simulation_images/image_%d.jpg" % compose_num
            image.save(image_name, "JPEG")




