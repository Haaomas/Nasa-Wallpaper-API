import datetime, random, urllib.request, json, ctypes, os
import webbrowser
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image

# Creation of the windows
windows = Tk()
windows.geometry("310x160")
windows.title("Nasa Daily Wallpaper")
windows.wm_iconbitmap("nasa.ico")
windows.config(bg="#1e2227")
windows.resizable(width=False, height=False)


def printhi():
    print("Hi!")


# IMAGE OF THE DAY
PATH = "C:/Users/barre/OneDrive/Bureau/Dev/Perso/GitHub/Nasa-Wallpaper-API/img/Full Moon Perseids 2022-08-18.jpg"
wallpaper_icon = ImageTk.PhotoImage(Image.open(PATH).resize((60, 60)))
panel = Label(windows, image=wallpaper_icon, bd=0)
panel.place(x=20, y=40)

font_1 = Font(
    family="Bauhaus 93",
    size=12,
    weight="normal",
)

# Wallpaper texte
wallpaper_texte = Label(
    windows,
    text="WALLPAPER",
    wraplength=280,
    fg="#8c8c7a",
    bg="#1e2227",
    font=font_1,
)
wallpaper_texte.place(x=20, y=10)

# Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)


# Title of the picture
title_picture = Label(
    windows,
    text="Full Moon Perseids",
    wraplength=180,
    fg="#FFF",
    bg="#1e2227",
    cursor="hand2",
    font=font_1,
)
title_picture.place(x=100, y=40)
title_picture.bind(
    "<Button-1>", lambda e: callback("https://apod.nasa.gov/apod/ap220818.html")
)


# Button Left and Right
btn_left = Button(
    windows, text="<- Previous", command=printhi, bg="#1e2227", font=font_1, bd=0
)
btn_left.place(x=20, y=120)

btn_right = Button(
    windows, text="Next ->", command=printhi, bg="#1e2227", font=font_1, bd=0
)
btn_right.place(x=240, y=120)


# Luncher
windows.mainloop()
