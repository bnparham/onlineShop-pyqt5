import sys,os
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog , QApplication , QWidget , QStackedWidget , QLabel , QPushButton
from datetime import datetime
import webbrowser

# --------------
# own Maduls
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context
from Program.Instances.user import User
from Program.Instances.product import Product
from Program.Instances.loginUser import LoginUser
from Program.Instances.operator import Operator
db = context()

# ----| mainWindowUI |----
class mainWindowUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\mainWindowUI.ui",self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("صفحه اصلی")
        self.afterLogin_widget.setHidden(True)
        self.addToCart_btn_1.setHidden(True)
        self.addToCart_btn_2.setHidden(True)
        self.addToCart_btn_3.setHidden(True)
        self.addToCart_btn_4.setHidden(True)
        self.account_btn.clicked.connect(self.OpenLoginWindowUI)
        self.ViewProductsOnHomePage_func()
        self.productDetails_btn_1.clicked.connect(lambda x : self.ProductDetailsBeforeLoginUI(1))
        self.productDetails_btn_2.clicked.connect(lambda x : self.ProductDetailsBeforeLoginUI(2))
        self.productDetails_btn_3.clicked.connect(lambda x : self.ProductDetailsBeforeLoginUI(3))
        self.productDetails_btn_4.clicked.connect(lambda x : self.ProductDetailsBeforeLoginUI(4))
        # social btns
        self.instagram_btn.clicked.connect(lambda x : self.goToSocial(self.instagram_btn.objectName()))
        self.twitter_btn.clicked.connect(lambda x : self.goToSocial(self.twitter_btn.objectName()))
        self.linkedin_btn.clicked.connect(lambda x : self.goToSocial(self.linkedin_btn.objectName()))
        self.aparat_btn.clicked.connect(lambda x : self.goToSocial(self.aparat_btn.objectName()))
        self.show()
    
    def goToSocial(self,objName):
        getSocial = objName.split("_")[0]
        if(getSocial == "instagram"):
            webbrowser.open_new_tab("https://www.instagram.com/digikalacom/")
        elif(getSocial == "twitter"):
            webbrowser.open_new_tab("https://twitter.com/digikalacom")
        elif(getSocial == "linkedin"):
            webbrowser.open_new_tab("https://www.linkedin.com/company/digikala/mycompany/")
        elif(getSocial == "aparat"):
            webbrowser.open_new_tab("https://www.aparat.com/digikala/")
            
    def OpenLoginWindowUI(self):
        self.close()
        self.window = LoginWindowUI()
        self.window.createNewAc_btn.clicked.connect(self.OpenRigisterWindowUI)
        self.window.backToHome_btn.clicked.connect(self.OpenHomePageUI)
        self.window.operator_btn.clicked.connect(self.OpenOperatorUI)
        self.window.show()
        
    def OpenOperatorUI(self):
        self.window = operatorLoginUI()
        self.window.backToHome_btn.clicked.connect(self.OpenHomePageUI)
        self.window.show()
            
    def ProductDetailsBeforeLoginUI(self,productID):
        self.veiwProduct = viewProductUI()
        self.veiwProduct.addToFave_btn.setHidden(True)      
        self.veiwProduct.addNewComment_btn.setHidden(True)
        self.veiwProduct.addnewCommnent_lbl.setHidden(True) 
        self.veiwProduct.viewComments_btn.clicked.connect(lambda x : self.ViewCommentsUI(productID))    
        product = Product(productID)
        product.showDetails(self.veiwProduct.productName_lbl,self.veiwProduct.show_productID,self.veiwProduct.show_details,self.veiwProduct.show_price,self.veiwProduct.show_date,self.veiwProduct.show_salerName,self.veiwProduct.show_cat)
        self.veiwProduct.show()
        
    def ViewCommentsUI(self,productID):
        self.veiwProduct = ViewCommentsUI()
        findProductName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
        self.veiwProduct.prdoductName_lbl.setText(f"نظرات درباره {findProductName}")
        self.veiwProduct.createDynamicComments(productID)
        self.veiwProduct.show()
        
    
    def ViewProductsOnHomePage_func(self):
        self.addToCart_btn_1.setHidden(True)
        self.addToCart_btn_2.setHidden(True)
        self.addToCart_btn_3.setHidden(True)
        self.addToCart_btn_4.setHidden(True)
        firstProduct = db.ProductsRepository.GetByID(1)
        secondProduct = db.ProductsRepository.GetByID(2)
        thirdProduct = db.ProductsRepository.GetByID(3)
        forthProduct = db.ProductsRepository.GetByID(4)
        self.productName_lbl_1.setText(firstProduct[0][1])
        self.productPrice_lbl_1.setText(str(firstProduct[0][3]))
        # ----------
        self.productName_lbl_2.setText(secondProduct[0][1])
        self.productPrice_lbl_2.setText(str(secondProduct[0][3]))
        # ----------
        self.productName_lbl_3.setText(thirdProduct[0][1])
        self.productPrice_lbl_3.setText(str(thirdProduct[0][3]))
        # ----------
        self.productName_lbl_4.setText(forthProduct[0][1])
        self.productPrice_lbl_4.setText(str(forthProduct[0][3]))
    
    def OpenRigisterWindowUI(self):
        self.window = RigisterWindowUI()
        self.window.back_btn.clicked.connect(self.OpenLoginWindowUI)
        self.window.goToHome_btn.clicked.connect(self.OpenHomePageUI)
        self.window.show()
        
    def OpenHomePageUI(self):
        self.window = mainWindowUI()

class mainWindowAfterLoginUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\mainWindowUI.ui",self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("صفحه اصلی")
        self.ViewProductsOnHomePage_func()
        self.beforLogin_widget.setHidden(True)
        self.afterLogin_widget.setHidden(False)
        self.addToCart_btn_1.setHidden(False)
        self.addToCart_btn_2.setHidden(False)
        self.addToCart_btn_3.setHidden(False)
        self.addToCart_btn_4.setHidden(False)
        self.show()
    
    def goToSocial(self,objName):
        getSocial = objName.split("_")[0]
        if(getSocial == "instagram"):
            webbrowser.open_new_tab("https://www.instagram.com/digikalacom/")
        elif(getSocial == "twitter"):
            webbrowser.open_new_tab("https://twitter.com/digikalacom")
        elif(getSocial == "linkedin"):
            webbrowser.open_new_tab("https://www.linkedin.com/company/digikala/mycompany/")
        elif(getSocial == "aparat"):
            webbrowser.open_new_tab("https://www.aparat.com/digikala/")        
        self.show()
        

    
    def ViewProductsOnHomePage_func(self):
        self.addToCart_btn_1.setHidden(True)
        self.addToCart_btn_2.setHidden(True)
        self.addToCart_btn_3.setHidden(True)
        self.addToCart_btn_4.setHidden(True)
        firstProduct = db.ProductsRepository.GetByID(1)
        secondProduct = db.ProductsRepository.GetByID(2)
        thirdProduct = db.ProductsRepository.GetByID(3)
        forthProduct = db.ProductsRepository.GetByID(4)
        self.productName_lbl_1.setText(firstProduct[0][1])
        self.productPrice_lbl_1.setText(str(firstProduct[0][3]))
        # ----------
        self.productName_lbl_2.setText(secondProduct[0][1])
        self.productPrice_lbl_2.setText(str(secondProduct[0][3]))
        # ----------
        self.productName_lbl_3.setText(thirdProduct[0][1])
        self.productPrice_lbl_3.setText(str(thirdProduct[0][3]))
        # ----------
        self.productName_lbl_4.setText(forthProduct[0][1])
        self.productPrice_lbl_4.setText(str(forthProduct[0][3]))
    

# ----| LoginWindowUI |----
class LoginWindowUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\LoginUI.ui", self)
        self.setWindowTitle("ورود")
        self.login_btn.clicked.connect(self.goToLogin)
        self.okLoign_lbl.setHidden(True)
        self.wrongEmail_lbl.setHidden(True)
        self.wrongPass_lbl.setHidden(True)
        self.wrongFields_lbl.setHidden(True)
        
    def goToLogin(self):
        # --- check if the email and password is correct ---
        user = User()
        if(user.Login(self.email_input.text(),self.pass_input.text(),self)):
            self.UserID = user.FindUserID
            self.AllUserInfo = db.userRepository.GetByID(self.UserID)
            self.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("با موفقیت وارد برنامه شدید")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("LogIn"))
            self.message.show()
            
    
    def OpenHomePageAferLoginUI(self):
        self.window = mainWindowAfterLoginUI()
        findUserName = db.userRepository.GetUserNameByID(self.UserID)[0][0]
        self.window.welcome_btn.setText(f'{findUserName}'+" خوش اومدی ")
        self.window.viewAcc_btn.clicked.connect(self.OpenViewAccountUI)
        self.window.exitAcc_btn.clicked.connect(self.goToExitAccount)
        self.window.myFaveList_btn.clicked.connect(self.OpenFavoritListUI)
        self.window.myShopCart_btn.clicked.connect(self.OpenShopCartWindowUI)
        # ProductDetails
        self.window.productDetails_btn_1.clicked.connect(lambda x : self.ProductDetailsAfterLoginUI(1,self.UserID))
        self.window.productDetails_btn_2.clicked.connect(lambda x : self.ProductDetailsAfterLoginUI(2,self.UserID))
        self.window.productDetails_btn_3.clicked.connect(lambda x : self.ProductDetailsAfterLoginUI(3,self.UserID))
        self.window.productDetails_btn_4.clicked.connect(lambda x : self.ProductDetailsAfterLoginUI(4,self.UserID))
        # addToCart
        self.window.addToCart_btn_1.clicked.connect(lambda x : self.OpenAddToCartUI(1,self.UserID))
        self.window.addToCart_btn_2.clicked.connect(lambda x : self.OpenAddToCartUI(2,self.UserID))
        self.window.addToCart_btn_3.clicked.connect(lambda x : self.OpenAddToCartUI(3,self.UserID))
        self.window.addToCart_btn_4.clicked.connect(lambda x : self.OpenAddToCartUI(4,self.UserID))   
        
        self.window.instagram_btn.clicked.connect(lambda x : self.window.goToSocial(self.window.instagram_btn.objectName()))
        self.window.twitter_btn.clicked.connect(lambda x : self.window.goToSocial(self.window.twitter_btn.objectName()))
        self.window.linkedin_btn.clicked.connect(lambda x : self.window.goToSocial(self.window.linkedin_btn.objectName()))
        self.window.aparat_btn.clicked.connect(lambda x : self.window.goToSocial(self.window.aparat_btn.objectName()))   
    
        self.window.show()
        
    def ProductDetailsAfterLoginUI(self,productID,userID):
        self.veiwProduct = viewProductUI() 
        self.veiwProduct.setWindowTitle("مشاهده محصول")
        self.veiwProduct.viewComments_btn.clicked.connect(lambda x : self.ViewCommentsUI(productID))   
        self.veiwProduct.addToFave_btn.setHidden(False)
        self.veiwProduct.addnewCommnent_lbl.setHidden(False) 
        self.veiwProduct.addNewComment_btn.setHidden(False) 
        product = Product(productID)
        product.showDetails(self.veiwProduct.productName_lbl,self.veiwProduct.show_productID,self.veiwProduct.show_details,self.veiwProduct.show_price,self.veiwProduct.show_date,self.veiwProduct.show_salerName,self.veiwProduct.show_cat)
        self.veiwProduct.addNewComment_btn.clicked.connect(lambda x : self.AddNewCommentUI(productID,userID))
        self.veiwProduct.addToFave_btn.clicked.connect(lambda x : self.goToAddFavoritList(productID,userID))     
        self.veiwProduct.show()  
    
    def ViewCommentsUI(self,productID):
        self.veiwProduct = ViewCommentsUI()
        findProductName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
        self.veiwProduct.prdoductName_lbl.setText(f"نظرات درباره {findProductName}")
        self.veiwProduct.createDynamicComments(productID)
        self.veiwProduct.show()
        
    
    def AddNewCommentUI(self,productID,userID):
        findCommentForThisProduct = db.AllcommentsRepository.GetCommentByUserAndProductID(userID,productID)
        if(findCommentForThisProduct == []):
            self.addNewCommentUI = AddNewCommentUI()
            self.addNewCommentUI.setWindowTitle("افزودن نظر جدید")
            self.addNewCommentUI.sendComment_btn.clicked.connect(lambda x : self.goToConfirmNewComment(productID))
            self.addNewCommentUI.show()
        else:
            self.message = MessgaeBoxUI()
            self.message.setWindowTitle("خطا")
            self.message.message_lbl.setText("شما قبلا دیدگاه خود را در مورد این محصول ثبت کرده اید")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("AddNewComment"))
            
    def goToConfirmNewComment(self,productID):
        UserLogIn = LoginUser(self.UserID)
        if(UserLogIn.AddComment(productID,self.addNewCommentUI.comment_input.toPlainText(), WarningComment_lbl = self.addNewCommentUI.WarningComment_lbl)):
            self.addNewCommentUI.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("نظر شما با موفقیت ثبت شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("AddNewComment"))
    
    def goToAddFavoritList(self,productID,userID):
        loginUser = LoginUser(self.UserID)
        if(loginUser.AddItemToFavorit(productID,userID)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("باموفقیت افزوده شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("AddToFavoritList"))
        else:
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("شما قبلا این محصول را به لیست علاقه مندی های خود اضافه کرده اید")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("AddToFavoritList"))
            
    def OpenFavoritListUI(self):
        self.favoritUI = favoritListUI() 
        self.favoritUI.createLables(self.UserID)
        self.favoritUI.refresh_btn.clicked.connect(self.goToRefreshFavoritList)
        self.favoritUI.show() 
    
    def goToRefreshFavoritList(self):
        self.favoritUI.close()
        self.OpenFavoritListUI()
    
    def OpenShopCartWindowUI(self):
        self.shopCartUI = shopCartUI()
        self.shopCartUI.createDynamicBtn(self.UserID)
        self.shopCartUI.refresh_btn.clicked.connect(self.refreshShopCartWindow)
        self.shopCartUI.clearAll_btn.clicked.connect(lambda x : self.shopCartUI.clearAllUserShopCartUI(self.UserID))
        self.shopCartUI.pay_btn.clicked.connect(lambda x : self.shopCartUI.OpenPayUI(self.UserID))
        self.shopCartUI.show()
        
    def refreshShopCartWindow(self):
        self.shopCartUI.close()
        self.OpenShopCartWindowUI()
        
    def OpenAddToCartUI(self,product_id,user_id):
        self.AddCH = addToCartUI()
        self.AddCH.confirmeAddToCart_btn.clicked.connect(lambda x : self.goToAddToCart(product_id,user_id))
        self.AddCH.show()
        
    def goToAddToCart(self,product_id,user_id):
        loginUser = LoginUser(self.UserID)
        
        if(loginUser.AddItemToShopCart(product_id,user_id,self.AddCH.count_input.text(),self.AddCH.discount_input.text(),self)):
            self.AddCH.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("با موفقیت به سبد خرید اضافه شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("AddTocart"))
            self.message.show()
    
    def OpenViewAccountUI(self):
        self.viewAc = viewAccountUI()
        self.viewAc.setWindowTitle("مشاهده حساب کاربری")
        self.viewAc.show()
        # --- show user profile ---
        loginUser = LoginUser(self.UserID)
        loginUser.SeeUserPanel(self.viewAc.show_userName,self.viewAc.show_email,self.viewAc.show_password,self.viewAc.show_date,self.viewAc.show_randomID,self.viewAc.show_balance)
        # ---END show user profile ---
        self.viewAc.edit_btn.clicked.connect(self.OpenEditAccountUI)
        self.viewAc.increaseBalance_btn.clicked.connect(self.OpenIncreaseBalanceUI)
        self.viewAc.userComments_btn.clicked.connect(self.OpenUserCommentsUI)
        self.viewAc.factor_btn.clicked.connect(self.OpenUserOrdersUI)
        
        
    def OpenUserOrdersUI(self):
        self.userOrderUI = usersOrderUI()
        self.userOrderUI.createDynamicInfo(self.UserID)
        self.userOrderUI.show()
    
    def goToExitAccount(self):
        # --- exit account ---
        self.window = mainWindowUI()
        self.window.show()
    
    def OpenUserCommentsUI(self):
        self.viewAc = ViewCommentsUI()
        findUserName = db.userRepository.GetUserNameByID(self.UserID)[0][0]
        self.viewAc.prdoductName_lbl.setText(f"{findUserName} نظرات ثبت شده توسط")
        self.viewAc.createUserDynamicComments(self.UserID)
        self.viewAc.show()
        
    def OpenEditAccountUI(self):
        self.viewAc = editAccountUI()
        AllUserInfo = db.userRepository.GetByID(self.UserID)
        self.viewAc.setWindowTitle("ویرایش حساب کاربری")
        self.viewAc.show()
        self.viewAc.back_btn.clicked.connect(self.OpenViewAccountUI)
        self.viewAc.backToHome_btn.setHidden(True)
        self.viewAc.wrongOldPass_lbl.setHidden(True)
        self.viewAc.notEqualPass_lbl.setHidden(True)
        self.viewAc.shouldEnterNewPass_lbl.setHidden(True)
        self.viewAc.okEdit_lbl.setHidden(True)
        self.viewAc.edit_userName_input.setText(AllUserInfo[0][1])
        self.viewAc.edit_email_input.setText(AllUserInfo[0][2])
        self.viewAc.confirmEdit_btn.clicked.connect(self.goToConfirmEdit)
        
    def goToConfirmEdit(self):
        # --- show user Edit profile ---
        loginUser = LoginUser(self.UserID)
        findAllUserInfo = db.userRepository.GetByID(self.UserID)
        findThisUserEmail = db.userRepository.GetEmailByID(self.UserID)[0][0]
        findAllUserByInputEmail = db.userRepository.GetByEmail(self.viewAc.edit_email_input.text())
        if(self.viewAc.edit_userName_input.text() != "" and self.viewAc.edit_email_input.text() != ""):
            if((self.viewAc.edit_email_input.text() == findThisUserEmail) or (self.viewAc.edit_email_input.text() != findThisUserEmail) and (findAllUserByInputEmail == [])):
                if(loginUser.EditUserInformation(self.viewAc.edit_userName_input.text(),self.viewAc.edit_email_input.text(),self.viewAc.edit_oldPassword_input.text(),findAllUserInfo[0][3],self.viewAc.edit_newPassword_input.text() , self)):
                    self.viewAc.close()
                    self.message = MessgaeBoxUI()
                    self.message.message_lbl.setText("اطلاعات شما با موفقیت ویرایش شد")
                    self.message.confirm_btn.setText("متوجه شدم")
                    self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("Edit"))
                    self.message.show()
            else:
                self.message = MessgaeBoxUI()
                self.message.message_lbl.setText("این ایمیل درحال استفاده میباشد ، لطفا ایمیل دیگری وارد نمایید")
                self.message.confirm_btn.setText("متوجه شدم")
                self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("ErrorEmail"))
                self.message.show()   
        else:
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("لطفا همه مقادیر را وارد نمایید")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("FillAllInputs"))
            self.message.show()   
    
        # ---END show user Edit profile ---
    
    def OpenIncreaseBalanceUI(self):
        self.BalancAc = accountBalanceUI()
        self.BalancAc.wrongEmptyBalance_lbl.setHidden(True)
        self.BalancAc.okBalance_lbl.setHidden(True)
        self.BalancAc.wrongJustNumber_lbl.setHidden(True)
        self.BalancAc.show()
        self.BalancAc.confirmBalance_btn.clicked.connect(self.goToConfirmBalance)
        
    def goToConfirmBalance(self):
        loginUser = LoginUser(self.UserID)
        if(loginUser.IncreaseAccountBalance(self.BalancAc.balance_input,wrongEmptyBalance_lbl = self.BalancAc.wrongEmptyBalance_lbl , wrongJustNumber_lbl = self.BalancAc.wrongJustNumber_lbl , okBalance_lbl = self.BalancAc.okBalance_lbl)):
            self.BalancAc.close()
            self.viewAc.show_balance.setText(f"{db.userBalanceRepository.GetBalance(self.UserID)[0][0]}")
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("موجودی کیف پول شما با موفقیت افزایش یافت")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("confirmBalance"))
            self.message.show()
    
    def goToCloseMessageBox(self,message):
        if(message == "LogIn"):
            self.message.close()
            self.OpenHomePageAferLoginUI()
        elif(message == "Edit" or message == "confirmBalance" or message == "AddNewComment" , message == "AddToFavoritList" or message == "AddTocart" or message == "ErrorEmail" or message == "FillAllInputs"):
            self.message.close()

# ----| RigisterWindowUI |----
class RigisterWindowUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\RigisterUI.ui", self)
        self.setWindowTitle("ثبت نام")
        self.rigister_btn.clicked.connect(self.goToRigister)
        # self.clear_btn.clicked.connect(self.goToClear)
        self.goToHome_btn.setHidden(True)
        self.wrongEmailUsed_lbl.setHidden(True)
        self.wrongFields_lbl.setHidden(True)
        self.wrongPersianChar_lbl.setHidden(True)
        self.wrongRePass_lbl.setHidden(True)
        self.okRigister_lbl.setHidden(True)
    def goToRigister(self):
        # --- Rigister User ---
        user = User()
        if(user.Rigister(self.username_input.text(),self.email_input.text(),self.pass_input.text(),self.repass_input.text(),wrongEmailUsed_lbl = self.wrongEmailUsed_lbl , wrongFields_lbl = self.wrongFields_lbl , wrongPersianChar_lbl = self.wrongPersianChar_lbl , wrongRePass_lbl = self.wrongRePass_lbl , okRigister_lbl = self.okRigister_lbl)):
            self.goToHome_btn.setHidden(False)
         
    
# ----| viewAccountUI |----
class viewAccountUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewAccountUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        
# ----| editAccountUI |----
class editAccountUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\editAccountUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.show()
        
# ----| accountBalanceUI |----   
class accountBalanceUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\BalanceUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("افزایش موجودی")
        self.show()
        
# ----| viewProductUI |----   
class viewProductUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewProductUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("مشاهده محصول")
        self.show()
        

# ----| favoritListUI |----   
class favoritListUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(587,793)
        self.setWindowTitle("لیست علاقه مندی ها")
        loadUi(os.getcwd()+"\\uiDesigns\\favoritListUI.ui", self)
        self.refresh_btn.setCursor(Qt.PointingHandCursor)
        
    def createLables(self,userID):
        loginUser = LoginUser(userID)
        loginUser.SeeFavoritList(self)
        
    def DeleteFromFaveUI(self,userID,objName):
        self.message = MessgaeBoxUI()
        findProductID = objName.split("_")[1]
        findProductName = db.ProductsRepository.GetProductNameByID(findProductID)[0][0]
        self.message.message_lbl.setText(f"آیا از حذف {findProductName} از لیست مورد علاقه مطمئن هستید؟")
        self.message.show()
        self.message.confirm_btn.clicked.connect(lambda: self.goToDeleteFromFave(userID,findProductID))
        
    def goToDeleteFromFave(self,userID,productID):
        loginUser = LoginUser(userID)
        if(loginUser.RemoveItemFromFavorit(productID)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("با موفقیت از لیست حذف شد ,لیست را به روز رسانی کنید ")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("confirm"))
            self.message.show()
    
    def DetailsFromFaveUI(self,userID,objName):
        self.veiwProduct = viewProductUI() 
        loginUser = LoginUser(userID)
        loginUser.SeeItemDetailFromFavorit(self,objName)
        self.veiwProduct.show()  

    
    def goToCloseMessageBox(self,message):
        if(message == "confirm"):
            self.message.close()


# ----| MessgaeBoxUI |----   
class MessgaeBoxUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\MessgaeBoxUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("پیغام")
        self.confirm_btn.setCursor(Qt.PointingHandCursor)
        self.show()
    
# ----| shopCartUI |----   
class shopCartUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\shopCartUI.ui", self)
        self.setWindowTitle("سبد خرید")
        self.setFixedSize(self.width(),self.height())
        
    def createDynamicBtn(self,userID):
        self.userID = userID
        loginUser = LoginUser(userID)
        loginUser.SeeUserShopCartPanel(self)
        
    
    def clearAllUserShopCartUI(self,userID):
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText("آیا از حذف تمام محصولات از سبد خرید مطمئن هستید؟")
        self.message.confirm_btn.clicked.connect(lambda: self.goToClearAllShopCart(userID))
        self.message.show()
    
    
    def goToClearAllShopCart(self,userID):
       loginUser = LoginUser(userID)
       if(loginUser.RemoveAllItemsFromShopCart(userID)):
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText("سبد خرید شما با موفقیت خالی شد")
        self.message.confirm_btn.setText("بستن")
        self.message.confirm_btn.clicked.connect(self.closeMessageBox)
        self.message.show()
        
    def OpenDeleteFromShopCartUI(self,userID,objName):
        self.message = MessgaeBoxUI()
        findProductID = objName.split("_")[1]
        findProductName = db.ProductsRepository.GetProductNameByID(findProductID)[0][0]
        self.message.message_lbl.setText(f"آیا از حذف {findProductName} از سبد خرید مطمن هستید؟")
        self.message.confirm_btn.clicked.connect(lambda: self.goTodeleteThisProductFromUserShopCart(userID,findProductID))
        self.message.show()
        
    def goTodeleteThisProductFromUserShopCart(self,userID,productID):
        loginUser = LoginUser(userID)
        if(loginUser.RemoveThisItemFromShopCart(userID,productID)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("با موفقیت از لیست حذف شد ,لیست را به روز رسانی کنید ")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
    
    def OpenPayUI(self,userID):
        user_shopCart_list = db.ShopCartRepository.GetAllByUserID(userID)
        if(user_shopCart_list != []):
            self.payWindow = PayWindowUI()
            loginUser = LoginUser(userID)
            totalPrice = loginUser.CalculateTotalUserShopCartPrice(user_shopCart_list)
            findUserBalance = db.userBalanceRepository.GetBalance(userID)
            if(findUserBalance != []):
                findUserBalance = findUserBalance[0][0]
            else:
                findUserBalance = 0
            self.payWindow.totalPrice_lbl.setText(str(totalPrice))
            self.payWindow.userBalance_lbl.setText(str(findUserBalance))
            self.payWindow.confrirmPay_btn.clicked.connect(lambda: self.payWindow.goToConfirmPayment(userID,findUserBalance,totalPrice))
            self.payWindow.show()
        else:
            self.message = MessgaeBoxUI()
            self.message.setWindowTitle("پیغام")
            self.message.message_lbl.setText("سبد خرید شما خالی است")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
            self.message.show()
    
    def closeMessageBox(self):
        self.message.close()

# ----| addToCartUI |----      
class addToCartUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\addToCartUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("افزودن به سبد خرید")
        self.okShopCart_lbl.setHidden(True)
        self.invalidDiscount_lbl.setHidden(True)
        self.wrongJustNumber_lbl.setHidden(True)
        self.atLeastOneItem_lbl.setHidden(True)
        self.show()

# ----| ViewCommentsUI |----      
class ViewCommentsUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\AllcommentsUI.ui", self)
        self.setWindowTitle("مشاهده نظرات")
        self.setFixedSize(self.width(),self.height())
        
    def createDynamicComments(self,productID):
        product = Product(productID)
        product.showComments(self)
    
    def createUserDynamicComments(self,userID):
        loginUser = LoginUser(userID)
        self.setFixedSize(644,865)
        loginUser.ViewComment(self
                              )
    def DeleteUserComment(self,userID,objName):
        productID = objName.split("_")[1]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText("آیا از حذف این نظر مطمن هستید؟")
        self.message.confirm_btn.clicked.connect(lambda x : self.goToDeleteComment(userID,productID))
        self.message.show()   
        
    def goToDeleteComment(self,userID,productID):
        loginUser = LoginUser(userID)
        if(loginUser.DeleteComment(productID)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("نظر شما با موفقیت حذف شد ، لطفا لیست را به روز رسانی کنید")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
            self.message.show()
            
    def closeMessageBox(self):
        self.message.close()
        
    def RefreshUserCommentUI(self,userID):
        self.close()
        self.window = ViewCommentsUI()
        self.window.createUserDynamicComments(userID)
        self.window.show()
    

# ----| AddNewCommentUI |----      
class AddNewCommentUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\addNewCommentUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.WarningComment_lbl.setHidden(True)

# ----| PayWindowUI |----      
class PayWindowUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\PayWindowUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.wrongMobile_lbl.setHidden(True)
        self.wrongField_lbl.setHidden(True)
        self.wrongMobileJustNumber_lbl.setHidden(True)
        
    def goToConfirmPayment(self,userID,UserBalance,totalPrice):
        loginUser = LoginUser(userID)
        if(totalPrice > UserBalance):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("موجودی شما برای پرداخت کافی نمیباشد.")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
        else:
            if(loginUser.ConfirmPeyment(self,userID,UserBalance,totalPrice)):
                self.close()
                self.message = MessgaeBoxUI()
                self.message.message_lbl.setText("سفارش شما با موفقیت ثبت شد")
                self.message.confirm_btn.setText("بستن")
                self.message.confirm_btn.clicked.connect(self.closeMessageBox)
                self.message.show()
            
    def closeMessageBox(self):
        self.message.close()
        
        
class operatorLoginUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\operatorLoginUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.login_btn.clicked.connect(self.goToLogin)
        self.okLoign_lbl.setHidden(True)
        self.wrongEmail_lbl.setHidden(True)
        self.wrongPass_lbl.setHidden(True)
        self.wrongFields_lbl.setHidden(True)
    def goToLogin(self):
        # --- check if the email and password is correct ---
        operator = Operator()
        if(operator.Login(self.email_input.text(),self.pass_input.text(),self)):
            self.OperatorID = operator.FindOperatorID
            self.AllOperatorInfo = db.OperatorRepository.GetByID(self.OperatorID)
            self.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("با موفقیت وارد پنل کاربری اپراتور شدید")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("LogIn"))
            self.message.show()
            
    def goToCloseMessageBox(self,message):
        if(message == "LogIn"):
            self.message.close()
            self.close()
            self.window = operatorPanelUI()
            self.window.HandelOperatorPanel_func(self.OperatorID,self.AllOperatorInfo)
            findUserName = db.OperatorRepository.GetUserNameByID(self.OperatorID)[0][0]
            self.window.welcome_btn.setText(f'{findUserName}'+" خوش اومدی ")
            self.window.show()

class operatorPanelUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\operatorUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.exitAcc_btn.clicked.connect(self.goToHomePageUI)
        self.viewOperator_btn.clicked.connect(self.OpenViewOperatorDetailsUI)
        self.viewUsers_btn.clicked.connect(self.OpenViewUsersDetailsUI)
        self.viewProducts_btn.clicked.connect(self.OpenViewProductsDetailsUI)
        self.viewCats_btn.clicked.connect(self.OpenViewCatUI)
        self.viewUsersShopCart_btn.clicked.connect(self.OpenViewHandelOrdersUI)
        self.viewDiscount_btn.clicked.connect(self.OpenViewDiscountsUI)
        self.viewSalers_btn.clicked.connect(self.OpenViewSalersUI)
                    
        
    def HandelOperatorPanel_func(self,OperatorID,AllInfo):
        self.OperatorID = OperatorID
        self.AllOperatorInfo = AllInfo
        
    def OpenViewSalersUI(self):
        self.viewSalers = viewSalersUI()
        self.viewSalers.show()
        
    def OpenViewDiscountsUI(self):
        self.viewDiscounts = viewDiscountUI()
        self.viewDiscounts.show()
        
    def OpenViewHandelOrdersUI(self):
        self.viewOperatorHandelOrders = operatorHandelOrdersUI()
        self.viewOperatorHandelOrders.show()   
        
    def goToHomePageUI(self):
        self.close()
        self.window = mainWindowUI()
        self.window.show()
        
    def OpenViewCatUI(self):
        self.viewCatUI = viewAllCatUI()
        self.viewCatUI.show()
        
    def OpenViewUsersDetailsUI(self):
        self.viewAllUserDetails = viewAllUserDetailsUI()
        self.viewAllUserDetails.Refresh_Btn.clicked.connect(self.goToRefreshViewUsersUI)
        self.viewAllUserDetails.show()
        
    def goToRefreshViewUsersUI(self):
        self.viewAllUserDetails.close()
        self.OpenViewUsersDetailsUI()
        
    def OpenViewProductsDetailsUI(self):
        self.viewAllProductsDetails = viewAllProductsDetailsUI()
        self.viewAllProductsDetails.show()
        
    def OpenViewOperatorDetailsUI(self):
        self.viewAc = viewAccountUI()
        self.viewAc.label_6.setHidden(True)
        self.viewAc.label_8.setHidden(True)
        self.viewAc.label_9.setHidden(True)
        self.viewAc.label_10.setHidden(True)
        self.viewAc.show_balance.setHidden(True)
        self.viewAc.increaseBalance_btn.setHidden(True)
        self.viewAc.factor_btn.setHidden(True)
        self.viewAc.userComments_btn.setHidden(True)
        self.viewAc.label_7.setText("شناسه اپراتور : ")
        self.goToViewOperator_func(self.OperatorID)
        self.viewAc.edit_btn.clicked.connect(lambda x : self.OpenEditOperatorUI(self.OperatorID))
        self.viewAc.show()
    
    def goToViewOperator_func(self,operatorID):
        operator = Operator()
        operator.ViewOperatorDetails(operatorID,self)
        
    def OpenEditOperatorUI(self,operatorID):
        self.viewAc = editAccountUI()
        self.viewAc.setWindowTitle("ویرایش حساب کاربری")
        self.viewAc.show()
        findAllUserInfo = db.OperatorRepository.GetByID(operatorID)
        self.viewAc.back_btn.clicked.connect(self.OpenViewOperatorDetailsUI)
        self.viewAc.backToHome_btn.setHidden(True)
        self.viewAc.wrongOldPass_lbl.setHidden(True)
        self.viewAc.notEqualPass_lbl.setHidden(True)
        self.viewAc.shouldEnterNewPass_lbl.setHidden(True)
        self.viewAc.okEdit_lbl.setHidden(True)
        self.viewAc.edit_userName_input.setText(findAllUserInfo[0][1])
        self.viewAc.edit_email_input.setText(findAllUserInfo[0][2])
        self.viewAc.confirmEdit_btn.clicked.connect(self.goToConfirmEdit)
        
    def goToConfirmEdit(self):
        # --- show user Edit profile ---
        operator = Operator()
        findAllUserInfo = db.OperatorRepository.GetByID(self.OperatorID)
        if(operator.EditOperatorInformation(self.OperatorID,self.viewAc.edit_userName_input.text(),self.viewAc.edit_email_input.text(),self.viewAc.edit_oldPassword_input.text(),findAllUserInfo[0][3],self.viewAc.edit_newPassword_input.text() , self)):
            self.viewAc.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("اطلاعات شما با موفقیت ویرایش شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("Edit"))
            self.message.show()
        # ---END show user Edit products ---
        
    def goToCloseMessageBox(self,message):
        if(message == "Edit"):
            self.message.close()
            
class viewAllUserDetailsUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewAllUsersUI.ui", self)
        self.setFixedSize(self.width(),self.height())   
        self.createDynamicUsersDetails()

        
    def createDynamicUsersDetails(self):
        operator = Operator()
        operator.viewAllUsersSection(self)
        
    def OpenViewAccountUI(self,objName):
        userID = objName.split("_")[1]
        self.viewAc = viewAccountUI()
        self.viewAc.factor_btn.setHidden(True)
        self.viewAc.userComments_btn.setHidden(True)
        self.viewAc.label_9.setHidden(True)
        self.viewAc.label_10.setHidden(True)
        # --- show user profile ---
        loginUser = LoginUser(userID)
        loginUser.SeeUserPanel(self.viewAc.show_userName,self.viewAc.show_email,self.viewAc.show_password,self.viewAc.show_date,self.viewAc.show_randomID,self.viewAc.show_balance)
        # ---END show user profile ---
        self.viewAc.edit_btn.clicked.connect(lambda x : self.OpenEditAccountUI(userID))
        self.viewAc.increaseBalance_btn.clicked.connect(lambda x : self.OpenIncreaseBalanceUI(userID))
        self.viewAc.show()
        
    def OpenEditAccountUI(self,userID):
        self.viewAc = editAccountUI()
        self.viewAc.setWindowTitle("ویرایش حساب کاربری")
        self.viewAc.show()
        AllUserInfo = db.userRepository.GetByID(userID)
        objName = f"objName_{userID}"
        self.viewAc.back_btn.clicked.connect(lambda x :  self.OpenViewAccountUI(objName))
        self.viewAc.backToHome_btn.setHidden(True)
        self.viewAc.wrongOldPass_lbl.setHidden(True)
        self.viewAc.notEqualPass_lbl.setHidden(True)
        self.viewAc.shouldEnterNewPass_lbl.setHidden(True)
        self.viewAc.okEdit_lbl.setHidden(True)
        self.viewAc.edit_userName_input.setText(AllUserInfo[0][1])
        self.viewAc.edit_email_input.setText(AllUserInfo[0][2])
        self.viewAc.confirmEdit_btn.clicked.connect(lambda x : self.goToConfirmEdit(userID))
        
    def goToConfirmEdit(self,userID):
        # --- show user Edit profile ---
        loginUser = LoginUser(userID)
        findAllUserInfo = db.userRepository.GetByID(userID)
        if(loginUser.EditUserInformation(self.viewAc.edit_userName_input.text(),self.viewAc.edit_email_input.text(),self.viewAc.edit_oldPassword_input.text(),findAllUserInfo[0][3],self.viewAc.edit_newPassword_input.text() , self)):
            self.viewAc.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("اطلاعات شما با موفقیت ویرایش شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("Edit"))
            self.message.show()
        # ---END show user Edit profile ---
        
    def goToCloseMessageBox(self,message):
        if(message == "LogIn" or message == "confirmBalance" or message == "ConfirmDelete" or message == "Edit"):
            self.message.close()
            
        
    def OpenIncreaseBalanceUI(self,userID):
        self.BalancAc = accountBalanceUI()
        self.BalancAc.wrongEmptyBalance_lbl.setHidden(True)
        self.BalancAc.okBalance_lbl.setHidden(True)
        self.BalancAc.wrongJustNumber_lbl.setHidden(True)
        self.BalancAc.show()
        self.BalancAc.confirmBalance_btn.clicked.connect(lambda x : self.goToConfirmBalance(userID))
        
    def goToConfirmBalance(self,userID):
        loginUser = LoginUser(userID)
        if(loginUser.IncreaseAccountBalance(self.BalancAc.balance_input,wrongEmptyBalance_lbl = self.BalancAc.wrongEmptyBalance_lbl , wrongJustNumber_lbl = self.BalancAc.wrongJustNumber_lbl , okBalance_lbl = self.BalancAc.okBalance_lbl)):
            self.BalancAc.close()
            self.viewAc.show_balance.setText(f"{db.userBalanceRepository.GetBalance(userID)[0][0]}")
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText("موجودی کیف پول شما با موفقیت افزایش یافت")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("confirmBalance"))
            self.message.show()
    
    def goToDeleteUserFromDB(self,objName):
            userID = objName.split("_")[1]
            userName = db.userRepository.GetUserNameByID(int(userID))[0][0]
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"آیا از حدف کاربر {userName} مطمن هستید؟")
            self.message.confirm_btn.setText("بله")
            self.message.confirm_btn.clicked.connect(lambda x : self.confirmDeleteUser(userID))
            self.message.show()
            
    def confirmDeleteUser(self,userID):
        operator = Operator()
        if(operator.ConfrimDeleteUser(userID)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"کاربر با موفقیت حذف شد ، لیست را به روز رسانی کنید")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("ConfirmDelete"))
            self.message.show()

class viewAllProductsDetailsUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewAllProductsUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.createDynamicUsersDetails()
        self.Refresh_Btn.clicked.connect(self.refreshviewAllProductDetailsUI)
        
    def createDynamicUsersDetails(self):
        operator = Operator()
        operator.viewAllProductsSection(self)
        
    def refreshviewAllProductDetailsUI(self):
        self.close()
        self.window = viewAllProductsDetailsUI()
        self.window.show()
        
    def OpenEditProductUI(self,objName):
        productID = objName.split("_")[1]
        self.viewEditProductUI = editProductUI()
        operator = Operator()
        operator.EditProductDetails(productID,self)
        self.viewEditProductUI.confirmEdit_btn.clicked.connect(lambda x : self.viewEditProductUI.confirmEditProductUI(productID))
        self.viewEditProductUI.show()

class viewAllCatUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewCatUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("مدیریت دسته بندی محصولات")
        self.createDynamicCat()
        self.addNewMainCat_btn.clicked.connect(self.OpenAddNewMainCatUI)
        self.refresh_btn.clicked.connect(self.refreshViewAllCatUI)
        
    def createDynamicCat(self):
        operator = Operator()
        operator.viewCatDetailsUI(self)
        
    def refreshViewAllCatUI(self):
        self.close()
        self.window = viewAllCatUI()
        self.window.show()    
    
    def openEditCatUI(self,objName):
        getCatID = objName.split("_")[1]
        self.close()
        self.viewCatEdit = viewCatEditUI()
        self.viewCatEdit.createDynamicEditCat(getCatID)
        self.viewCatEdit.addNewSubCat_btn.clicked.connect(lambda x : self.viewCatEdit.OpenAddNewSubCatUI(getCatID) )
        self.viewCatEdit.back_btn.clicked.connect(self.goTobackViewCats)
        self.viewCatEdit.refresh_btn.clicked.connect(lambda x : self.goToRefreshViewCats(objName))
        self.viewCatEdit.removeMainCat_btn.clicked.connect(lambda x : self.viewCatEdit.OpenDeleteMainCatUI(getCatID))
        self.viewCatEdit.show()
        
    def goToRefreshViewCats(self,objaName):
        self.viewCatEdit.close()
        self.openEditCatUI(objaName)


    def goTobackViewCats(self):
        self.viewCatEdit.close()
        self.window = viewAllCatUI()
        self.window.show()
        
    def OpenAddNewMainCatUI(self):
        self.viewAddNewSubCat = addNewSubCatUI()
        self.viewAddNewSubCat.label_5.setText("شاخه جدید را اضافه کنید")
        self.viewAddNewSubCat.confirm_btn.clicked.connect(self.viewAddNewSubCat.goToCreateNewMainCat)
        self.viewAddNewSubCat.show()


class viewCatEditUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\editCatUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("ویرایش شاخه")
        self.confirmEdit_btn.clicked.connect(self.OpenConfirmEditCatsUI)
        
        
    def createDynamicEditCat(self,getCatID):
        operator = Operator()
        operator.editCatDetails(getCatID,self)
    
    def OpenConfirmRemoveSubCatUI(self,objName):
        catID = objName.split("_")[1]
        findCatName = db.CatRepository.GetCatNameById(catID)[0][0]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از حدف {findCatName} مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.confirmDeleteSubCat(catID))
        self.message.show()
        
    def confirmDeleteSubCat(self,catID):
        getAllProducts = db.ProductsRepository.GetAllByCatID(catID)
        if(getAllProducts == []):
            operator = Operator()
            if(operator.removeSubCat(catID)):
                self.message = MessgaeBoxUI()
                self.message.message_lbl.setText(f"شاخه با موفقیت حذف شد")
                self.message.confirm_btn.setText("بستن")
                self.message.confirm_btn.clicked.connect(self.goTocloseEditCatsUI)
                self.message.show()
        else:
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"این زیر شاخه در حال اسفاده میباشد ، لطفا ابتدا محصول وابسته به آن را ویراش کنید")
            self.message.message_lbl.setStyleSheet("QLabel {font : 15pt 'B narm';}")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.goToCloseMessageBox)
            self.message.show()
            
    def goToCloseMessageBox(self):
        self.message.close()
        
        
    def OpenConfirmEditCatsUI(self):
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از ثبت ویرایش شاخه ها مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(self.gotoConfirmEditCats)
        self.message.show()
    
    def gotoConfirmEditCats(self):
        self.message.close()
        operator = Operator()
        if(operator.confirmEditcat(self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"شاخه ها به موفقیت ویرایش شدند")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.goTocloseEditCatsUI)
            self.message.show()
            
    def goTocloseEditCatsUI(self):
        self.message.close()
        self.close()
        self.window = viewAllCatUI()
        self.window.show()
        
    def OpenAddNewSubCatUI(self,mainCatID):
        self.viewAddNewSubCat = addNewSubCatUI()
        self.viewAddNewSubCat.confirm_btn.clicked.connect(lambda x : self.viewAddNewSubCat.goToConfirmNewSubCat(mainCatID))
        self.viewAddNewSubCat.show()
        
    def OpenDeleteMainCatUI(self,mainCatID):
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از حذف کل این شاخه به همراه زیر شاخه های آن مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.goToConfirmDeleteMainCat(mainCatID))
        self.message.show()
        
    def goToConfirmDeleteMainCat(self,mainCatID):
        getAllUubCats = db.CatRepository.GetAllSubCatbyID(mainCatID)
        flag = False
        for i in getAllUubCats:
            subCatID = i[0]
            findProduct = db.ProductsRepository.GetAllByCatID(subCatID)
            if(findProduct != []):
                flag = True
        if(flag):
                self.message = MessgaeBoxUI()
                self.message.message_lbl.setText(f"زیر شاخه های این شاخه در حال استفاده میباشند ، ابتدا محصولات مرتبط به آن را حذف کنید")
                self.message.confirm_btn.setText("بستن")
                self.message.message_lbl.setStyleSheet("QLabel {font : 15pt 'B narm';}")
                self.message.confirm_btn.clicked.connect(self.goToCloseMessageBox)
                self.message.show()
        else:
            operator = Operator()
            if(operator.removeMainCat(mainCatID)):
                self.message = MessgaeBoxUI()
                self.message.message_lbl.setText(f"شاخه اصلی و زیرمجموعه های با موفقیت حذف شد")
                self.message.confirm_btn.setText("بستن")
                self.message.message_lbl.setStyleSheet("QLabel {font : 15pt 'B narm';}")
                self.message.confirm_btn.clicked.connect(self.goTocloseEditCatsUI)
                self.message.show()
        
        
class addNewSubCatUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\addNewSubCatUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("افزودن زیر شاخه جدید")
        self.wrong_lbl.setHidden(True)
        
    def goToConfirmNewSubCat(self,mainCatID):        
        operator = Operator()
        if(operator.addNewSubCat(mainCatID,self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"زیر شاخه جدید با موفقیت اضافه شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.gotoCloseAddNewSubCat)
            self.message.show()
            
    def gotoCloseAddNewSubCat(self):
        self.message.close()
        self.close()
    
    def goToCreateNewMainCat(self):
        operator = Operator()
        if(operator.addNewMainCat(self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"شاخه جدید با موفقیت اضافه شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.gotoCloseAddNewSubCat)
            self.message.show()

class editProductUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\editProductUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        self.setWindowTitle("ویرایش محصول")
        
    def confirmEditProductUI(self,productID):
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از ویراش اطلاعات این محصول مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.gotoCloseConfirmEdit(productID))
        self.message.show()

            
    def gotoCloseConfirmEdit(self,productID):
        self.message.close()
        operator = Operator()
        if(operator.ConfrimEditProduct(productID,self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"محصول با موفقیت ویرایش شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(self.gotoCloseConfirmEditProduct)
            self.message.show()
            
    def gotoCloseConfirmEditProduct(self):
        self.message.close()
        self.close()
        
class usersOrderUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\UserOrdersUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        
    def createDynamicInfo(self,userID):
        loginUser = LoginUser(userID)
        loginUser.SeeFactorList(self)
        
    def OpenDetialsOfFactorUI(self,objName):
        findIDs = objName.split("_")[1]
        findUserID = findIDs.split("|")[0]
        findBuyID = findIDs.split("|")[1]
        self.close()
        self.viewFactor = viewFactorDetailsUI()
        self.viewFactor.createDynamicFactor(findUserID,findBuyID)
        self.viewFactor.back_btn.clicked.connect(self.BackToUserOrdersUI)
        self.viewFactor.show()
        
    def BackToUserOrdersUI(self):
        self.viewFactor.close()
        self.show()

class viewFactorDetailsUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewFactorDetailsUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        
    def createDynamicFactor(self,userID,buyID):
        loginUser = LoginUser(userID)
        loginUser.seeDetailsOfFactor(buyID,self)


class operatorHandelOrdersUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\OperatorHadnelOrdersUI.ui", self)
        self.createDynamicInfo()
        self.setFixedSize(self.width(),self.height())
        self.refresh_btn.clicked.connect(self.goToRefreshOnlineShop)
        
    def goToRefreshOnlineShop(self):
        self.close()
        self.window = operatorHandelOrdersUI()
        self.window.show()
        
    def createDynamicInfo(self):
        operator = Operator()
        operator.ConfirmUserShopCart(self)
        
    def goToConfrimOrder(self,objName):
        findIDs = objName.split("_")[1]
        userID = findIDs.split("|")[0]
        buyID = findIDs.split("|")[1]
        findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از ثبت سفارش کاربر {findUserName} مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.gotoCloseConfirmOrder(userID,buyID))
        self.message.show()
    
    def gotoCloseConfirmOrder(self,userID,buyID):
        operator = Operator()
        if(operator.goToSendOrder(userID,buyID)):       
            findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
            self.message.message_lbl.setText(f"سفارش کاربر {findUserName} با موفقیت ثبت شد و در حال ارسال قرار گرفت")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
            self.message.show()
    
    def goToIgnoreOrder(self,objName):
        findIDs = objName.split("_")[1]
        userID = findIDs.split("|")[0]
        buyID = findIDs.split("|")[1]
        findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از لغو سفارش کاربر {findUserName} مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.gotoCloseIgnoreOrder(userID,buyID))
        self.message.show()
        
    def gotoCloseIgnoreOrder(self,userID,buyID):
        operator = Operator()
        if(operator.goToIgnoreOrder(userID,buyID)):
            findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
            self.message.close()
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"سفارش کاربر {findUserName} با موفقیت لغو و وجه برگشت داده شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(self.closeMessageBox)
            self.message.show()
    
    def closeMessageBox(self):
        self.message.close()
        self.close()

class viewDiscountUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewDiscountUI.ui", self)
        self.createDynamicInfo()
        self.setFixedSize(self.width(),self.height())
        self.addNewOffer_btn.clicked.connect(self.OpenAddNewDiscountUI)
        self.refresh_btn.clicked.connect(self.goToRefreshViewDiscountUI)
        
        
    def goToRefreshViewDiscountUI(self):
        self.close()
        self.window = viewDiscountUI()
        self.window.show()
        
    def OpenAddNewDiscountUI(self):
        self.viewEditOffersUI = viewEditOffersUI()
        self.viewEditOffersUI.label_2.setText("افزودن کد تخفیف جدید")
        self.viewEditOffersUI.label_2.setStyleSheet("QLabel { font: 24pt 'B narm';}")
        self.viewEditOffersUI.confirm_btn.setText("افزودن")
        self.goToAddNewOffer()
        self.viewEditOffersUI.show()    
        
    def createDynamicInfo(self):
        operator = Operator()
        operator.viewDiscountUI(self)
        
    def goToEditOffer(self,objName):
        findOfferID = objName.split("_")[1]
        self.close()
        self.window = viewEditOffersUI()
        self.window.OpenEditUI(findOfferID)
        self.window.show()

    def goToDeleteOffer(self,objName):
        findOfferID = objName.split("_")[1]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از حذف این کد تخفیف مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.goToConfirmDeleteOffer(findOfferID))
        self.message.show()
        
    def goToConfirmDeleteOffer(self,offerID):
        db.OffersRepository.Delete(offerID)
        db.OffersRepository.Save()
        self.message.close()
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"کد تخفیف با موفقیت پاک شد")
        self.message.confirm_btn.setText("بستن")
        self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("DeleteOffer"))
        self.message.show()
        
    def goToAddNewOffer(self):
        self.viewEditOffersUI.confirm_btn.clicked.connect(self.confirmAddNewOffer)
        
    def confirmAddNewOffer(self):
        operator = Operator()
        if(operator.AddNewOffer(self.viewEditOffersUI)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"کد تخفیف جدید با موفقیت افزوده شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("create"))
            self.message.show()
        else:
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"لطفا همه مقادیر را کامل کنید")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("wrong"))
            self.message.show()
        
    def goToCloseMessageBox(self,message):
        if(message == "DeleteOffer"):
            self.message.close()
            self.close()
            self.window = viewDiscountUI()
            self.window.show()
        elif(message == "create"):
            self.message.close()
            self.close()
            self.viewEditOffersUI.close()
            self.window = viewDiscountUI()
            self.window.show()
        elif(message =="wrong"):
            self.message.close()

class viewEditOffersUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\EditOfferUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        
    def OpenEditUI(self,offerID):
        findOffName = db.OffersRepository.GetCodeNameBYID(offerID)[0][0]
        findDiscount = db.OffersRepository.GetDiscountBYID(offerID)[0][0]
        self.offer_input.setText(f"{findOffName}")
        self.discount_input.setText(f"{findDiscount}")
        self.confirm_btn.clicked.connect(lambda x : self.goToConfirmEditOffers(offerID))
        
    def goToConfirmEditOffers(self,offerID):
        operator = Operator()
        if(operator.ConfirmEditOffer(offerID,self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"کد تخفیف با موفقیت ویرایش شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.closeMessageBox("edit"))
            self.message.show()
            
    def closeMessageBox(self,message):
        if(message == "edit"):
            self.message.close()
            self.close()
            self.window = viewDiscountUI()
            self.window.show()
            
class viewSalersUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\viewSalersUI.ui", self)
        self.createDynamicInfo()
        self.setFixedSize(self.width(),self.height())  
        self.addNewSaler_btn.clicked.connect(self.OpenAddNewSalerUI)
        self.refresh_btn.clicked.connect(self.goToRefreshSalerUI)
        
    def createDynamicInfo(self):
        operator = Operator()
        operator.ViewSalersUI(self)
    
    def goToRefreshSalerUI(self):
        self.close()
        self.window = viewSalersUI()
        self.window.show()
        
    def OpenAddNewSalerUI(self):
        self.viewEditSalersUI = viewEditSalersUI()
        self.viewEditSalersUI.label_2.setText("افزودن فروشنده جدید")
        self.viewEditSalersUI.label_2.setStyleSheet("QLabel { font: 24pt 'B narm';}")
        self.viewEditSalersUI.label_4.setHidden(True)
        self.viewEditSalersUI.randomID_input.setHidden(True)
        self.viewEditSalersUI.confirm_btn.setText("افزودن")
        self.goToAddNewSaler()
        self.viewEditSalersUI.show()    
        
    def goToAddNewSaler(self):
        self.viewEditSalersUI.confirm_btn.clicked.connect(self.confirmAddNewSaler)
        
    def confirmAddNewSaler(self):
        operator = Operator()
        if(operator.AddNewSaler(self.viewEditSalersUI)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"فروشنده جدید با موفقیت افزوده شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("create"))
            self.message.show()
        else:
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"لطفا همه مقادیر را کامل کنید")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("wrong"))
            self.message.show()
        
    def goToCloseMessageBox(self,message):
        if(message == "create"):
            self.message.close()
            self.close()
            self.viewEditSalersUI.close()
            self.window = viewSalersUI()
            self.window.show()
        elif(message =="wrong"):
            self.message.close()
        elif(message == "DeleteSaler"):
            self.message.close()
            self.close()
            self.window = viewSalersUI()
            self.window.show()
        
    def goToEditSaler(self,objName):
        findSalerID = objName.split("_")[1]
        self.close()
        self.window = viewEditSalersUI()
        self.window.OpenEditUI(findSalerID)
        self.window.show()
        
    def goToDeleteSaler(self,objName):
        findSalerID = objName.split("_")[1]
        findSalerName = db.SalerRepository.GetSalerNameByID(findSalerID)[0][0]
        self.message = MessgaeBoxUI()
        self.message.message_lbl.setText(f"آیا از حذف فروشنده {findSalerName} مطمن هستید؟")
        self.message.confirm_btn.setText("بله")
        self.message.confirm_btn.clicked.connect(lambda x : self.goToConfirmDeleteSaler(findSalerID))
        self.message.show()
        
    def goToConfirmDeleteSaler(self,findSalerID):
        self.message.close()
        operator = Operator()
        if(operator.DeleteSaler(findSalerID) == 2):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"فروشنده با موفقیت حذف شد")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("DeleteSaler"))
            self.message.show()
        elif(operator.DeleteSaler(findSalerID) == 0):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"این فروشنده درحال حاظر در حال ارائه خدمات میباشد ، ابتدا محصولات وابسته به آن را ویرایش کنید")
            self.message.message_lbl.setStyleSheet("QLabel { font: 15pt 'B narm';}")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("wrong"))
            self.message.show()
        elif(operator.DeleteSaler(findSalerID) == 1):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"از این فروشنده قبلا محصولی خریداری شده است و به ثبت رسیده است ، لذا تنها ویرایش اطلاعات آن ممکن است")
            self.message.message_lbl.setStyleSheet("QLabel { font: 15pt 'B narm';}")
            self.message.confirm_btn.setText("بستن")
            self.message.confirm_btn.clicked.connect(lambda x : self.goToCloseMessageBox("wrong"))
            self.message.show()


class viewEditSalersUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.getcwd()+"\\uiDesigns\\EditSalerUI.ui", self)
        self.setFixedSize(self.width(),self.height())
        
    def OpenEditUI(self,salerID):
        findSalerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
        findRandomID = db.SalerRepository.GetRandomIDByID(salerID)[0][0]
        self.salerName_input.setText(f"{findSalerName}")
        self.randomID_input.setText(f"{findRandomID}")
        self.confirm_btn.clicked.connect(lambda x : self.goToConfirmEditSaler(salerID))
        
    def goToConfirmEditSaler(self,salerID):
        operator = Operator()
        if(operator.ConfirmEditSaler(salerID,self)):
            self.message = MessgaeBoxUI()
            self.message.message_lbl.setText(f"اطلاعات فروشنده با موفقیت ویرایش شد")
            self.message.confirm_btn.setText("متوجه شدم")
            self.message.confirm_btn.clicked.connect(lambda x : self.closeMessageBox("edit"))
            self.message.show()
            
    def closeMessageBox(self,message):
        if(message == "edit"):
            self.message.close()
            self.close()
            self.window = viewSalersUI()
            self.window.show()
        

app = QApplication(sys.argv)
mainUI = mainWindowUI()
sys.exit(app.exec_())