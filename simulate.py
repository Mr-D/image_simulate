__author__ = 'tony'

from utils import *






def build_checkpoints(image, size):
    Checks = []
    for i in range(0, size):
        coor = (random.randint(1, x) - 1, random.randint(1, y) - 1)
        Checks.append(CheckPoint(coor, image.getpixel(coor)))
    return Checks

image = Image.open("07.jpg", "r")


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
        # self.img.show()
        # self.__do_mutate__()
        # self.img = build_img(self.triangulars)
        # self.img.show()

    def __do_mutate__(self):
        for triangular in self.triangulars:
            triangular.__do_mutate__()

    def make(sim1, sim2):
        a, b = splits_rand_parts(tria_size, tria_size / 2)

        triangulars = range(0, tria_size)
        for index in a:
            triangulars[index] = sim1.triangulars[index]
        for index in b:
            triangulars[index] = sim2.triangulars[index]

        return Simi(triangulars)


def one_iterate(checks, parents):
    pair_set = get_norepeate_pairs(parents.__len__(), 40)
    children = []
    diff_score = []
    for pair in pair_set:
        sim = Simi.make(parents[pair[0]], parents[pair[1]])
        print "make a pair"
        children.append(sim)
        diff_score.append(get_diff(sim, checks))
    sorted_index = sorted(range(len(diff_score)), key=lambda k: diff_score[k])

    next_generation = []
    for i in range(0, 10):
        next_generation.append(children[sorted_index[i]])
    return next_generation


def mutation():
    checks = build_checkpoints(image, 500)

    next = []
    for i in range(0, 10):
        next.append(get_random_simi())

    iterate_num = 10
    for i  in range(0, iterate_num):
        print "%d generation" % i
        next = one_iterate(checks, next)

    for n in next:
        n.img.show()


mutation()


# sim1 = get_random_simi()
# sim2 = get_random_simi()
# sim3 = Simi.make(sim1, sim2)
# print get_diff(sim1, checks)
