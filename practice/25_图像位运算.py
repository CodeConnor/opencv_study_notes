# 按位与运算
# 创建一个掩模，在掩模中央保留一个十字形的白色区域，让掩模与花图像做位运算
import numpy as np
import cv2

flower = cv2.imread('../imgs/amygdalus triloba.png')
mask = np.zeros(flower.shape, np.uint8)
mask[120:180, :] = 255
mask[:, 80:180] = 255
img_and = cv2.bitwise_and(flower, mask)  # 按位与运算
img_or = cv2.bitwise_or(flower, mask)  # 按位或运算
img_not = cv2.bitwise_not(flower)  # 按位取反运算
img_xor = cv2.bitwise_xor(flower, mask)  # 按位异或运算
cv2.imshow('flower', flower)
cv2.imshow('mask', mask)
cv2.imshow('and', img_and)
cv2.imshow('or', img_or)
cv2.imshow('not', img_not)
cv2.imshow('xor', img_xor)
cv2.waitKey()
cv2.destroyAllWindows()
