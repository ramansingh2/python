from bs4 import BeautifulSoup
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import requests

page=requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XocMkIgzahM")
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)
# print()
# print(soup.find_all('a'))
week=soup.find(id="seven-day-forecast-body")
#print(week)
items=week.find_all(class_="tombstone-container")
# print(items[0])
print(items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())
print()
period_names=[item.find(class_="period-name").get_text() for item in items]
short_des=[item.find(class_="short-desc").get_text() for item in items]
temp=[item.find(class_="temp").get_text() for item in items]
print(period_names)
print(short_des)
print(temp)
print()
weather=pd.DataFrame(
    {'period':period_names,
     'short_desc':short_des,
     'temp':temp,}
)
print(weather)
weather.to_csv('weather.csv')
print()
headers=['sno','time','desc','temp']
print(tabulate(weather,headers=headers,tablefmt='grid'))
