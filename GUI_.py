import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 建立主視窗
main = tk.Tk()
main.title('驗證碼解析')
main.geometry('300x200')

frame1 = tk.Frame( main).pack()
frame2 = tk.Frame( main).pack()

# 建立解析驗證碼之按鈕
parse_test = tk.StringVar()
parse_test.set('解\n析')
parse = tk.Button( frame1, textvariable=parse_test, padx=5, pady=5).pack( side='left', fill='y')

# 建立圖片放置位置
before_img = tk.Label( frame2, background='yellow', text='驗證前').pack( side='top', fill='both', expand=1)
after_img = tk.Label( frame2, background='green', text='驗證後').pack( side='top', fill='both', expand=1)

# tkinter執行
main.mainloop()