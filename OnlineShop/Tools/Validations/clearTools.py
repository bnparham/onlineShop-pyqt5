class clearTools:
    def Feilds(self,*args):
        for field in args:
            field.setText("")
    def labels(self,*args):
        for label in args:
            label.setHidden(True)