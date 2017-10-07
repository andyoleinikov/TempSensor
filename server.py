from flask import Flask, abort, request, render_template
from tdb import Temp, db_session, add_temp
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/')
def all_news():
    return render_template('test_case.html')

@app.route('/temp/', methods=['POST'])
def temp_reciever():
    secret_key = request.form.get('key')
    if secret_key == '1234':
        temperature_recieved = request.form.get('temperature_recieved')
        device_name = request.form.get('device_name')
        print(temperature_recieved)
        print(device_name)


        add_temp("Zapolitsy", float(temperature_recieved), device_name, commit=True)

        return render_template('temperature.html', device_name = device_name, temperature_recieved = temperature_recieved)
    else:
        print('wrong key')
        return 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80 )

