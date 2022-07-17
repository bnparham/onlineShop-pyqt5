import sys,os
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context
from Tools.Validations.loginValid import loginValid
from Tools.Validations.editValid import editValid
from DataLayer.Tables.operatorTabels import operatorTabels
from DataLayer.Tables.usersTable import userTable
from DataLayer.Tables.catTable import catTable
from DataLayer.Tables.productTable import productTable
import random


from PyQt5.QtWidgets import QLabel , QPushButton , QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

db = context()

class Operator:
    def __init__(self):
        pass
    
    @property
    def FindOperatorID(self):
        return db.OperatorRepository.GetIDByEmail(self.Email)[0][0]    

    def Login(self,email,password,instance):
        self.Email = email
        self.Password = password
        # validation for login page
        validation = loginValid(self.Email,self.Password,db).operatorValidate()
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
    
    def viewAllUsersSection(self,instance):
        AllUsersInfo = db.userRepository.GetAll()
        instance.count_lbl.setText(f"تعداد کاربران فروشگاه : {len(AllUsersInfo)}")
        radif_dict = {}
        userName_dict = {}
        email_dict = {}
        password_dict = {}
        date_dict = {}
        randomID_dict = {}
        btn_del = {}
        btn_dt = {}
        height = 230
        height2 = 240
        index = 0
        for i in AllUsersInfo:
            userID = i[0]
            userName = i[1]
            email = i[2]
            password = i[3]
            date = i[4]
            randomID = i[5]
            # ---- createDynamic ----
            radif_dict[index] = QPushButton(instance)
            radif_dict[index].setText(f"{index}")
            radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            radif_dict[index].setGeometry(1040,height,81,71)
            radif_dict[index].setObjectName(f"showFaveLbl_{userID}")
            # -------
            userName_dict[index] = QPushButton(instance)
            userName_dict[index].setText(f"{userName}")
            userName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            userName_dict[index].setGeometry(920,height,121,71)
            userName_dict[index].setObjectName(f"userName_{userID}")
            # -------
            email_dict[index] = QPushButton(instance)
            email_dict[index].setText(f"{email}")
            email_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            email_dict[index].setGeometry(740,height,181,71)
            email_dict[index].setObjectName(f"Email_{userID}")
            # -------
            password_dict[index] = QPushButton(instance)
            password_dict[index].setText(f"{password}")
            password_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            password_dict[index].setGeometry(610,height,131,71)
            password_dict[index].setObjectName(f"Password_{userID}")
            # -------
            date_dict[index] = QPushButton(instance)
            date_dict[index].setText(f"{date}")
            date_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            date_dict[index].setGeometry(480,height,131,71)
            date_dict[index].setObjectName(f"Date_{userID}")
            # -------
            randomID_dict[index] = QPushButton(instance)
            randomID_dict[index].setText(f"{randomID}")
            randomID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            randomID_dict[index].setGeometry(350,height,131,71)
            randomID_dict[index].setObjectName(f"RandomID{userID}")
            # -------
            btn_del[index] = QPushButton(instance)
            btn_del[index].setText(f"حذف")
            btn_del[index].setStyleSheet("QPushButton {border-radius : 10%;background-color: #e0270f;color : #fff;font: 10pt 'IRANSans';}")
            btn_del[index].setGeometry(140,height2,91,51)
            btn_del[index].setObjectName(f"userDeleteBtn_{userID}")
            btn_del[index].setCursor(Qt.PointingHandCursor)
            # -------
            btn_dt[index] = QPushButton(instance)
            btn_dt[index].setText("مشاهده")
            btn_dt[index].setStyleSheet("QPushButton {border-radius : 10%;background-color: #1cc275;color : #fff;font: 10pt 'IRANSans';}")
            btn_dt[index].setGeometry(240,height2,101,51)
            btn_dt[index].setObjectName(f"userDetailsBtn_{userID}")
            btn_dt[index].setCursor(Qt.PointingHandCursor)
            # ------
            height += 70
            height2 += 70
            index += 1
            
        num = len(btn_del)
        for i in range(num,20):
            btn_del[i] = QPushButton(instance)
            btn_dt[i] = QPushButton(instance)
            btn_del[i].setHidden(True)
            btn_dt[i].setHidden(True)
            
        #  deleteFavorit btn click functions
        btn_del[0].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[0].objectName()))
        btn_del[1].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[1].objectName()))
        btn_del[2].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[2].objectName()))
        btn_del[3].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[3].objectName()))
        btn_del[4].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[4].objectName()))
        btn_del[5].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[5].objectName()))
        btn_del[6].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[6].objectName()))
        btn_del[7].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[7].objectName()))
        btn_del[8].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[8].objectName()))
        btn_del[9].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[9].objectName()))
        btn_del[10].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[10].objectName()))

        
        btn_dt[0].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[0].objectName()))
        btn_dt[1].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[1].objectName()))
        btn_dt[2].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[2].objectName()))
        btn_dt[3].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[3].objectName()))
        btn_dt[4].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[4].objectName()))
        btn_dt[5].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[5].objectName()))
        btn_dt[6].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[6].objectName()))
        btn_dt[7].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[7].objectName()))
        btn_dt[8].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[8].objectName()))
        btn_dt[9].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[9].objectName()))
        btn_dt[10].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[10].objectName()))

    def viewAllProductsSection(self,instance):
        AllProductsInfo = db.ProductsRepository.GetAll()
        instance.count_lbl.setText(f"تعداد محصولات فروشگاه : {len(AllProductsInfo)}")
        radif_dict = {}
        productName_dict = {}
        productDetails_dict = {}
        cat_dict = {}
        price_dict = {}
        date_dict = {}
        randomID_dict = {}
        saler_dict = {}
        # btn_delete = {}
        # lbl_delete = {}
        btn_edit = {}
        lbl_edit = {}
        height = 230
        height2 = 240
        index = 0
        for i in AllProductsInfo:
            productID = i[0]
            productName = i[1]
            productDetail = i[2]
            price = i[3]
            date = i[4]
            randomID = i[5]
            salerID = i[6]
            catID = i[7]
            findSalerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
            findCatName = db.CatRepository.GetCatNameById(catID)[0][0]
            # ---- createDynamic ----
            radif_dict[index] = QPushButton(instance)
            radif_dict[index].setText(f"{index}")
            radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            radif_dict[index].setGeometry(1040,height,81,71)
            radif_dict[index].setObjectName(f"showFaveLbl_{productID}")
            # -------
            productName_dict[index] = QPushButton(instance)
            productName_dict[index].setText(f"{productName}")
            productName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            productName_dict[index].setGeometry(920,height,121,71)
            productName_dict[index].setObjectName(f"userName_{productID}")
            # -------
            productDetails_dict[index] = QPushButton(instance)
            productDetails_dict[index].setText(f"... {productDetail[0:20]}")
            productDetails_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            productDetails_dict[index].setGeometry(720,height,201,71)
            productDetails_dict[index].setObjectName(f"Email_{productID}")
            # -------
            cat_dict[index] = QPushButton(instance)
            cat_dict[index].setText(f"{findCatName}")
            cat_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            cat_dict[index].setGeometry(610,height,111,71)
            cat_dict[index].setObjectName(f"Email_{productID}")
            # -------
            price_dict[index] = QPushButton(instance)
            price_dict[index].setText(f"{price}")
            price_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            price_dict[index].setGeometry(520,height,91,71)
            price_dict[index].setObjectName(f"Password_{productID}")
            # -------
            date_dict[index] = QPushButton(instance)
            date_dict[index].setText(f"{date}")
            date_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            date_dict[index].setGeometry(430,height,91,71)
            date_dict[index].setObjectName(f"Date_{productID}")
            # -------
            randomID_dict[index] = QPushButton(instance)
            randomID_dict[index].setText(f"{randomID}")
            randomID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            randomID_dict[index].setGeometry(320,height,111,71)
            randomID_dict[index].setObjectName(f"RandomID{productID}")
            # -------
            saler_dict[index] = QPushButton(instance)
            saler_dict[index].setText(f"{findSalerName}")
            saler_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            saler_dict[index].setGeometry(200,height,121,71)
            saler_dict[index].setObjectName(f"RandomID{productID}")
            # ---create remove icon lbl
            # lbl_delete[index] = QLabel(instance)
            # lbl_delete[index].setGeometry(100,height+10,51,51)
            # lbl_delete[index].setObjectName(f"removeIconLbl_{productID}")
            # img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            # lbl_delete[index].setPixmap(img)
            # # ---create remove icon btn
            # btn_delete[index] = QPushButton(instance)
            # btn_delete[index].setGeometry(100,height+10,51,51)
            # btn_delete[index].setObjectName(f"removeIconbtn_{productID}")
            # btn_delete[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            # btn_delete[index].setCursor(Qt.PointingHandCursor)
            # ---create edit icon lbl
            lbl_edit[index] = QLabel(instance)
            lbl_edit[index].setGeometry(150,height+10,51,51)
            lbl_edit[index].setObjectName(f"editIconLbl_{productID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            lbl_edit[index].setPixmap(img)
            # ---create edit icon btn
            btn_edit[index] = QPushButton(instance)
            btn_edit[index].setGeometry(150,height+10,51,51)
            btn_edit[index].setObjectName(f"editIconbtn_{productID}")
            btn_edit[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            btn_edit[index].setCursor(Qt.PointingHandCursor)
            # ------
            height += 70
            height2 += 70
            index += 1
            
        # num = len(btn_delete)
        # for i in range(num,20):
        #     btn_delete[i] = QPushButton(instance)
        #     btn_delete[i].setHidden(True)
            
        num = len(btn_edit)
        for i in range(num,20):
            btn_edit[i] = QPushButton(instance)
            btn_edit[i].setHidden(True)
            
        #  btn_delete click functions
        # btn_delete[0].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_delete[0].objectName()))

        #  btn_edit click functions
        btn_edit[0].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[0].objectName()))
        btn_edit[1].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[1].objectName()))
        btn_edit[2].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[2].objectName()))
        btn_edit[3].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[3].objectName()))
        btn_edit[4].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[4].objectName()))
        btn_edit[5].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[5].objectName()))
        btn_edit[6].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[6].objectName()))
        btn_edit[7].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[7].objectName()))
        btn_edit[8].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[8].objectName()))
        btn_edit[9].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[9].objectName()))
        btn_edit[10].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[10].objectName()))
    
    def viewDiscountCode(self):
        pass
    
    def viewCatDetailsUI(self,instance):
        mainCat_dict = {}
        subCat_dict = {}
        edit_lbl = {}
        edit_btn = {}
        main_width = 700
        main_height = 20
        sub_width = 620
        index = 0
        getMainCats = db.CatRepository.getMainCats()
        for main in getMainCats:
            if(main_width < 0 ):
                main_width = 700
                sub_width = 620
                main_height += 290
            sub_height = main_height + 40
            mainCatID = main[0]
            findMainCatName = db.CatRepository.GetCatNameById(mainCatID)[0][0]
            # ---- create main cat lbl ----
            mainCat_dict[index] = QLabel(instance)
            mainCat_dict[index].setText(f"{findMainCatName}")
            mainCat_dict[index].setStyleSheet("QLabel {font: 15pt 'B Koodak';}")
            mainCat_dict[index].setGeometry(main_width,main_height,161,41)
            mainCat_dict[index].setObjectName(f"mainCat_{mainCatID}")
            
            # ---- ceate edit lbl ----
            edit_lbl[index] = QLabel(instance)
            edit_lbl[index].setGeometry(main_width+170,main_height,51,41)
            edit_lbl[index].setObjectName(f"editlbl_{mainCatID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            edit_lbl[index].setPixmap(img)
            # ---- ceate edit btn ----
            edit_btn[index] = QPushButton(instance)
            edit_btn[index].setGeometry(main_width+170,main_height,51,41)
            edit_btn[index].setObjectName(f"editbtn_{mainCatID}")
            edit_btn[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            edit_btn[index].setCursor(Qt.PointingHandCursor)
            
            
            # ---- find and create subcats ----
            getSubCats = db.CatRepository.GetAllSubCatbyID(mainCatID)
            for sub in getSubCats:
                subCatID = sub[0]
                findSubCatName = db.CatRepository.GetCatNameById(subCatID)[0][0]
                subCat_dict[index] = QLabel(instance)
                subCat_dict[index].setText(f"{findSubCatName}")
                subCat_dict[index].setStyleSheet("QLabel {font: 15pt 'B nazanin';}")
                subCat_dict[index].setGeometry(sub_width,sub_height,161,41)
                subCat_dict[index].setObjectName(f"subCat_{mainCatID}")
                sub_height += 40
            main_width -= 300
            sub_width -= 300
            index += 1
            
        num = len(edit_btn)
        for i in range(num,20):
            edit_btn[i] = QPushButton(instance)
            edit_btn[i].setHidden(True)
        
        edit_btn[0].clicked.connect(lambda: instance.openEditCatUI(edit_btn[0].objectName()))
        edit_btn[1].clicked.connect(lambda: instance.openEditCatUI(edit_btn[1].objectName()))
        edit_btn[2].clicked.connect(lambda: instance.openEditCatUI(edit_btn[2].objectName()))
        edit_btn[3].clicked.connect(lambda: instance.openEditCatUI(edit_btn[3].objectName()))
        edit_btn[4].clicked.connect(lambda: instance.openEditCatUI(edit_btn[4].objectName()))
        edit_btn[5].clicked.connect(lambda: instance.openEditCatUI(edit_btn[5].objectName()))
        edit_btn[6].clicked.connect(lambda: instance.openEditCatUI(edit_btn[6].objectName()))
        edit_btn[7].clicked.connect(lambda: instance.openEditCatUI(edit_btn[7].objectName()))
        edit_btn[8].clicked.connect(lambda: instance.openEditCatUI(edit_btn[8].objectName()))
        edit_btn[9].clicked.connect(lambda: instance.openEditCatUI(edit_btn[9].objectName()))
        edit_btn[10].clicked.connect(lambda: instance.openEditCatUI(edit_btn[10].objectName()))
                    
    def editCatDetails(self,mainCatID,instance):
        findMainCatName = db.CatRepository.GetCatNameById(mainCatID)[0][0]
        subCatlbl_dict = {}
        instance.subCatInput_dict = {}
        removeIconlbl_dict = {}
        removeIconbtn_dict = {}
        index = 0
        height = 100
        # create subcat
        findAllSubcats = db.CatRepository.GetAllSubCatbyID(mainCatID)
        for s in findAllSubcats:
            subcatID = s[0]
            # --- create subCat_lbl ----
            subCatlbl_dict[index] = QLabel(instance)
            subCatlbl_dict[index].setGeometry(900,height,121,41)
            subCatlbl_dict[index].setObjectName(f"subcatlbl_{subcatID}")
            subCatlbl_dict[index].setText(f"زیر شاخه {index+1} : ")
            subCatlbl_dict[index].setStyleSheet("QLabel {font: 15pt 'B nazanin';}")
            # --- create subCat_btn ----
            findSubCatName = db.CatRepository.GetCatNameById(subcatID)[0][0]
            instance.subCatInput_dict[index] = QLineEdit(instance)
            instance.subCatInput_dict[index].setGeometry(540,height,301,51)
            instance.subCatInput_dict[index].setObjectName(f"CatInput_{subcatID}")
            instance.subCatInput_dict[index].setStyleSheet("QLineEdit { border : 1px solid #b1afaf; border-radius : 10%;font: 12pt 'Century Gothic';} QLineEdit:focus {border : 1px solid #df2569;}")
            instance.subCatInput_dict[index].setText(findSubCatName)
            # ---create remove icon lbl
            removeIconlbl_dict[index] = QLabel(instance)
            removeIconlbl_dict[index].setGeometry(460,height,51,51)
            removeIconlbl_dict[index].setObjectName(f"removeIconLbl_{subcatID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            removeIconlbl_dict[index].setPixmap(img)
            # ---create remove icon btn
            removeIconbtn_dict[index] = QPushButton(instance)
            removeIconbtn_dict[index].setGeometry(460,height,51,51)
            removeIconbtn_dict[index].setObjectName(f"removeIconbtn_{subcatID}")
            removeIconbtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            removeIconbtn_dict[index].setCursor(Qt.PointingHandCursor)
            # -------
            index += 1
            height += 70
            
        # ---- create mainCat_input ----
        instance.subCatInput_dict[index] = QLineEdit(instance)
        instance.subCatInput_dict[index].setGeometry(540,20,301,51)
        instance.subCatInput_dict[index].setObjectName(f"CatInput_{mainCatID}")
        instance.subCatInput_dict[index].setStyleSheet("QLineEdit { border : 1px solid #b1afaf; border-radius : 10%;font: 12pt 'Century Gothic';} QLineEdit:focus {border : 1px solid #df2569;}")
        instance.subCatInput_dict[index].setText(findMainCatName)
        
        # --- crate mainCat_lbl ----
        subCatlbl_dict[index] = QLabel(instance)
        subCatlbl_dict[index].setGeometry(870,20,201,41)
        subCatlbl_dict[index].setObjectName("mainCatLbl")
        subCatlbl_dict[index].setText(f"عنوان شاخه اصلی : ")
        subCatlbl_dict[index].setStyleSheet("QLabel {font: 18pt 'B Koodak';}")
        height = 110
                    
        num = len(removeIconbtn_dict)
        for i in range(num,20):
            removeIconbtn_dict[i] = QPushButton(instance)
            removeIconbtn_dict[i].setHidden(True)
            
        
        removeIconbtn_dict[0].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[0].objectName()))
        removeIconbtn_dict[1].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[1].objectName()))
        removeIconbtn_dict[2].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[2].objectName()))
        removeIconbtn_dict[3].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[3].objectName()))
        removeIconbtn_dict[4].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[4].objectName()))
        removeIconbtn_dict[5].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[5].objectName()))
        removeIconbtn_dict[6].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[6].objectName()))
        removeIconbtn_dict[7].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[7].objectName()))
        removeIconbtn_dict[8].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[8].objectName()))
        removeIconbtn_dict[9].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[9].objectName()))
        removeIconbtn_dict[10].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[10].objectName()))
        
    def confirmEditcat(self,instance):
        num = len(instance.subCatInput_dict)
        for i in range(num):
            findInput_objName = instance.subCatInput_dict[i].objectName()
            findInputID = findInput_objName.split("_")[1]
            findInputText = instance.subCatInput_dict[i].text()
            newCat = catTable(findInputID,findInputText)
            db.CatRepository.Update(newCat)
            db.CatRepository.Save()
        return True
            
    def addNewSubCat(self,mainCatID,instance):
        getInputText = instance.addNewSubCat_input.text()     
        if(getInputText == ""):
            instance.wrong_lbl.setHidden(False)
        else:
            instance.wrong_lbl.setHidden(True)
            newCat = catTable(mainCatID,getInputText)
            db.CatRepository.createSubCat(newCat)
            db.CatRepository.Save()
            return True
    
    def removeSubCat(self,subcatID):
        db.CatRepository.Delete(subcatID)  
        db.CatRepository.Save()
        return True

    def addNewMainCat(self,instance):
        getInputText = instance.addNewSubCat_input.text()     
        if(getInputText == ""):
            instance.wrong_lbl.setHidden(False)
        else:
            instance.wrong_lbl.setHidden(True)
            newCat = catTable(0,getInputText)
            db.CatRepository.CreateMainCat(newCat)
            db.CatRepository.Save()
            return True
         
    def removeMainCat(self,mainID):
        getAllSubCat = db.CatRepository.GetAllSubCatbyID(mainID)
        for i in getAllSubCat:
            subCatID = i[0]
            db.CatRepository.Delete(subCatID)
        db.CatRepository.Delete(mainID)
        db.CatRepository.Save()
        return True 
            
    def ViewOperatorDetails(self,ID,instance):
        findAllOperatorDetails = db.OperatorRepository.GetByID(ID)
        for detail in findAllOperatorDetails:
            userName = detail[1]
            email = detail[2]
            password = detail[3]
            randomID = detail[4]
            date = detail[5]
        instance.viewAc.show_userName.setText(f"{userName}")
        instance.viewAc.show_email.setText(f"{email}")
        instance.viewAc.show_password.setText(f"{password}")
        instance.viewAc.show_date.setText(f"{date}")
        instance.viewAc.show_randomID.setText(f"{randomID}")
        
    def EditOperatorInformation(self,OperatorID,userName,email,oldPass,dbPass,newPass,instance):
        findAllUserInfo = db.OperatorRepository.GetByID(OperatorID)
        validation = editValid(oldPass,dbPass,newPass).operatorValidate()
        if(validation == 0):
            instance.viewAc.wrongOldPass_lbl.setHidden(False)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 1):
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(False)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 2):
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(False)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 3):
            # successful edit user info
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(False)
            updateOperator = operatorTabels(userName,email,newPass,findAllUserInfo[0][4],findAllUserInfo[0][5])
            db.OperatorRepository.Update(updateOperator,OperatorID)
            db.OperatorRepository.Save()
            return True
         
    def EditProductDetails(self,productID,instance):
        productName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
        productPrice = db.ProductsRepository.GetPriceByID(productID)[0][0]
        productDate = db.ProductsRepository.GetDateByID(productID)[0][0]
        productRandomID = db.ProductsRepository.GetRandomID(productID)[0][0]
        productDetails = db.ProductsRepository.GetDetailsByID(productID)[0][0]
        salerID = db.ProductsRepository.GetSalerIDByID(productID)[0][0]
        salerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
        catID = db.ProductsRepository.GetCatIDByID(productID)[0][0]
        catName = db.CatRepository.GetCatNameById(catID)[0][0]
        findAllSalerName = db.SalerRepository.GetAll()
        findAllSubCats = db.CatRepository.GetAllSubCats()
        
        instance.viewEditProductUI.productName_input.setText(f"{productName}")
        instance.viewEditProductUI.productPrice_input.setText(f"{productPrice}")
        instance.viewEditProductUI.productDate_input.setText(f"{productDate}")
        instance.viewEditProductUI.productRandomID_input.setText(f"{productRandomID}")
        instance.viewEditProductUI.productDetails_input.setPlainText(f"{productDetails}")
        instance.viewEditProductUI.salerName_lbl.setText(f"{salerName}")
        instance.viewEditProductUI.catName_lbl.setText(f"{catName}")
        for saler in findAllSalerName:
            salerName = saler[1]
            instance.viewEditProductUI.saler_comboBox.addItem(salerName)
        for subCats in findAllSubCats:
            catName = subCats[2]
            instance.viewEditProductUI.cat_comboBox.addItem(catName)
            
    def ConfrimEditProduct(self,productID,instance):
        getProductName = instance.productName_input.text()
        getProductDetails = instance.productDetails_input.toPlainText()
        getProductPrice = instance.productPrice_input.text()
        getProductDate = instance.productDate_input.text()
        getProductRandomID = instance.productRandomID_input.text()
        getProductSalerName = instance.saler_comboBox.currentText()
        getProductCatName = instance.cat_comboBox.currentText()
        
        findSalerID = db.SalerRepository.GetSalerIDByName(getProductSalerName)[0][0]
            
        findCatId = db.CatRepository.GetCatIDByName(getProductCatName)[0][0]
            
        newProduct = productTable(getProductName,getProductDetails,getProductPrice,getProductDate,getProductRandomID,findSalerID,findCatId)
        db.ProductsRepository.Update(newProduct,productID)
        db.ProductsRepository.Save()
        
        return True
    
    def ConfirmUserShopCart(self,instance):
        getAllNotConfirmOrders = db.OperatorConfirmOrderRepository.GetAllNotConfirm()
        radif_dict = {}
        nameAndFamily_dict = {}
        userName_dict = {}
        orderID_dict = {}
        totalPrice_dict = {}
        confirmStatus_lbl = {}
        confirmStatus_btn = {}
        ignoreStatus_lbl = {}
        ignoreStatus_btn = {}
        index = 0
        height = 230
        if(getAllNotConfirmOrders != []):
            for i in getAllNotConfirmOrders:
                userID =i[1]
                buyID = i[2]
                status = i[3]
                findName = db.UserPaymentRepository.GetNameByUserAndBuyID(userID,buyID)[0][0]
                findFamily = db.UserPaymentRepository.GetFamilyByUserAndBuyID(userID,buyID)[0][0]
                findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
                findTotalPrice = db.UserPaymentRepository.GetTotalPriceByUserAndBuyID(userID,buyID)[0][0]
                # ---radif_btn
                radif_dict[index] = QPushButton(instance)
                radif_dict[index].setText(f"{index}")
                radif_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                radif_dict[index].setGeometry(820,height,81,71)
                radif_dict[index].setObjectName(f"radift_{userID}|{buyID}")
                # ---nameAndFamily_btn
                nameAndFamily_dict[index] = QPushButton(instance)
                nameAndFamily_dict[index].setText(f"{findName} {findFamily}")
                nameAndFamily_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                nameAndFamily_dict[index].setGeometry(700,height,121,71)
                nameAndFamily_dict[index].setObjectName(f"nameAndFamily_{userID}|{buyID}")
                # ---userName_btn
                userName_dict[index] = QPushButton(instance)
                userName_dict[index].setText(f"{findUserName}")
                userName_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                userName_dict[index].setGeometry(580,height,121,71)
                userName_dict[index].setObjectName(f"userName_{userID}|{buyID}")
                # ---orderID_btn
                orderID_dict[index] = QPushButton(instance)
                orderID_dict[index].setText(f"{buyID}")
                orderID_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                orderID_dict[index].setGeometry(450,height,131,71)
                orderID_dict[index].setObjectName(f"orderID_{userID}|{buyID}")
                # ---orderID_btn
                totalPrice_dict[index] = QPushButton(instance)
                totalPrice_dict[index].setText(f"{findTotalPrice}")
                totalPrice_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                totalPrice_dict[index].setGeometry(320,height,131,71)
                totalPrice_dict[index].setObjectName(f"totalPrice_{userID}|{buyID}")
                # ---confirmStatus_lbl
                confirmStatus_lbl[index] = QLabel(instance)
                confirmStatus_lbl[index].setGeometry(260,height+10,51,51)
                confirmStatus_lbl[index].setObjectName(f"confirmlbl_{userID}|{buyID}")
                img = QPixmap(os.getcwd()+"\\Tools\\imgs\\confirmIcon.jpg")
                confirmStatus_lbl[index].setPixmap(img)
                # ---confirmStatus_btn
                confirmStatus_btn[index] = QPushButton(instance)
                confirmStatus_btn[index].setGeometry(260,height+10,51,51)
                confirmStatus_btn[index].setObjectName(f"confirmbtn_{userID}|{buyID}")
                confirmStatus_btn[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
                confirmStatus_btn[index].setCursor(Qt.PointingHandCursor)
                # ---ignoreStatus_lbl
                ignoreStatus_lbl[index] = QLabel(instance)
                ignoreStatus_lbl[index].setGeometry(200,height+10,51,51)
                ignoreStatus_lbl[index].setObjectName(f"ignorelbl_{userID}|{buyID}")
                img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
                ignoreStatus_lbl[index].setPixmap(img)
                # ---ignoreStatus_btn
                ignoreStatus_btn[index] = QPushButton(instance)
                ignoreStatus_btn[index].setGeometry(200,height+10,51,51)
                ignoreStatus_btn[index].setObjectName(f"ignorebtn_{userID}|{buyID}")
                ignoreStatus_btn[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
                ignoreStatus_btn[index].setCursor(Qt.PointingHandCursor)
                # ----
                index += 1
                height += 70
                
            num = len(confirmStatus_btn)
            for i in range(num,20):
                confirmStatus_btn[i] = QPushButton(instance)
                confirmStatus_btn[i].setHidden(True)
                
            num = len(ignoreStatus_btn)
            for i in range(num,20):
                ignoreStatus_btn[i] = QPushButton(instance)
                ignoreStatus_btn[i].setHidden(True)
                
            confirmStatus_btn[0].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[0].objectName()))
            confirmStatus_btn[1].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[1].objectName()))
            confirmStatus_btn[2].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[2].objectName()))
            confirmStatus_btn[3].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[3].objectName()))
            confirmStatus_btn[4].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[4].objectName()))
            confirmStatus_btn[5].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[5].objectName()))
            confirmStatus_btn[6].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[6].objectName()))
            confirmStatus_btn[7].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[7].objectName()))
            confirmStatus_btn[8].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[8].objectName()))
            confirmStatus_btn[9].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[9].objectName()))
            confirmStatus_btn[10].clicked.connect(lambda: instance.goToConfrimOrder(confirmStatus_btn[10].objectName()))
            
            ignoreStatus_btn[0].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[0].objectName()))
            ignoreStatus_btn[1].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[1].objectName()))
            ignoreStatus_btn[2].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[2].objectName()))
            ignoreStatus_btn[3].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[3].objectName()))
            ignoreStatus_btn[4].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[4].objectName()))
            ignoreStatus_btn[5].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[5].objectName()))
            ignoreStatus_btn[6].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[6].objectName()))
            ignoreStatus_btn[7].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[7].objectName()))
            ignoreStatus_btn[8].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[8].objectName()))
            ignoreStatus_btn[9].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[9].objectName()))
            ignoreStatus_btn[10].clicked.connect(lambda: instance.goToIgnoreOrder(ignoreStatus_btn[10].objectName()))
    
        else:
            # --->notOrderYet!
            notOrderYet = QPushButton(instance)
            notOrderYet.setText("هنوز سفارش جدیدی ثبت نشده است")
            notOrderYet.setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
            notOrderYet.setGeometry(110,240,911,501)
            notOrderYet.setObjectName(f"notOrderYet")
        
    def ConfrimDeleteUser(self,userID):
        findAllUserInfo = db.userRepository.GetByID(userID)
        userName = findAllUserInfo[0][1]
        email = findAllUserInfo[0][2]
        password = findAllUserInfo[0][3]
        date = findAllUserInfo[0][4]
        randomID = findAllUserInfo[0][5]
        newUser = userTable(userName,email,password,date,randomID)
        db.userRepository.Delete(newUser,userID)
        db.userRepository.Save()
        return True
    
    def goToSendOrder(self,userID,buyID):
        # Update status to 1
        db.OperatorConfirmOrderRepository.UpdateConfrimOrder(userID,buyID)
        db.OperatorConfirmOrderRepository.Save()
        return True
        
    def goToIgnoreOrder(self,userID,buyID):
        # Update Status to 2
        db.OperatorConfirmOrderRepository.UpdateIgnoreOrder(userID,buyID)
        db.OperatorConfirmOrderRepository.Save()
        # ---------
        findTotalPrice = db.UserPaymentRepository.GetTotalPriceByUserAndBuyID(userID,buyID)[0][0]
        findUserBalance = db.userBalanceRepository.GetBalance(userID)[0][0]
        # --------
        # restore Balance
        RestoreBalance = findTotalPrice + findUserBalance
                
        db.userBalanceRepository.UpdateWithOutInstance(userID,RestoreBalance)
        db.userBalanceRepository.Save()
        return True
    
    def viewDiscountUI(self,instance):
        getAllOffers = db.OffersRepository.GetAll()
        OfferName_dict = {}
        discount_dict = {}
        editlbl_dict = {}
        editbtn_dict = {}
        deletelbl_dict = {}
        deletebtn_dict = {}
        index = 0
        height = 140
        for i in getAllOffers[1:]:
            id = i[0]
            name = i[1]
            discount = i[2]
            
            # --- offerName
            OfferName_dict[index] = QLabel(instance)
            OfferName_dict[index].setText(f"کد تخفیف : {name}")
            OfferName_dict[index].setStyleSheet("QLabel { font: 15pt 'B Nazanin';}")
            OfferName_dict[index].setGeometry(390,height,181,51)
            OfferName_dict[index].setObjectName(f"offerName_{id}")
            # --- discount
            discount_dict[index] = QLabel(instance)
            discount_dict[index].setText(f"مقدار تخفیف : {discount} درصد")
            discount_dict[index].setStyleSheet("QLabel { font: 15pt 'B Nazanin';}")
            discount_dict[index].setGeometry(160,height,201,51)
            discount_dict[index].setObjectName(f"discount_{id}")
            # --- edit_lbl
            editlbl_dict[index] = QLabel(instance)
            editlbl_dict[index].setGeometry(90,height,51,51)
            editlbl_dict[index].setObjectName(f"editlbl_{id}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            editlbl_dict[index].setPixmap(img)
            # ---edit_btn
            editbtn_dict[index] = QPushButton(instance)
            editbtn_dict[index].setGeometry(90,height,51,51)
            editbtn_dict[index].setObjectName(f"editbtn_{id}")
            editbtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            editbtn_dict[index].setCursor(Qt.PointingHandCursor)
            # --- delete_lbl
            deletelbl_dict[index] = QLabel(instance)
            deletelbl_dict[index].setGeometry(30,height,51,51)
            deletelbl_dict[index].setObjectName(f"deletelbl_{id}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            deletelbl_dict[index].setPixmap(img)
            # ---delete_btn
            deletebtn_dict[index] = QPushButton(instance)
            deletebtn_dict[index].setGeometry(30,height,51,51)
            deletebtn_dict[index].setObjectName(f"deletebtn_{id}")
            deletebtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            deletebtn_dict[index].setCursor(Qt.PointingHandCursor)
            # -----
            index += 1
            height += 60
            
        num = len(editbtn_dict)
        for i in range(num,20):
            editbtn_dict[i] = QPushButton(instance)
            editbtn_dict[i].setHidden(True)  
            
        num = len(deletebtn_dict)
        for i in range(num,20):
            deletebtn_dict[i] = QPushButton(instance)
            deletebtn_dict[i].setHidden(True)
            

            
        editbtn_dict[0].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[0].objectName()))
        editbtn_dict[1].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[1].objectName()))
        editbtn_dict[2].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[2].objectName()))
        editbtn_dict[3].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[3].objectName()))
        editbtn_dict[4].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[4].objectName()))
        editbtn_dict[5].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[5].objectName()))
        editbtn_dict[6].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[6].objectName()))
        editbtn_dict[7].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[7].objectName()))
        editbtn_dict[8].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[8].objectName()))
        editbtn_dict[9].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[9].objectName()))
        editbtn_dict[10].clicked.connect(lambda: instance.goToEditOffer(editbtn_dict[10].objectName()))

        deletebtn_dict[0].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[0].objectName()))
        deletebtn_dict[1].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[1].objectName()))
        deletebtn_dict[2].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[2].objectName()))
        deletebtn_dict[3].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[3].objectName()))
        deletebtn_dict[4].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[4].objectName()))
        deletebtn_dict[5].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[5].objectName()))
        deletebtn_dict[6].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[6].objectName()))
        deletebtn_dict[7].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[7].objectName()))
        deletebtn_dict[8].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[8].objectName()))
        deletebtn_dict[9].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[9].objectName()))
        deletebtn_dict[10].clicked.connect(lambda: instance.goToDeleteOffer(deletebtn_dict[10].objectName()))
    
    def ConfirmEditOffer(self,offerID,instance):
        getOfferText = instance.offer_input.text()
        getOfferdiscount = instance.discount_input.text()
        db.OffersRepository.Update(offerID,getOfferText,getOfferdiscount)
        db.OffersRepository.Save()
        return True
    
    def AddNewOffer(self,instance):
        offName = instance.offer_input.text()
        discount = instance.discount_input.text()
        if(offName != "" and discount != ""):
            db.OffersRepository.Create(offName,discount)
            db.OffersRepository.Save()
            return True
        else:
            return False
        
    def ViewSalersUI(self,instance):
        getAllSalers = db.SalerRepository.GetAll()
        salerName_dict = {}
        randomID_dict = {}
        editlbl_dict = {}
        editbtn_dict = {}
        deletelbl_dict = {}
        deletebtn_dict = {}
        index = 0
        height = 140
        for i in getAllSalers:
            id = i[0]
            name = i[1]
            randomID = i[2]
            
            # --- offerName
            salerName_dict[index] = QLabel(instance)
            salerName_dict[index].setText(f"نام: {name}")
            salerName_dict[index].setStyleSheet("QLabel { font: 14pt 'B Nazanin';}")
            salerName_dict[index].setGeometry(390,height,181,51)
            salerName_dict[index].setObjectName(f"offerName_{id}")
            # --- discount
            randomID_dict[index] = QLabel(instance)
            randomID_dict[index].setText(f"شناسه : {randomID}")
            randomID_dict[index].setStyleSheet("QLabel { font: 14pt 'B Nazanin';}")
            randomID_dict[index].setGeometry(160,height,201,51)
            randomID_dict[index].setObjectName(f"discount_{id}")
            # --- edit_lbl
            editlbl_dict[index] = QLabel(instance)
            editlbl_dict[index].setGeometry(90,height,51,51)
            editlbl_dict[index].setObjectName(f"editlbl_{id}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            editlbl_dict[index].setPixmap(img)
            # ---edit_btn
            editbtn_dict[index] = QPushButton(instance)
            editbtn_dict[index].setGeometry(90,height,51,51)
            editbtn_dict[index].setObjectName(f"editbtn_{id}")
            editbtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            editbtn_dict[index].setCursor(Qt.PointingHandCursor)
            # --- delete_lbl
            deletelbl_dict[index] = QLabel(instance)
            deletelbl_dict[index].setGeometry(30,height,51,51)
            deletelbl_dict[index].setObjectName(f"deletelbl_{id}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            deletelbl_dict[index].setPixmap(img)
            # ---delete_btn
            deletebtn_dict[index] = QPushButton(instance)
            deletebtn_dict[index].setGeometry(30,height,51,51)
            deletebtn_dict[index].setObjectName(f"deletebtn_{id}")
            deletebtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            deletebtn_dict[index].setCursor(Qt.PointingHandCursor)
            # -----
            index += 1
            height += 60
            
        num = len(editbtn_dict)
        for i in range(num,20):
            editbtn_dict[i] = QPushButton(instance)
            editbtn_dict[i].setHidden(True)  
            
        num = len(deletebtn_dict)
        for i in range(num,20):
            deletebtn_dict[i] = QPushButton(instance)
            deletebtn_dict[i].setHidden(True)
            

            
        editbtn_dict[0].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[0].objectName()))
        editbtn_dict[1].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[1].objectName()))
        editbtn_dict[2].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[2].objectName()))
        editbtn_dict[3].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[3].objectName()))
        editbtn_dict[4].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[4].objectName()))
        editbtn_dict[5].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[5].objectName()))
        editbtn_dict[6].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[6].objectName()))
        editbtn_dict[7].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[7].objectName()))
        editbtn_dict[8].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[8].objectName()))
        editbtn_dict[9].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[9].objectName()))
        editbtn_dict[10].clicked.connect(lambda: instance.goToEditSaler(editbtn_dict[10].objectName()))
        
        deletebtn_dict[0].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[0].objectName()))
        deletebtn_dict[1].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[1].objectName()))
        deletebtn_dict[2].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[2].objectName()))
        deletebtn_dict[3].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[3].objectName()))
        deletebtn_dict[4].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[4].objectName()))
        deletebtn_dict[5].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[5].objectName()))
        deletebtn_dict[6].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[6].objectName()))
        deletebtn_dict[7].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[7].objectName()))
        deletebtn_dict[8].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[8].objectName()))
        deletebtn_dict[9].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[9].objectName()))
        deletebtn_dict[10].clicked.connect(lambda: instance.goToDeleteSaler(deletebtn_dict[10].objectName()))
        
    def ConfirmEditSaler(self,salerID,instance):
        getSalerNameText = instance.salerName_input.text()
        getSalerRandomIDText = instance.randomID_input.text()
        db.SalerRepository.UpdateWithOutInstance(salerID,getSalerNameText,getSalerRandomIDText)
        db.SalerRepository.Save()
        return True
    
    def AddNewSaler(self,instance):
        salerName = instance.salerName_input.text()
        numbers_list = [0,1,2,3,4,5,6,7,8,9]
        random_list = []
        for i in range(6):
            random_list.append(f"{random.choice(numbers_list)}")
        randomID = "SL"+"".join(random_list)
        if(salerName != ""):
            db.SalerRepository.CreateWithOutInstance(salerName,randomID)
            db.SalerRepository.Save()
            return True
        else:
            return False
        
    def DeleteSaler(self,salerID):
        findProduct = db.ProductsRepository.GetAllBySalerID(salerID)
        if(findProduct == []):
            findOrderinShopCartAfterPeyment = db.ShopCartAfterPeymentRepository.GetAllBySalerID(salerID)
            if(findOrderinShopCartAfterPeyment == []):
                db.SalerRepository.DeleteWithOutInstance(salerID)
                db.SalerRepository.Save()
                return 2
            else:
                return 1
        else:
            return 0
    
    