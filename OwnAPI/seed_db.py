from app import db
from models import Product, Category


db.create_all()


category1 = Category(name='Toy', description='dog toys')
category2 = Category(name='Grooming products', description='animal grooming products')
db.session.add(category1)
db.session.add(category2)
db.session.commit()


product1 = Product(name='Ball', description='Ball for dogs', sku='12345', price=5.00, category_id=category1.id, tags='toy, dog')
product2 = Product(name='Wet food', description='Food for cats', sku='67890', price=2.50, category_id=category2.id, tags='cats, food')
db.session.add(product1)
db.session.add(product2)
db.session.commit()
