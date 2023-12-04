import create_CAPTCHA
import main

# 圖片處理套件
from PIL import Image, ImageTk

# GUI套件
import tkinter as tk
from tkinter import ttk

# 輸出驗證碼圖片
def create():
    global img2

    # 呼叫create_CAPTCHA.py生成驗證碼
    create_CAPTCHA.createImg()
    img2 = Image.open('test.png')
    img2 = img2.resize(( 420, 200))
    img2 = ImageTk.PhotoImage( img2)

    # 在output標籤輸出圖片
    output.configure( image=img2)

# 輸出解析後的結果圖
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
        parse_text.set('解析')

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
style.theme_use('alt')

# 建立標籤顯示驗證圖/結果圖
output = ttk.Label( root, font=('15'))
output.place( relx=0, rely=0.0, relwidth=1.0, relheight=0.7)

style.configure( 'TNotebook.Tab', font=('STHeiti', 20, 'bold'), padding=( 10, 5))

# 建立按鈕控制圖片輸出
parse_text = tk.StringVar()
parse_text.set('產圖')
parse = ttk.Button( root, textvariable=parse_text, padding=5)
parse.config( command=press_button)
parse.place( relx=0.5, rely=0.9, anchor='center')

# 分割線
sep1 = ttk.Separator( root, orient='horizontal').place( rely=0.7, relwidth=1)

# tkinter執行
root.mainloop()