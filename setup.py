from flask import *
import os
import sys
import logging

app = Flask(__name__)
app.secret_key='qohaevjiobsnerrrre'

@app.route('/')
@app.route('/index')
def index():
    return "hello world"

if __name__ == '__main__':
    #localhost version
    #app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')
    #c9/server config
    app.run(debug=True, host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 33507)))