import cv2
import numpy as np

# 水平拼接三个数组 a = [1,2,3],b = [4,5,6], c = [7,8,9]
# 创建数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
# 拼接数组
h_stack = np.hstack((a, b, c))
print(h_stack)

# 垂直拼接三个数组 a = [1,2,3],b = [4,5,6], c = [7,8,9]
v_stack = np.vstack((a, b, c))
print(v_stack)

# 水平垂直拼接图像：../imgs/stone.jpg
stone = cv2.imread('../imgs/stone.jpg')
# 拼接图像
hst_stone = np.hstack((stone, stone))
vst_stone = np.vstack((stone, stone))
cv2.imshow('hst', hst_stone)
cv2.imshow('vst', vst_stone)
cv2.waitKey()
cv2.destroyAllWindows()
