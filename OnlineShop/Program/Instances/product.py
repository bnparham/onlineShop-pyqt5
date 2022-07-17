import sys
sys.path.append('../onlineShop')
from DataLayer.Services.UserRepository import UserRepository
from DataLayer.Context.UnitOfWork import context
from PyQt5.QtWidgets import QLabel , QPushButton

db = context()

class Product:
    def __init__(self,productID):
        self.ProductID = productID
    def showDetails(self,product,productID,details,price,date,salerName,CatName):
        findProduct = db.ProductsRepository.GetByID(self.ProductID)
        findSaler = db.SalerRepository.GetSalerNameByID(findProduct[0][6])
        findCatName = db.CatRepository.GetCatNameById(findProduct[0][7])
        product.setText(" اطلاعات " + findProduct[0][1])
        productID.setText(findProduct[0][5])
        details.setText(findProduct[0][2])
        price.setText(str(findProduct[0][3]))
        date.setText(findProduct[0][4])
        salerName.setText(findSaler[0][0])
        CatName.setText(findCatName[0][0])
        
    def showComments(self,instance):
        findAllComments = db.AllcommentsRepository.GetAllByProductID(self.ProductID)
        userName_btn = {}
        userComment_btn = {}
        height = 130
        index = 0
        if(findAllComments == []):
           noCommentBtn = QPushButton(instance)
           noCommentBtn.setText("هیچ نظری ثبت نشده است")
           noCommentBtn.setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;font: 22pt 'B Nazanin';}")
           noCommentBtn.setGeometry(70,210,441,411)
           noCommentBtn.setObjectName(f"noCommentBtn")
        else:
            for i in findAllComments:
                userID = i[2]
                findUserName = db.userRepository.GetUserNameByID(userID)[0][0]
                comment = i[3]
                # --->userName
                userName_btn[index] = QPushButton(instance)
                userName_btn[index].setText(findUserName)
                userName_btn[index].setStyleSheet("QPushButton { border:1px solid #000;background-color  : transparent;font: 15pt 'B Nazanin';}")
                userName_btn[index].setGeometry(430,height,141,61)
                userName_btn[index].setObjectName(f"userName_{userID}")
                # ---->userComment
                userComment_btn[index] = QLabel(instance)
                userComment_btn[index].setText(comment)
                userComment_btn[index].setWordWrap(True)
                userComment_btn[index].setStyleSheet("QLabel {font: 14pt 'B Nazanin';}")
                userComment_btn[index].setGeometry(10,height,401,81)
                userComment_btn[index].setObjectName(f"userComment_{userID}")
                # -----
                index += 1
                height += 110
    