import cv2
import numpy as np

# 生成图像
size = 256
h = size // 8
image = np.zeros((size, size), dtype=np.uint8)
for i in range(1, 8, 2):
    image[i * h : (i + 1) * h] = 255

# 计算频谱图
dft_ori = cv2.dft(np.float32(image), flags=cv2.DFT_SCALE | cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft_ori)
spectrum = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])

# 转置DFT函数
dft_shift = dft_shift.transpose((1, 0, 2))
spectrum_t = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])

image_new = cv2.idft(np.fft.ifftshift(dft_shift))
image_new = cv2.magnitude(image_new[:,:,0], image_new[:,:,1])
image_new = image_new.astype(np.uint8).clip(0, 255)

cv2.imshow("image", image)
cv2.imshow("spectrum", spectrum)
cv2.imshow("spectrum t", spectrum_t)
cv2.imshow("new image", image_new)
cv2.waitKey()
cv2.destroyAllWindows()