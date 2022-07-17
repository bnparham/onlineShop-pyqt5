class users_balanceTable:
    def __init__(self,userID,Balance):
        self.userID = userID
        self.Balance = Balance
    def values(self):
        return (self.userID,self.Balance)