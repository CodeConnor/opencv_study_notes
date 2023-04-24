# 加权合并，addWeighted()方法
# 读取两幅不同的风景照片，使用addWeighted()方法计算两幅图像的加权和，两幅图像的权重都为0.6，标量为0
import cv2

sun = cv2.imread('../imgs/sunset.jpg')
beach = cv2.imread('../imgs/beach.jpg')
rows, cols, channel = sun.shape  # sun的图像尺寸
beach = cv2.resize(beach, (cols, rows))  # 将beach缩放为sun图像大小
img = cv2.addWeighted(sun, 0.6, beach, 0.6, 0)  # 计算加权和
cv2.imshow('sun', sun)
cv2.imshow('beach', beach)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# 覆盖图像就是直接把前景图像显示在背景图像中，前景图像挡住背景图像。
# 直接用修改图像像素值的方式实现图像的覆盖、拼接效果：从A图像中取像素值，直接赋值给B图像的像素
# 读取小猫原始图像，将原始图像中75～400行、120～260列的像素单独保存成一幅小猫图像，并将小猫图像缩放成70×160大小。
# 读取沙滩图像，将小猫图像覆盖到沙滩图像(100, 200)的坐标位置。覆盖过程中将小猫图像的像素逐个赋值给沙滩图像中对应位置的像素
img1 = cv2.imread('../imgs/cat.jpg')  # cat原图
cv2.imshow('cat_img1', img1)
cat = cv2.resize(img1[75:400, 120:260, :], (70, 160))  # 截取并缩放cat
cv2.imshow('cat', cat)
beach = cv2.imread('../imgs/beach.jpg')  # beach原图
cv2.imshow('beach', beach)
rows, cols, c = cat.shape  # 记录截取图像的行数和列数
beach[100:100+rows, 200:200+cols, :] = cat  # 覆盖图像
cv2.imshow('beach_cat', beach)
cv2.waitKey()
cv2.destroyAllWindows()
