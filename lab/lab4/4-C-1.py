import cv2
import numpy as np

def get_random_color():
    return (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))

# 读取图像
image = cv2.imread('BirdFly.png')
height, width, _ = image.shape

# 转换到灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用自适应阈值化分割
thresh = cv2.adaptiveThreshold(
    src=gray_image,
    # 阈值化后将要设置的最大值，这通常设置为 255（对应于8位灰度图像的最大亮度值）。
    maxValue=255,
    # 自适应阈值化算法
    #   cv2.ADAPTIVE_THRESH_MEAN_C 使用邻近区域的平均值来计算阈值
    #   cv2.ADAPTIVE_THRESH_GAUSSIAN_C 使用邻近区域像素的加权和，权重则由一个高斯窗口确定
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    # 阈值化的类型
    #   cv2.THRESH_BINARY 如果像素值大于阈值，则像素值设置为 maxValue，否则设置为 0。
    #   cv2.THRESH_BINARY_INV 如果像素值大于阈值，则像素值设置为 0，否则设置为 maxValue。
    thresholdType=cv2.THRESH_BINARY, 
    # 决定计算阈值时所用区域大小的邻域尺寸，是一个奇数
    blockSize=601, 
    # 一个常数，会从计算出来的自适应阈值中被减去，以便微调结果。可以为负数或正数。
    C=15
)

# 开运算去除二值图像中的噪声
se = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10), (-1, -1))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, se)   # 去除噪声

cv2.imshow("Thresh", thresh)

# 将单通道图像扩展为三通道图像，便于涂色
# https://numpy.org/devdocs/reference/generated/numpy.dstack.html
result = np.dstack([thresh, thresh, thresh])

# mask用于标记已填充点，会被floodFill函数主动修改
mask = np.zeros((height + 2, width + 2), np.uint8)

# 遍历图像中的所有点，进行涂色
for y in range(height):
    for x in range(width):
        # 如果当前点是前景点且未被填充，执行 floodFill
        if mask[y + 1, x + 1] == 0:
            # 如果当前点在二值图像中被标记为物体，执行floodFill进行涂色
            if thresh[y, x] == 0:
                cv2.floodFill(result, mask, (x, y), get_random_color(), (5,)*3, (5,)*3)
            # 否则说明当前点是背景，涂统一的背景色
            else:
                result[y, x] = (204, 204, 204)

# 显示填充后的图像
cv2.imshow('Final', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
