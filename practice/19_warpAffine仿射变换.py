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
p1 = np.zeros((3, 2), np.float32)  # 32位浮点型空列表，原图3个点
p1[0] = [0, 0]          # 左上角A点坐标
p1[1] = [cols-1, 0]     # 右上角B点坐标
p1[2] = [0, rows-1]     # 左下角C点坐标
p2 = np.zeros((3, 2), np.float32)  # 32位浮点型空列表，倾斜图3个点
p2[0] = [50, 0]         # 左上角A点坐标，向右移动50像素
p2[1] = [cols-1, 0]     # 右上角B点坐标，位置不变
p2[2] = [0, rows-1]     # 左下角C点坐标，位置不变
M = cv2.getAffineTransform(p1, p2)  # 计算M矩阵
dst3 = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', img)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()

# ----------------------------------------------------eg.4
# 模拟从底部观察图像得到的透视效果，将图像顶部边缘收窄90像素，底部边缘保持不变
# 使用eg.1中的图像信息：img、rows、cols
p1 = np.zeros((4, 2), np.float32)  # 32位浮点型空列表，原图4个点
p1[0] = [0, 0]              # 左上角A点坐标
p1[1] = [cols-1, 0]         # 右上角B点坐标
p1[2] = [0, rows-1]         # 左下角C点坐标
p1[3] = [cols-1, rows-1]    # 右下角D点坐标
p2 = np.zeros((4, 2), np.float32)  # 32位浮点型空列表，倾斜图4个点
p2[0] = [90, 0]             # 左上角A点坐标，向右移动90像素
p2[1] = [cols-1-90, 0]      # 右上角A点坐标，向左移动90像素
p2[2] = [0, rows-1]         # 左下角C点坐标，位置不变
p2[3] = [cols-1, rows-1]    # 右下角C点坐标，位置不变
M = cv2.getPerspectiveTransform(p1, p2)  # 计算变换矩阵
dst4 = cv2.warpPerspective(img, M, (cols, rows))  # 三维空间的仿射
cv2.imshow('img', img)
cv2.imshow('dst4', dst4)
cv2.waitKey()
cv2.destroyAllWindows()

