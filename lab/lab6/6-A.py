import cv2
import numpy as np

image = cv2.imread('Flower.png')
qualities = [60, 80, 90]

for i in range(len(qualities)):
    cv2.imwrite(f'Temp{i}.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), qualities[i]])

for i in range(len(qualities)):
    new_image = cv2.imread(f'Temp{i}.jpg')
    # PSNR越大，图像质量越好
    print(f"Temp{i}.jpg quality={qualities[i]} PSNR={cv2.PSNR(new_image, image)}")

channels = cv2.split(image)
green_channel = channels[1]

kernel1 = (1 / 9) * np.ones((3, 3))
kernel2 = (1 / 16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

image1 = cv2.filter2D(green_channel, -1, kernel1)
image2 = cv2.filter2D(green_channel, -1, kernel2)

print(f"image1 PSNR={cv2.PSNR(image1, green_channel)}")
print(f"image2 PSNR={cv2.PSNR(image2, green_channel)}")