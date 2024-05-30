import cv2
import numpy as np

image = cv2.imread("circles.jpg")

image_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", image)

_, image_thresh = cv2.threshold(image_thresh, thresh=87, maxval=255, type=cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))

outline = cv2.morphologyEx(image_thresh, cv2.MORPH_GRADIENT,kernel)

cv2.imshow("Outline", outline)

image_processed = image.copy()

for pos in np.argwhere(outline == 255):
    i, j = pos
    image_processed[i, j] = [0, 0, 255]

cv2.imshow("Processed Image", image_processed)

cv2.waitKey()
cv2.destroyAllWindows()