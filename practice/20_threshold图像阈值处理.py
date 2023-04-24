# retval, dst = cv2.threshold(src, thresh, maxval, type)
# 参数说明：
# src：被处理的图像，可以是多通道图像。
# thresh：阈值，阈值在125～150取值的效果最好。
# maxval：阈值处理采用的最大值。
# type：阈值处理类型。
# type有下面这些常用类型：
#   cv2.THRESH_BINARY: 二值化阈值。超过阈值的像素值将被设为最大值（一般为255），低于阈值的像素值将被设为0。
#   cv2.THRESH_BINARY_INV: 反二进制阈值。超过阈值的像素值将被设为0，低于阈值的像素值将被设为最大值（一般为255）。
#   cv2.THRESH_TRUNC: 截断阈值。超过阈值的像素值将被设为阈值，低于阈值的像素值将保持不变。
#   cv2.THRESH_TOZERO: 零阈值。低于阈值的像素值将被设为0，超过阈值的像素值将保持不变。
#   cv2.THRESH_TOZERO_INV: 反零阈值。超过阈值的像素值将被设为0，低于阈值的像素值将保持不变。
# 返回值说明：
# retval：处理时采用的阈值。
# dst：经过阈值处理后的图像

# --------------------------------------------------------eg.1
# 进行阈值处理，取0~255的中间值127作为阈值，将255作为最大值
import cv2

img = cv2.imread('../imgs/black.png', 0)  # 将图像读取为灰度图，用彩色图直接二值化图片中间会出现蓝色或者红色线
t1, dst1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 二值化
t2, dst2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 反二值化
t3, dst3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # 零阈值
t4, dst4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 反零阈值
t5, dst5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 截断阈值
# 显示图像
cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.imshow('dst5', dst5)
cv2.waitKey()
cv2.destroyAllWindows()
