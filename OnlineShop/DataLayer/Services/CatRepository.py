import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.ICatRepository import ICatRepository

class CatRepository(ICatRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        return self.db.getData(f"SELECT * FROM categories")
    
    def GetByID(self,id):
        pass
    
    def GetCatNameById(self,id):
        return self.db.getData(f"SELECT catName FROM categories WHERE id = {id}")
    
    def GetAllSubCatbyID(self,catID):
        return self.db.getData(f"SELECT * FROM categories WHERE catID = {catID} ")
    
    def GetAllSubCats(self):
        return self.db.getData(f"SELECT * FROM categories WHERE catID != 0")
    
    def getMainCats(self):
        return self.db.getData(f"SELECT * FROM categories WHERE catID = 0")
    
    def GetCatIDByName(self,name):
        return self.db.getData(f"SELECT id FROM categories WHERE catName = '{name}'")
    
    def GetByEmail(self,value):
        pass
    
    def Create(self,cat):
        pass
    
    def CreateMainCat(self,cat):
        self.db.runQuery("INSERT INTO categories VALUES (NULL, ?, ?);", tuple(reversed(cat.values())))
    
    def createSubCat(self,cat):
        self.db.runQuery("INSERT INTO categories VALUES (NULL, ?, ?);", tuple(reversed(cat.values())))

    
    def Update(self,cat):
        self.db.runQuery(f"UPDATE categories SET catName = ? WHERE id = ? ", cat.values())
    
    def Delete(self,id):
        self.db.runQueryWithOutInstance(f"DELETE FROM categories WHERE id = {id}")
    
    def Save(self):
        return self.db.commit()