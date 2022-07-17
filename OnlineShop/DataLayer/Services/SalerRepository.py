import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.ISalerRepository import ISalerRepository

class SalerRepository(ISalerRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        return self.db.getData("SELECT * FROM salers")
    
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM salers WHERE id = {id}")
    
    def GetSalerNameByID(self,id):
        return self.db.getData(f"SELECT salerName FROM salers WHERE id = {id}") 
    
    def GetSalerIDByName(self,name):
        return self.db.getData(f"SELECT id FROM salers WHERE salerName =   '{name}' ") 
    
    def GetRandomIDByID(self,id):
        return self.db.getData(f"SELECT salerRandomID FROM salers WHERE id =   '{id}' ") 
    
    def Create(self,saler):
        self.db.runQuery("INSERT INTO salers VALUES (NULL, ?, ?);", saler.values())
        
    def CreateWithOutInstance(self,salerName,randomID):
        self.db.runQueryWithOutInstance(f"INSERT INTO salers VALUES (NULL, '{salerName}', '{randomID}');")
        
        
    def Update(self,saler,id):
        self.db.runQuery(f"UPDATE salers SET salerName = ?,salerRandomID = ?  WHERE id = {id} ", saler.values())
        
    def UpdateWithOutInstance(self,id,salerName,salerRandomID):
        self.db.runQueryWithOutInstance(f"UPDATE salers SET salerName = '{salerName}' , salerRandomID = '{salerRandomID}'  WHERE id = {id} ")


    def Delete(self,id):
        self.db.runQuery(f"DELETE FROM salers WHERE id = {id}")
        
    def DeleteWithOutInstance(self,id):
        self.db.runQueryWithOutInstance(f"DELETE FROM salers WHERE id = {id}")

    
    def Save(self):
        return self.db.commit()