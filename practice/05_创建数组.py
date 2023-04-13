import numpy as np

# 创建一维和二维数组
n1 = np.array([1, 2, 3])  # 一维数组
n2 = np.array([0.1, 0.2, 0.3])  # 包含小数的一维数组
n3 = np.array([[1, 2, 3], [4, 5, 6]])  # 二维数组
print(n1)
print(n2)
print(n3)

# 创建浮点数数组
list1 = [1, 2, 3]
n4 = np.array(list1, dtype=np.float_)
# 或者n4 = np.array(list1, dtype=float)
print(n4)  # [1. 2. 3.]
print(n4.dtype)  # float64
print(type(n4))  # <class 'numpy.ndarray'>

# 创建三维数组
nd1 = [1, 2, 3]
nd2 = np.array(nd1, ndmin=3)  # 三维数组
print(nd2)  # [[[1 2 3]]]，可见一维数组被转换为了三维数组

# 创建2行3列的未初始化整数数组
n = np.empty([2, 3], dtype=np.int8)
print(n)

# 创建3行、3列、数字类型为无符号8位整数的纯0数组
n = np.zeros([3, 3], dtype=np.uint8)
print(n)

# 创建3行、3列、数字类型为无符号8位整数的纯1数组
n = np.ones([3, 3], dtype=np.uint8)
print(n)

# randint方法
n1 = np.random.randint(1, 3, 10)  # 维度默认为1，共10个元素
print('随机生成10个1～3且不包括3的整数：')
print(n1)
n2 = np.random.randint(5, 10)
print('size数组大小为空随机返回一个整数：')
print(n2)
n3 = np.random.randint(5, size=(2, 3))  # 每个数组3个元素
print('随机生成5以内二维数组：')
print(n3)

