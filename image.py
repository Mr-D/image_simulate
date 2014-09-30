#coding=utf8
__author__ = 'tony'

import Image, ImageDraw
import random

# im = Image.open("lena.pgm")
# im = Image.new("RGBA", (500, 500), "white")
# im2 = Image.new("RGBA", (500, 500), "white")
# draw1 = ImageDraw.Draw(im)
# draw2 = ImageDraw.Draw(im2)
#
#
# # write to stdout
# draw1.polygon([(100,100), (200, 200), (150, 100)], fill=(200, 10, 10, 128))
#
# draw2.polygon([(140,200), (200, 200), (150, 100)], fill=(200, 255, 10, 128))
#
# im.show()


def random_img(x, y, color):
    im = Image.new("RGBA", (x, y), "white")

    x1 = random.randint(0, x)
    y1 = random.randint(0, y)

    x2 = random.randint(0, x)
    y2 = random.randint(0, y)

    x3 = random.randint(0, x)
    y3 = random.randint(0, y)

    draw1 = ImageDraw.Draw(im)


    # draw1.polygon([(x1,y1), (x2, y2), (x3, y3)],
    #               fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128))

    draw1.polygon([(x1,y1), (x2, y2), (x3, y3)], fill=color)

    return im


def blend_imgs(colors):
    x = 500
    y = 500
    img = random_img(x, y, colors[0])
    for i in range(1, 100):
        img_b = random_img(x, y, colors[i])
        # img_b.show()
        img = Image.blend(img, img_b, 0.15)
    img.show()


def get_rand_pixels(image):
    x, y = image.size

    pixels = []

    for i in range(0, 100):
        rgb = image.getpixel((random.randint(0, x), random.randint(0, y)))
        pixels.append(rgb)
    return pixels


# blend_imgs()


colors = get_rand_pixels(image)
blend_imgs(colors)


