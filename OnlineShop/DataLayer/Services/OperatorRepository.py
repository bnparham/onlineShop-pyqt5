import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IOperatorRepository import IOperatorRepository

class OperatorRepository(IOperatorRepository):
    def  __init__(self,db):
        self.db = db
        
    def GetAll(self):
        pass
    
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM operators WHERE id = {id}")
    
    def GetByEmail(self,value):
        return self.db.getData(f"SELECT * FROM operators WHERE email = '{value}'")

    def GetIDByEmail(self, email):
        return self.db.getData(f"SELECT id FROM operators WHERE email = '{email}'")
    
    def GetUserNameByID(self, id):
        return self.db.getData(f"SELECT userName FROM operators WHERE id = {id}")
    
    def Create(self,operator):
        pass
    
    def Update(self,operator,id):
        self.db.runQuery(f"UPDATE operators SET userName = ?,Email = ? , password = ? , RandomID = ? , Date = ?  WHERE id = {id} ", operator.values())
    
    def Delete(self,id):
        pass
    
    def Save(self):
        return self.db.commit()