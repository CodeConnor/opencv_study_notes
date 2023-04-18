import cv2
import numpy as np
import matplotlib.pyplot as plt
# 先拆分图5.1中的通道，再显示拆分后的通道图像，再合并通道显示图像
img1 = cv2.imread('../imgs/5.1.jpg')
# 拆分
b, g, r = cv2.split(img1)
# 显示
cv2.imshow('B', b)
cv2.imshow('G', g)
cv2.imshow('R', r)
# 合并
img1_BGR = cv2.merge([b, g, r])
cv2.imshow('BGR', img1_BGR)
cv2.waitKey()
cv2.destroyAllWindows()

# 首先将图5.1从BGR色彩空间转换到HSV色彩空间
# 然后拆分得到的HSV图像中的通道，显示拆分后的通道图像
# 接着合并拆分后的通道图像，最后将合并通道后的图像从HSV色彩空间转换到BGR色彩空间
img2 = cv2.imread('../imgs/5.1.jpg')
img2_HSV = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
# 拆分
h, s, v = cv2.split(img2_HSV)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)
# 合并
img2_merge = cv2.merge([h, s, v])
cv2.imshow('merge', img2_merge)
cv2.waitKey()
cv2.destroyAllWindows()

# 首先将图5.1从BGR色彩空间转换到HSV色彩空间；然后拆分HSV图像中的通道；
# 接着让S通道和V通道的值保持不变，把H通道的值调整为180；
# 再接着合并拆分后的通道图像，把这个图像从HSV色彩空间转换到BGR色彩空间；最后显示得到的BGR图像
# 把V通道的值调整为255，把S通道的值调整为255
img3 = cv2.imread('../imgs/5.1.jpg')
img3_HSV = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
# 拆分, 修改值
h, s, v = cv2.split(img2_HSV)
# h[:, :] = 180
s[:, :] = 255
# v[:, :] = 255
# cv2.imshow('h180', h)
cv2.imshow('s255', h)
# cv2.imshow('v255', h)

# 合并
img3_merge = cv2.merge([h, s, v])
cv2.imshow('merge', img3_merge)
cv2.waitKey()
cv2.destroyAllWindows()


