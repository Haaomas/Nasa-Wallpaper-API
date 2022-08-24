import datetime, random, urllib.request, json, ctypes, os
import webbrowser
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


# Creation of the windows
windows = Tk()
windows.geometry("310x120")
# windows.geometry("500x300")
windows.title("Nasa Daily Wallpaper")
windows.wm_iconbitmap("nasa.ico")
windows.config(bg="#1e2227")
windows.resizable(width=False, height=False)

# Font for the text
font_title = Font(family="Caladea", size=16, weight="normal")
font_text = Font(family="Caladea", size=14, weight="normal", underline=TRUE)
font_artist = Font(family="Caladea", size=12, weight="normal", slant="italic")


# Wallpaper texte
wallpaper_texte = Label(
    windows,
    text="WALLPAPER",
    fg="#8c8c7a",
    bg="#1e2227",
    font=font_title,
)
wallpaper_texte.grid(row=0, column=0, pady=10)


# IMAGE OF THE DAY
PATH = "C:/Users/barre/OneDrive/Bureau/Dev/Perso/GitHub/Nasa-Wallpaper-API/img/Full Moon Perseids 2022-08-18.jpg"
wallpaper_icon = ImageTk.PhotoImage(Image.open(PATH).resize((60, 60)))
panel = Label(windows, image=wallpaper_icon, bd=0)
# panel.place(x=20, y=40)
panel.grid(row=1, rowspan=3, column=0)


# Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)


# Title of the picture
title_picture = Label(
    windows,
    text="Full Moon Perseids",
    fg="#3893ef",
    bg="#1e2227",
    cursor="hand2",
    font=font_text,
)
title_picture.grid(row=1, column=1)
title_picture.bind(
    "<Button-1>", lambda e: callback("https://apod.nasa.gov/apod/ap220818.html")
)

# # Text of the picture
# text = img = Label(
#     windows,
#     text="The annual Perseid meteor shower was near its peak on August 13. As planet Earth crossed through streams of debris left by periodic Comet Swift-Tuttle meteors rained in northern summer night skies. But even that night's nearly Full Moon shining near the top of this composited view couldn't hide all of the popular shower's meteor streaks. The image captures some of the brightest perseid meteors in many short exposures recorded over more than two hours before the dawn. It places the shower's radiant in the heroic constellation of Perseus just behind a well-lit medieval tower in the village of Sant Llorenc de la Muga, Girona, Spain. Observed in medieval times, the Perseid meteor shower is also known in Catholic tradition as the Tears of St. Lawrence, and festivities are celebrated close to the annual peak of the meteor shower. Joining the Full Moon opposite the Sun, bright planet Saturn also shines in the frame at the upper right.",
#     wraplength=180,
#     fg="#FFF",
#     bg="#1e2227",
#     font=font_title,
# )
# text.grid(row=2, rowspan=2, column=1, columnspan=2, padx=25, pady=10)


# Name of the artiste
name_artist = Label(
    windows,
    text="@Juan Carlos Casado",
    fg="#FFF",
    bg="#1e2227",
    font=font_artist,
)
name_artist.grid(row=2, column=1)

# # ! To remove TEST
# def printhi():
#     print("Hi!")

# ? Maybe for a next feature
# # Button Left and Right
# btn_left = Button(
#     windows, text="<- Previous", command=printhi, bg="#1e2227", font=font_title, bd=0
# )
# btn_left.place(x=20, y=120)

# btn_right = Button(
#     windows, text="Next ->", command=printhi, bg="#1e2227", font=font_title, bd=0
# )
# btn_right.place(x=240, y=120)


# Luncher
windows.mainloop()
