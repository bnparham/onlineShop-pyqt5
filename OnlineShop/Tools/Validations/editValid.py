class editValid:
    def __init__(self,oldPass,dbPass,newPass):
        self.oldPass = oldPass
        self.dbPass = dbPass
        self.newPass = newPass
    def userValidate(self):
        if(self.dbPass != self.oldPass):
            return 0
        elif(self.newPass == ""):
            return 1
        elif(self.newPass == self.dbPass):
            return 2
        else:
            return 3
    def operatorValidate(self):
        if(self.dbPass != self.oldPass):
            return 0
        elif(self.newPass == ""):
            return 1
        elif(self.newPass == self.dbPass):
            return 2
        else:
            return 3