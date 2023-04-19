# 将一个图像按照宽100像素、高100像素的大小进行缩小，再按照宽400像素、高400像素的大小进行放大
import cv2
img = cv2.imread('../imgs/demo.png')
dst1 = cv2.resize(img, (100, 100))  # 缩小
dst2 = cv2.resize(img, (400, 400))  # 放大
cv2.imshow('img', img)
cv2.imshow('100x100', dst1)
cv2.imshow('400x400', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# 将一个图像宽缩小到原来的1/3、高缩小到原来的1/2，再将图像宽放大2倍，高也放大2倍
dst3 = cv2.resize(img, None, fx=1/3, fy=1/2)
dst4 = cv2.resize(img, None, fx=2, fy=2)
cv2.imshow('img', img)
cv2.imshow('x1/3', dst3)
cv2.imshow('x2', dst4)
cv2.waitKey()
cv2.destroyAllWindows()

