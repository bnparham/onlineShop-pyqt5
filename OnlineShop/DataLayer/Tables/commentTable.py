class commentTable:
    def __init__(self, userID,ProductID,comment):
        self.userID = userID
        self.productID = ProductID
        self.comment = comment
    def values(self):
        return (self.productID,self.userID, self.comment)
    def userID_productID_Values(self):
        return (self.productID,self.userID)
