class loginValid:
    def __init__(self,EmailField,PasswordField,database):
        self.Email = EmailField
        self.Password = PasswordField
        self.db = database
        
    def userValidate(self):
        if(self.Email != "" and self.Password != ""):
            findEmail = self.db.userRepository.GetByEmail(self.Email)
            if(findEmail):
                if(self.Password == findEmail[0][3]):
                    return 3
                    # print("succsessfully Login !!")
                else:
                    return 2
                    # print("Password is incorrect")
            else:
                return 1
                # print("Email is incorrect")
        else:
            return 0
            # print("please fill all the fields")
            
    def operatorValidate(self):
        if(self.Email != "" and self.Password != ""):
            findEmail = self.db.OperatorRepository.GetByEmail(self.Email)
            if(findEmail):
                if(self.Password == findEmail[0][3]):
                    return 3
                    # print("succsessfully Login !!")
                else:
                    return 2
                    # print("Password is incorrect")
            else:
                return 1
                # print("Email is incorrect")
        else:
            return 0
            # print("please fill all the fields")