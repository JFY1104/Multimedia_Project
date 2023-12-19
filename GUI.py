import main
import tkinter as tk
from tkinter import ttk
import create_CAPTCHA
from PIL import Image, ImageTk

'''輸出驗證碼圖片'''
def create():
    global img2

    # 生成驗證碼
    create_CAPTCHA.createImg()                  # 呼叫驗證碼
    img2 = Image.open('test.png')               # 開啟圖片
    img2 = img2.resize(( 420, 200))             # 調整圖片大小
    img2 = ImageTk.PhotoImage( img2)            # 轉換成tkinter可以使用之圖片

    # 在output標籤輸出圖片
    output.configure( image=img2)

'''輸出解析後的結果圖'''
def result():
    global img3
    
    # 呼叫main.py生成結果圖
    main.main()
    img3 = Image.open('result.png')
    img3 = img3.resize(( 420, 200))
    img3 = ImageTk.PhotoImage( img3)

    # 在output標籤輸出圖片
    output.configure( image=img3)

# 按下按鈕後執行並切換按鈕內容
def press_button():
    if parse_text.get() == '產圖':
        parse_text.set('解析')      # 置換按鈕內內容

        # 驗證碼
        create()
    else:
        parse_text.set('產圖')

        # 解析驗證碼結果
        result()

# 建立主視窗
root = tk.Tk()
root.title('驗證碼解析')
root.geometry('420x300')
root.resizable( False, False)

# 風格設定
style = ttk.Style()
style.theme_use('alt')                                                                  # 使用內建主題'alt'
style.configure( 'TNotebook.Tab', font=('STHeiti', 20, 'bold'), padding=( 10, 5))       # 風格細節設定(樣式，字型，間距)

# 建立標籤顯示驗證圖/結果圖
output = ttk.Label( root)
output.place( relx=0, rely=0.0, relwidth=1.0, relheight=0.7)                            # 位置設定(視窗內的相對位置)

# 建立按鈕控制圖片輸出
parse_text = tk.StringVar()                                                             # 定義一變數，按鈕內文字
parse_text.set('產圖')
parse = ttk.Button( root, textvariable=parse_text, padding=5)                           # 控制按鈕
parse.config( command=press_button)                                                     # 連結function(press_button)
parse.place( relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator( root, orient='horizontal').place( rely=0.7, relwidth=1)

# tkinter執行
root.mainloop()