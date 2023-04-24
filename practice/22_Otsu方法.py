# 对于有些图像，当阈值被设置为127时，得到的效果并不好，这时就需要一个个去尝试，直到找到最合适的阈值。
# 逐个寻找最合适的阈值不仅工作量大，而且效率低。
# 为此，OpenCV提供了Otsu方法。Otsu方法能够遍历所有可能的阈值，从中找到最合适的阈值。
import cv2

img = cv2.imread('../imgs/4.36.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t1, dst1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)  # 二值化处理
t2, dst2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Otsu方法
print(f'best threshold:{t2}')
cv2.imshow('img', img_gray)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
