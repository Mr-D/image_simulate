#coding=utf8
import Image

__author__ = 'tony'


###  三角形个数
tria_size = 100

###  迭代次数
max_iterate = 20000
### 最优函数目标值
min_optimal = 5000

###  采点个数  （用于最优函数分析）
max_checks = 1000


#  mutate rate #
coordinator_mutate_rate = 1000
color_mutate_rate = 1500
#  mutate rate #


####
origin_image = Image.open("11.jpg", "r")
x, y = origin_image.size