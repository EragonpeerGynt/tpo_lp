from flask import *
import index as IND
import os
import calendar_app
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/calendar/add')
def koledar():
    return render_template("calendar_conf.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')
