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


app = Blueprint('calendar_app', __name__)

@app.route('/add/<date>')
def koledar(date):
    return render_template("calendar_add.html", date=date)
    
@app.route('/add/confirm')
def koledar_potrdi_prazen():
    return render_template("index.html")
 
@app.route('/add/confirm', methods=['post']) 
def koledar_potrdi():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
        
    elif request.form.get('continue') == "Save changes":
        
        naziv = request.form.get('title')
        opis = request.form.get('description')
        trajanje = request.form.get('duration')
        zacetekTH = request.form.get('timeH')
        zacetekTM = request.form.get('timeM')
        zacetekD = request.form.get('date')
        zacetekD = zacetekD.split("-")
        idU = str(session['id_u'])
        zacetek = datetime.datetime(int(zacetekD[0]), int(zacetekD[1]), int(zacetekD[2]), int(zacetekTH), int(zacetekTM))
        zacetek = zacetek.strftime('%Y-%m-%d %H:%M')
        
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((naziv, opis, trajanje, zacetek, idU))
        dat =  (naziv, opis, trajanje, zacetek, idU)
        query = 'INSERT INTO `vnosKoledar` (naziv, opis, trajanje, zacetek, idU) VALUES (%s, %s, %s, %s, %s);'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))
        
@app.route('/update/<id_calendar>')
def koledar_posodobi(id_calendar):
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT * FROM `vnosKoledar` WHERE id = %s AND idU = %s'
    try:
        dat = (id_calendar, session['id_u'])
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
        opis=event[2]
        trajanje=event[3]
        zacetek=event[4]
        id_calendar=event[0]
        date = str(zacetek.year) + "-" + str(zacetek.month) + "-" + str(zacetek.day)
        zacetekTH = str(zacetek.hour)
        zacetekTM = str(zacetek.minute)
        current_app.logger.error(opis)
        return render_template("calendar_update.html", id_calendar=id_calendar, title=naziv, duration=trajanje, timeH=zacetekTH, timeM=zacetekTM, date=date, description=opis)
        
    else:
        return redirect(url_for("index"))
        
@app.route('/update/confirm', methods=['post'])
def koledar_posodobi_vnos():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
    elif request.form.get('continue') == "Save changes":
        id_calendar = request.form.get('id_calendar')
        naziv = request.form.get('title')
        opis = request.form.get('description')
        trajanje = request.form.get('duration')
        zacetekTH = request.form.get('timeH')
        zacetekTM = request.form.get('timeM')
        zacetekD = request.form.get('date')
        zacetekD = zacetekD.split("-")
        idU = str(session['id_u'])
        zacetek = datetime.datetime(int(zacetekD[0]), int(zacetekD[1]), int(zacetekD[2]), int(zacetekTH), int(zacetekTM))
        zacetek = zacetek.strftime('%Y-%m-%d %H:%M')
        
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((naziv, opis, trajanje, zacetek, idU))
        dat = (naziv, opis, trajanje, zacetek, id_calendar, idU)
        query = 'UPDATE `vnosKoledar` SET naziv = %s, opis = %s, trajanje = %s, zacetek = %s WHERE id = %s AND idU = %s'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))