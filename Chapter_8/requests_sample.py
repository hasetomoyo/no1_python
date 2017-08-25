import requests

city_code ='130010'
r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010', proxies={"http" : 'http://e024779:tiyoyo7!@172.17.96.21:12080'})
weather_data = r.json()
city = weather_data['location']['city']
label = weather_data['forecasts'][0]['dateLabel']
telop = weather_data['forecasts'][0]['telop']
response = '{}ノ{}ノ天気ハ「{}」デス'.format(city, label, telop)

print(r.status_code)
print(response)