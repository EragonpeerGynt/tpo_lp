from flask import *
import os
import datetime
from dbase import database
import sys
import logging

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
        idU = '3'
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