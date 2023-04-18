import cv2
import numpy as np
import matplotlib.pyplot as plt
# 编写一个程序，使用line()方法分别绘制颜色为蓝色、绿色、红色和黄色，
# 线条宽度为5、10、15和20的4条线段
# 并且这4条线段能够拼成一个“王”字
# “王字”四个最外侧的坐标是：(50,50),(250,50),(50,250),(250,250)

# 创建白色画布
canvas = np.ones((300, 300, 3), dtype=np.uint8) * 255
# 画线
canvas = cv2.line(canvas, (50, 50), (250, 50), (255, 0, 0,), 5)
canvas = cv2.line(canvas, (100, 150), (200, 150), (0, 255, 0), 10)
canvas = cv2.line(canvas, (150, 50), (150, 250), (0, 0, 255), 15)
canvas = cv2.line(canvas, (50, 250), (250, 250), (0, 255, 255), 20)
# 显示
canvas_RGB = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
plt.imshow(canvas_RGB)
plt.show()

# ------------------------------------------------------------------eg.2
# 画布300x300，使用rectangle()方法分别绘制3个正方形边框和1个实心正方形，具体要求如下。
# （1）左上角坐标为(50, 50)、右下角坐标为(250, 250)、红色的、线条宽度为40的正方形边框。
# （2）左上角坐标为(90, 90)、右下角坐标为(210, 210)、绿色的、线条宽度为30的正方形边框。
# （3）左上角坐标为(120, 120)、右下角坐标为(180, 180)、蓝色的、线条宽度为20的正方形边框。
# （4）左上角坐标为(140, 140)、右下角坐标为(160, 160)、黄色的实心正方形。

canvas1 = np.ones((300, 300, 3), dtype=np.uint8) * 255
# 画矩形
canvas1 = cv2.rectangle(canvas1, (50, 50), (250, 250), (0, 0, 255), 40)
canvas1 = cv2.rectangle(canvas1, (90, 90), (210, 210), (0, 255, 0), 30)
canvas1 = cv2.rectangle(canvas1, (120, 120), (180, 180), (255, 0, 0), 20)
canvas1 = cv2.rectangle(canvas1, (140, 140), (160, 160), (0, 255, 255), -1)  # -1代表实心
# 显示
canvas1_RGB = cv2.cvtColor(canvas1, cv2.COLOR_BGR2RGB)
plt.imshow(canvas1_RGB)
plt.show()

