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
main.geometry('300x200')

# 建立解析驗證碼之按鈕
parse_test = tk.StringVar()
parse_test.set('解析')
parse = ttk.Button( main, textvariable=parse_test).pack( side='top', fill='both', expand=1)
before_img = ttk.Label( main, background='yellow').pack( side='left', fill='x', expand=1)
after_img = ttk.Label( main, background='green').pack( side='left', fill='x', expand=1)

# tkinter執行
main.mainloop()