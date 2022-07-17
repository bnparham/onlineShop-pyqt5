import sqlite3

class DataBase():
    def __init__(self,dbAddress):
        self.address = dbAddress
        self.connection = sqlite3.connect(dbAddress)
        self.cursor = self.connection.cursor()
    def runQuery(self,query,instance):
        self.cursor.execute(query,instance)
    def runQueryWithOutInstance(self,query):
        self.cursor.execute(query)
    def commit(self):
        self.connection.commit()
    def getData(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def close(self):
        self.connection.close()