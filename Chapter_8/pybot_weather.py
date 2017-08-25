import requests

def weather_command():
    # base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    # city_code ='130010'
    # proxy_code = "proxies={'http' : 'http://e024779:tiyoyo7!@172.17.96.21:12080'}"
    # url = '{}?city={}, {}'.format(base_url, city_code, proxy_code)
    # r = requests.get(url)
    r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010', proxies={"http" : 'http://e024779:tiyoyo7!@172.17.96.21:12080'})
    weather_data = r.json()
    city = weather_data['location']['city']
    label = weather_data['forecasts'][0]['dateLabel']
    telop = weather_data['forecasts'][0]['telop']

    response = '{}ノ天気ハ「{}」デス'.format(city, label, telop)
    return response