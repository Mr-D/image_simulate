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


def all_move(value_list, min, max, mutate_rate):
    rand = random.randint(1, mutate_rate)
    if rand > 1:
        return False, value_list

    while True:
        v = int(__norm_mutate__(0, max, min))

        if v == 0:
            return False, value_list

        valid = True
        for value in value_list:
            mutate_v = value + v
            if mutate_v >= max or mutate_v < min:
                valid = False
                break

        if valid:
            for i in range(0, value_list.__len__()):
                value_list[i] += 1
            return True, value_list


def do_mutate(value, min, max, mutate_rate):
    rand = random.randint(1, mutate_rate)
    if rand > 1:
        return False, value

    while True:
        v = int(__norm_mutate__(value, max, min))
        if min <= v < max:
            if v == value:
                return False, v
            return True, v

