import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IUserRepository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, db):
        self.db = db

    def GetAll(self):
        return self.db.getData("SELECT * FROM users")

    def GetByID(self, id):
        return self.db.getData(f"SELECT * FROM users WHERE id = {id}")
    
    def GetByEmail(self, value):
        return self.db.getData(f"SELECT * FROM users WHERE email = '{value}'")
    
    def GetIDByEmail(self, email):
        return self.db.getData(f"SELECT id FROM users WHERE email = '{email}'")
    
    def GetEmailByID(self,id):
        return self.db.getData(f"SELECT Email FROM users WHERE id = '{id}'")
    
    def GetUserNameByID(self, id):
        return self.db.getData(f"SELECT UserName FROM users WHERE id = {id}")

    def Create(self, user):
        self.db.runQuery("INSERT INTO users VALUES (NULL, ?, ?, ? ,?,?);", user.values())

    def Update(self, user, id):
        self.db.runQuery(f"UPDATE users SET UserName = ?,Email = ? ,Password = ? , Date = ? , RandomID = ?  WHERE id = {id} ", user.values())

    def Delete(self,user,id):
        self.db.runQuery(f"DELETE FROM users WHERE id = {id} AND UserName = ? AND Email = ? AND Password = ? AND Date = ? AND RandomID = ? ", user.values())
        
    def Save(self):
        return self.db.commit()