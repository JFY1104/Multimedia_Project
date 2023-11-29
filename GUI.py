import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def built():
#     # 呼叫create_CAPTCH.py

# def result():
#     # 開啟圖片(驗證碼)
#     parse_result = Image.open('')
#     ImageTk.PhotoImage( parse_result)

#     # 呼叫main.py

def exit_func():
    """關閉main視窗"""
    main.destroy()

# 建立主視窗
main = tk.Tk()
main.title('驗證碼解析')
main.geometry('210x250')

# frame1 = tk.Frame( main, bg='red', width=210, height=20).pack()
# frame2 = tk.Frame( main, bg='blue', width=210, height=200).pack()

# 建立解析驗證碼之按鈕
parse_text = tk.StringVar()
parse_text.set('解析')
parse = tk.Button( main, textvariable=parse_text, padx=5, pady=5).place( relx=0, relheight=0.2, relwidth=0.5)

close_text = tk.StringVar()
close_text.set('結束')
close = tk.Button( main, textvariable=close_text, command=exit_func, padx=5, pady=5).place( relx=0.5, relheight=0.2, relwidth=0.5)

# 建立圖片放置位置
before_img = tk.Label( main, background='yellow', text='驗證前', font=('15')).place( relx=0, rely=0.2, relheight=0.4, relwidth=1.0)
after_img = tk.Label( main, background='green', text='驗證後', font=('15')).place( relx=0, rely=0.6, relheight=0.4, relwidth=1.0)

# tkinter執行
main.mainloop()