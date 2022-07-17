import sys
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context

db = context()

a = db.userRepository.GetByEmail("aa@email.com")
print(a)