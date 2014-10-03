__author__ = 'tony'

import random

def __norm_random_init__(num):
    random_list = []
    size = 0
    while True:
        norm_value = random.normalvariate(0, 1)
        if -20 < norm_value < 20:
            random_list.append(norm_value)
            size += 1
            if size >= num:
                return random_list

norm_random_list = __norm_random_init__(20000)
# print norm_random_list


def __norm_mutate__(value, min, max):
    index = random.randint(0, norm_random_list.__len__() - 1)
    norm_rand = norm_random_list[index] / 1.96 * (max - min) * 0.05
    return value + norm_rand


def do_mutate(value, min, max, mutate_rate):
    rand = random.randint(1, mutate_rate)
    if rand > 1:
        return value
    while True:
        v = int(__norm_mutate__(value, max, min))
        if min <= v < max:
            return v

