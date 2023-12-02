import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import glob
import cv2
import create_CAPTCHA
# import main

def press_button():
    global img2,img3

    # def empty_img():
    #     # 建立底層畫面
    #     img = np.zeros(( 100, 210, 3), dtype='uint8')
    #     img = Image.fromarray( img)
    #     img = ImageTk.PhotoImage( img)
    #     return img
    
    if parse_text.get() == '產圖':
        parse_text.set('解析')

        # 將after_img中圖片刪除
        after_img.configure( image=None)
        before_img.configure( image=None)
        
        # img = empty_img()
        # img = ImageTk.PhotoImage( img)
        # after_img.config( image=img)

        # 取產生驗證碼圖片
        img2 = Image.open('test1.png')
        # img2 = create_CAPTCHA.createImg()
        img2 = ImageTk.PhotoImage( img2)

        # 投影出圖片
        before_img.configure( image=img2)
        
    else:
        parse_text.set('產圖')

        # 產生解析驗證碼結果

        # result_img()
        img3 = Image.open('test2.png')
        img3 = ImageTk.PhotoImage( img3)

        after_img.configure( image=img3)



# 建立主視窗
root = tk.Tk()
root.title('驗證碼解析')
root.geometry('210x250')
root.minsize( 210, 250)

# 建立圖片放置位置
before_img = tk.Label( root, text='解析前', font=('15'))
before_img.place( relx=0, rely=0.0, relheight=0.4, relwidth=1.0)
after_img = tk.Label( root, text='解析後', font=('15'))
after_img.place( relx=0, rely=0.4, relheight=0.4, relwidth=1.0)

# 建立解析驗證碼之按鈕
parse_text = tk.StringVar()
parse_text.set('產圖')
parse = tk.Button( root, textvariable=parse_text, padx=5, pady=5, font=('15'))
parse.config( command=lambda: press_button())
parse.place( relx=0.5, rely=0.9, anchor='center')


# 分割線
sep1 = ttk.Separator( root, orient='horizontal').place( rely=0.4, relwidth=1)
sep2 = ttk.Separator( root, orient='horizontal').place( rely=0.8, relwidth=1)

# tkinter執行
root.mainloop()

cv2.destroyAllWindows()