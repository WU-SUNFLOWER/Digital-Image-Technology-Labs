import cv2
im = cv2.imread('Flower.png')
cv2.imshow('The 1st Window', im)
# waitKey(x) 表示等待x秒继续执行
# waitKey(0) 表示无限等待直到用户按下键盘
cv2.waitKey(0)
cv2.destroyAllWindows()