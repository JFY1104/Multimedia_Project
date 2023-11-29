import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# def built():
#     # 呼叫create_CAPTCH.py
#     img = Image.open('test1.png')
#     img = img.resize( img)
#     before_img.config( image=img)

# def result():
#     # 開啟圖片(驗證碼)
#     parse_result = Image.open('')
#     ImageTk.PhotoImage( parse_result)

#     # 呼叫main.py

# 建立主視窗
main = tk.Tk()
main.title('驗證碼解析')
main.geometry('210x250')
main.minsize( 210, 250)

# 建立圖片放置位置
before_img = tk.Label( main, text='驗證前', font=('15')).place( relx=0, rely=0.0, relheight=0.4, relwidth=1.0)

after_img = tk.Label( main, text='驗證後', font=('15')).place( relx=0, rely=0.4, relheight=0.4, relwidth=1.0)

# 建立解析驗證碼之按鈕
parse_text = tk.StringVar()
parse_text.set('解析')
parse = tk.Button( main, textvariable=parse_text, padx=5, pady=5).place( relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator( main, orient='horizontal').place( rely=0.4, relwidth=1)
sep2 = ttk.Separator( main, orient='horizontal').place( rely=0.8, relwidth=1)

# tkinter執行
main.mainloop()