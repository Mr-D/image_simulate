__author__ = 'tony'

from utils import *


def build_img(triangulars):
    img = draw_triangular(triangulars[0])
    for i in range(1, triangulars.__len__()):
        img_b = draw_triangular(triangulars[i])
        img = Image.blend(img, img_b, alpha)
        del img_b

    return img


def get_random_simi():
    x, y = image.size

    triangulars = []
    for i in range(0, tria_size):
        c1 = (random.randint(1, x) - 1, random.randint(1, y) - 1)
        c2 = (random.randint(1, x) - 1, random.randint(1, y) - 1)
        c3 = (random.randint(1, x) - 1, random.randint(1, y) - 1)


        color = image.getpixel((random.randint(1, 255) - 1, random.randint(1, 255) - 1))
        triangulars.append(Triangular([c1, c2, c3], color))
    return Simi(triangulars)


class Simi():

    def __init__(self, triangulars):
        self.triangulars = triangulars
        self.__do_mutate__()
        self.img = build_img(self.triangulars)
        self.img.show()
        self.__do_mutate__()
        self.img = build_img(self.triangulars)
        self.img.show()

    def __do_mutate__(self):
        for triangular in self.triangulars:
            print "mutate a tria"
            triangular.__do_mutate__()

    def make(sim1, sim2):
        a, b = splits_rand_parts(tria_size, tria_size / 2)

        triangulars = range(0, tria_size)
        for index in a:
            triangulars[index] = sim1.triangulars[index]
        for index in b:
            triangulars[index] = sim2.triangulars[index]

        return Simi(triangulars)




get_random_simi()

