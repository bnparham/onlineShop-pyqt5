class commentValid:
    def __init__(self,comment):
        self.comment = comment
    def valid(self):
        if(self.comment == ""):
            return 0
        else:
            return 1