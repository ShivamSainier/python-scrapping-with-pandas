import requests
import bs4 as bs
import pandas as pd
import csv

req=requests.get('https://forecast.weather.gov/MapClick.php?x=133&y=65&site=mfr&zmx=&zmy=&map_x=133&map_y=65#.XkuaaSgzbIU')
soup=bs.BeautifulSoup(req.content,'html.parser')
items=soup.find(id='seven-day-forecast-list')

period=[item.find(class_="period-name").get_text() for item in items]
short=[item.find(class_="short-desc").get_text() for item in items]

weekframe=pd.DataFrame({
    'period-time':period,
    'short':short
    })
print(weekframe)
weekframe.to_csv('wheather.csv')


