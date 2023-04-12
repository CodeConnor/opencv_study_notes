import cv2


# 读取彩图
img = cv2.imread('../imgs/cat.jpg', 1)  # 1 = cv2.IMREAD_COLOR
# 输出彩图属性
print(img.shape)

# 读取灰度图
img = cv2.imread('../imgs/cat.jpg', 0)  # 0 = cv2.IMREAD_GRAYSCALE
# 输出灰度图属性
print(img.shape)  # 通道数为1
# 展示灰度图
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


