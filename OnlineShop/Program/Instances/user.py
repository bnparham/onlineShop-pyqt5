import sys
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context
from DataLayer.Tables.usersTable import userTable
from Tools.Validations.loginValid import loginValid
from Tools.Validations.rigisterValid import rigisterValid
import random
from datetime import datetime


db = context()

class User:
    def __init__(self):
        pass
 
    @property
    def FindUserID(self):
        return db.userRepository.GetIDByEmail(self.Email)[0][0]
    
    def Login(self,email,password,instance):
        self.Email = email
        self.Password = password
        # validation for login page
        validation = loginValid(self.Email,self.Password,db).userValidate()
        if(validation == 0):
            instance.wrongEmail_lbl.setHidden(True)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(False)
            return False
        elif(validation == 1):
            instance.wrongEmail_lbl.setHidden(False)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(True)
            return False
        elif(validation == 2):
            instance.wrongEmail_lbl.setHidden(True)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(False)
            instance.wrongFields_lbl.setHidden(True)
            return False
        elif(validation == 3):
            instance.wrongEmail_lbl.setHidden(False)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(True)
            return True
    
    def Rigister(self,UserName,Email,Password,RePassword,**lbls):
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
        self.RePassword = RePassword
        # validation for rigister page
        validation = rigisterValid(self.UserName,self.Email,self.Password,self.RePassword,db).validate()
        if(validation == 0):
            lbls["wrongEmailUsed_lbl"].setHidden(True)
            lbls["wrongFields_lbl"].setHidden(True)
            lbls["wrongPersianChar_lbl"].setHidden(False)
            lbls["wrongRePass_lbl"].setHidden(True)
            lbls["okRigister_lbl"].setHidden(True)
            return False
        elif(validation == 1):
            lbls["wrongEmailUsed_lbl"].setHidden(True)
            lbls["wrongFields_lbl"].setHidden(False)
            lbls["wrongPersianChar_lbl"].setHidden(True)
            lbls["wrongRePass_lbl"].setHidden(True)
            lbls["okRigister_lbl"].setHidden(True)
            return False
        elif(validation == 2):
            lbls["wrongEmailUsed_lbl"].setHidden(False)
            lbls["wrongFields_lbl"].setHidden(True)
            lbls["wrongPersianChar_lbl"].setHidden(True)
            lbls["wrongRePass_lbl"].setHidden(True)
            lbls["okRigister_lbl"].setHidden(True)
            return False
        elif(validation == 3):
            lbls["wrongEmailUsed_lbl"].setHidden(True)
            lbls["wrongFields_lbl"].setHidden(True)
            lbls["wrongPersianChar_lbl"].setHidden(True)
            lbls["wrongRePass_lbl"].setHidden(False)
            lbls["okRigister_lbl"].setHidden(True)
            return False
        elif(validation == 4):
            # successfuly rigister
            lbls["wrongEmailUsed_lbl"].setHidden(True)
            lbls["wrongFields_lbl"].setHidden(True)
            lbls["wrongPersianChar_lbl"].setHidden(True)
            lbls["wrongRePass_lbl"].setHidden(True)
            lbls["okRigister_lbl"].setHidden(False)
            numbers_list = [0,1,2,3,4,5,6,7,8,9]
            random_list = []
            for i in range(6):
                random_list.append(f"{random.choice(numbers_list)}")
            self.randomKey = "CU"+"".join(random_list)
            newUser = userTable(self.UserName,self.Email,self.Password,datetime.date(datetime.now()),self.randomKey)
            db.userRepository.Create(newUser)
            db.userRepository.Save()
            return True