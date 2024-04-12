import cv2
import numpy as np

def compute_spectrum(image):
    dft_ori = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT | cv2.DFT_SCALE)
    dft_shift = np.fft.fftshift(dft_ori)
    spectrum = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])
    return spectrum

image = cv2.imread("LennaFace.png", cv2.IMREAD_GRAYSCALE)
image_equalized = cv2.equalizeHist(image)


# 计算幅度谱
s1 = compute_spectrum(image)
s2 = compute_spectrum(image_equalized)

# 显示结果
image_result = np.hstack([image, image_equalized])
s_result = np.hstack([s1, s2])
cv2.imshow("image_result", image_result)
cv2.imshow("s_result", s_result)

cv2.waitKey()
cv2.destroyAllWindows()