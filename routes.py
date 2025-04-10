from run import app
from flask import request,jsonify 
from config import db
from models import Products
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/add_product',methods=['POST'])
def add_product():
    data = request.get_json()
    if 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({'message':'Error no name or no price or no stock'}),404
    try:
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')
        product = Products(name=name,price=price,stock=stock)
        db.session.add(product)
        db.session.commit()
        return jsonify ('Item insertado con éxito'),201
        
    except:
        return jsonify ({'Error':'Error to the request'}),400