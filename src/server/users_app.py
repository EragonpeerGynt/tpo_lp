from flask import *
#from flask_mail import Mail
#from flask_mail import Message
#from validate_email import validate_email
import smtplib
from email import message
import os
import datetime
from datetime import timedelta
from dbase import database
import sys
import logging
import re
import hashlib

app = Blueprint('users_app', __name__)

@app.route('/register', methods=['POST'])
def registracija():
    
    #preverimo, da nihce ni prijavljen
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U != -1:
        return redirect(url_for("index"))
    
    if request.form['knof'] == "Prijavi se":
        return redirect(url_for('users_app.vpis'))
    obvestilo=""
    uporabnisko = request.form['mail']
    geslo = request.form['geslo']
    
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", uporabnisko):
        obvestilo="Elektronski naslov ni veljaven."
        return render_template("register.html", napaka=obvestilo)
    
    
    if len(geslo) < 8:
        obvestilo="Geslo je prekratko."
        return render_template("register.html", napaka=obvestilo)
    
    db = database.dbcon()
    cur = db.cursor()
    
    table = 'SELECT COUNT(*) FROM Uporabnik where mail=%s;'
    cur.execute(table, (uporabnisko, ))
    records = cur.fetchone()
    
    st_takih=1
    
    try:
        st_takih= records[0]
    except:
        st_takih= 0
    
    #ce ze obstaja
    if st_takih != 0:
        obvestilo="Ta elektronski naslov je ze registriran."
        return render_template("register.html", napaka=obvestilo)
        
        
    query = 'INSERT INTO `Uporabnik` (mail, geslo, status, potrjen) VALUES (%s, %s, %s, %s)'
    cur.execute(query, (uporabnisko, geslo, 0, 0))
    db.commit()
    cur.close()
    
    #naredimo vsebino emaila
    now = datetime.datetime.now()
    leto= str(now.year)
    mesec= str(now.month)
    dan= str(now.day)
    
    vsebina= uporabnisko+leto+mesec+dan
    
    hesh=hashlib.md5(vsebina).hexdigest()
    
    sporocilo = url_for('users_app.preveri2',  _external=True)+"/"+uporabnisko+"<>"+hesh
    
    #naredimo mail
    #from_addr = 'info.straightas@yandex.com'
    from_addr = 'info.starightas@gmail.com'
    to_addr = uporabnisko
    subject = 'Registracija pri StraightAs'
    body = 'Pozdrav. Pred kratkim je bila opravljena registracija na strani StraightAs. Tukaj je link za potrditev registracije: '+sporocilo
    
    msg = message.Message()
    msg.add_header('from', from_addr)
    msg.add_header('to', to_addr)
    msg.add_header('subject', subject)
    msg.set_payload(body)
    
    #current_app.logger.error("Naredimo sporocilo")
    #current_app.logger.error(body)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    
    #current_app.logger.error("Povezemo na server")
    
    server.login(from_addr, 'tpo072019')
    
    #current_app.logger.error("Posljemo login informacije")
    
    #server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
    
    server.sendmail(from_addr, to_addr, msg.as_string())
    
    #current_app.logger.error("Posljemo sporocilo")
    
    server.quit()
    
    obvestilo="Na vnesen elektronski naslov smo poslali sporocilo za potrditev registracije. Registracijo morate potrditi v dveh dnevih."
    
    return render_template("register.html", napaka=obvestilo)
    
@app.route('/register')
def regist():
    
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U != -1:
        return redirect(url_for("index"))
    
    obvestilo=""
    return render_template("register.html", napaka=obvestilo)
    
@app.route('/preveri')
def preveri2():
    return redirect(url_for("index"))
    
@app.route('/preveri/<nekaj>')
def preveri(nekaj):
    obvestilo=""
    
    #preverimo, da nihce ni prijavljen
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U != -1:
        return redirect(url_for("index"))
    
    hesh=nekaj
    
    uporabnisko, hesh=hesh.split("<>")
    
    now = datetime.datetime.now()
    leto= str(now.year)
    mesec= str(now.month)
    dan= str(now.day)
    
    danes= leto+mesec+dan
    
    vceraj= datetime.date.today() - timedelta(days=1)
    letoV= str(vceraj.year)
    mesecV= str(vceraj.month)
    danV= str(vceraj.day)
    
    vceraj= letoV+mesecV+danV
    
    vceraj2= datetime.date.today() - timedelta(days=2)
    letoP= str(vceraj2.year)
    mesecP= str(vceraj2.month)
    danP= str(vceraj2.day)
    
    predvcernjem= letoP+mesecP+danP
    
    vsebina1=uporabnisko+danes
    vsebina2= uporabnisko+vceraj
    vsebina3= uporabnisko+predvcernjem
    
    hesh1=hashlib.md5(vsebina1).hexdigest()
    hesh2=hashlib.md5(vsebina2).hexdigest()
    hesh3=hashlib.md5(vsebina3).hexdigest()
    
    current_app.logger.error(('zunanji if', hesh1, hesh2, hesh3, hesh))
    
    if hesh1 == hesh or hesh2 == hesh or hesh3 == hesh:
        
        db = database.dbcon()
        cur = db.cursor()
        
        stavek = 'SELECT id from `Uporabnik` where mail=%s and potrjen=%s;'
        cur.execute(stavek, (uporabnisko, '1', ))
        preveri=cur.fetchall()
        
        current_app.logger.error(('notranji if', preveri))
        
        if len(preveri) != 0:
            obvestilo="Ta elektronski naslov je ze bil potrjen."
            return render_template("preverjanje.html", napaka=obvestilo)
        
        query = 'UPDATE `Uporabnik` SET potrjen = %s WHERE mail = %s;'
        cur.execute(query, ('1', uporabnisko, ))
        db.commit()
        cur.close()
        
        obvestilo="Uspesno ste potrdili registracijo."
        return render_template("preverjanje.html", napaka=obvestilo)
        
    else:
        obvestilo="Registracije niste potrdili pravocasno."
        
    if request.form['knof'] == "Prijavi se":
        return redirect(url_for('users_app.vpis'))
    
    return render_template("preverjanje.html", napaka=obvestilo)
    
@app.route('/logout')
def izpis():
    session.clear()
    return redirect(url_for('users_app.vpis'))
 
@app.route('/login', methods = ['POST']) 
def vpis():
    
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U != -1:
        return redirect(url_for("index"))
    
    
    obvestilo=""
    
    if request.form['knof'] == "Registriraj se":
        return redirect(url_for('users_app.registracija'))
    
    uporabnisko = request.form['uporabnisko']
    geslo = request.form['geslo']
    
    current_app.logger.error(uporabnisko);
    
    db = database.dbcon()
    cur = db.cursor()
    
    #pogledamo, ce obstaja, in uzamemo se geslo
    table = 'SELECT mail FROM Uporabnik where mail = %s;'
    cur.execute(table, (uporabnisko, ))
    records = cur.fetchall()
    
    current_app.logger.error(records);
    
    if len(records) == 0:
        obvestilo="Ta elektronski naslov se ni registriran."
        return render_template("login.html", napaka=obvestilo)
    
    table = 'SELECT id FROM Uporabnik where mail = %s and geslo = %s and potrjen = %s;'
    cur.execute(table, (uporabnisko, geslo, '1', ))
    records = cur.fetchall()
    
    cur.close();
    idU = 222
    
    try:
        idU = records[0]
    except:
        obvestilo="Napacen elektronski naslov ali geslo."
        return render_template("login.html", napaka=obvestilo)
    
    #ce je geslo vredu
    session['id_u'] = idU
            
    return redirect(url_for("index"))
    
@app.route('/login')
def vpis_zacetni():
    
    id_U=-1
    try:
        id_U = session['id_u']
    except:
        id_U = -1
        
    if id_U != -1:
        return redirect(url_for("index"))
    
    obvestilo=""
    return render_template("login.html", napaka=obvestilo)