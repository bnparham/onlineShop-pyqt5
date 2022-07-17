import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IShopCartRepository import IShopCartRepository

class ShopCartRepository(IShopCartRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        return self.db.getData("SELECT * FROM shopCart")
    
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM shopCart WHERE id = {id}")
    
    def GetAllByProductID(self,productID):
        return self.db.getData(f"SELECT * FROM shopCart WHERE productID = {productID}")
    def GetAllByUserID(self,userID):
        return self.db.getData(f"SELECT * FROM shopCart WHERE userID = {userID}")
    def GetAllByUserAndProductID(self,userID,productID):
        return self.db.getData(f"SELECT * FROM shopCart WHERE userID = {userID} AND productID = {productID}")
    
    def GetIDByProductID(self,productID):
        return self.db.getData(f"SELECT id FROM shopCart WHERE productID = {productID}")
    
    def GetProductIDByID(self,id):
        return self.db.getData(f"SELECT productID FROM shopCart WHERE id = {id}")
    def GetCountByProductID(self,productID):
        return self.db.getData(f"SELECT count FROM shopCart WHERE productID = {productID}")
    def GetOffIDByProductID(self,productID):
        return self.db.getData(f"SELECT offID FROM shopCart WHERE productID = {productID}")
    
    def Create(self,shopcart):
        self.db.runQuery("INSERT INTO shopCart VALUES (NULL, ?, ?, ? , ? , ?);", shopcart.values())

    
    def Update(self,shopcart,id):    
        self.db.runQuery(f"UPDATE shopCart SET productID = ?,userID = ? ,SalerID = ? , count = ? , offID= ?  WHERE id = {id} ", shopcart.values())
    
    def Delete(self,shopcart):
        self.db.runQuery(f"DELETE FROM shopCart WHERE id = ?", shopcart.id())
        
    def Save(self):
        return self.db.commit()
    