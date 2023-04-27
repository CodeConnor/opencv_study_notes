# ---------------------------------------------------------------多模板匹配
# 在原始图像中找到与模板一样的图案，并在该图案上绘制红色方框。
# 原始图像中有很多重复的图案，每一个与模板相似的图案都需要被标记出来
# 将template、template2、template3作为模板，将background2作为原始图像
# 每一个模板都要做一次“单模板多目标匹配”，最后把所有模板的匹配结果汇总到一起。
# “单模板多目标匹配”的过程可以封装成一个方法，方法参数为模板和原始图像，方法内部将计算结果再加工一下，
# 直接返回所有红框左上角和右下角两点横纵坐标的列表。

import cv2


# 自定义方法，获取模板匹配成功后所有红框位置的坐标
def myMatchTemplate(img, templ):
    height, width, c = templ.shape
    results = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)  # 按照标准相关系数匹配
    loc = list()  # 红框的坐标列表
    for y in range(len(results)):  # 遍历结果数组的行
        for x in range(len(results[y])):  # 遍历结果数组的列
            if results[y][x] > 0.99:  # 如果相关系数大于0.99则认为匹配成功
                # 在列表中添加匹配成功的红框对角线两点坐标
                loc.append((x, y, x + width, y + height))
    return loc


img = cv2.imread('../imgs/background2.jpg')
templs = []  # 模板对象列表
templs.append(cv2.imread('../imgs/template.png'))
templs.append(cv2.imread('../imgs/template2.png'))
templs.append(cv2.imread('../imgs/template3.png'))

loc = []  # 所有模板匹配成功位置的红框坐标列表
for j in templs:  # 遍历所有模板
    loc += myMatchTemplate(img, j)  # 记录该模板匹配得出的坐标

for i in loc:  # 遍历所有红框的坐标
    img = cv2.rectangle(img, (i[0], i[1]), (i[2], i[3]), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
