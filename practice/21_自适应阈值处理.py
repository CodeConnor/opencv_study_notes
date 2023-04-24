# 当图像色彩不均匀时，如果只使用一种阈值处理类型，就无法得到清晰有效的结果。
# 这时可以使用自适应处理，能更好地处理明暗分布不均的图像，获得更简单的图像效果。
import cv2

img = cv2.imread('../imgs/4.27.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst_MEAN = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
dst_GAUS = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
cv2.imshow('GRAY', img_gray)
cv2.imshow('MEAN', dst_MEAN)
cv2.imshow('GAUS', dst_GAUS)
cv2.waitKey()
cv2.destroyAllWindows()