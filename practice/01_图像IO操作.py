import cv2  # opencv默认读取格式是BRG
import matplotlib.pyplot as plt
import numpy as np

# 读取图片
img = cv2.imread('../imgs/cat.jpg')

# cv2显示图片
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# matplotlib显示
plt.imshow(img[:, :, ::-1])  # 使用切片将BGR转换成RGB
plt.show()

# 使用函数转换图像属性
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_RGB)
plt.show()
