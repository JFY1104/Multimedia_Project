import cv2
import numpy as np

# 直接以灰階圖讀取img
img = cv2.imread('test.png',0)
# 將灰階圖的img_array變成one dimension
new_np_array = img.flatten()
#得出img中最多的數值(背景顏色)
thresh_guess = np.argmax(np.bincount(new_np_array))
# print(thresh_guess) 印出重複最多的值
# 遍歷img_array 將重複最多的值設為白色 其餘黑色(白底黑字)
for x in range(img.shape[0]):   
	for y in range(img.shape[1]):   
		if img[x,y] == thresh_guess:
			img[x,y] = 255
		else:
			img[x,y] = 0
		

# 用OTSU算法自動判別threshold
# thresh_value, img = cv2.threshold(img,1,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# print(thresh_value)
cv2.imshow('windows',img)
cv2.waitKey(0)
