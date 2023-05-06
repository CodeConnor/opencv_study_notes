import cv2
import numpy as np

# 均值滤波
# 分别使用大小为3×3、5×5和9×9的滤波核对花朵图像amygdalus triloba.jpg进行均值滤波操作
flower = cv2.imread('../imgs/amygdalus triloba.jpg')
# 均值滤波操作
dst1 = cv2.blur(flower, (3, 3))
dst2 = cv2.blur(flower, (5, 5))
dst3 = cv2.blur(flower, (9, 9))
# 显示图像
cv2.imshow('flower', flower)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()