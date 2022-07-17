class catTable:
    def __init__(self, catID,catName):
        self.catID = catID
        self.catName = catName
        
    def values(self):
        return (self.catName,self.catID)
    
    def catNameValue(self):
        return self.catName