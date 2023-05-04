# 导入模块
import cv2
import numpy as np

# 梯度运算 = 膨胀图 - 腐蚀图
# 顶帽运算 = 原图 - 开运算图
# 黑帽运算 = 闭运算图 - 原图
# 使用5×5的核对小蜘蛛图像spider.png进行三种形态学运算
spider = cv2.imread('../imgs/spider.png')
spider2 = cv2.imread('../imgs/spider2.png')
k = np.ones((5, 5), np.uint8)  # 核
dst1 = cv2.morphologyEx(spider, cv2.MORPH_GRADIENT, k)  # 1、梯度运算
dst2 = cv2.morphologyEx(spider, cv2.MORPH_TOPHAT, k)  # 2、顶帽运算
dst3 = cv2.morphologyEx(spider2, cv2.MORPH_BLACKHAT, k)  # 3、黑帽运算
cv2.imshow('spider', spider)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()


