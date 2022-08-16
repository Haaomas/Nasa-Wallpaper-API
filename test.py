import datetime, random, urllib.request, json 

# nasa_api = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# start_date = datetime.date(2010, 1, 1)
# print('start_date: ', start_date)
# print(type(start_date))
# end_date = datetime.date(2022, 8, 16)
# print('end_date: ', end_date)
# time_between_dates = end_date - start_date
# print('time_between_dates: ', time_between_dates)
# days_between_dates = time_between_dates.days
# print('days_between_dates: ', days_between_dates)
# random_number_of_days = random.randrange(days_between_dates)
# date_of_the_day = start_date + datetime.timedelta(days=random_number_of_days)
# date_of_the_day = date_of_the_day.strftime("%Y-%m-%d")
# print('date_of_the_day: ', date_of_the_day)
# print(type(date_of_the_day))

# # nasa_api = nasa_api + "&date=" + date_of_the_day
# # response = urllib.request.urlopen(nasa_api)
# # nasa_data = json.loads(response.read())

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2022, 8, 16)


def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date_of_the_day = start_date + datetime.timedelta(days=random_number_of_days)
    date_of_the_day = date_of_the_day.strftime("%Y-%m-%d")
    return date_of_the_day

test = random_date(start_date, end_date)
print(test)
