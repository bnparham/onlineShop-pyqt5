class userPaymentTable:
    def __init__(self,userID,buyID,userName,userFamily,mobile,address,state,city,totalPrice,date):
        self.userID = userID
        self.buyID = buyID
        self.userName = userName
        self.userFamily = userFamily
        self.mobile = mobile
        self.address = address
        self.state = state
        self.city = city
        self.totalPrice = totalPrice
        self.date = date
    def values(self):
        return (self.userID,self.buyID,self.userName,self.userFamily,self.mobile,self.address,self.state,self.city,self.totalPrice,self.date)