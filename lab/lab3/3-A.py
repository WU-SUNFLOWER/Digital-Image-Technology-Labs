import cv2
import numpy as np

# opencv读取的图片数值为BGR格式
image = cv2.imread("Lenna.jpg")
blue_channel, green_channel, red_channel = cv2.split(image)

### PART A START ###

# 傅里叶变换，得到一个含两个matrix的tensor
# 两个matrix分别为变换结果的实数部分和虚数部分
dft_ori = cv2.dft(np.float32(green_channel[100:110, 100:110]), flags=cv2.DFT_COMPLEX_OUTPUT)

# 计算频谱
# magnitude = sqrt(a^2 + b^2)
spectrum = cv2.magnitude(dft_ori[:,:,0], dft_ori[:,:,1])
print(spectrum[0:10, 0:10])

### PART A END ###

### PART B START ###

# 创建圆形低通滤波器
def create_low_pass_mask(radius, height, width):
    mask = np.zeros((height, width), np.uint8)
    cy, cx = int(height / 2), int(width / 2)
    y, x = np.ogrid[:height, :width]
    mask_area = (y - cy) ** 2 + (x - cx) ** 2 <= radius ** 2
    mask[mask_area] = 1
    return mask

height, width = green_channel.shape
dft_ori = cv2.dft(np.float32(green_channel), flags=cv2.DFT_COMPLEX_OUTPUT)

# 将频率坐标原点移到中心
dft_shift = np.fft.fftshift(dft_ori)

radius_list = [12, 24, 32]
for radius in radius_list:
    mask = create_low_pass_mask(radius, height, width)
    dft_filtered = dft_shift * mask[:,:,np.newaxis]
    # 逆DFT
    f_ishift = np.fft.ifftshift(dft_filtered)
    image_new = cv2.idft(f_ishift, flags=cv2.DFT_SCALE)
    image_new = cv2.magnitude(image_new[:,:,0], image_new[:,:,1])
    image_new = image_new.astype(np.uint8).clip(0, 255)
    cv2.imshow(f"idft radius={radius}", image_new)    

cv2.waitKey()
cv2.destroyAllWindows()

### PART B END ###

### PART C START ###

"""
取红色分量图像左上角为(100,100)，大小为 8*8 的一个正方形区域，作傅立叶变换，且计算频谱，根据频谱的中心对称特征，找出分别与位置
(2，3)，(3，2)，(3，5)频谱值相等的坐标位置。
"""

size = 8
square_area = red_channel[100:100 + size, 100:100 + size]
dft_ori = cv2.dft(np.float32(square_area), flags=cv2.DFT_COMPLEX_OUTPUT)
print("由共轭对称性可知：")
points = [[2, 3], [3, 2], [3, 5]]
for point in points:
    v, u = point
    print(f"DFT[{u},{v}]={dft_ori[v, u]}, DFT[{size - u}, {size - v}]={dft_ori[size - v, size - u]}")

### PART C END ###

### PART D START ###
image_face = cv2.imread('LennaFace.png', cv2.IMREAD_GRAYSCALE)
image_ref = cv2.imread('Flower_1x1.png', cv2.IMREAD_GRAYSCALE)
height, width = image_face.shape

# 计算image_face的DFT
dft_face = cv2.dft(np.float32(image_face), flags=cv2.DFT_COMPLEX_OUTPUT)

# 计算image_ref的DFT
dft_ref = cv2.dft(np.float32(image_ref), flags=cv2.DFT_COMPLEX_OUTPUT)
spectrum = cv2.magnitude(dft_ref[:,:,0], dft_ref[:,:,1])

# 混合
dft_face += dft_ref * 0.3

# 重建图像
image_new = cv2.idft(dft_face, flags=cv2.DFT_SCALE)
image_new = cv2.magnitude(image_new[:,:,0], image_new[:,:,1])

image_new = image_new.astype(np.uint8).clip(0, 255)



cv2.imshow('orignal', image_face)
cv2.imshow('test', image_new)
cv2.waitKey()
cv2.destroyAllWindows()

### PART D END ###