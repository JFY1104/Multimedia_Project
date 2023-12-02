import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
img = ImageTk.PhotoImage( Image.open('test1.png'))
l = tk.Label(root, image=img)

root.mainloop()