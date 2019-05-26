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
    geslo1 = 'NjegovoGeslo'
    gesloNovo= 'NjegovoGesloNovo'
    
    #test, da je prvo geslo pravilno
    def test_geslo1(self):
        
        db = database.dbcon()
        cur = db.cursor()
        
        table = 'SELECT id FROM Uporabnik where mail=%s and geslo = %s;'
        cur.execute(table, (self.uporabnisko, self.geslo, ))
        records = cur.fetchone()
        cur.close()
        
        dolzina = 0
        
        try:
            dolzina = len(records)
        except:
            dolzina = 0
        
        #ce najdemo, ne smemo uporabit
        self.assertEqual(dolzina, 1)
        
    #test, da je drugo geslo pravilno
    def test_geslo2(self):
        
        db = database.dbcon()
        cur = db.cursor()
        
        table = 'SELECT id FROM Uporabnik where mail=%s and geslo = %s;'
        cur.execute(table, (self.uporabnisko, self.geslo1, ))
        records = cur.fetchone()
        cur.close()
        
        dolzina = 0
        
        try:
            dolzina = len(records)
        except:
            dolzina = 0
        
        #ce najdemo, ne smemo uporabit
        self.assertEqual(dolzina, 1)
        
    #test, da je novo geslo dobro
    def test_geslonovo(self):
        
        dolzina = len(self.gesloNovo)
        self.assertGreater(dolzina, 7)

if __name__ == '__main__':
    unittest.main()