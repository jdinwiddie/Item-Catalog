from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, CatalogItem
 
engine = create_engine('sqlite:///superitemcatalogwithusers.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()



catalogItem1 = CatalogItem(name = "French Fries", description = "with garlic and parmesan", price = "$2.99")

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50")

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99")

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99")

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99")

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(name = "Iced Tea", description = "with Lemon", price = "$.99")

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese")

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices")

session.add(catalogItem8)
session.commit()
