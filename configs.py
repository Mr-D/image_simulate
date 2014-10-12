#coding=utf8
import Image

__author__ = 'tony'


####
origin_image = Image.open("dd.png", "r")
divide_size = (200, 200)
# x, y = origin_image.size

###  采点个数  （用于最优函数分析）
# MAX_CHECKS = int(x * y / 10)
def get_checks_count(image):
    x, y = image.size
    return int(x * y / 10)

##
POLYGON_SMALL = "SMALL"
POLYGON_BIG = "BIG"

###  三角形个数
POLYGON_POINTS = 3

<<<<<<< HEAD
POLYGON_NUM_MIN = int(x * y / 200)
POLYGON_NUM_MAX = int(POLYGON_NUM_MIN * 3)
=======
# POLYGON_NUM_MIN = int(x * y / 300)
# POLYGON_NUM_MAX = int(POLYGON_NUM_MIN * 2.5)
def get_polygon_min_max((x, y)):
    min = int(x * y / 300)
    return min, int(min * 2.5)



>>>>>>> 5fbff9afd5e485d779584a20bb5a29aff74583b5
###  小尺寸的多边形的比例
SMALL_POLYGON_PERCENT = 90


## 迭代终止条件
###  迭代次数
MAX_ITERATE = 20000
### 最优函数目标值
MIN_OPTIMAL = 10000

##  局部优化进入条件
LOCAL_OPTIMIZATION_IT = 20




#  mutate rate #
COORDINATOR_MUTATE_RATE = 500
COLOR_MUTATE_RATE = 1000

POLYGON_MOVE_MUTATE_RATE = 400

#
POLYGON_DROP_RATE = 20
POKYGON_NEW_RATE = 19
#  mutate rate #


