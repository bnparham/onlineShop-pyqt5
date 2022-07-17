class accountBalanceValid:
    def __init__(self,amount):
        self.amount = amount
    def validate(self):
        if(self.amount == ""):
            return 0
        elif(self.amount.isdigit() and int(self.amount)==0):
            return 0
        elif(not self.amount.isdigit()):
            return 1
        else:
            return 2