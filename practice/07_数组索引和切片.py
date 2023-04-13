import numpy as np

# 对一维数组进行切片
n = np.array([1, 2, 3])
print(n[::])
print(n[-3::1])
print(n[::-1])
print(n[:-2:1])
print(n[1:])

# 分别获取二维数组中索引为1的元素、第2行第3列的元素、索引为-1的元素
n = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(n)
print(n[1])
print(n[1, 2])  # 等价于print(n[1][2])
print(n[-1])

# 二维数组切片
n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n)
print(n[:2, 1:])  # 2356
print(n[1:2, :2])  # 45
print(n[:2, -1:])  # 36
print(n[:, :1])  # 147
