# -*- coding: utf-8 -*-
from flask import *
import os
from dbase import database
import sys
import logging

from calendar_app import app as calendar_app
from urnik_app import app as urnik_app
from todo_app import app as todo_app
from users_app import app as users_app
from event_app import app as event_app

app = Flask(__name__)
app.secret_key='qohaevjiobsnerrrre'

app.register_blueprint(calendar_app, url_prefix = '/calendar')
app.register_blueprint(todo_app, url_prefix = '/todo')
app.register_blueprint(urnik_app, url_prefix = '/urnik')
app.register_blueprint(event_app, url_prefix = '/event')
app.register_blueprint(users_app, url_prefix = '')


@app.route('/')
@app.route('/index')



def index():
    return render_template("index.html")

def heroku_start():
    return app

if __name__ == '__main__':
#    #localhost version
#    #app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')
#    #c9/server config
    app.run(debug=True, host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 8080)))
#    app.run(debug=True, use_reloader=True)


