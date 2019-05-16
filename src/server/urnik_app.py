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


app = Blueprint('urnik_app', __name__)

@app.route('/add')
def urnik():
    return render_template("urnik_add.html", date="2019-05-11")
    
@app.route('/add/confirm')
def urnik_potrdi_prazen():
    return render_template("index.html")
 
@app.route('/add/confirm', methods=['post']) 
def urnik_potrdi():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
        
    elif request.form.get('continue') == "Save changes":
        
        naziv = request.form.get('title')
        barva = request.form.get('color')
        trajanje = request.form.get('duration')
        zacetek = request.form.get('time')
        dan = request.form.get('day')
        idU = str(session['id_u'])
        
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((naziv, barva, trajanje, zacetek, dan, idU))
        dat =  (naziv, barva, trajanje, zacetek, dan, idU)
        query = 'INSERT INTO `vnosurnik` (naziv, barva, trajanje, zacetek, dan, idU) VALUES (%s, %s, %s, %s, %s, %s);'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))
        
@app.route('/update/<id_urnik>')
def urnik_posodobi(id_urnik):
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT * FROM `vnosurnik` WHERE id = %s AND idU = %s'
    try:
        dat = (id_urnik, session['id_u'])
    except:
        return redirect(url_for("index"))
    cur.execute(query, dat)
    
    event = cur.fetchall()
    cur.close
    current_app.logger.error(event)
    
    if len(event) != 0:
        event = event[0]
        current_app.logger.error(event)
        
        naziv=event[1]
        barva=event[2]
        trajanje=event[3]
        zacetek=event[4]
        dan=event[5]
        id_urnik=event[0]
        #current_app.logger.error(opis)
        return render_template("urnik_update.html", id_urnik=id_urnik, title=naziv, duration=trajanje, time=zacetek,  day=dan, color=barva)
        
    else:
        return redirect(url_for("index"))
        
@app.route('/update/confirm', methods=['post'])
def urnik_posodobi_vnos():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
    elif request.form.get('continue') == "Save changes":
        id_urnik = request.form.get('id_urnik')
        naziv = request.form.get('title')
        barva = request.form.get('color')
        trajanje = request.form.get('duration')
        zacetek = request.form.get('time')
        dan = request.form.get('day')
        idU = str(session['id_u'])
        
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((naziv, opis, trajanje, zacetek, idU))
        dat = (naziv, barva, trajanje, zacetek, dan, id_urnik, idU)
        query = 'UPDATE `vnosurnik` SET naziv = %s, barva = %s, trajanje = %s, zacetek = %s dan = %s WHERE id = %s AND idU = %s'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))