# 分别让图像沿X轴翻转，沿Y轴翻转，同时沿X轴、Y轴翻转，查看翻转的效果
import cv2
img = cv2.imread('../imgs/demo.png')
dst1 = cv2.flip(img, 0)
dst2 = cv2.flip(img, 1)
dst3 = cv2.flip(img, -1)
cv2.imshow('img', img)
cv2.imshow('X', dst1)
cv2.imshow('Y', dst2)
cv2.imshow('XY', dst3)
cv2.waitKey()
cv2.destroyAllWindows()
