import cv2
import numpy as np

# 读取图像
image = cv2.imread('coins.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 预处理图像: 高斯模糊
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# 边缘检测
edges = cv2.Canny(blurred, 30, 150)

cv2.imshow("after canny", edges)

# 形态学操作: 闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6, 6))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cv2.imshow("after close", closed)

# 查找轮廓
contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最小和最大半径
min_radius = float('inf')
max_radius = float('-inf')

for contour in contours:
    # 计算最小外接圆
    (x, y), radius = cv2.minEnclosingCircle(contour)
    radius = int(radius)

    # 更新最小和最大半径
    if radius < min_radius:
        min_radius = radius
    if radius > max_radius:
        max_radius = radius

# 打印最小和最大半径
print(f"最小半径: {min_radius} 像素")
print(f"最大半径: {max_radius} 像素")

# 可视化结果
output = image.copy()
for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    cv2.circle(output, (int(x), int(y)), int(radius), (0, 255, 0), 2)

cv2.imshow('Detected Coins', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
