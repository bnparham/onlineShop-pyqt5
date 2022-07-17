import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IOperatorConfirmOrderRepository import IOperatorConfirmOrderRepository

class OperatorConfirmOrderRepository(IOperatorConfirmOrderRepository):
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        return self.db.getData("SELECT * FROM operatorConfirmOrder")
    
    def GetAllNotConfirm(self):
        return self.db.getData("SELECT * FROM operatorConfirmOrder WHERE status = 0")

    def GetAllConfirm(self):
        return self.db.getData("SELECT * FROM operatorConfirmOrder WHERE status = 1") 
    
    def CheckOrderStatus(self,userID,buyID):
        return self.db.getData(f"SELECT status FROM operatorConfirmOrder WHERE userID = '{userID}' and buyID = '{buyID}' ") 
    
    def GetByID(self,id):
        pass
    def GetByEmail(self,value):
        pass
    
    def Create(self,userID,buyID):
        self.db.runQueryWithOutInstance(f"INSERT INTO operatorConfirmOrder VALUES (NULL,'{userID}','{buyID}',0);")
    
    def UpdateConfrimOrder(self,userID,buyID):
        self.db.runQueryWithOutInstance(f"UPDATE operatorConfirmOrder SET status = 1  WHERE userID = '{userID}' AND buyID = '{buyID}' ")
        
    def UpdateIgnoreOrder(self,userID,buyID):
        self.db.runQueryWithOutInstance(f"UPDATE operatorConfirmOrder SET status = 2  WHERE userID = '{userID}' AND buyID = '{buyID}' ")
    
    def Update(self,user,id):
        pass
    def Delete(self,id):
        pass
    def Save(self):
        return self.db.commit()