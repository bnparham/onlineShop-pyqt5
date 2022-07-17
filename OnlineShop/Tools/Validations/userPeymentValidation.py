class userPeymentValidation:
    def __init__(self,nameInput,familyInput,mobileInput,stateInput,cityInput,addressInput):
        self.nameInput = nameInput
        self.familyInput = familyInput
        self.mobileInput = mobileInput
        self.stateInput = stateInput
        self.cityInput = cityInput
        self.addressInput = addressInput
        
    def validate(self):
        if(self.nameInput == ""):
            return 0
        elif(self.familyInput == ""):
            return 0
        elif(self.mobileInput == ""):
            return 0
        elif(self.stateInput == ""):
            return 0
        elif(self.cityInput == ""):
            return 0
        elif(self.addressInput == ""):
            return 0
        elif(not self.mobileInput.isdigit()):
            return 1
        elif(len(self.mobileInput) != 11):
            return 2
        else:
            return 3