import cv2
import numpy as np

image = cv2.imread("Lenna.jpg")

# 获取图片的宽高（单位px）
height, width, _ = image.shape

# 截取4个子图像
sub_images = []
width_sub_image = 80
height_sub_image = 80
for i in range(4):
    top_start = np.random.randint(0, height- height_sub_image)
    left_start = np.random.randint(0, width-width_sub_image)
    sub_image = image[top_start : top_start + height_sub_image, 
                      left_start : left_start + width_sub_image,
                      :]
    print(f"CHIP{i}:")
    print(sub_image)
    sub_images.append(sub_image)
    
new_image = np.hstack(sub_images)
print(new_image)
cv2.imshow('New Image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()