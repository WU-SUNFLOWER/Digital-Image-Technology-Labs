import cv2
import numpy as np

def transformer(val):
    if 0 <= val and val <= 88:
        ans = val * 60 / 88
    elif 88 < val and val <= 162:
        ans = (val - 88) * 140 / 74 + 60
    elif 162 < val and val <= 255:
        ans = (val - 162) * 56 / 94 + 200
    else:
        raise "Invalid grayscale value"
    return round(ans)
        
image = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)

result = image.copy()

rows, cols = image.shape
for i in range(0, rows):
    for j in range(0, cols):
        result[i][j] = transformer(image[i][j])
        
cv2.imshow("Original Image", image)
cv2.imshow("Result Image", result)
cv2.waitKey()
cv2.destroyAllWindows()