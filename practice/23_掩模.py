# 掩模，也叫作掩码，英文为mask，在程序中用二值图像来表示：
# 0值（纯黑）区域表示被遮盖的部分，255值（纯白）区域（感兴趣区域）表示暴露的部分（某些场景下也会用0和1当作掩模的值）。

# 利用numpy库的zeros()方法创建一幅掩模图像，
# 感兴趣区域为在该图像中横坐标为20、纵坐标为50、宽为60、高为50的矩形，展示该掩模图像。
import numpy as np
import cv2

mask = np.zeros((150, 150, 3), np.uint8)
mask[50:100, 20:80, :] = 255
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
