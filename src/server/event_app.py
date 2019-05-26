# -*- coding: utf-8 -*-
from flask import *
import os
import datetime
from dbase import database
import sys
import logging

try:
    basestring
    decode = lambda x: x.decode("utf-8")
except NameError:
    decode = lambda x: x


app = Blueprint('event_app', __name__)

@app.route('/')
def zacetna_stran():
    try:
        user_id = session['id_u']
    except:
        return redirect( url_for('index') )
    
        
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT status FROM `Uporabnik` WHERE id = %s'
    dat = (user_id,)
    cur.execute(query, dat)
    dat = cur.fetchall()
    cur.close()
    
    try:
        status = dat[0]
    except:
        return redirect( url_for('index') )
        
    cur = db.cursor()
    query = 'SELECT id, ime, datum FROM `dogodek`'
    cur.execute(query, ())
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
    
    
    current_app.logger.error(status)
    return render_template("events.html", podatki_dogodki=future_cal, status=status)

@app.route('/add')
def vnesi_podatke_nov():
    try:
        user_id = session['id_u']
    except:
        return redirect( url_for('index') )
    
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT id FROM `Uporabnik` WHERE id = %s AND status = %s'
    dat = (user_id, '1')
    cur.execute(query, dat)
    
    event = cur.fetchall()
    cur.close
    
    if len(event) == 0:
        return redirect( url_for('index') )
    
    return render_template("event_add.html")
    
@app.route('/add', methods=['post'])
def dodaj_dogodek():
    try:
        user_id = session['id_u']
    except:
        return redirect( url_for('index') )
    
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT id FROM `Uporabnik` WHERE id = %s AND status = %s'
    dat = (user_id, '1')
    cur.execute(query, dat)
    
    event = cur.fetchall()
    
    if len(event) == 0:
        cur.close()
        return redirect( url_for('index') )
        
    name = request.form.get('name')
    date = request.form.get('date')
    organizer = request.form.get('organizer')
    description = request.form.get('description')
    
    dat = (name, date, organizer, description)
    current_app.logger.error(dat)
    
    query = 'INSERT INTO `dogodek` (ime, datum, organizator, opis) VALUES (%s, %s, %s, %s);'
    cur.execute(query, dat)
    db.commit()
    cur.close()
        
    return redirect( url_for("index") )