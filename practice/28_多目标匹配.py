# 将图background2作为模板，将图template作为原始图像，使用cv2.TM_SQDIFF_NORMED方式进行模板匹配，
# 在原始图像中找到与模板一样的图案，并在该图案上绘制红色方框。
# 原始图像中有很多重复的图案，每一个与模板相似的图案都需要被标记出来
import cv2

img = cv2.imread('../imgs/background2.jpg')  # 读取原始图像
templ = cv2.imread('../imgs/template.png')  # 读取模板图像
height, width, c = templ.shape  # 获取模板高，宽，通道数
results = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)  # 按照标准平方差匹配，返回数组
for y in range(len(results)):  # 遍历结果数组的行
    for x in range(len(results[y])):  # 遍历结果数组的列
        if results[y][x] > 0.99:  # 如果相关系数大于0.99则认为匹配成功
            # 在最佳匹配结果位置绘制红色方框
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
