# 创建一个100行、200列（即宽200、高100）的数组，
# 数组元素格式为无符号8位整数，用0填充整个数组，将该数组当作图像显示出来
import cv2
import numpy as np
# 图像高和宽
height = 100
width = 200
# 创建图像，数组用0填充
img_black = np.zeros([height, width], dtype=np.uint8)
cv2.imshow('black', img_black)
cv2.waitKey()
cv2.destroyAllWindows()


# 创建一个100行、200列（即宽200、高100）的数组，数组元素格式为无符号8位整数
# 用1填充整个数组，然后让数组乘以255，最后将该数组当作图像显示出来
# 图像高和宽
height = 100
width = 200
# 创建图像用1填充，再乘以255
img_white = np.ones([100, 200], dtype=np.uint8) * 255
cv2.imshow('white', img_white)
cv2.waitKey()
cv2.destroyAllWindows()

# 先绘制纯黑图像作为背景，然后使用切片式索引操作将图像中横坐标为50~100、纵坐标为25~75的矩形区域颜色改为纯白色
# 图像高和宽
h1 = 100
w1 = 200
# 创建图像，数组用0填充
img1 = np.zeros([h1, w1], dtype=np.uint8)
# 将图像切片，修改切片区域为白色
img1[25:76, 50:101] = 255
cv2.imshow('img1', img1)
cv2.waitKey()
cv2.destroyAllWindows()

# 先绘制纯黑图像作为背景
# 然后在循环中使用切片式索引操作绘制黑白间隔图像
# 白色宽度为20
h2 = 100
w2 = 200
img2 = np.zeros([h2, w2], dtype=np.uint8)
# 遍历范围是图片宽度，步长40（白色黑色宽度各20）
for i in range(0, w2, 40):
    # 白色区域
    img2[:, i:i + 20] = 255
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()

# 创建彩色图像数组时要将数组创建成三维数组，元素类型仍然为无符号8位整数。
# 创建好表示纯黑图像的三维数组后，复制出3个副本，3个副本分别修改最后一个索引代表的元素值。
# 根据BGR的顺序，索引0表示蓝色分量，索引1表示绿色分量，索引2表示红色分量
# 让3个副本分别显示纯蓝、纯绿和纯红
h3 = 100
w3 = 200
img3 = np.zeros([h3, w3, 3], dtype=np.uint8)
blue = img3.copy()  # 创建图像副本
blue[:, :, 0] = 255  # 显示纯蓝
green = img3.copy()
green[:, :, 1] = 255
red = img3.copy()
red[:, :, 2] = 255
# 显示所有图片
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)
cv2.waitKey()
cv2.destroyAllWindows()

# 使用NumPy提供的random.randint()方法就可以创建随机数组，
# 将随机值的取值范围设定在0～256（即像素值范围），元素类型设定为无符号8位整数
h4 = 100
w4 = 200
# 生成黑白随机图片
img4 = np.random.randint(256, size=[h4, w4], dtype=np.uint8)
# 随机彩色图像
img5 = np.random.randint(256, size=[h4, w4, 3], dtype=np.uint8)
cv2.imshow('img4', img4)
cv2.imshow('img5', img5)
cv2.waitKey()
cv2.destroyAllWindows()
