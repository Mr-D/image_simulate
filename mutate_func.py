#coding=utf8
__author__ = 'tony'

import random


def norm_mutate(value, min, max):
    """
    0, 1的正态分布，95%的可能性变异的幅度为 0.1 * （max - min）
    """
    norm_random = random.normalvariate(0, 1)
    norm_rand = norm_random / 1.96 * (max - min) * 0.05
    return int(value + norm_rand)


def all_move(value_list, min, max, mutate_rate):
    rand = random.randint(1, mutate_rate)
    if rand > 1:
        return False, value_list

    while True:
        v = norm_mutate(0, max, min)

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
        v = norm_mutate(value, max, min)
        if min <= v < max:
            if v == value:
                return False, v
            return True, v

