
__author__ = 'tony'
import random,sys
import configs
import draw_elements as drawing


def get_random_simi():

    triangulars = []
    for i in range(0, configs.tria_size):
        c1 = (random.randint(1, configs.x) - 1, random.randint(1, configs.y) - 1)
        c2 = (random.randint(1, configs.x) - 1, random.randint(1, configs.y) - 1)
        c3 = (random.randint(1, configs.x) - 1, random.randint(1, configs.y) - 1)

        color = list(configs.origin_image.getpixel(c1))
        triangulars.append(drawing.Triangular([c1, c2, c3], color))
    return drawing.SimImage(triangulars)





def start_mutate():
    sim_image = get_random_simi()
    max_diff = sim_image.get_diff()

    iterate_round = 0
    all_iterate_count = 0

    while True:
        all_iterate_count += 1
        clone_image = sim_image.clone()
        sim_image.__do_mutate__()
        new_diff = sim_image.get_diff()

        if new_diff > max_diff:
            del sim_image
            sim_image = clone_image
            continue

        max_diff = new_diff
        iterate_round += 1
        if iterate_round > configs.max_iterate and max_diff < configs.min_optimal:
            break

        print "all iteratecount %d effective iterate %d optimal value :%d" % (
        all_iterate_count, iterate_round, max_diff)
        if iterate_round % 100 == 0:
            image_name = "simulation_images/image_%d.jpg" % iterate_round
            sim_image.img.save(image_name, "JPEG")

    image_name = "image_%d.jpg" % iterate_round
    sim_image.img.save(image_name, "JPEG")


if __name__ == "__main__":
    start_mutate()


