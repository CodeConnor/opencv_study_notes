# ----------------------------------------------------eg.1
# 将图像demo向右移动50像素、向下移动100像素
import cv2
import numpy as np
# 读取图像，获取图像尺寸
img = cv2.imread('../imgs/demo.png')
rows = len(img)  # 图像像素行数
cols = len(img[0])  # 图像像素列数
M = np.float32([[1, 0, 50], [0, 1, 100]])  # 创建仿射矩阵M
dst1 = cv2.warpAffine(img, M, (cols, rows))  # 移动图像
cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.waitKey()
cv2.destroyAllWindows()

# ----------------------------------------------------eg.2
# 让图像逆时针旋转30°的同时缩小到原来的80%
# 使用eg.1中的图像信息：img、rows、cols
center = (rows/2, cols/2)  # 图像的中心店
M = cv2.getRotationMatrix2D(center, 30, 0.8)  # 以图像为中心，逆时针旋转30°，缩放0.8倍
dst2 = cv2.warpAffine(img, M, (cols, rows))  # 按照M缩放
cv2.imshow('img', img)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# ----------------------------------------------------eg.3
# 让图像向右倾斜（图像左上角的点向右移动50像素）
# 使用eg.1中的图像信息：img、rows、cols
