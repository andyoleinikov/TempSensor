from flask import Flask, abort, request, render_template
from tdb import Temp, db_session, add_temp
from datetime import datetime
from graph_plotter_easy import get_plot_html


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/')
def plot_graph():
    source = request.args.get('source', 'gismeteo')
    req_date = request.args.get('date', 'now')
    # return render_template('test_case.html')
    if req_date == 'now': 
        return get_plot_html(source=source, date=datetime.now())
    else:
        req_date = datetime.strptime(req_date, '%Y-%m-%d')
        plot_html = get_plot_html(source=source, date =req_date)
        return render_template('test_case.html', plot_html=plot_html)



@app.route('/temp/', methods=['POST'])
def temp_reciever():
    secret_key = request.form.get('key')
    if secret_key == '1234':
        temperature_recieved = request.form.get('temperature_recieved')
        source = request.form.get('source')
        date = request.form.get('date')
        print(temperature_recieved)
        print(source)


        add_temp("Zapolitsy", float(temperature_recieved), source=source, date = date, commit=True)

        return render_template('temperature.html', source = source, temperature_recieved = temperature_recieved)
    else:
        print('wrong key')
        return 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000 , debug=True)

