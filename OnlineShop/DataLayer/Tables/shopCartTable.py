import sys
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context

class shopCartTable:
    def __init__(self,productID,userID,salerID,count,discount):
        self.productID = productID
        self.userID = userID
        self.salerID = salerID
        self.count = count
        self.discount = discount

    def values(self):
        return (self.productID,self.userID,self.salerID,self.count,self.discount)
    
    def id(self):
        db = context()
        shopCartID = db.ShopCartRepository.GetIDByProductID(self.productID)[0][0]
        return (shopCartID,)