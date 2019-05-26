import os
import unittest
import re
import sys
dirname, filename = os.path.split(os.path.abspath(__file__))
serverdir = os.path.join(dirname, "..", "src", "server")
sys.path.append(serverdir)
from dbase import database

class TestRegistracije(unittest.TestCase):
    
    uporabnisko = 'andreja1@gmail.com'
    geslo = 'DobroGeslo'
    
    #test, da je vnesen pravi email
    def test_uporabnisko_sintaksa(self):
        jePravilno = 0
        
        print "Vnesen email "+self.uporabnisko
        
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.uporabnisko):
            jePravilno= 1
            
        self.assertEqual(jePravilno, 1)
    
    #test, da je geslo dovolj dolgo    
    def test_geslo_dolzina(self):
        
        dolzina = len(self.geslo)
        self.assertGreater(dolzina, 7)
    
    #test, da uporabnisko ni zasedeno
    def test_zasedeno_uporabnisko(self):
        
        db = database.dbcon()
        cur = db.cursor()
        
        table = 'SELECT id FROM Uporabnik where mail=%s;'
        cur.execute(table, (self.uporabnisko, ))
        records = cur.fetchone()
        cur.close()
        
        dolzina = 0
        
        try:
            dolzina = len(records)
        except:
            dolzina = 0
        
        #ce najdemo, ne smemo uporabit
        self.assertEqual(dolzina, 0)

if __name__ == '__main__':
    unittest.main()