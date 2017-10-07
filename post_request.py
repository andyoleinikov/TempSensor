import requests 

API_ENDPOINT = "http://10.56.5.109/temp/" 
data = {
    'key': '1234',
    'device_name': 'RPI_sensor', 
    'temperature_recieved': '16'
}
r = requests.post(url = API_ENDPOINT, data = data)

r
print(r)