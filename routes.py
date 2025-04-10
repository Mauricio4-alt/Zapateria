from flask import request,jsonify 
from config import db
from models import Products
def register_routes(app):
    @app.route('/add_product',methods=['POST'])
    def add_product():
        data = request.get_json()
        if 'name' not in data or 'price' not in data or 'stock' not in data:
            return jsonify({'message':'Error no name or no price or no stock'}),400
        try:
            name = data.get('name',None)
            price = data.get('price',None)
            stock = data.get('stock',None)
            product = Products(name=name,price=price,stock=stock)
            db.session.add(product)
            db.session.commit()
            return jsonify ({'message':'Item insertado con éxito'}),200
            
        except:
            return jsonify ({'Error':'Error to the request'}),400
    
    @app.route('/get_products',methods=['GET'])
    def get_products():
        products = Products.query.all()
        data = []
        for product in products:
            data.append({
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'stock':product.stock
            })
        return jsonify({'results':data})
    
    @app.route('/update_products',methods=['PUT'])
    def update_products():
        data = request.get_json()
        if 'name' not in data:
            return jsonify({'message','Error no hay parametro de busqueda name'})
        try: 
            name = data.get('name',None)
            product = Products.query.filter_by(name=name).first()
            if 'price' in data:
                product.price = data.get('price')
                db.session.commit()
            if 'stock' in data:
                product.stock = data.get('stock')
                db.session.commit()
            return jsonify({'message':'Cambios realizados con éxito'})
        except :
            return jsonify({'Error':'Error to the request'})
    
    @app.route('/delete_product',methods=['DELETE'])
    def delete_product():
        name = request.get_json().get('name',None)
        if not name:
            return jsonify({'message':'Sorry no name founded'})
        try: 
            product = Products.query.filter_by(name = name).first()
            db.session.delete(product)
            db.session.commit()
            return jsonify ({'message':'Producto eliminado satisfactoriamente'})
        except:
            return jsonify({'error':'Error to the request'})    


