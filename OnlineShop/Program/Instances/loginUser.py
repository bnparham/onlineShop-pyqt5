import sys,os
sys.path.append('../onlineShop')
from datetime import datetime

from DataLayer.Services.UserRepository import UserRepository
from Tools.Validations.editValid import editValid
from Tools.Validations.accountBalanceValid import accountBalanceValid
from Tools.Validations.commentValid import commentValid
from Tools.Validations.shopCartValid import shopCartValid
from Tools.Validations.userPeymentValidation import userPeymentValidation

from DataLayer.Tables.usersTable import userTable
from DataLayer.Tables.users_balanceTable import users_balanceTable
from DataLayer.Tables.commentTable import commentTable
from DataLayer.Tables.favoritListTable import favoritListTable
from DataLayer.Tables.shopCartTable import shopCartTable
from DataLayer.Tables.users_balanceTable import users_balanceTable
from DataLayer.Tables.shopCartAfterPeymentTable import shopCartAfterPeymentTable
from DataLayer.Tables.userPaymentTable import userPaymentTable

from Program.Instances.product import Product

from PyQt5.QtWidgets import QLabel , QPushButton
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon, QPixmap

from DataLayer.Context.UnitOfWork import context

db = context()

class LoginUser:
    def __init__(self,userID):
        self.userID = userID
        self.GetAlluserInfo = db.userRepository.GetByID(self.userID)
        
    def SeeUserPanel(self,userName,email,password,date,randomID,balance):
        userName.setText(self.GetAlluserInfo[0][1])  
        email.setText(self.GetAlluserInfo[0][2])  
        password.setText(self.GetAlluserInfo[0][3])
        date.setText(self.GetAlluserInfo[0][4])
        randomID.setText(self.GetAlluserInfo[0][5])
        self.get_balanceAmount = db.userBalanceRepository.GetBalance(self.userID)
        if(self.get_balanceAmount != []):
            balance.setText(f"{self.get_balanceAmount[0][0]}")
        else:
            balance.setText("0")
            
    def LoggedOut(self):
        pass
    
    def AddComment(self,productID,commentText,**keyargs):
        validation = commentValid(commentText).valid()
        if(validation == 0):
            keyargs["WarningComment_lbl"].setHidden(False)
        else:
            newComment = commentTable(self.userID,productID,commentText)
            db.AllcommentsRepository.Create(newComment)
            db.AllcommentsRepository.Save()
            return True
     
    def ViewComment(self,instance):
        findAllComments = db.AllcommentsRepository.GetAllByUserID(self.userID)
        productName_btn = {}
        userComment_btn = {}
        delete_icon = {}
        delete_btn = {}
        height = 130
        height2 = 140
        index = 0
        if(findAllComments == []):
           noCommentBtn = QPushButton(instance)
           noCommentBtn.setText("هیچ نظری ثبت نشده است")
           noCommentBtn.setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;font: 22pt 'B Nazanin';}")
           noCommentBtn.setGeometry(70,210,441,411)
           noCommentBtn.setObjectName(f"noCommentBtn")
        else:
            for i in findAllComments:
                productID = i[1]
                findProductName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
                comment = i[3]
                # --->userName
                productName_btn[index] = QPushButton(instance)
                productName_btn[index].setText(f"برای {findProductName}")
                productName_btn[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;font: 12pt 'B Nazanin';}")
                productName_btn[index].setGeometry(430,height,141,61)
                productName_btn[index].setObjectName(f"userName_{productID}")
                # ---->userComment
                userComment_btn[index] = QLabel(instance)
                userComment_btn[index].setText(comment)
                userComment_btn[index].setWordWrap(True)
                userComment_btn[index].setStyleSheet("QLabel {font: 14pt 'B Nazanin';}")
                userComment_btn[index].setGeometry(10,height,401,81)
                userComment_btn[index].setObjectName(f"userComment_{productID}")
                # ---->userDeleteComment_icon
                delete_icon[index] = QLabel(instance)
                delete_icon[index].setGeometry(580,height2,51,41)
                delete_icon[index].setObjectName(f"userDeleteCommentIcon_{productID}")
                img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
                delete_icon[index].setPixmap(img)
                # ---->userDeleteComment_btn
                delete_btn[index] = QPushButton(instance)
                delete_btn[index].setGeometry(580,height2,51,41)
                delete_btn[index].setObjectName(f"userDeleteCommentBtn_{productID}")
                delete_btn[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
                delete_btn[index].setCursor(Qt.PointingHandCursor)
                
                # -----
                index += 1
                height += 110
                height2 += 110
           
        # --- add refreshBtnToThisUI ---
            refresh_lbl = QLabel(instance)
            refresh_lbl.setGeometry(10,30,51,51)
            refresh_lbl.setObjectName(f"refresh_lbl")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\refresh_btn.jpg")
            refresh_lbl.setPixmap(img)
            # ---
            refresh_btn = QPushButton(instance)
            refresh_btn.setGeometry(10,30,51,51)
            refresh_btn.setObjectName(f"refreh_btn")
            refresh_btn.setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            refresh_btn.setCursor(Qt.PointingHandCursor)
            refresh_btn.clicked.connect(lambda x : instance.RefreshUserCommentUI(self.userID))
         
        num = len(delete_btn)
        for i in range(num,20):
            delete_btn[i] = QPushButton(instance)
            delete_btn[i].setHidden(True)
        # deleteFavorit btn click functions
        delete_btn[0].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[0].objectName()))
        delete_btn[1].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[1].objectName()))
        delete_btn[2].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[2].objectName()))
        delete_btn[3].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[3].objectName()))
        delete_btn[4].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[4].objectName()))
        delete_btn[5].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[5].objectName()))
        delete_btn[6].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[6].objectName()))
        delete_btn[7].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[7].objectName()))
        delete_btn[8].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[8].objectName()))
        delete_btn[9].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[9].objectName()))
        delete_btn[10].clicked.connect(lambda: instance.DeleteUserComment(self.userID,delete_btn[10].objectName()))
        
    def DeleteComment(self,productID):
        newComment = commentTable(self.userID,productID,"")
        db.AllcommentsRepository.Delete(newComment)  
        db.AllcommentsRepository.Save()
        return True    
                

    def AddItemToFavorit(self,productID,userID):
        isEqual = False
        checkIfExist= db.FavoritListRepository.GetProductsByID(userID)
        if(checkIfExist != []):
            for f in checkIfExist:
                if(f[1:3] == (userID,productID)):
                    isEqual = True
                    return False
            if(isEqual == False):
                # if product not exist in favorit list add it
                fav = favoritListTable(userID,productID)
                db.FavoritListRepository.Create(fav)
                db.FavoritListRepository.Save()
                return True
        else:
            fav = favoritListTable(userID,productID)
            db.FavoritListRepository.Create(fav)
            db.FavoritListRepository.Save()
            return True
        
    def SeeFavoritList(self,instance):
        user_favorit_list = db.FavoritListRepository.GetProductsByID(self.userID)
        lbl = {}
        btn_del = {}
        btn_dt = {}
        height = 130
        index = 0
        for i in user_favorit_list:
            productID = i[2]
            findProduct_Randomid = db.ProductsRepository.GetRandomID(productID)
            lbl[index] = QLabel(instance)
            lbl[index].setText(f"محصول {findProduct_Randomid[0][0]}")
            lbl[index].setStyleSheet("QLabel { font: 17pt 'B Nazanin';}")
            lbl[index].setGeometry(360,height,221,51)
            lbl[index].setObjectName(f"showFaveLbl_{productID}")
            # -------
            btn_del[index] = QPushButton(instance)
            btn_del[index].setText(f"حذف")
            btn_del[index].setStyleSheet("QPushButton { border-radius : 10%; background-color : #df2569; color : white; font : 12pt 'IRANSans';}")
            btn_del[index].setGeometry(20,height,101,51)
            btn_del[index].setObjectName(f"showDelFaveBtn_{productID}")
            btn_del[index].setCursor(Qt.PointingHandCursor)
            # -------
            btn_dt[index] = QPushButton(instance)
            btn_dt[index].setText("جزئیات")
            btn_dt[index].setStyleSheet("QPushButton { border-radius : 10%; background-color : #df2569; color : white; font : 12pt 'IRANSans';}")
            btn_dt[index].setGeometry(130,height,101,51)
            btn_dt[index].setObjectName(f"showDetailsFaveBtn_{productID}")
            btn_dt[index].setCursor(Qt.PointingHandCursor)
            # ------
            height += 80
            index += 1
            
        num = len(btn_del)
        for i in range(num,20):
            btn_del[i] = QPushButton(instance)
            btn_dt[i] = QPushButton(instance)
            btn_del[i].setHidden(True)
            btn_dt[i].setHidden(True)
        # deleteFavorit btn click functions
        btn_del[0].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[0].objectName()))
        btn_del[1].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[1].objectName()))
        btn_del[2].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[2].objectName()))
        btn_del[3].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[3].objectName()))
        btn_del[4].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[4].objectName()))
        btn_del[5].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[5].objectName()))
        btn_del[6].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[6].objectName()))
        btn_del[7].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[7].objectName()))
        btn_del[8].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[8].objectName()))
        btn_del[9].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[9].objectName()))
        btn_del[10].clicked.connect(lambda: instance.DeleteFromFaveUI(self.userID,btn_del[10].objectName()))
        
        btn_dt[0].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[0].objectName()))
        btn_dt[1].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[1].objectName()))
        btn_dt[2].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[2].objectName()))
        btn_dt[3].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[3].objectName()))
        btn_dt[4].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[4].objectName()))
        btn_dt[5].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[5].objectName()))
        btn_dt[6].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[6].objectName()))
        btn_dt[7].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[7].objectName()))
        btn_dt[8].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[8].objectName()))
        btn_dt[9].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[9].objectName()))
        btn_dt[10].clicked.connect(lambda: instance.DetailsFromFaveUI(self.userID,btn_dt[10].objectName()))
    
    def RemoveItemFromFavorit(self,productID):
        fav = favoritListTable(None,productID)
        db.FavoritListRepository.Delete(fav)
        db.FavoritListRepository.Save()
        return True
    
    def CalculateTotalUserShopCartPrice(self,userShopCart):
        totalPrice = 0
        for i in userShopCart:
            ProductPrice = db.ProductsRepository.GetPriceByID(i[1])[0][0]
            ProductCount = i[4]
            ProductDiscount = db.OffersRepository.GetDiscountBYID(i[5])[0][0]
            priceBeforeOff = ProductPrice * ProductCount
            priceAferOff = int(priceBeforeOff - (priceBeforeOff * ProductDiscount / 100))
            totalPrice += priceAferOff
        return totalPrice
    
    def SeeItemDetailFromFavorit(self,instance,objName):
        productID = objName.split("_")[1]
        instance.veiwProduct.setWindowTitle("مشاهده محصول")
        instance.veiwProduct.viewComments_btn.clicked.connect(lambda x : instance.ViewCommentsUI(productID))   
        instance.veiwProduct.addToFave_btn.setHidden(True)
        instance.veiwProduct.addnewCommnent_lbl.setHidden(True) 
        instance.veiwProduct.addNewComment_btn.setHidden(True) 
        instance.veiwProduct.viewComments_btn.setHidden(True)
        instance.veiwProduct.allComments_lbl.setHidden(True)
        product = Product(productID)
        product.showDetails(instance.veiwProduct.productName_lbl,instance.veiwProduct.show_productID,instance.veiwProduct.show_details,instance.veiwProduct.show_price,instance.veiwProduct.show_date,instance.veiwProduct.show_salerName,instance.veiwProduct.show_cat)  
    
    def AddItemToShopCart(self,product_id,user_id,count,discount,instance):
        validation = shopCartValid(count,discount,db).validate()
        if(validation == 0):
            instance.AddCH.okShopCart_lbl.setHidden(True)
            instance.AddCH.invalidDiscount_lbl.setHidden(True)
            instance.AddCH.wrongJustNumber_lbl.setHidden(True)
            instance.AddCH.atLeastOneItem_lbl.setHidden(False)
        elif(validation == 1):
            instance.AddCH.okShopCart_lbl.setHidden(True)
            instance.AddCH.invalidDiscount_lbl.setHidden(True)
            instance.AddCH.wrongJustNumber_lbl.setHidden(False)
            instance.AddCH.atLeastOneItem_lbl.setHidden(True)
        elif(validation == 2):
            instance.AddCH.okShopCart_lbl.setHidden(True)
            instance.AddCH.invalidDiscount_lbl.setHidden(False)
            instance.AddCH.wrongJustNumber_lbl.setHidden(True)
            instance.AddCH.atLeastOneItem_lbl.setHidden(True)
        elif(validation == 3):
            # successfully added to cart
            instance.AddCH.okShopCart_lbl.setHidden(False)
            instance.AddCH.invalidDiscount_lbl.setHidden(True)
            instance.AddCH.wrongJustNumber_lbl.setHidden(True)
            instance.AddCH.atLeastOneItem_lbl.setHidden(True)
            checkShopCart = db.ShopCartRepository.GetAllByProductID(product_id)
            isEqual = False
            discountID = 1
            if(discount != ""):
                find_DiscountID = db.OffersRepository.GetIdByCode(discount)[0][0]
                discountID = find_DiscountID
            findSalerID = db.ProductsRepository.GetSalerIDByID(product_id)[0][0]
            newShopCart = shopCartTable(product_id,user_id,findSalerID,int(count),discountID)
            if(checkShopCart != []):
                for i in checkShopCart:
                    if((product_id,user_id) == i[1:3]):
                        isEqual = True
                        break
                if(isEqual == False):
                    # print("created!!")
                    db.ShopCartRepository.Create(newShopCart)
                    db.ShopCartRepository.Save()
                    return True
                else:
                    # print("updated!!")
                    find_id = db.ShopCartRepository.GetIDByProductID(product_id)[0][0]
                    db.ShopCartRepository.Update(newShopCart,find_id)
                    db.ShopCartRepository.Save()
                    return True
            else:
                # print("created!!")
                db.ShopCartRepository.Create(newShopCart)
                db.ShopCartRepository.Save()
                return True
    
    def RemoveThisItemFromShopCart(self,userID,productID):
        getAllShopCart = db.ShopCartRepository.GetAllByUserAndProductID(userID,productID)
        for i in getAllShopCart:
            newShopCart = shopCartTable(i[1],i[2],i[3],i[4],i[5])
        db.ShopCartRepository.Delete(newShopCart)
        db.ShopCartRepository.Save()
        return True
    
    def RemoveAllItemsFromShopCart(self,userID):
        user_shopCart_list = db.ShopCartRepository.GetAllByUserID(userID)
        for i in user_shopCart_list:
            newShopCart = shopCartTable(i[1],i[2],i[3],i[4],i[5])
            db.ShopCartRepository.Delete(newShopCart)
            db.ShopCartRepository.Save()
        return True
    
    def SeeUserShopCartPanel(self,instance):
        user_shopCart_list = db.ShopCartRepository.GetAllByUserID(self.userID)
        instance.count_lbl.setText(f"تعداد کالای اضافه شده به سبد : {str(len(user_shopCart_list))}")
        radif_dict = {}
        productName_dict = {}
        productRandomID_dict = {}
        productSalerName_dict = {}
        productPrice_dict = {}
        procudtCount_dict = {}
        productOff_dict = {}
        totalPrice_dict = {}
        totalPriceAfterOff_dict = {}
        btn_del = {}
        height = 250
        btn_height = 270
        index = 0
        self.TotalPriceAfterOff = 0
        if(user_shopCart_list != []):
            for i in user_shopCart_list:
                shopCartID = i[0]
                productID = db.ShopCartRepository.GetProductIDByID(shopCartID)[0][0]
                # || FindProductName ||
                productName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
                # || FindProductRandomID ||
                productRandomID = db.ProductsRepository.GetRandomID(productID)[0][0]
                # || find SalerID and Name ||
                salerID = db.ProductsRepository.GetSalerIDByID(productID)[0][0]
                salerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
                # || find ProductPrice ||
                price = db.ProductsRepository.GetPriceByID(productID)[0][0]
                # || find ProductCount ||
                count = db.ShopCartRepository.GetCountByProductID(productID)[0][0]
                # || find productOff ID and Name||
                offID  = db.ShopCartRepository.GetOffIDByProductID(productID)[0][0]
                offName = db.OffersRepository.GetCodeNameBYID(offID)[0][0]
                if(offName == "None"):
                    offName = "بدون تخفیف"
                offDicsount = db.OffersRepository.GetDiscountBYID(offID)[0][0]
                # offName = "a"
                # offDicsount = 20
                # || calculate Price before off ||
                priceBeforeOff = price * count
                # calculate Price after off
                priceAferOff = int(priceBeforeOff - (priceBeforeOff * offDicsount / 100))
                self.TotalPriceAfterOff += priceAferOff
                # ==== Create buttons ===
                # --->radif
                radif_dict[index] = QPushButton(instance)
                radif_dict[index].setText(str(index))
                radif_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent; text-align:center}")
                radif_dict[index].setGeometry(1040,height,81,71)
                radif_dict[index].setObjectName(f"radif_{productID}")
                # --->productName
                productName_dict[index] = QPushButton(instance)
                productName_dict[index].setText(productName)
                productName_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                productName_dict[index].setGeometry(920,height,121,71)
                productName_dict[index].setObjectName(f"productName_{productID}")
                # --->productRandomID
                productRandomID_dict[index] = QPushButton(instance)
                productRandomID_dict[index].setText(productRandomID)
                productRandomID_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                productRandomID_dict[index].setGeometry(800,height,121,71)
                productRandomID_dict[index].setObjectName(f"productRandomID_{productID}")
                # ---->productSalerName
                productSalerName_dict[index] = QPushButton(instance)
                productSalerName_dict[index].setText(salerName)
                productSalerName_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                productSalerName_dict[index].setGeometry(670,height,131,71)
                productSalerName_dict[index].setObjectName(f"productSalerName_{productID}")
                # --->productPrice
                productPrice_dict[index] = QPushButton(instance)
                productPrice_dict[index].setText(str(price))
                productPrice_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                productPrice_dict[index].setGeometry(540,height,131,71)
                productPrice_dict[index].setObjectName(f"productOff_{productID}")
                # --->productCount
                procudtCount_dict[index] = QPushButton(instance)
                procudtCount_dict[index].setText(str(count))
                procudtCount_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                procudtCount_dict[index].setGeometry(450,height,91,71)
                procudtCount_dict[index].setObjectName(f"procudtCount_{productID}")
                # --->offName
                productOff_dict[index] = QPushButton(instance)
                productOff_dict[index].setText(offName)
                productOff_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                productOff_dict[index].setGeometry(330,height,121,71)
                productOff_dict[index].setObjectName(f"productOff_{productID}")
                # --->totalPrice
                totalPrice_dict[index] = QPushButton(instance)
                totalPrice_dict[index].setText(str(priceBeforeOff))
                totalPrice_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                totalPrice_dict[index].setGeometry(250,height,81,71)
                totalPrice_dict[index].setObjectName(f"totalPrice_{productID}")
                # --->totalPriceAfterOff
                totalPriceAfterOff_dict[index] = QPushButton(instance)
                totalPriceAfterOff_dict[index].setText(str(priceAferOff))
                totalPriceAfterOff_dict[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;text-align:center}")
                totalPriceAfterOff_dict[index].setGeometry(120,height,131,71)
                totalPriceAfterOff_dict[index].setObjectName(f"totalPriceAfterOff_{productID}")
                # --->delete button
                btn_del[index] = QPushButton(instance)
                btn_del[index].setText("حذف این کالا")
                btn_del[index].setStyleSheet("QPushButton { border:none;background-color  : #df2569;color : #fff;font: 8pt 'IRANSans';}")
                btn_del[index].setGeometry(10,btn_height,101,31)
                btn_del[index].setObjectName(f"btndel_{productID}")
                btn_del[index].setCursor(Qt.PointingHandCursor)
                # ----
                height += 70
                btn_height += 70
                index += 1
        else:
            emptybtn = QPushButton(instance)
            emptybtn.setText("سبد خرید شما خالی است")
            emptybtn.setStyleSheet("QPushButton { border:1px solid #000;background-color:transparent;;font: 24pt 'B Nazanin';;}")
            emptybtn.setGeometry(200,340,761,301)
            
            
        num = len(btn_del)
        for i in range(num,20):
            btn_del[i] = QPushButton(instance)
            btn_del[i].setHidden(True)
        btn_del[0].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[0].objectName()))
        btn_del[1].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[1].objectName()))
        btn_del[2].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[2].objectName()))
        btn_del[3].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[3].objectName()))
        btn_del[4].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[4].objectName()))
        btn_del[5].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[5].objectName()))
        btn_del[6].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[6].objectName()))
        btn_del[7].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[7].objectName()))
        btn_del[8].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[8].objectName()))
        btn_del[9].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[9].objectName()))
        btn_del[10].clicked.connect(lambda: instance.OpenDeleteFromShopCartUI(self.userID,btn_del[10].objectName()))
    
    def ConfirmPeyment(self,instance,userID,UserBalance,totalPrice):
        nameInput = instance.name_input.text()
        familyInput = instance.family_input.text()
        mobileInput = instance.mobile_input.text()
        stateInput = instance.state_input.text()
        cityInput = instance.city_input.text()
        addressInput = instance.address_input.toPlainText()
        validation = userPeymentValidation(nameInput,familyInput,mobileInput,stateInput,cityInput,addressInput).validate()
        
        if(validation == 0):
            instance.wrongMobile_lbl.setHidden(True)
            instance.wrongField_lbl.setHidden(False)
            instance.wrongMobileJustNumber_lbl.setHidden(True)
        elif(validation == 1):
            instance.wrongMobile_lbl.setHidden(True)
            instance.wrongField_lbl.setHidden(True)
            instance.wrongMobileJustNumber_lbl.setHidden(False)
        elif(validation == 2):
            instance.wrongMobile_lbl.setHidden(False)
            instance.wrongField_lbl.setHidden(True)
            instance.wrongMobileJustNumber_lbl.setHidden(True)
        else:
            # --- UpdateUserBalance ---
            findUserBalance = db.userBalanceRepository.GetBalance(userID)[0][0]
            NewUserBalance = findUserBalance - totalPrice
            NewUserBalance = users_balanceTable(userID,NewUserBalance)
            db.userBalanceRepository.Update(NewUserBalance)
            db.userBalanceRepository.Save()
            # --- UpdateUserBalance ---
            
            checkUserBuys = db.ShopCartAfterPeymentRepository.GetALLByUserID(userID)
            user_shopCart_list = db.ShopCartRepository.GetAllByUserID(userID)
            # --- create buydID ---
            if(checkUserBuys == []):
                self.buyID = 0
            else:
                self.buyID = db.ShopCartAfterPeymentRepository.GetBuyIDByUserID(userID)[0][0] + 1
            # --- create buydID ---
            
            # --- Add To ShopCart After Peyment Table ---
            for item in user_shopCart_list:
                NewShopCartAfterPey =  shopCartAfterPeymentTable(self.buyID,item[1],item[2],item[3],item[4],item[5])
                db.ShopCartAfterPeymentRepository.Create(NewShopCartAfterPey)
                db.ShopCartAfterPeymentRepository.Save()
            # --- Add To ShopCartAfterPeyment Table ---
            
            # --- Add To this order to operator Panel ---
            db.OperatorConfirmOrderRepository.Create(self.userID,self.buyID)
            db.OperatorConfirmOrderRepository.Save()
            # --- Add To this order to operator Panel ---
            
            # --- save userPayment ---
            newUserPeyment= userPaymentTable(userID,self.buyID,nameInput,familyInput,mobileInput,addressInput,stateInput,cityInput,totalPrice,datetime.date(datetime.now()))
            db.UserPaymentRepository.Create(newUserPeyment)
            db.UserPaymentRepository.Save()
            # --- save userPayment ---       

            # --- clear shopCart ---
            for i in user_shopCart_list:
                newShopCart = shopCartTable(i[1],i[2],i[3],i[4],i[5])
                db.ShopCartRepository.Delete(newShopCart)
            db.ShopCartRepository.Save()
            # --- clear shopCart ---
            return True
    
    def IncreaseAccountBalance(self,balance,**keyargs):
        self.amount = balance.text()
        validation = accountBalanceValid(self.amount).validate()
        if(validation == 0):
            keyargs["wrongEmptyBalance_lbl"].setHidden(False)
            keyargs["okBalance_lbl"].setHidden(True)
            keyargs["wrongJustNumber_lbl"].setHidden(True)
            return False
        elif(validation == 1):
            keyargs["wrongEmptyBalance_lbl"].setHidden(True)
            keyargs["okBalance_lbl"].setHidden(True)
            keyargs["wrongJustNumber_lbl"].setHidden(False)
            return False
        elif(validation == 2):
            # confirm increase Amount
            getAmount = db.userBalanceRepository.GetBalance(self.userID)
            if(getAmount == []):
                getAmount = 0
                sum = getAmount + int(self.amount)
                newBalance = users_balanceTable(self.userID,sum)
                db.userBalanceRepository.Create(newBalance)
                db.userBalanceRepository.Save()
                balance.setText(f"{sum}")
            else:
                getAmount = getAmount[0][0]
                sum = getAmount + int(self.amount)
                newBalance = users_balanceTable(self.userID,sum)
                db.userBalanceRepository.Update(newBalance)
                db.userBalanceRepository.Save()
                balance.setText(f"{sum}")
            keyargs["wrongEmptyBalance_lbl"].setHidden(True)
            keyargs["okBalance_lbl"].setHidden(False)
            keyargs["wrongJustNumber_lbl"].setHidden(True)
            return True
            
    def EditUserInformation(self,userName,email,oldPass,dbPass,newPass,instance):
        validation = editValid(oldPass,dbPass,newPass).userValidate()
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
            updateUser = userTable(userName,email,newPass,self.GetAlluserInfo[0][4],self.GetAlluserInfo[0][5])
            db.userRepository.Update(updateUser,self.userID)
            db.userRepository.Save()
            return True
        
    def SeeFactorList(self,instance):
        findAlluserPayment = db.UserPaymentRepository.GetByUserID(self.userID)
        instance.orderCount_lbl.setText(f"تعداد سفارش ها : {len(findAlluserPayment)}")
        radif_dict = {}
        nameAndFamily_dict = {}
        orderID_dict = {}
        price_dict = {}
        date_dict = {}
        Details_dict = {}
        status_dict = {}
        height = 230
        index = 0
        for i in findAlluserPayment:
            paymentID = i[0]
            userID = i[1]
            buyID = i[2]
            userShortName = i[3]
            userFamily = i[4]
            totalPrice = i[9]
            date = i[10]
            
            checkOrderStatus = db.OperatorConfirmOrderRepository.CheckOrderStatus(userID,buyID)[0][0]
            
            # ---- createDynamic ----
            radif_dict[index] = QPushButton(instance)
            radif_dict[index].setText(f"{index}")
            radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            radif_dict[index].setGeometry(940,height,81,71)
            radif_dict[index].setObjectName(f"radif_{userID}|{buyID}")
            # -------
            nameAndFamily_dict[index] = QPushButton(instance)
            nameAndFamily_dict[index].setText(f"{userShortName} {userFamily}")
            nameAndFamily_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            nameAndFamily_dict[index].setGeometry(820,height,121,71)
            nameAndFamily_dict[index].setObjectName(f"userNameAndFamily_{userID}|{buyID}")
            # -------
            orderID_dict[index] = QPushButton(instance)
            orderID_dict[index].setText(f"{buyID}")
            orderID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            orderID_dict[index].setGeometry(690,height,131,71)
            orderID_dict[index].setObjectName(f"buyID_{userID}|{buyID}")
            # -------
            price_dict[index] = QPushButton(instance)
            price_dict[index].setText(f"{totalPrice}")
            price_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            price_dict[index].setGeometry(560,height,131,71)
            price_dict[index].setObjectName(f"PriceDict_{userID}|{buyID}")
            # -------
            date_dict[index] = QPushButton(instance)
            date_dict[index].setText(f"{date}")
            date_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            date_dict[index].setGeometry(440,height,121,71)
            date_dict[index].setObjectName(f"Email_{userID}|{buyID}")
            # -------
            Details_dict[index] = QPushButton(instance)
            Details_dict[index].setText(f"جزئییات")
            Details_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;font: bold 10pt 'B Nazanin';}")
            Details_dict[index].setGeometry(320,height,121,71)
            Details_dict[index].setObjectName(f"Details_{userID}|{buyID}")
            Details_dict[index].setCursor(Qt.PointingHandCursor)
            # -------
            status_dict[index] = QPushButton(instance)
            if(checkOrderStatus == 0):
                status_dict[index].setText(f"درحال برسی")
                status_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000; color : #000 ; font: bold 10pt 'B Nazanin';}")
                status_dict[index].setGeometry(50,height,271,71)
                status_dict[index].setObjectName(f"Status_{userID}|{buyID}")
            elif(checkOrderStatus == 1):
                status_dict[index].setText(f"تایید شده - درحال ارسال")
                status_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000; color : green; font: bold 10pt 'B Nazanin';}")
                status_dict[index].setGeometry(50,height,271,71)
                status_dict[index].setObjectName(f"Status_{userID}|{buyID}")   
            else:
                status_dict[index].setText(f"لغو شده - برگشت وجه")
                status_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000; color : red; font: bold 10pt 'B Nazanin';}")
                status_dict[index].setGeometry(50,height,271,71)
                status_dict[index].setObjectName(f"Status_{userID}|{buyID}")   
            
            # -----
            index += 1
            height += 70

            num = len(Details_dict)
            for i in range(num,20):
                Details_dict[i] = QPushButton(instance)
                Details_dict[i].setHidden(True)
                
            Details_dict[0].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[0].objectName()))
            Details_dict[1].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[1].objectName()))
            Details_dict[2].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[2].objectName()))
            Details_dict[3].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[3].objectName()))
            Details_dict[4].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[4].objectName()))
            Details_dict[5].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[5].objectName()))
            Details_dict[6].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[6].objectName()))
            Details_dict[7].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[7].objectName()))
            Details_dict[8].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[8].objectName()))
            Details_dict[9].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[9].objectName()))
            Details_dict[10].clicked.connect(lambda: instance.OpenDetialsOfFactorUI(Details_dict[10].objectName()))
            
    def seeDetailsOfFactor(self,BuyID,instance):
        findAlluserPayment = db.UserPaymentRepository.GetAllByUserAndBuyID(self.userID,BuyID)
        
        findAllShopCartAfterPayment = db.ShopCartAfterPeymentRepository.GetAllByUserAndBuyID(self.userID , BuyID)
        
        for i in findAlluserPayment:
            paymentID = i[0]
            userID = i[1]
            buyID = i[2]
            userShortName = i[3]
            userFamily = i[4]
            mobile = i[5]
            Address = i[6]
            state = i[7]
            city = i[8]
            totalPrice = i[9]
            date = i[10]
        instance.orderName_lbl.setText(f"سفارش به نام : {userShortName} {userFamily}")
        instance.mobile_lbl.setText(f"شماره تماس : {mobile}")
        instance.count_lbl.setText(f"تعداد لیست : {len(findAllShopCartAfterPayment)}")
        instance.factorIndex_lbl.setText(f"شماره فاکتور : {buyID}")
        instance.date_lbl.setText(f"تاریخ سفارش : {date}")
        instance.Adress_lbl.setText(f"{Address}")
        instance.state_lbl.setText(f"{state}")
        instance.city_lbl.setText(f"{city}")
        instance.totalPrice_lbl.setText(f"هزینه نهایی : {totalPrice}")
        
        Radif_dict = {}
        ProductName_dict = {}
        RandomID_dict = {}
        SalerName_dict = {}
        Price_dict = {}
        count_dict = {}
        OffName_dict = {}
        beforAff_dict = {}
        AfterOff_dict = {}
        height = 440
        index = 0
        
        for i in findAllShopCartAfterPayment:
            shopCartID = i[0]
            _buyID = i[1]
            productID = i[2]
            _userID = i[3]
            _salerID = i[4]
            count = i[5]
            _offID = i[6]
            
            findProductName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
            findProductRandomID = db.ProductsRepository.GetRandomID(productID)[0][0]
            findProductPrice = db.ProductsRepository.GetPriceByID(productID)[0][0]
            findSalerName = db.SalerRepository.GetSalerNameByID(_salerID)[0][0]
            findOffName = db.OffersRepository.GetCodeNameBYID(_offID)[0][0]
            if(findOffName == "None"):
                findOffName = "بدون تخفیف"
            findOffDiscount = db.OffersRepository.GetDiscountBYID(_offID)[0][0]
            price_beforOff = count * findProductPrice
            price_afterOff = int(price_beforOff - (price_beforOff * findOffDiscount / 100))
            
            # --- create Dynamics ---
            Radif_dict[index] = QPushButton(instance)
            Radif_dict[index].setText(f"{index}")
            Radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            Radif_dict[index].setGeometry(970,height,81,71)
            Radif_dict[index].setObjectName(f"index_{productID}")
            # -------
            ProductName_dict[index] = QPushButton(instance)
            ProductName_dict[index].setText(f"{findProductName}")
            ProductName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            ProductName_dict[index].setGeometry(850,height,121,71)
            ProductName_dict[index].setObjectName(f"productName_{productID}")
            # -------
            RandomID_dict[index] = QPushButton(instance)
            RandomID_dict[index].setText(f"{findProductRandomID}")
            RandomID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            RandomID_dict[index].setGeometry(730,height,121,71)
            RandomID_dict[index].setObjectName(f"productRandomID_{productID}")
            # -------
            SalerName_dict[index] = QPushButton(instance)
            SalerName_dict[index].setText(f"{findSalerName}")
            SalerName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            SalerName_dict[index].setGeometry(600,height,131,71)
            SalerName_dict[index].setObjectName(f"salerName_{productID}")
            # -------
            Price_dict[index] = QPushButton(instance)
            Price_dict[index].setText(f"{findProductPrice}")
            Price_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            Price_dict[index].setGeometry(470,height,131,71)
            Price_dict[index].setObjectName(f"priceDict_{productID}")
            # -------
            count_dict[index] = QPushButton(instance)
            count_dict[index].setText(f"{count}")
            count_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            count_dict[index].setGeometry(380,height,91,71)
            count_dict[index].setObjectName(f"count_{productID}")
            # -------
            OffName_dict[index] = QPushButton(instance)
            OffName_dict[index].setText(f"{findOffName}")
            OffName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            OffName_dict[index].setGeometry(260,height,121,71)
            OffName_dict[index].setObjectName(f"offName_{productID}")
            # -------
            beforAff_dict[index] = QPushButton(instance)
            beforAff_dict[index].setText(f"{price_beforOff}")
            beforAff_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            beforAff_dict[index].setGeometry(180,height,81,71)
            beforAff_dict[index].setObjectName(f"priceBeforOff_{productID}")
            # -------
            AfterOff_dict[index] = QPushButton(instance)
            AfterOff_dict[index].setText(f"{price_afterOff}")
            AfterOff_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            AfterOff_dict[index].setGeometry(50,height,131,71)
            AfterOff_dict[index].setObjectName(f"priceAfterOff_{productID}")
            
            index += 1
            height += 70
            
            
        