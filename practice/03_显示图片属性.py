# 先获取../imgs下的3.1.jpg的属性，
# 再获取由3.1.jpg转换得到的灰度图像的属性
import cv2
import matplotlib.pyplot as plt
# 彩色图像
img = cv2.imread('../imgs/3.1.jpg')
print(f'shape = {img.shape}')
print(f'size = {img.size}')
print(f'dtype = {img.dtype}')

# 灰度图
img_gray = cv2.imread('../imgs/3.1.jpg', 0)
print(f'shape = {img_gray.shape}')
print(f'size = {img_gray.size}')
print(f'dtype = {img_gray.dtype}')

