thresh_value, img = cv2.threshold(img,1,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# print(thresh_value)