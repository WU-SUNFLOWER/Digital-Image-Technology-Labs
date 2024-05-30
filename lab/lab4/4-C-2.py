import cv2
import numpy as np

# 读取图像
img = cv2.imread('region_bright.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用一个简单的阈值来搜索所有亮点
brightest = 210
_, bright_regions = cv2.threshold(img, brightest, 255, cv2.THRESH_BINARY)

cv2.imshow('Bright Region', bright_regions)

# 获取所有亮点的坐标
bright_points = np.where(bright_regions > 0)
rows, cols = bright_points
size = rows.shape[0]

# 漫水填充
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
flooded = img.copy()
for i in range(size):
    col, row = cols[i], rows[i]
    if mask[row+1, col+1] == 0:
        cv2.floodFill(flooded, mask, (col, row), 0, 3, 3)

# 应用二值化将分割区域变为白色
_, flooded = cv2.threshold(flooded, 1, 255, cv2.THRESH_BINARY_INV)

# 计算分割区域的宽度和高度
x,y,w,h = cv2.boundingRect(flooded)
crack_width = w
crack_height = h

print(f'Crack Width: {crack_width} pixels')
print(f'Crack Height: {crack_height} pixels')

brcnt = np.array([
    [[x,y]],
    [[x+w, y]], 
    [[x+w, y+h]], 
    [[x,y+h]]
])
cv2.drawContours(img, [brcnt], -1, 0, 2)

cv2.imshow('Image', img)
cv2.imshow('FloodFilled Crack', flooded)

cv2.waitKey(0)
cv2.destroyAllWindows()