import sys 
# setting path
sys.path.append('../DataLayer')
from DataLayer.Repository.IProductsRepository import IProductsRepository


class ProductsRepository(IProductsRepository):
    
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
       return self.db.getData("SELECT * FROM products")
   
    def GetByID(self,id):
        return self.db.getData(f"SELECT * FROM products WHERE id = {id}")
    
    def GetRandomID(self,id):
        return self.db.getData(f"SELECT RandomID FROM products WHERE id = {id}")
    def GetProductNameByID(self,id):
        return self.db.getData(f"SELECT productName FROM products WHERE id = {id}")
    def GetSalerIDByID(self,id):
        return self.db.getData(f"SELECT SalerID FROM products WHERE id = {id}")
    def GetPriceByID(self,id):
        return self.db.getData(f"SELECT Price FROM products WHERE id = {id}")
    def GetCatIDByID(self,id):
        return self.db.getData(f"SELECT catID FROM products WHERE id = {id}") 
    def GetDateByID(self,id):
        return self.db.getData(f"SELECT Date FROM products WHERE id = {id}")
    def GetDetailsByID(self,id):
        return self.db.getData(f"SELECT productDetail FROM products WHERE id = {id}") 
    
    def GetAllByCatID(self,catID):
        return self.db.getData(f"SELECT * FROM products WHERE catID = {catID}")
    
    def GetAllBySalerID(self,salerID):
        return self.db.getData(f"SELECT * FROM products WHERE salerID = {salerID}")
    
    def Create(self,product):
        self.db.runQuery("INSERT INTO products VALUES (NULL, ?, ?, ? ,?,?,?);", product.values())
        
    def Update(self,product,id):
        self.db.runQuery(f"UPDATE products SET productName = ?,productDetail = ? ,Price = ? , Date = ? ,  RandomID = ? , SalerID = ? , catID = ?  WHERE id = {id} ", product.values())
        
    def Delete(self,id):
        self.db.runQuery(f"DELETE FROM products WHERE id = {id}")
    
    def Save(self):
        return self.db.commit()