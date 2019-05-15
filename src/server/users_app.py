from flask import *
import os
import datetime
from dbase import database
import sys
import logging

app = Blueprint('users_app', __name__)

@app.route('/register')
def registracija():
    obvestilo=""
    uporabnisko = request.form['uporabnisko']
    geslo = request.form['geslo']
    
    if len(geslo) < 8:
        obvestilo="Geslo je prekratko."
        return render_template("register.html", napaka=obvestilo)
    
    db = database.dbcon()
    cur = db.cursor()
    
    table = 'SELECT COUNT(*) FROM Uporabnik where mail=%s;'
    cur.execute(table, (uporabnisko, ))
    records = cur.fetchone()
    
    st_takih= records[0]
    
    #ce ze obstaja
    if st_takih != 0:
        obvestilo="Ta elektronski naslov je ze registriran."
        return render_template("register.html", napaka=obvestilo)
        
    query = 'INSERT INTO `Uporabnik` (mail, geslo, status, potrjen) VALUES (%s, %s, %s, %s)'
    cur.execute(query, (uporabnisko, geslo, 0, 0))
    db.commit()
    cur.close()
    
    obvestilo="Na vnesen elektronski naslov smo poslali sporocilo za potrditev registracije. Registracijo morate potrditi v dveh dnevih."
    
    return render_template("login.html", napaka=obvestilo)
    
@app.route('/logout')
def izpis():
    session.clear()
    obvestilo = ""
    return render_template("login.html", napaka=obvestilo)
 
@app.route('/login', methods = ['POST']) 
def vpis():
    obvestilo=""
    uporabnisko = request.form['uporabnisko']
    geslo = request.form['geslo']
    
    db = database.dbcon()
    cur = db.cursor()
    
    #pogledamo, ce obstaja, in uzamemo se geslo
    table = 'SELECT COUNT(*) FROM Uporabnik where mail=%s;'
    cur.execute(table, (uporabnisko, ))
    records = cur.fetchone()
    
    st_takih= records[0]
    
    
    #ce ni takega
    if st_takih == 0:
        obvestilo="Ta elektronski naslov se ni registriran."
        return render_template("login.html", napaka=obvestilo)
    
    #ce je tak
    table = 'SELECT geslo, id FROM Uporabnik where mail=%s;'
    cur.execute(table, (uporabnisko, ))
    records = cur.fetchone()
    
    cur.close();
    
    geslo1 = records[0][0]
    
    #ce je geslo napacno
    if (geslo1 != geslo ):
        obvestilo="Napacen elektronski naslov ali geslo."
        return render_template("login.html", napaka=obvestilo)
        
    #ce je geslo vredu
    idU = records[0][1]
    session['id_u'] = idU
            
    return redirect(url_for("index"))
    
@app.route('/login')
def vpis_zacetni():
    return render_template("login.html")