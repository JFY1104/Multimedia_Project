import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# def built():
#     # 呼叫create_CAPTCH.py

# def result():
#     # 開啟圖片(驗證碼)
#     parse_result = Image.open('')
#     ImageTk.PhotoImage( parse_result)

#     # 呼叫main.py


# 建立主視窗
main = tk.Tk()
main.title('驗證碼解析')
main.geometry('210x220')

frame1 = tk.Frame( main).pack()
frame2 = tk.Frame( main).pack()

# 建立解析驗證碼之按鈕
parse_test = tk.StringVar()
parse_test.set('解析')
parse = tk.Button( frame1, textvariable=parse_test, padx=5, pady=5).pack( fill='x')

# 建立圖片放置位置
before_img = tk.Label( frame2, background='yellow', text='驗證前', font=('15')).pack( side='top', fill='both', expand=1)
after_img = tk.Label( frame2, background='green', text='驗證後', font=('15')).pack( side='top', fill='both', expand=1)

# tkinter執行
main.mainloop()