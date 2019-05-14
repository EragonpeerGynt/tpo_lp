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


app = Blueprint('todo_app', __name__)

@app.route('/add')
def todo():
    return render_template("todo_add.html", date="2019-05-11")
    
@app.route('/add/confirm')
def todo_potrdi_prazen():
    return render_template("index.html")
 
@app.route('/add/confirm', methods=['post']) 
def todo_potrdi():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
        
    elif request.form.get('continue') == "Save changes":
        
        vsebina = request.form.get('content')
        
        idU = str(session['id_u'])
                
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((vsebina, idU))
        dat =  (vsebina, idU)
        query = 'INSERT INTO `vnosTODO` (vsebina, idU) VALUES (%s, %s);'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))
        
@app.route('/update/<id_todo>')
def todo_posodobi(id_todo):
    db = database.dbcon()
    cur = db.cursor()
    query = 'SELECT * FROM `vnosTODO` WHERE id = %s AND idU = %s'
    try:
        dat = (id_todo, session['id_u'])
    except:
        return redirect(url_for("index"))
    cur.execute(query, dat)
    
    event = cur.fetchall()
    cur.close
    current_app.logger.error(event)
    
    if len(event) != 0:
        event = event[0]
        current_app.logger.error(event)
        
        vsebina = request.form.get('content')
        
        idU = str(session['id_u'])
        
        return render_template("todo_update.html", id_todo=id_todo, content=vsebina)
        
    else:
        return redirect(url_for("index"))
        
@app.route('/update/confirm', methods=['post'])
def todo_posodobi_vnos():
    if request.form.get("continue") == "cancel":
        return redirect(url_for("index"))
    elif request.form.get('continue') == "Save changes":
        id_todo = request.form.get('id_todo')
        vsebina = request.form.get('content')
        idU = str(session['id_u'])
        
        db = database.dbcon()
        cur = db.cursor()
        current_app.logger.error((vsebina, idU))
        dat = (vsebina, idU)
        query = 'UPDATE `vnosTODO` SET vsebina = %s WHERE id = %s AND idU = %s'
        cur.execute(query, dat)
        db.commit()
        cur.close()
        
        return redirect(url_for("index"))
        
    else:
        #dodaj za error screen
        return redirect(url_for("index"))