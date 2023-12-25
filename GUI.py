import main
import tkinter as tk
from tkinter import ttk
import create_CAPTCHA
from PIL import Image, ImageTk

class control:
    '''建立主視窗框架'''
    def __init__(self, master: tk.Tk):
        # 建立主視窗
        self.main = master
        self.main.title('驗證碼解析')
        self.main.geometry('840x250')
        self.main.resizable( False, False)

        # 建立標籤顯示驗證圖
        self.create_output = ttk.Label(self.main)
        self.create_output.place(relx=0, rely=0.0, relwidth=0.5, relheight=0.8)                             # 位置設定(視窗內的相對位置)

        # 建立標籤顯示結果圖
        self.result_output = ttk.Label(self.main)
        self.result_output.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.8)

        # 建立按鈕控制圖片輸出
        self.parse_text = tk.StringVar()                                                                    # 定義一變數，並在下一行設定按鈕內文字
        self.parse_text.set('產圖')
        self.parse = tk.Button( self.main, textvariable=self.parse_text, font=("MingLiU", 15, ))            # 控制按鈕
        self.parse.config(command=self.press_button)                                                        # 連結function(press_button)
        self.parse.place(relx=0.5, rely=0.9, anchor='center')

        # 分割線
        self.sep1 = ttk.Separator(self.main, orient='horizontal').place( rely=0.8, relwidth=1)
        self.sep2 = ttk.Separator(self.main, orient='vertical').place(relx=0.5, relheight=0.8)
    
    '''輸出驗證碼圖片'''
    def create(self):
        create_CAPTCHA.createImg()                              # 呼叫create_CAPTCHA產生驗證碼
        img = Image.open('test.png')                            # 開啟圖片
        img = img.resize(( 420, 200))                           # 調整圖片大小
        img = ImageTk.PhotoImage(img)                           # 轉換成tkinter可以使用之圖片

        # 在create_output標籤輸出圖片
        self.create_output.configure(image=img)                 # 將create_label中的圖片設為none
        self.create_output.image = img                          # 確保刪除

    '''輸出解析後的結果圖'''
    def result(self):
        main.main()                                             # 呼叫main.py生成結果圖
        img = Image.open('result.png')
        img = img.resize(( 420, 200))
        img = ImageTk.PhotoImage(img)

        # 在result_output標籤輸出圖片
        self.result_output.configure(image=img)
        self.result_output.image = img

    '''按下按鈕後執行並切換按鈕內容'''
    def press_button(self):
        if self.parse_text.get() == '產圖':
            self.parse_text.set('解析')                         # 置換按鈕內內容
            # 將輸出結果之欄位清空
            self.result_output.configure(image=None)
            self.result_output.image = None
            self.create()                                       # 驗證碼
        else:
            self.parse_text.set('產圖')
            self.result()                                       # 解析驗證碼結果

if __name__ == "__main__":
    root = tk.Tk()
    control(root)
    root.mainloop()

