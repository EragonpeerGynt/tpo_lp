import auth
import MySQLdb
from os import environ

class DummyCursor:
    def close(self):
        return

    def execute(self, *largs):
        return

    def fetchall(self):
        return []

    def fetchone(self):
        return ()

    def __iter__(self):
        return iter([])

class DummyDB:
    cur = DummyCursor()

    def cursor(self):
        return self.cur

    def close(self):
        return

class Database:
    db = None
    dummy = DummyDB()

    def dbcon(self):
        try:
            try:
                self.db.ping()
            except:
                self.db = MySQLdb.connect(host=auth.dbhost, user=environ.get(auth.dbuser),
                                            passwd=environ.get(auth.dbpass), db=auth.dbase,
                                            charset = 'utf8', use_unicode = True)
        except MySQLdb.OperationalError:
            return self.dummy
        return self.db

database = Database()
