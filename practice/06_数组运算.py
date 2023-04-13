# 使用NumPy创建2个数组，分别使用“>=”“==”“<=”和“!=”运算符比较2个数组
import numpy as np

n1 = np.array([1, 2, 3])
n2 = np.array([1, 3, 2])
print(n1 >= n2)  # [ True False  True]
print(n1 == n2)  # [ True False False]
print(n1 <= n2)  # [ True  True False]
print(n1 != n2)  # [False  True  True]



