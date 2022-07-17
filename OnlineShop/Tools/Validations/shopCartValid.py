class shopCartValid:
    def __init__(self,count,discount,database):
        self.count = count
        self.discount = discount
        self.db = database
    def validate(self):
        if(self.count == ""):
            return 0
        elif(not self.count.isdigit()):
            return 1
        elif(self.count.isdigit() and int(self.count) == 0):
            return 0
        elif(self.discount != ""):
            checkDiscount = self.db.OffersRepository.GetAllByCode(self.discount)
            if(checkDiscount == []):
                return 2
            else:
                return 3
        elif(self.discount == ""):
            return 3
        else:
            return 3
        