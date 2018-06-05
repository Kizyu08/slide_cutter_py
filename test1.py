import cv2
import os

image_dir = 'C:/Users\s1100/Documents/pdf2jpg/'
image_file = 'DistributedSystems_1_EJ_01.jpg'
out_dir = image_dir + 'output/'
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)
src = cv2.imread(image_dir + image_file, 1)
image = src
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
otu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
cntimage, contours, hierarchy = cv2.findContours(otu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 矩形検出された数（デフォルトで0を指定）
detect_count = 0
height, width, channels = src.shape[:3]
count = len(contours)
rects[counts]

# 各輪郭に対する処理
for i in range(0, counts):
    # 輪郭の領域を計算
    area = cv2.contourArea(contours[i])
    # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
    if area < 1e3 or (width*height-1000) < area:
        continue
    rect = contours[i]
    x, y, w, h = cv2.boundingRect(rect)
    rects[i] = {x, y, w, h}
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.imwrite(image_dir + 'output/' + str(detect_count) + '.jpg', src[y:y + h, x:x + w])
    print('X='+ str(x) +', Y='+ str(y) +', W='+ str(w)+', H='+ str(h))
    detect_count = detect_count + 1

cv2.namedWindow('show', cv2.WINDOW_NORMAL|cv2.WINDOW_KEEPRATIO)
cv2.imshow('show', image)
print(detect_count)
cv2.waitKey()
