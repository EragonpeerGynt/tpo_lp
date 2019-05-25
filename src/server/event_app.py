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