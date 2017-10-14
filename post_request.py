import requests 
import random 
import time


while True:
    input_temp = random.randrange(-30, 30, 1)    
    API_ENDPOINT = "http://10.56.5.109/temp/" 
    data = {
        'key': '1234',
        'source': 'RPI_sensor', 
        'temperature_recieved': input_temp
    }
    r = requests.post(url = API_ENDPOINT, data = data)
    r
    print(r)
    print(input_temp)
    time.sleep(15)


