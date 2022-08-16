import datetime
import urllib.request, json


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
NasaApi = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Get the date of the day with the good format for the API 
dateOfTheDay = datetime.datetime.now()
dateOfTheDay = dateOfTheDay.strftime("%Y-%m-%d")

# Concatenate to get the img of the day 
NasaApi = NasaApi + "&date=" + dateOfTheDay

# Get the json data from the picture 
response = urllib.request.urlopen(NasaApi)
NasaData = json.loads(response.read())
print(NasaData['url'])

# 2 - Save the Image in a folder 
imgTitle = NasaData['title'] + " " + dateOfTheDay + ".jpg"
print('imgTitle: ', imgTitle)
pathToFolder = "C:/Users/barre/OneDrive/Images/Nasa Wallpaper Python/" + imgTitle
print('pathToFolder: ', pathToFolder)
urllib.request.urlretrieve(NasaData['url'], pathToFolder)



# 3 - Rename the image with the date of the day 
# 4 - Set a time when the wallpaper should change (10am) 
# 5 - Change the wallpaper with the image of the day (same as the date of the computer)
# 6 - Delete the image older than 7 days 
    
    