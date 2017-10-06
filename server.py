from flask import Flask, abort, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/')
def all_news():
    return render_template('test_case.html')

# @app.route('/login/', methods=['POST'])
# def login():
#     return render_template('login.html', email=request.form.get('email'), password=request.form.get('password'))



if __name__ == '__main__':
    app.run(port = 5000, debug= True)
