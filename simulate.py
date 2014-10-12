#coding=utf8
import threading

__author__ = 'tony'

import sys
import configs
import polygon_mutation
import optimal_func
import image_build


class Simulation(threading.Thread):
    def __init__(self, thread_num, divide_image, cond):
        threading.Thread.__init__(self)
        self.__thread_num = thread_num
        self.__cond = cond
        # self.image_arr = image_arr
        self.divide_image = None
        self.origin = divide_image.image
        self.divide = divide_image
        self.x, self.y = self.origin.size
        self.iterate_round = 0
        self.score = 0
        self.sim_image = polygon_mutation.get_random_simi((self.x, self.y))
        self.check_points = optimal_func.get_check_pixels(self.origin, configs.get_checks_count(self.origin))

    def run(self):
        self.start_mutate()

    def start_mutate(self):
        sim_image = self.sim_image
        sim_image.img.show()
        max_diff = sim_image.get_diff(self.check_points)

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

            max_diff = new_diff
            self.iterate_round += 1

            self.score = max_diff

            # print "[thread %d] all iteratecount %d effective iterate %d optimal value :%d" % (
            # self.__thread_num, all_iterate_count, self.iterate_round, max_diff)
            # sys.stdout.flush()


            if self.iterate_round % 10 == 0:
                self.divide_image = image_build.DivideImage(sim_image.img, self.divide.location)
                # image_name = "simulation_images/image_%d.jpg" % iterate_round
                # sim_image.img.save(image_name, "JPEG")
                # self.image_arr.append(self.divide_image)
                self.__cond.acquire()
                self.__cond.notify()
                self.__cond.release()

        # image_name = "image_%d.jpg" % iterate_round
        # sim_image.img.save(image_name, "JPEG")


if __name__ == "__main__":

    images = image_build.divide_image(configs.origin_image, configs.divide_size)

    cond = threading.Condition()

    sims = []
    for i in range(0, images.__len__()):
        simulation = Simulation(i, images[i], cond)
        simulation.start()
        sims.append(simulation)

    compose_num = 0
    while True:
        cond.acquire()
        cond.wait()
        cond.release()

        all_iterate_count = []
        scores = []
        divides = []
        for sim in sims:
            all_iterate_count.append(sim.iterate_round)
            scores.append(str(sim.score))
            divides.append(sim.divide_image)

        if sum(all_iterate_count) % 200 == 0:
            print "job diff is %s " % ("  ".join(scores))

            if divides.__len__() == images.__len__():
                compose_num += 1
                image = image_build.compose(divides)
                image.show()
                image_name = "simulation_images/image_%d.jpg" % compose_num
                image.save(image_name, "JPEG")




