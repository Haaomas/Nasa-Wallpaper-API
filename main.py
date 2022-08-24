# Get the picture of  the day from the NASA API and change the windows wallpaper
import datetime, random, urllib.request, json, ctypes, os, webbrowser
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


# * 1 - Get the daily image from the NASA API (using the date of the computer)
# Get the basic URL of the API
NASA_API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date="
PATH = "C:/Users/barre/OneDrive/Bureau/Dev/Perso/GitHub/Nasa-Wallpaper-API/img/"

# Get the date of the day with the good format for the API
date_of_the_day = datetime.datetime.now()
date_of_the_day = date_of_the_day.strftime("%Y-%m-%d")

# Concatenate to get the img of the day (exemple with 2022-08-14 for a video)
nasa_api_of_the_day = NASA_API + date_of_the_day

# Get the json data from the picture
response = urllib.request.urlopen(nasa_api_of_the_day)
nasa_data = json.loads(response.read())
print("Data from the picture: ", nasa_data)


# * 2 - Date for the random_date function in case the post of the day is a video (between 2010 for HD content and the date of when the software is over to get wallpaper that I nerver saw before)
# Use for the make_random_date function
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2022, 8, 16)

# Return a date between the two argument in (YYYY-MM-DD)
def make_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date_of_the_day = start_date + datetime.timedelta(days=random_number_of_days)
    return date_of_the_day.strftime("%Y-%m-%d")


# Get only the img (safe state with loop)
loop = 0
while nasa_data["media_type"] != "image" or loop == 3:
    # Function random date
    random_date = make_random_date(start_date, end_date)

    # Get a new image with a random date generate by the function
    nasa_api_of_the_day = NASA_API + random_date

    # Get the json data from the picture
    response = urllib.request.urlopen(nasa_api_of_the_day)
    nasa_data = json.loads(response.read())
    print("nasa_data: ", nasa_data)
    print("loop: ", loop)

    # Incrémentation of loop for the safe state
    loop = loop + 1


# * 3 - Save the Image in a folder and rename it
# Rename wi th the date the img
img_title = date_of_the_day + ".jpg"

# Get the path for the save and download the img
path_to_img = PATH + img_title
saver = urllib.request.urlretrieve(nasa_data["hdurl"], path_to_img)


# * 4 - Change the wallpaper with the image of the day (same as the date of the computer)
ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_img, 0)


# * 5 - Delete the image older than 7 days
# To change if we want more or less time
SECONDE_IN_WEEK = 604800

# Read the variable's name
timestamp_of_the_day = datetime.datetime.now().timestamp()

# Get a dictionary of all the files in the PATH
files = os.listdir(PATH)

# Watch for the modification date of all the files in a folder
def delete_file_after_amount_of_time(files, path_to_folder, timestamp, amount_of_time):
    # Check for all files in the folder
    for file in range(len(files)):
        # Get the path and add the name of the file
        path_to_file = path_to_folder + files[file]

        # Get the timestamp of the modification date of the file
        timestamps_file = os.path.getmtime(path_to_file)

        # Calc the gap between the the current date and the file
        gap_timestamp = timestamp - timestamps_file

        # If the gap is greater than the select amount of time delete the file
        if gap_timestamp > amount_of_time:
            os.remove(path_to_file)
            print(f"Delete of the file {files[file]} complete")


delete_file_after_amount_of_time(files, PATH, timestamp_of_the_day, SECONDE_IN_WEEK)


# * 6 - Get a GUI


# Creation of the windows
windows = Tk()
# windows.geometry("310x120")
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
wallpaper_texte.grid(row=0, column=0, pady=10, padx=(25, 0))


# IMAGE OF THE DAY
# PATH = "C:/Users/barre/OneDrive/Bureau/Dev/Perso/GitHub/Nasa-Wallpaper-API/img/Full Moon Perseids 2022-08-18.jpg"
wallpaper_icon = ImageTk.PhotoImage(Image.open(path_to_img).resize((80, 80)))
panel = Label(windows, image=wallpaper_icon, bd=0)
# panel.place(x=20, y=40)
panel.grid(row=1, rowspan=3, column=0, pady=(0, 20))


# Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)


# Title of the picture
date_of_the_day = date_of_the_day[2:]
date_of_the_day_no_kebab = date_of_the_day.replace("-", "")
more_info_img_url = "https://apod.nasa.gov/apod/ap" + date_of_the_day_no_kebab + ".html"

title_picture = Label(
    windows,
    text=nasa_data["title"],
    fg="#3893ef",
    bg="#1e2227",
    cursor="hand2",
    font=font_text,
)
title_picture.grid(row=1, column=1, padx=(0, 20))
title_picture.bind("<Button-1>", lambda e: callback(more_info_img_url))

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
if "copyright" in nasa_data:
    name_artist = Label(
        windows,
        text=nasa_data["copyright"],
        fg="#FFF",
        bg="#1e2227",
        font=font_artist,
    )
    name_artist.grid(row=2, column=1, pady=(10, 0))
else:
    name_artist = Label(
        windows,
        text="@Danijel Cecelja",
        fg="#FFF",
        bg="#1e2227",
        font=font_artist,
    )
    name_artist.grid(row=2, column=1, pady=(10, 0))


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

# * 7 - Set a time when the wallpaper should change (10am)
