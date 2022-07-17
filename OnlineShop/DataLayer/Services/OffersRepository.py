import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IOffersRepository import IOffersRepository

class OffersRepository(IOffersRepository):
    def __init__(self, db):
        self.db = db
    def GetAll(self):
        return self.db.getData("SELECT * FROM offers")
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM offers WHERE id = {id}")
    def findOffByID(self,id):
        return self.db.getData(f"SELECT offerCode FROM offers WHERE id = {id}")
    def GetAllByCode(self,offerCode):
        return self.db.getData(f"SELECT * FROM offers WHERE offerCode = '{offerCode}'")
    
    def GetIdByCode(self,offerCode):
        return self.db.getData(f"SELECT id FROM offers WHERE offerCode = '{offerCode}'")
    
    def GetCodeNameBYID(self,id):
        return self.db.getData(f"SELECT offerCode FROM offers WHERE id = {id}")
    
    def GetDiscountBYID(self,id):
        return self.db.getData(f"SELECT discount FROM offers WHERE id = {id}")
    
    def Create(self,offName,discount):
        self.db.runQueryWithOutInstance(f"INSERT INTO offers VALUES (NULL,'{offName}', '{discount}' );")
    
    def Update(self,id,offercode,discount):
        self.db.runQueryWithOutInstance(f"UPDATE offers SET offerCode = '{offercode}' , discount = '{discount}'  WHERE id = {id} ")
    
    
    def Delete(self,id):
        self.db.runQueryWithOutInstance(f"DELETE FROM offers WHERE id = {id} ")
    
    def Save(self):
        return self.db.commit()