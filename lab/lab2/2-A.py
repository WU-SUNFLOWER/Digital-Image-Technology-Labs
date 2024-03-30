import cv2
import numpy as np

image = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)

###  PART 1 START   ###
image_blur = cv2.blur(image, ksize=(3, 3))

# 高斯模糊中sigma调得越大，图像越模糊
image_gaussian_blur = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=1)
image_gaussian_blur2 = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=100000)

# 中值滤波不依赖卷积运算，因此它的核只有一个参数，表示进行取中值运算邻域的大小
image_median_blur = cv2.medianBlur(image, 3) 

cv2.imshow('Original Image', image)
cv2.imshow('Blur Test', image_blur)
cv2.imshow('Median Blur Test', image_median_blur)
cv2.imshow('Gaussian Blur 10', image_gaussian_blur)
cv2.imshow('Gaussian Blur 1000', image_gaussian_blur2)

cv2.waitKey()
cv2.destroyAllWindows()
###   PART 2 END ###

### PART2 START ###
"""
第二个参数是输出图像的深度，cv2.CV_64F是一种64位浮点数类型，可以获取梯度的正负变化。
第三和第四个参数分别是dx和dy，代表X方向和Y方向的导数（差分）阶数，设置为1表示计算该方向的一阶导数，另一个方向设置为0。
最后一个参数ksize是Sobel算子的大小，它可以是1, 3, 5, 或7。算子的大小影响图像的平滑程度和边缘检测的灵敏度。
"""
sobelx = cv2.Sobel(image_gaussian_blur, cv2.CV_64F, 2, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(image_gaussian_blur, cv2.CV_64F, 0, 2, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
laplacian = cv2.Laplacian(image_gaussian_blur, cv2.CV_64F, ksize=3)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow('Original Image', image_gaussian_blur)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Laplacian', laplacian)

cv2.waitKey()
cv2.destroyAllWindows()
### PART2 END ###

### PART3 START ###
ker_emb = np.array((
    [-4, -2, 0],
    [-1, 1, 1],
    [0, 2, 4]
), dtype="float32")

# 一键进行图像卷积
filtered_img = cv2.filter2D(image, -1, ker_emb)
filtered_img = cv2.convertScaleAbs(filtered_img)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", filtered_img)

cv2.waitKey()
cv2.destroyAllWindows()

### PART3 END ###