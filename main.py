# Get the picture of  the day from the NASA API and change the windows wallpaper
import datetime, random, urllib.request, json, ctypes, os


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
# Rename the img
img_title = nasa_data["title"] + " " + date_of_the_day + ".jpg"
# Get the path for the save and download the img
path_to_img = PATH + img_title
urllib.request.urlretrieve(nasa_data["hdurl"], path_to_img)


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


# * 6 - Set a time when the wallpaper should change (10am)
