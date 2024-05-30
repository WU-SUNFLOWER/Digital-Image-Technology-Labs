import cv2
import numpy as np

# 读取图像
image = cv2.imread('Lenna.jpg')

# 提取绿色分量
channels = cv2.split(image)
green_channel = channels[1]

# 提取左上角为(80,80)，大小为8*8的区域
block = green_channel[0:100, 0:100]

# 定义DCT和逆DCT变换函数
def dct_2d(block):
    return cv2.dct(np.float32(block))

def idct_2d(block):
    return cv2.idct(block)

# 处理DCT系数的函数
def process_dct_coefficients(dct_block, factor):
    processed_block = np.floor(dct_block / factor) * factor
    return processed_block

# 计算均方差的函数
def mean_squared_error(original, processed):
    return np.mean((original - processed) ** 2)

# 进行二维DCT变换
dct_block = dct_2d(block)

# 按x=floor(x/8)*8处理DCT系数
processed_dct_block_8 = process_dct_coefficients(dct_block, 8)

# 进行逆DCT变换
idct_block_8 = idct_2d(processed_dct_block_8)

cv2.imshow('fuck1', block)
cv2.imshow('fuck2', idct_block_8)

cv2.waitKey()
cv2.destroyAllWindows()