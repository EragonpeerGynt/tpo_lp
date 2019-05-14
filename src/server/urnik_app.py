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
        dat =  (naziv, opis, trajanje, zacetek, idU)
        query = 'INSERT INTO `vnosurnik` (naziv, barva, trajanje, zacetek, dan, idU) VALUES (%s, %s, %s, %s, %s, %s);'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))
        
