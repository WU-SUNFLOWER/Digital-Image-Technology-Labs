import cv2
import numpy as np

# 读入图像
img = cv2.imread('j_outnoise.png', cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

# 定义结构元素
kernel = np.ones((6,6), np.uint8)

# 执行开运算
opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 显示结果
cv2.imshow('Original Image', img)
cv2.imshow('Opened Image', opened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('j_innoise.png', cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
closed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Opened Image', closed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()