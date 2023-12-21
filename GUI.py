import main
import tkinter as tk
from tkinter import ttk
import create_CAPTCHA
from PIL import Image, ImageTk

'''輸出驗證碼圖片'''
def create():
    # 生成驗證碼
    create_CAPTCHA.createImg()                  # 呼叫驗證碼
    img = Image.open('test.png')                # 開啟圖片
    img = img.resize(( 420, 200))               # 調整圖片大小
    img = ImageTk.PhotoImage( img)              # 轉換成tkinter可以使用之圖片

    # 在create_output標籤輸出圖片
    create_output.configure(image=img)
    create_output.image = img

'''輸出解析後的結果圖'''
def result():
    # 呼叫main.py生成結果圖
    main.main()
    img = Image.open('result.png')
    img = img.resize(( 420, 200))
    img = ImageTk.PhotoImage( img)

    # 在result_output標籤輸出圖片
    result_output.configure(image=img)
    result_output.image = img

'''按下按鈕後執行並切換按鈕內容'''
def press_button():
    if parse_text.get() == '產圖':
        parse_text.set('解析')                  # 置換按鈕內內容
        # 將輸出結果之欄位清空
        result_output.configure(image=None)
        result_output.image = None
        create()                                # 驗證碼
    else:
        parse_text.set('產圖')
        result()                                # 解析驗證碼結果

'''建立主視窗框架'''
# 建立主視窗
root = tk.Tk()
root.title('驗證碼解析')
root.geometry('840x250')
root.resizable( False, False)

# 建立標籤顯示驗證圖
create_output = ttk.Label(root)
create_output.place(relx=0, rely=0.0, relwidth=0.5, relheight=0.8)                      # 位置設定(視窗內的相對位置)

# 建立標籤顯示結果圖
result_output = ttk.Label(root)
result_output.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.8)

# 建立按鈕控制圖片輸出
parse_text = tk.StringVar()                                                             # 定義一變數，按鈕內文字
parse_text.set('產圖')
parse = tk.Button( root, textvariable=parse_text, font=("MingLiU", 15, ))               # 控制按鈕
parse.config(command=press_button)                                                      # 連結function(press_button)
parse.place(relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator(root, orient='horizontal').place( rely=0.8, relwidth=1)
sep2 = ttk.Separator(root, orient='vertical').place(relx=0.5, relheight=0.8)

# 視窗執行
root.mainloop()