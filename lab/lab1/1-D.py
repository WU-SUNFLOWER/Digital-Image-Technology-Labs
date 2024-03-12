import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 读取图像并转换为灰度图像
image = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("图像文件未找到，请检查路径。")
    exit()

"""
cv2.calcHist调用参数含义如下：
    1. 图像数组（在这里是单个图像所以用[image]包装）
    2. channels指定要计算直方图的通道。对于灰度图像就是 [0]；对于彩色图像，可以传入 [0]、[1] 或 [2] 来分别计算蓝色、绿色或红色通道的直方图。
    3. 掩码（在此为None，代表处理整个图像）
    4. [256]表示histSize。它决定了直方图将被分成多少个区间（或称之为“bin”或“条形”）。每个区间对应图像中一组像素值的分布情况。因此，如果你选择较大的histSize，比如[256]对于灰度图，那么你会得到一个非常细粒度的直方图，每个像素值都对应一个单独的直方图条形。反之，如果你选择较小的histSize，比如[16]，那么每个直方图条形将代表更宽的像素值范围，从而生成一个更粗略的直方图概览。
    5.[0, 256]表示range。它定义了统计直方图中横坐标的范围，即你想要分析的像素值的范围。这个范围指定了像素值的最小值和最大值，直方图只会统计这个范围内的像素值。对于大多数灰度图像，这个范围是[0, 256]，意味着考虑所有可能的灰度值，但不包含256。如果你想要针对特定范围内的像素值分析其直方图，可以通过调整这个参数来实现。
"""

"""
hist的数据类型为numpy.ndarray，其内部结构为：
[[0.000e+00]
 [1.000e+00]
 [0.000e+00]
 [1.000e+00]
 [2.000e+00]
 [1.000e+00]
 ...(总共256行)
]
"""
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# 打印灰度值介于100-128的像素数目
pixels_100_128 = np.sum(hist[100:129])
print("灰度值介于100-128的像素数目为：", int(pixels_100_128))

# 2. 计算binwidth等于8的直方图
# 计算binwidth为8的直方图，即将256个灰度级分成32个组（bin），每个组覆盖8个灰度级。
hist_8 = cv2.calcHist([image], [0], None, [32], [0, 256])
"""
hist_8的数据类型为numpy.ndarray，其内部结构为：
[[0.000e+00]
 [1.000e+00]
 [0.000e+00]
 [1.000e+00]
 [2.000e+00]
 [1.000e+00]
 ...(总共32行)
]
"""

# 计算binwidth等于16的直方图
# 计算binwidth为16的直方图，与上面类似，但这次是将灰度级分成16组，每组16个灰度级。
hist_16 = cv2.calcHist([image], [0], None, [16], [0, 256])
"""
hist_16的数据类型为numpy.ndarray，其内部结构为：
[[2.4000e+01]
 [3.0300e+02]
 [6.5920e+03]
 [1.0956e+04]
 ...(总共16行)
]
"""


# 3. 寻找具有最多像素数目的灰度级 (在宽度为8的直方图中)
# np.argmax会首先将数组扁平化，再在已扁平化的数组中寻找最大值元素的下标
max_pixel_bin_1 = np.argmax(hist)
print(f"在bindwidth为1的直方图中，最多像素数目的灰度级为{max_pixel_bin_1}")

max_pixel_bin_8 = np.argmax(hist_8)
print(f"在binwidth为8的直方图中, 最多像素数目的灰度级为({max_pixel_bin_8 * 8}~{(max_pixel_bin_8 + 1) * 8})，像素点总数为")

# 在宽度为16的直方图中
max_pixel_bin_16 = np.argmax(hist_16)
print(f"在binwidth为16的直方图中, 最多像素数目的灰度级为({max_pixel_bin_16 * 16}~{(max_pixel_bin_16 + 1) * 16})，像素点总数为")


# 4. 使用matplotlib画出直方图
# 使用 matplotlib.pyplot 模块创建一个新的图形窗口，并设置其大小为18英寸宽、6英寸高。
plt.figure(figsize=(18, 6))

# 原始256灰度级直方图
"""
plt.subplot方法的作用是在一个窗口（figure）中创建一个子图（subplot）。通过这种方式，您可以在同一个窗口中并排显示多个图形，非常适合对比不同的数据可视化。该方法的参数通常为三个数字：第一个数字表示子图的行数，第二个数字表示子图的列数，第三个数字表示当前子图的位置（从左到右，从上到下数）。例如，plt.subplot(1, 3, 1)表示创建一个1行3列的图表排列，并在第一个位置上绘制子图。
"""
plt.subplot(1, 3, 1)
plt.plot(hist)  # plt.plot方法用于描点绘制连续的曲线
plt.title("256 Bins Histogram")  # 设置图片的标题
plt.xlim([0, 256])  # 设置x的范围

# binwidth等于8的直方图
plt.subplot(1, 3, 2)
""" 
plt.bar表示绘制直方图
第一个参数range(0, 256, 8)用于生成序列0, 8, 16, ..., 248，这些数值表示每个bar在直方图x轴上的起始位置，
因此直方图中第一个bar对应的灰度值范围为[0, 7]，第二个bar对应的灰度值范围为[8, 15]

第二个参数是一个一维数组，表示每个bar的高度
.ravel()方法将hist_8数组展平，确保其作为一维数组传递给plt.bar，以便每个bin的像素计数能正确地作为条形的高度。

第三个参数 (width=8) 指定了每个bar的宽度占几个单位。在这个例子中，设置为8表示每个条形覆盖8个灰度级的范围，与range(0, 256, 8)生成的序列相匹配，确保直方图的每个bar的宽度都与x坐标轴的相应刻度匹配。
"""
plt.bar(range(0, 256, 8), hist_8.ravel(), width=8)
plt.title("32 Bins Histogram")
plt.xlim([0, 256])

# binwidth等于16的直方图
plt.subplot(1, 3, 3)
plt.bar(range(0, 256, 16), hist_16.ravel(), width=16)
plt.title("16 Bins Histogram")
plt.xlim([0, 256])

plt.show()
