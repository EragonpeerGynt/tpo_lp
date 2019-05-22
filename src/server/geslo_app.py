from flask import *
from flask_mail import Mail
from flask_mail import Message
import os
import datetime
from dbase import database
import sys
import logging

app = Blueprint('geslo_app', __name__)

@app.route('/spremembaGesla')
def sprem():
    obvestilo=""
    return render_template("geslo.html", napaka=obvestilo)

@app.route('/spremembaGesla', methods = ['POST'])
def spremeni():
    if request.form['knof'] == "Nazaj":
        return redirect(url_for("index"))
        
    obvestilo=""    
    
    geslo1 = request.form['geslo1']
    geslo2 = request.form['geslo2']
    novoGeslo = request.form['novoGeslo']
    
    if len(novoGeslo) < 8:
        obvestilo="Geslo je prekratko."
        return render_template("geslo.html", napaka=obvestilo)
    
    #id_U= session['id_u']
    id_U=1
    
    db = database.dbcon()
    cur = db.cursor()
    
    #pogledamo, ce obstaja, in uzamemo se geslo
    table = 'SELECT id FROM `Uporabnik` WHERE id = %s AND geslo = %s OR geslo = %s;'
    cur.execute(table, (id_U, geslo1, geslo2, ))
    records = cur.fetchall()
    
    takih=0
    
    try:
        takih=len(records)
    except:
        takih=0
    
    if takih == 0:
        obvestilo="Vpisano staro geslo je napacno."
        return render_template("geslo.html", napaka=obvestilo)
        
    query = 'UPDATE `Uporabnik` SET geslo = %s WHERE id = %s'
    cur.execute(query, (novoGeslo, id_U, ))
    db.commit()
    
    cur.close();
    
    obvestilo="Geslo je bilo uspesno posodobljeno."
    return render_template("geslo.html", napaka=obvestilo)