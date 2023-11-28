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
main.geometry('900x600')

# # 建立架構
# frame1 = tk.Frame( main).pack( side='top')
# frame2 = tk.Frame( main).pack( side='left')
# frame3 = tk.Frame( main).pack( side='left')

# 建立解析驗證碼之按鈕
s = ttk.Style()
s.theme_use('alt')
parse = ttk.Button( main, text='解析')
before_img = ttk.Label( main, background='lightyellow')
after_img = ttk.Label( main, background='lightgreen')

# parse.pack( side='top', fill='x', expand=1)
# before_img.pack( side='left', fill='both', expand=1)
# after_img.pack( side='left', fill='both', expand=1)

parse.pack()
before_img.pack()
after_img.pack()

# tkinter執行
main.mainloop()