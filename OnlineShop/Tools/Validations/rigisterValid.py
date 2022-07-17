class rigisterValid:
    def __init__(self,UserNameField,EmailField,PasswordField,RePasswordField,database):
        self.UserName = UserNameField
        self.Email = EmailField
        self.Password = PasswordField
        self.RePassword = RePasswordField
        self.db = database
    def validate(self):
        state = False
        persainchar_list = ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي']
        for char in self.UserName :
            if char in persainchar_list:
                state = True
        for char in self.Email :
            if char in persainchar_list:
                state = True
        if(state == False):
            if(self.UserName != "" and self.Email != "" and self.Password != "" and self.RePassword != ""):
                findEmail = self.db.userRepository.GetByEmail(self.Email)
                if(findEmail == []):
                    if(self.Password == self.RePassword):
                        return 4
                        #print("succsessfully Register !!")
                    else:
                        return 3
                        # print("password is not match")
                else:
                    return 2
                    # print("this email can not to be used!")  
            else:
                return 1
                # print("please fill all the fields")
        else:
            return 0
            # print("persian char is not allowed")