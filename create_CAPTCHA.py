import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter


def getRandomColor():
    """ 取得隨機顏色 """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def getRandomChar():
    """ 隨機從0-9選擇數字 """
    random_num = str(random.randint(0, 9))
    random_char = random.choice([random_num])
    return random_char

def drawLine(draw):
    """ 在寬高隨機範圍內生成干擾線 """
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())

def drawPoint(draw):
    """ 在寬高範圍內隨機生成雜訊點 """
    for i in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x,y), fill=getRandomColor())

def createImg():
    """ 生成圖片的function """
    bg_color = getRandomColor()
    # 創建隨機背景色的圖片
    img = Image.new(mode="RGB", size=(width, height), color=bg_color)
    # 用img建立draw物件
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="arial.ttf", size=85)
    for i in range(4):
        # 隨機生成數字
        random_txt = getRandomChar()
        txt_color = getRandomColor()
        # 確保文字顏色不與背景重合
        while txt_color == bg_color:
            txt_color = getRandomColor()
        # draw文字
        draw.text((10 + 50 * i, 5), text=random_txt, fill=txt_color, font=font)
    # 畫干擾線及干擾點
    drawLine(draw)
    drawPoint(draw)
    # 生成檔案
    with open("test.png", "wb") as f:
        img.save(f, format="png")
    
# 圖片寬高
width = 210
height = 100
createImg()
