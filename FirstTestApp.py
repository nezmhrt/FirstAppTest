import requests
from bs4 import BeautifulSoup


# url for tenki.jp
url = 'https://tenki.jp/forecast/3/17/4620/14152/'

r = requests.get(url)


soup = BeautifulSoup(r.content, "html.parser")

todays_weather = soup.find(class_="today-weather")

# Todays weather
weather = todays_weather.p.string

print('今日の天気は{}です。'.format(weather))
