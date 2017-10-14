import requests 
import time
from get_temp import get_temp_from_file


API_ENDPOINT = "http://52.59.246.220/temp" 
while True:
    temp = get_temp_from_file()
    data = {
        'key': '1234',
        'device_name': 'RPI_sensor', 
        'temperature_recieved': temp
    }
    r = requests.post(url = API_ENDPOINT, data = data)
    print(r)
    print(r.text)
    time.sleep(5)
