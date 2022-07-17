import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IFavoritListRepository import IFavoritListRepository


class FavoritListRepository(IFavoritListRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        return self.db.getData("SELECT * FROM favoritList")
    
    def GetProductsByID(self,userID):
        return self.db.getData(f"SELECT * FROM favoritList WHERE userID = {userID}")
    
    def Create(self,favoritList):
        self.db.runQuery("INSERT INTO favoritList VALUES (NULL, ?, ?);", favoritList.values())
    
    def Update(self,favoritList,id):
        self.db.runQuery(f"UPDATE favoritList SET userID = ?,productID = ? WHERE id = {id} ", favoritList.values())
        
    def Delete(self,favoritList):
        self.db.runQuery(f"DELETE FROM favoritList WHERE productID = ?",favoritList.id())
        
    def Save(self):
        return self.db.commit()