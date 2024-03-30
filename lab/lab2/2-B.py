import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lenna.jpg')

blue_channel, green_channel, red_channel = cv2.split(image)

dst = cv2.equalizeHist(blue_channel)

plt.figure()
plt.hist(blue_channel.ravel(), 64, [0, 256], color='b')
plt.hist(dst.ravel(), 64, [0, 256], color='r')
plt.show()