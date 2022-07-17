class userTable:
    def __init__(self,UserName,Email,Password,DateTime,RandomID):
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
        self.Date = DateTime
        self.RandomID = RandomID
    def values(self):
        return (self.UserName,self.Email,self.Password,self.Date,self.RandomID)