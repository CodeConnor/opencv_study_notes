# 读取一幅图像，让该图像自己对自己做加法运算，分别使用“+”运算符和add()方法
import cv2
import numpy as np

img = cv2.imread('../imgs/beach.jpg')
sum1 = img + img
sum2 = cv2.add(img, img)
cv2.imshow('img', img)
cv2.imshow('+', sum1)
cv2.imshow('add', sum2)
cv2.waitKey()
cv2.destroyAllWindows()
# 从结果可以看出，“+”运算符的计算结果如果超出了255，就会取相加和除以255的余数，也就是取模运算，像素值相加后反而变得更小，由浅色变成了深色；
# 而add()方法的计算结果如果超过了255，就取值255，很多浅颜色像素彻底变成了纯白色。


# 创建纯蓝和纯红2幅图像，使用add()方法对2幅图像进行加法运算，并在方法中添加一个掩模
# 创建纯色图像
blue = np.zeros((150, 150, 3), np.uint8)
blue[:, :, 0] = 255
red = np.zeros((150, 150, 3), np.uint8)
red[:, :, 2] = 255
# 两图像相加
img = cv2.add(blue, red)
cv2.imshow('no mask', img)
# 创建掩模
m = np.zeros((150, 150, 1), np.uint8)  # 掩模必须是单通道，否则报错
m[50:100, 50:100] = 255
cv2.imshow('mask', m)
# 添加掩模相加
img_m = cv2.add(blue, red, mask=m)
cv2.imshow('use mask', img_m)

cv2.waitKey()
cv2.destroyAllWindows()
