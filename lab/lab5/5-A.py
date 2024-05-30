import cv2
import numpy as np

# 读入图像
img = cv2.imread('linux.jpg')

# 转换成灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
对图像进行阈值化处理
cv2.THRESH_BINARY表示图像中灰度值小于thresh的像素置为0
大于thresh的像素置为maxval
"""
ret, thresh_img = cv2.threshold(gray_img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

# 腐蚀运算
kernel = np.ones((5,5), np.uint8)
eroded_img = cv2.erode(thresh_img, kernel, iterations=1)

# 显示结果
cv2.imshow('Original Image', img)
cv2.imshow('Thresh Image', thresh_img)
cv2.imshow('Eroded Image', eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 膨胀运算
dilate_img = cv2.dilate(thresh_img, kernel, iterations=1)
dilate_again_img = cv2.dilate(dilate_img, kernel, iterations=1)

cv2.imshow('Thresh Image', thresh_img)
cv2.imshow('Dilate Image', dilate_img)
cv2.imshow('Dilate Again Image', dilate_again_img)
cv2.waitKey(0)
cv2.destroyAllWindows()