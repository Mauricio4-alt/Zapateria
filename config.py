from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:mauricioj18@localhost/zapatos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
    
    db.init_app(app)

    from routes import register_routes
    register_routes(app)
    return app
