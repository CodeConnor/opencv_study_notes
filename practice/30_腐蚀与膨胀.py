import cv2
import numpy as np

# 使用3×3的核对仙人球图像cactus.jpg进行腐蚀操作
cactus = cv2.imread('../imgs/cactus.jpg')
k = np.ones((3, 3), np.uint8)  # 创建3x3的数组作为核
dst1 = cv2.erode(cactus, k)  # 腐蚀操作
cv2.imshow('cactus', cactus)
cv2.imshow('dst', dst1)
cv2.waitKey()
cv2.destroyAllWindows()

# 近视眼由于聚焦不准，看东西都需要放大并且模模糊糊的，利用膨胀操作可以将正常画面处理成近视眼看到的画面
# 处理sunset.jpg
sunset = cv2.imread('../imgs/sunset.jpg')
k = np.ones((9, 9), np.uint8)
dst2 = cv2.dilate(sunset, k)  # 膨胀操作
cv2.imshow('sunset', sunset)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# 开运算 = 先腐蚀再膨胀
# 抹除黑种草图像中的针状叶子, nigella.png, 使用5×5的核对图像进行开运算
nigella = cv2.imread('../imgs/nigella.png')
k = np.ones((5, 5), np.uint8)  # 5x5的核
dst_1 = cv2.erode(nigella, k)  # 腐蚀
dst_nigella = cv2.dilate(dst_1, k)  # 膨胀
cv2.imshow('nigella', nigella)
cv2.imshow('dst', dst_nigella)
cv2.waitKey()
cv2.destroyAllWindows()

# 闭运算 = 先膨胀再腐蚀
# 对汉字图片进行闭运算，使用15×15的核对tianye.png做闭运算
tianye = cv2.imread('../imgs/tianye.png')
k = np.ones((15, 15), np.uint8)  # 核
dst_2 = cv2.dilate(tianye, k)  # 膨胀
dst_tianye = cv2.erode(dst_2, k)  # 腐蚀
cv2.imshow('tianye', tianye)
cv2.imshow('dst', dst_tianye)
cv2.waitKey()
cv2.destroyAllWindows()

