import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw(picture, title, data):
    x_coords = range(len(data))
    picture.bar(x_coords, data)
    picture.set_title(title)
    picture.set_xlabel('Gray Value')
    picture.set_ylabel('Frequency')
    picture.set_xticks(x_coords, labels=x_coords, rotation=90)

def calc_cdf(hist):
    # 计算像素点总数
    total_pixels = hist.sum()
    # 计算每种灰度值在原图中出现的频率
    frequencies = hist.ravel() / total_pixels
    # 计算各灰度级的累积分布函数值
    cumulative_sum = frequencies.cumsum()
    return cumulative_sum

image = cv2.imread('lenna.jpg')

blue_channel, green_channel, red_channel = cv2.split(image)

"""
以均衡化处理后的绿色分量图像的直方图为目标直方图，对 Lenna 的蓝色分量图像作直方图规定化
"""

source_hist = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
reference_hist = cv2.calcHist([green_channel], [0], None, [256], [0, 256])

source_cdf = calc_cdf(source_hist)
reference_cdf = calc_cdf(reference_hist)

M = np.zeros((256, ), dtype=np.uint8)
for src_val in range(0, 256):
    target_val = np.abs(source_cdf[src_val] - reference_cdf).argmin()
    M[src_val] = target_val
    
result_image = M[blue_channel]

fig, (picture1, picture2, picture3) = plt.subplots(1, 3, figsize=(25, 6))

source_hist = cv2.calcHist([blue_channel], [0], None, [32], [0, 256])
draw(picture1, "Source Image", source_hist.ravel())

reference_hist = cv2.calcHist([green_channel], [0], None, [32], [0, 256])
draw(picture2, "Reference Image", reference_hist.ravel())

result_hist = cv2.calcHist([result_image], [0], None, [32], [0, 256])
draw(picture3, "Result Image", result_hist.ravel())

plt.tight_layout()
plt.show()