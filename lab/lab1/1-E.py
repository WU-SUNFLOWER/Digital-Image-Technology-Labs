import cv2
import numpy as np

image = cv2.imread("Flower.png")
green_channel = image[:, :, 1]

# 获取绿色分量图像的最大值和最小值
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(green_channel)
print(f"min value={min_val}, max_val={max_val} min_loc={min_loc} max_loc={max_loc}")

# 获取绿色分量图像的均值和标准差
mean, std_dev = cv2.meanStdDev(green_channel)

"""
对于多通道图像，cv2.meanStdDev方法的返回值如下：
mean = [
    [ 77.03799221]
    [136.42353554]
    [151.0554386 ]
]
std_dev=[
    [41.2196401 ]
    [55.47241198]
    [60.25877578]
]

对于单通道图像，返回值如下：
mean = [
    [136.42353554]
]
std_dev = [
    [55.47241198]
]
"""

print(mean)
print(std_dev)
print(f"mean={mean[0][0]}, std deviation={std_dev[0][0]}")