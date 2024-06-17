from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://daan:welkom0162@daandb.lan/webshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    tags = db.Column(db.String(200), nullable=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    products = db.relationship('Product', backref='category', lazy=True)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@app.route('/products', methods=['POST'])
def post_products():
    new_products = request.json
    for product_data in new_products:
        new_product = product_schema.load(product_data, session=db.session)
        db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Products posted successfully"}), 200

@app.route('/products/search', methods=['POST'])
def search_products():
    criteria = request.json
    query = Product.query
    if 'keyword' in criteria:
        keyword = criteria['keyword']
        query = query.filter(Product.name.like(f"%{keyword}%") | Product.description.like(f"%{keyword}%"))
    if 'category' in criteria:
        category = criteria['category']
        query = query.filter(Product.category.has(name=category))
    if 'tags' in criteria:
        tags = criteria['tags']
        for tag in tags:
            query = query.filter(Product.tags.like(f"%{tag}%"))
    products = query.all()
    return products_schema.jsonify(products)

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return categories_schema.jsonify(categories)

@app.route('/categories', methods=['POST'])
def post_category():
    new_category = category_schema.load(request.json, session=db.session)
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category created successfully"}), 201

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        db.create_all()
    app.run(debug=True)
