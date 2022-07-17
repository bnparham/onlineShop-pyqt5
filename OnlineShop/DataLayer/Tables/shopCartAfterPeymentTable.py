class shopCartAfterPeymentTable:
    def __init__(self,buyID,productID,userID,salerID,count,offID):
        self.productID = productID
        self.userID = userID
        self.salerID = salerID
        self.buyID = buyID
        self.count = count
        self.offID = offID

    def values(self):
        return(self.buyID,self.productID,self.userID,self.salerID,self.count,self.offID)