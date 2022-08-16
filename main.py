import datetime, random, urllib.request, json, ctypes

"""
1 - Get the daily image from the NASA API (using the date of the computer)
2 - Save the Image in a folder and rename it 
3 - Set a time when the wallpaper should change (10am) 
4 - Change the wallpaper with the image of the day (same as the date of the computer)
5 - Delete the image older than 7 days 

Bonus : 
Keep the metadata of the img 
"""

# 1 - Get the daily image from the NASA API (using the date of the computer)
# Get the basic URL of the API
NASA_API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date="

# Date for the random_date function in case the post of the day is a video (between 2010 for HD content and the date of when the software is over to get wallpaper that I nerver saw before)
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2022, 8, 16)

# Get the date of the day with the good format for the API
date_of_the_day = datetime.datetime.now()
date_of_the_day = date_of_the_day.strftime("%Y-%m-%d")

# Concatenate to get the img of the day (exemple with 2022-08-14 for a video)
nasa_api_of_the_day = NASA_API + "2022-08-14"
# NASA_API = NASA_API + date_of_the_day

# Get the json data from the picture
response = urllib.request.urlopen(nasa_api_of_the_day)
nasa_data = json.loads(response.read())

# Return a date between the two argument in (YYYY-MM-DD)
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date_of_the_day = start_date + datetime.timedelta(days=random_number_of_days)
    return date_of_the_day.strftime("%Y-%m-%d")


# Get only the img
while nasa_data["media_type"] != "image":
    # Function random date
    date_of_the_day = random_date(start_date, end_date)
    nasa_api_of_the_day = NASA_API + date_of_the_day
    response = urllib.request.urlopen(nasa_api_of_the_day)
    nasa_data = json.loads(response.read())
    print("nasa_data: ", nasa_data)

# # 2 - Save the Image in a folder and rename it
# Rename the img
img_title = nasa_data["title"] + " " + date_of_the_day + ".jpg"
# Get the path for the save and download the img
path_to_img = "C:/Users/barre/OneDrive/Images/Nasa Wallpaper Python/" + img_title
urllib.request.urlretrieve(nasa_data["hdurl"], path_to_img)

# 3 - Change the wallpaper with the image of the day (same as the date of the computer)
ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_img, 0)

# 4 - Set a time when the wallpaper should change (10am)

# 5 - Delete the image older than 7 days
