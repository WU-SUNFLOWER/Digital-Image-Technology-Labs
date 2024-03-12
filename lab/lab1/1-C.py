import cv2

# 读取图像
image = cv2.imread('Flower.png')

# 指定矩形区域的左上角和右下角坐标
top_left = (400, 360)
bottom_right = (670, 660)

# 复制原图像以便操作
image_copy = image.copy()

# 将所选区域的颜色转换为补色
# 注意：OpenCV中的图像格式是BGR而不是RGB
# 在NumPy数组中，表示图像时，数组的形状通常是（高度，宽度，通道数）
image_copy[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = \
    255 - image_copy[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

# 显示原图像和修改后的图像
cv2.imshow('Modified Image', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
