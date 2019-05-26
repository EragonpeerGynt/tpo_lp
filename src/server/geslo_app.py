from flask import *
from flask_mail import Mail
from flask_mail import Message
import os
import datetime
from dbase import database
import sys
import logging
import hashlib

app = Blueprint('geslo_app', __name__)

@app.route('/spremembaGesla')
def sprem():
    
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U == -1:
        return redirect(url_for('users_app.vpis'))
    
    obvestilo=""
    return render_template("geslo.html", napaka=obvestilo)

@app.route('/spremembaGesla', methods = ['POST'])
def spremeni():
    
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U == -1:
        return redirect(url_for('users_app.vpis'))
    
    if request.form['knof'] == "Nazaj":
        return redirect(url_for("index"))
        
    obvestilo=""    
    
    geslo1 = request.form['geslo1']
    geslo2 = request.form['geslo2']
    novoGeslo = request.form['novoGeslo']
    
    if geslo1 != geslo2:
        obvestilo="Vpisano staro geslo je napacno."
        return render_template("geslo.html", napaka=obvestilo)
    
    if len(novoGeslo) < 8:
        obvestilo="Geslo je prekratko."
        return render_template("geslo.html", napaka=obvestilo)
    
    #id_U= session['id_u']
    
    gesloo=hashlib.md5(geslo1).hexdigest()
    
    db = database.dbcon()
    cur = db.cursor()
    
    #pogledamo, ce obstaja, in uzamemo se geslo
    table = 'SELECT id FROM `Uporabnik` WHERE id = %s AND geslo = %s;'
    cur.execute(table, (id_U, gesloo, ))
    records = cur.fetchall()
    
    if len(records) == 0:
        obvestilo="Vpisano staro geslo je napacno."
        return render_template("geslo.html", napaka=obvestilo)
        
    geslooo=hashlib.md5(novoGeslo).hexdigest()    
        
    query = 'UPDATE `Uporabnik` SET geslo = %s WHERE id = %s'
    cur.execute(query, (geslooo, id_U, ))
    db.commit()
    
    cur.close();
    
    obvestilo="Geslo je bilo uspesno posodobljeno."
    return render_template("geslo.html", napaka=obvestilo)