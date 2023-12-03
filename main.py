import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
# def rectangle2square(img):
#     maxside = max(img.shape[0],img.shape[1])
#     white_img = np.zeros((maxside,maxside,1),np.uint8)
#     white_img.fill(255)
#     for x in range(img.shape[0]):
#         for y in range(img.shape[1]):
#             white_img[x,y] = img[x,y]
#     print(white_img.shape)
#     cv2.imshow("windows2",white_img)

# def use_model(img):
#     resize_img = rectangle2square(img)
#     resize_img = cv2.resize(resize_img, (28, 28))
#     # cv2.imshow("win", resize_img)
#     reshape_array = resize_img.flatten()
#     reshape_array = np.expand_dims(reshape_array, axis=0)
#     reshape_array = reshape_array.astype(np.float32) / 255
#     # print(reshape_array)
#     predictions = model.predict(reshape_array)
#     predicted_class_index = np.argmax(predictions)
#     print(predicted_class_index)

# model = keras.models.load_model("num_model.h5")

# 直接以灰階圖讀取img
ori_img = cv2.imread("test.png", 0)
img = ori_img
# 將灰階圖的img_array變成one dimension
new_np_array = img.flatten()
# 得出img中最多的數值(背景顏色)
thresh_guess = np.argmax(np.bincount(new_np_array))
# print(thresh_guess) 印出重複最多的值
# 遍歷img_array 將重複最多的值設為白色 其餘黑色(白底黑字)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if img[x, y] == thresh_guess:
            img[x, y] = 255
        else:
            img[x, y] = 0

# 用OTSU算法自動判別threshold
# thresh_value, img = cv2.threshold(img,1,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# print(thresh_value)

# https://shengyu7697.github.io/python-opencv-erode-dilate/
# 利用膨脹消除雜訊點及干擾線(白色背景增大)
kernel = np.ones([3, 3])
img = cv2.dilate(img, kernel)

# 利用侵蝕將數字線條變寬
kernel = np.ones([4, 4])
img = cv2.erode(img, kernel)

# https://blog.csdn.net/laobai1015/article/details/76400725
# 用Contours 把數字輪廓畫出
contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 計算所有輪廓面積並將前四大的輸出(避免有沒清除的雜訊點被偵測)
areas = []
for c in contours:
    area = cv2.contourArea(c)
    areas.append(area)
areas = np.array(areas)
index = np.argsort(areas)[-5:]
top4_areas = []
for i in range(4):
    top4_areas.append(contours[index[i]])
    # print(cv2.contourArea(top4_areas[-1]))


# 利用boundingrect得到的x,y,w,h 傳進rectangle中並畫框

for each_num_contours in top4_areas:
    x, y, w, h = cv2.boundingRect(each_num_contours)
    cv2.rectangle(img, [x, y], [x + w, y + h], 2)
    # reconize_img = img[y : y + h, x : x + w]
    # reconize_img = rectangle2square(reconize_img)
    # use_model(reconize_img)


cv2.imshow("windows", img)
cv2.waitKey(0)
