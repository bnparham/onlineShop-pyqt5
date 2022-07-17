import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IUserBalanceRepository import IUserBalanceRepository

class UserBalanceRepository(IUserBalanceRepository):
    def __init__(self,db):
        self.db = db
        
    def GetBalance(self,userID):
        return self.db.getData(f"SELECT Balance FROM users_Balance WHERE userID = {userID}")
        
    def Create(self,userBalance):
        self.db.runQuery("INSERT INTO users_Balance VALUES (NULL, ?, ?);", userBalance.values())
    
    def Update(self,userBalance):
        self.db.runQuery(f"UPDATE users_Balance SET Balance = ? WHERE userId = ? ", tuple(reversed(userBalance.values())))
        
    def UpdateWithOutInstance(self,userID,amount):
        self.db.runQueryWithOutInstance(f"UPDATE users_Balance SET Balance = {amount} where userID = '{userID}'")
    
    def Delete(self,id):
        self.db.runQuery(f"DELETE FROM users_Balance WHERE id = {id}")
    
    def Save(self):
        return self.db.commit()