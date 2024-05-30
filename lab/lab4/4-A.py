import cv2

image = cv2.imread('Flower.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 法表示梯度值的门限:
#   threshold1: 第一个阈值，任何梯度小于此值的都不被认为是边缘。
#   threshold2: 第二个阈值，任何梯度大于此值的一定是边缘。
edges = cv2.Canny(gray_image, threshold1=50, threshold2=200)

cv2.imshow("Egdes", edges)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2.findContours函数的参数:
#   image: 输入图像（这里是Canny边缘检测的结果）。
#   mode: 轮廓检索模式（RETR_TREE检索所有轮廓并重构嵌套轮廓的完整层级）。
#   method: 轮廓逼近方法（CHAIN_APPROX_SIMPLE压缩水平、垂直和对角线段，仅保留它们的端点）。
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours函数的参数:
#   image: 输入图像（这里是原始图像）。
#   contours: 轮廓列表。
#   contourIdx: 轮廓索引（-1表示绘制所有轮廓）。
#   color: 轮廓颜色。
#   thickness: 轮廓线的厚度。
contoured_image = image.copy()
cv2.drawContours(contoured_image, contours, -1, (0, 255, 0), 3)

cv2.imshow("Egdes", contoured_image)
cv2.waitKey()
cv2.destroyAllWindows()