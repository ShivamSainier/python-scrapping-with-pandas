import requests
import bs4 as bs

req=requests.get('https://forecast.weather.gov/MapClick.php?x=133&y=65&site=mfr&zmx=&zmy=&map_x=133&map_y=65#.XkuaaSgzbIU')
soup=bs.BeautifulSoup(req.content,'html.parser')
item=soup.find(id='seven-day-forecast-list')

period=item.find_all(class_="period-name")
short=item.find_all(class_="short-desc")
temp=item.find_all(class_="temp temp-low")
print(period)
print(short)
print(temp)
