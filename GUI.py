import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import glob
import cv2
import create_CAPTCHA
import main

def adjust_size(img):
    new_w = root.winfo_width()
    new_h = new_w * 10 / 21

    img = img.resize(( new_w, new_h))

def create():
    global img2
    # 取產生驗證碼圖片
    create_CAPTCHA.createImg()
    img2 = Image.open('test.png')

    img2 = ImageTk.PhotoImage( img2)

    # 投影出圖片
    output.configure( image=img2)

def result():
    global img3
    
    # img3 = Image.open('test1.png')
    main.main()
    img3 = Image.open('result.png')
    img3 = ImageTk.PhotoImage( img3)

    output.configure( image=img3)

def press_button():
    global img2,img3
    
    if parse_text.get() == '產圖':
        parse_text.set('解析')

        # 建立驗證碼
        create()
    else:
        parse_text.set('產圖')

        # 產生解析驗證碼結果
        result()

# 建立主視窗
root = tk.Tk()
root.title('驗證碼解析')
root.geometry('210x150')
root.minsize( 210, 150)

style = ttk.Style()
style.theme_use('alt')

# 建立圖片放置位置
output = ttk.Label( root, font=('15'))
output.place( relx=0, rely=0.0, relwidth=1.0, relheight=0.7)

style.configure( 'TNotebook.Tab', font=('STHeiti', 20, 'bold'), padding=( 10, 5))

# 建立解析驗證碼之按鈕
parse_text = tk.StringVar()
parse_text.set('產圖')
parse = ttk.Button( root, textvariable=parse_text, padding=5)
parse.config( command=press_button)
parse.place( relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator( root, orient='horizontal').place( rely=0.7, relwidth=1)

# tkinter執行
root.mainloop()