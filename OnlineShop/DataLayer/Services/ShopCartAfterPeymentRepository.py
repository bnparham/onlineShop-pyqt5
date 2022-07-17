import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IShopCartAfterPeymentRepository import IShopCartAfterPeymentRepository

class ShopCartAfterPeymentRepository(IShopCartAfterPeymentRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        pass
    
    def GetByID(self,id):
        pass
    
    def GetAllByUserAndBuyID(self,userID,buyID):
        return self.db.getData(f"SELECT * FROM shopCartAfterPeyment WHERE userID = {userID} AND buyID = {buyID}")
    
    def GetALLByUserID(self,userID):
        return self.db.getData(f"SELECT * FROM shopCartAfterPeyment WHERE userID = {userID}")
    
    def GetBuyIDByUserID(self,userID):
        return self.db.getData(f"SELECT BuyID FROM shopCartAfterPeyment WHERE userID = {userID} ORDER BY BuyID DESC")
    
    def GetAllBySalerID(self,salerID):
        return self.db.getData(f"SELECT * FROM shopCartAfterPeyment WHERE salerID = '{salerID}' ")
    
    def Create(self,shopCartAfterPeyment):
        self.db.runQuery("INSERT INTO shopCartAfterPeyment VALUES (NULL, ?, ?, ? ,?,?,?);", shopCartAfterPeyment.values())
    
    def Update(self,user,id):
        pass
    
    def Delete(self,id):
        pass
    
    def Save(self):
        return self.db.commit()
