import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.DataBase.connectionString import DataBase
from DataLayer.Services.UserRepository import UserRepository
from DataLayer.Services.UserBalanceRepository import UserBalanceRepository
from DataLayer.Services.ProductsRepository import ProductsRepository
from DataLayer.Services.FavoritRepository import FavoritListRepository
from DataLayer.Services.ShopCartRepository import ShopCartRepository
from DataLayer.Services.SalerRepository import SalerRepository
from DataLayer.Services.OffersRepository import OffersRepository
from DataLayer.Services.OperatorRepository import OperatorRepository
from DataLayer.Services.AllCommentsRepository import AllcommentsRepository
from DataLayer.Services.UserPaymentRepository import UserPaymentRepository
from DataLayer.Services.ShopCartAfterPeymentRepository import ShopCartAfterPeymentRepository
from DataLayer.Services.CatRepository import CatRepository
from DataLayer.Services.OperatorConfrimOrderRepository import OperatorConfirmOrderRepository


class context:
    def __init__(self):
        self.db = DataBase(r"DataLayer/Context/data.db")
        self.__userRepository = None
        self._userBalanceRepository = None
        self._ProductsRepository = None
        self._FavoritListRepository = None
        self._ShopCartRepository = None
        self._SalerRepository = None
        self._OffersRepository = None
        self._AllcommentsRepository = None
        self._UserPaymentRepository = None
        self._ShopCartAfterPeymentRepository = None
        self._OperatorRepository = None
        self._CatRepository = None
        self._OperatorConfirmOrderRepository = None
        
    @property
    def userRepository(self):
        if self.__userRepository is None:
            self.__userRepository = UserRepository(self.db)
        return self.__userRepository
    @property
    def userBalanceRepository(self):
        if self._userBalanceRepository is None:
            self._userBalanceRepository = UserBalanceRepository(self.db)
        return self._userBalanceRepository
    @property
    def ProductsRepository(self):
        if self._ProductsRepository is None:
            self._ProductsRepository = ProductsRepository(self.db)
        return self._ProductsRepository   
    @property
    def FavoritListRepository(self):
        if self._FavoritListRepository is None:
            self._FavoritListRepository = FavoritListRepository(self.db)
        return self._FavoritListRepository
    @property
    def ShopCartRepository(self):
        if self._ShopCartRepository is None:
            self._ShopCartRepository = ShopCartRepository(self.db)
        return self._ShopCartRepository
    @property
    def SalerRepository(self):
        if self._SalerRepository is None:
            self._SalerRepository = SalerRepository(self.db)
        return self._SalerRepository
    @property
    def OffersRepository(self):
        if self._OffersRepository is None:
            self._OffersRepository = OffersRepository(self.db)
        return self._OffersRepository
    @property
    def AllcommentsRepository(self):
        if self._AllcommentsRepository is None:
            self._AllcommentsRepository = AllcommentsRepository(self.db)
        return self._AllcommentsRepository
    @property
    def UserPaymentRepository(self):
        if self._UserPaymentRepository is None:
            self._UserPaymentRepository = UserPaymentRepository(self.db)
        return self._UserPaymentRepository
    @property
    def ShopCartAfterPeymentRepository(self):
        if self._ShopCartAfterPeymentRepository is None:
            self._ShopCartAfterPeymentRepository = ShopCartAfterPeymentRepository(self.db)
        return self._ShopCartAfterPeymentRepository
    
    @property
    def OperatorRepository(self):
        if self._OperatorRepository is None:
            self._OperatorRepository = OperatorRepository(self.db)
        return self._OperatorRepository
    
    @property
    def CatRepository(self):
        if self._CatRepository is None:
            self._CatRepository = CatRepository(self.db)
        return self._CatRepository
    
    @property
    def OperatorConfirmOrderRepository(self):
        if self._OperatorConfirmOrderRepository is None:
            self._OperatorConfirmOrderRepository = OperatorConfirmOrderRepository(self.db)
        return self._OperatorConfirmOrderRepository
    