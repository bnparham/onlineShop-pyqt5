import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IAllcommentsRepository import IAllcommentsRepository

class AllcommentsRepository(IAllcommentsRepository):
    def __init__(self, db):
        self.db = db
    def GetAll(self):
        pass
    def GetByID(self,id):
        pass
    
    def GetAllByProductID(self,productID):
        return self.db.getData(f"SELECT * FROM AllComments WHERE productID = {productID}")
    
    def GetAllByUserID(self,userID):
        return self.db.getData(f"SELECT * FROM AllComments WHERE userID = {userID}")
    
    def GetCommentByUserAndProductID(self,userID,productID):
        return self.db.getData(f"SELECT * FROM AllComments WHERE userID = {userID} AND productID = {productID}")
    
    def GetByEmail(self,value):
        pass
    def Create(self,comment):
        self.db.runQuery("INSERT INTO AllComments VALUES (NULL, ?, ?, ?);", comment.values())
        
    def Update(self,user,id):
        pass
    
    def Delete(self,commentInstance):
        self.db.runQuery(f"DELETE FROM AllComments WHERE productID = ? AND userID =? ", commentInstance.userID_productID_Values())
    
    
    def Save(self):
        return self.db.commit()