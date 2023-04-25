# 将图background作为模板，将图template作为原始图像，使用cv2.TM_SQDIFF_NORMED方式进行模板匹配，
# 在原始图像中找到与模板一样的图案，并在该图案上绘制红色方框。
import cv2

img = cv2.imread('../imgs/background.jpg')  # 读取原始图像
templ = cv2.imread('../imgs/template.png')  # 读取模板图像
height, width, c = templ.shape  # 获取模板高，宽，通道数
result = cv2.matchTemplate(img, templ, cv2.TM_SQDIFF_NORMED)  # 按照标准平方差匹配，返回数组
print(result)
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)  # 获取匹配结果中的最小值，最大值，最小值坐标，最大值坐标
resultPoint1 = minLoc  # 将最小值坐标作为最佳匹配区域的左上角点坐标
resultPoint2 = (resultPoint1[0] + width, resultPoint1[1] + height)  # 计算出最佳匹配区域的右下角点坐标
cv2.rectangle(img, resultPoint1, resultPoint2, (0, 0, 255), 2)  # 在最佳匹配区域绘制红线方框
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
