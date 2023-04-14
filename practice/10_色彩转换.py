import cv2
import matplotlib.pyplot as plt

# 将图5.1从BGR色彩空间转换到GRAY色彩空间
img = cv2.imread('../imgs/5.1.jpg')
cv2.imshow('img', img)
# 转换色彩空间
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img_gray)
cv2.waitKey()
cv2.destroyAllWindows()

# 将图5.1从BGR色彩空间转换到HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', img_hsv)
cv2.waitKey()
cv2.destroyAllWindows()

# 使用matplotlib进行显示，显示的默认通道是RGB
# 如果不将图片由BGR转换为RGB，显示的图像颜色会出错
plt.imshow(img)
plt.show()
# 通过切片转换
img_RGB = img[:, :, ::-1]
# 还可通过cvt方法转换: img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_RGB)
plt.show()
