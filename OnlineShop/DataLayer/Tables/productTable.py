class productTable:
    def __init__(self,productName,productDetails,price,date,RandomID,salerID,catID):
        self.productName = productName
        self.productDetails = productDetails
        self.price = price
        self.Date = date
        self.RandomID = RandomID
        self.salerID = salerID
        self.catID = catID
        
    def values(self):
        return (self.productName,self.productDetails,self.price,self.Date,self.RandomID,self.salerID,self.catID)