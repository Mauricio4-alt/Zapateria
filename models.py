from config import db

class  Products(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name =db.Column(db.String(255),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    stock = db.COlumn(db.Integer,nullable=False)
