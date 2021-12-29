from tkinter import *
from PIL import Image, ImageDraw, ImageFont
def savey():
    with open("tiifin.txt","a") as f:
        f.write(f'''
        Idli:{0}#include variables in placce of zeros.
        Dosa:{0}
        Puri:{0}
        Punugu:{0}
        Parota:{0}
        Chapathi:{0}
        Vada:{0}
        ''')
        
def printy():  
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((10,10), "", font=fnt, fill=(255, 255, 0))
    
    img.save('pil_text_font.png')

root=Tk()

root.title("Hi")
root.geometry("625x625")

mymenu=Menu(root)
mymenu.add_command(label="Save",command=savey)
mymenu.add_command(label="Print",command=printy)

root.config(menu=mymenu)

root.mainloop()