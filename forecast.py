import requests
import datetime
import settings

city_id = 580227
apikey = settings.apikey


def get_weather_json(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else: 
        return 'something is wrong'


def get_weather_lists(city_id = 580227):
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=%s&units=metric' %(city_id, apikey)
    weather = get_weather_json(url)
    forecast_temps = []
    forecast_dates = []

    for element in range(0, len(weather['list'])):
        temp = float(weather['list'][element]['main']['temp_min'])
        forecast_temps.append(temp)
        forecast_dates.append(datetime.datetime.strptime(weather['list'][element]['dt_txt'] ,'%Y-%m-%d %H:%M:%S'))
    return(forecast_dates, forecast_temps)



if __name__ == '__main__':
    get_weather_lists()
