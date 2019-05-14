# -*- coding: utf-8 -*-
from flask import *
import os
from dbase import database
import sys
import logging

from calendar_app import app as calendar_app
from urnik_app import app as urnik_app

app = Flask(__name__)
app.secret_key=os.urandom(16)

app.register_blueprint(calendar_app, url_prefix = '/calendar')
app.register_blueprint(urnik_app, url_prefix = '/urnik')

@app.route('/')
@app.route('/index')
def index():
    session['id_u'] = 3
    return render_template("index.html")


if __name__ == '__main__':
    #localhost version
    #app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')
    #c9/server config
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
