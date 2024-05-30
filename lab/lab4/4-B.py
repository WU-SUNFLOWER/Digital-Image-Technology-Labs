import cv2
import numpy as np

image = cv2.imread('building.png')

def get_edges(image):
    edges = cv2.Canny(
        image, 
        threshold1=100, 
        threshold2=150
    )
    return edges

def get_lines(image):
    return cv2.HoughLinesP(image, rho=1, theta=np.pi / 180, threshold=180)
    
def draw(image, lines):
    lines = sorted(
        lines, 
        key=lambda x: (x[0][0] - x[0][2]) ** 2 + (x[0][1] - x[0][3]) ** 2,
        reverse=True
    )
    lines = lines[:5]
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)    

ksize_ar = [1, 3, 5, 7, 9]
for ksize in ksize_ar:
    image_blurred = cv2.medianBlur(image, ksize)
    edges = get_edges(image_blurred)
    lines = get_lines(edges)
    draw(image_blurred, lines)
    cv2.imshow(f'Hough Lines with blurred kernel {ksize}', image_blurred)
   
cv2.waitKey()
cv2.destroyAllWindows()