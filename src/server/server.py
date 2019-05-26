# -*- coding: utf-8 -*-
from flask import *
import os
from dbase import database
import sys
import logging
import datetime
from calendar_app import app as calendar_app
from urnik_app import app as urnik_app
from todo_app import app as todo_app
from users_app import app as users_app
from geslo_app import app as geslo_app
from event_app import app as event_app

app = Flask(__name__)
app.secret_key='qohaevjiobsnerrrre'

app.register_blueprint(calendar_app, url_prefix = '/calendar')
app.register_blueprint(todo_app, url_prefix = '/todo')
app.register_blueprint(urnik_app, url_prefix = '/urnik')
app.register_blueprint(event_app, url_prefix = '/event')
app.register_blueprint(users_app, url_prefix = '')
app.register_blueprint(geslo_app, url_prefix = '')


@app.route('/')
@app.route('/index')
def index():
    try:
        user_id = session['id_u']
    except:
        return redirect(url_for("users_app.vpis"))
    current_app.logger.error(user_id)
    datum = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    dat=(user_id, datum)
    
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT id, naziv, zacetek FROM `vnosKoledar` WHERE idU = %s AND zacetek > %s ORDER BY zacetek ASC'
    cur.execute(query, dat)
    prihajajoce = cur.fetchall()
    cur.close()
    
    #current_app.logger.error(prihajajoce)
    #current_app.logger.error(prihajajoce[0][2].strftime('%d. %m. %Y %H:%M'))
    
    if len(prihajajoce) != 0:
        imena = ['id', 'naziv', 'datum']
        #for i in range(len(prihajajoce)):
        #    prihajajoce[i][2] = prihajajoce[i][2].strftime('%d. %m. %Y %H:%M')
        future_cal = [ { imena[j]:prihajajoce[i][j] for j in range(3)} for i in range(len(prihajajoce)) ]
        for i in range(len(future_cal)):
            future_cal[i]['datum'] = future_cal[i]['datum'].strftime('%d. %m. %Y %H:%M')
    else:
        future_cal = []
    
    return render_template("index.html", podatki_koledar=future_cal)

def heroku_start():
    return app

if __name__ == '__main__':
#    #localhost version
#    #app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')
#    #c9/server config
    app.run(debug=True, host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 8080)))
#    app.run(debug=True, use_reloader=True)


