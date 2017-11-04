from flask import Flask, abort, request, render_template
from tdb import Temp, db_session, add_temp
from datetime import datetime
from graph_plotter_easy import get_plot


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/graph/')
def plot_graph():
    tempage = 'test_case_graph.html' if request.is_xhr else 'test_case.html'

    req_date = request.args.get('date', None)
    if req_date: 
        req_date = datetime.strptime('2017-'+req_date, '%Y-%m-%d')
    else:
        req_date = datetime.now()

    plot_html = get_plot(date=req_date, output='html')
    return render_template(tempage, plot_html=plot_html)


@app.route('/temp/', methods=['POST'])
def temp_reciever():
    secret_key = request.form.get('key')
    if secret_key == '1234':
        temperature_recieved = request.form.get('temperature_recieved')
        source = request.form.get('source')
        date_recieved = datetime.strptime( request.form.get('date'), '%Y %m %d %H:%M')
        print(temperature_recieved)
        print(source, '  date recieved ',date_recieved )
        date = date_recieved #.strftime('%Y $m $d %H %M')


        add_temp("Zapolitsy", float(temperature_recieved), source=source, date = date, commit=True)

        return render_template('temperature.html', source = source, temperature_recieved = temperature_recieved)
    else:
        print('wrong key')
        return 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000 , debug=True)

