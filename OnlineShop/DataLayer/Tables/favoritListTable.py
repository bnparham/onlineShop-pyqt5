class favoritListTable:
    def __init__(self,userID,productID):
        self.userID = userID
        self.productID = productID

    def values(self):
        return (self.userID , self.productID)
    
    def id(self):
        return self.productID