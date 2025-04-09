from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:mauricioj18@localhost/zapatos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
    app.config['SECRET_KEY'] ='mi_clave_secreta'
    db.init_app(app)
    return app
