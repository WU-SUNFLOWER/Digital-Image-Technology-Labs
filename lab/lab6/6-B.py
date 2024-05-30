import cv2
import numpy as np

def foo(block, factor):
    dct = cv2.dct(block.astype(np.float32))
    dct = np.floor(dct / factor) * factor
    return cv2.idct(dct).astype(np.uint8)

def compute_std(original, processed):
    size = original.shape[0] * original.shape[1]
    ret = np.sqrt(np.sum((original - processed) ** 2) / size)
    return ret

image = cv2.imread('lenna.jpg')
channels = cv2.split(image)
green_channel = channels[1]
block = green_channel[0:500, 0:500]

new_block1 = foo(block, 8)
new_block2 = foo(block, 16)

cv2.imshow('Block', block)
cv2.imshow('Block1', new_block1)
cv2.imshow('Block2', new_block2)

# factor越大，丢失的信息越多，std越大
print(f"Block1 factor=8 std={compute_std(new_block1, block)}")
print(f"Block2 factor=16 std={compute_std(new_block2, block)}")

cv2.waitKey()
cv2.destroyAllWindows()