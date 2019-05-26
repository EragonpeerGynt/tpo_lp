import os
import unittest
import re
import sys
dirname, filename = os.path.split(os.path.abspath(__file__))
serverdir = os.path.join(dirname, "..", "src", "server")
sys.path.append(serverdir)
from dbase import database

class TestPrijave(unittest.TestCase):
    
    uporabnisko = 'blaz@gmail.com'
    geslo = 'NjegovoGeslo'
    
    #test, da je uporabnisko registrirano
    def test_uporabnisko(self):
        
        db = database.dbcon()
        cur = db.cursor()
        
        table = 'SELECT id FROM Uporabnik where mail=%s and potrjen = %s;'
        cur.execute(table, (self.uporabnisko, 1, ))
        records = cur.fetchone()
        cur.close()
        
        dolzina = 0
        
        try:
            dolzina = len(records)
        except:
            dolzina = 0
        
        #ce najdemo, ne smemo uporabit
        self.assertEqual(dolzina, 1)
        
    #test, da sta uporabnisko in geslo ok
    def test_uporabnisko_geslo(self):
        
        db = database.dbcon()
        cur = db.cursor()
        
        table = 'SELECT id FROM Uporabnik where mail=%s and potrjen = %s and geslo = %s;'
        cur.execute(table, (self.uporabnisko, 1, self.geslo, ))
        records = cur.fetchone()
        cur.close()
        
        dolzina = 0
        
        try:
            dolzina = len(records)
        except:
            dolzina = 0
        
        #ce najdemo, ne smemo uporabit
        self.assertEqual(dolzina, 1)

if __name__ == '__main__':
    unittest.main()