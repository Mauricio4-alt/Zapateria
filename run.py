from config import create_app,db
app = create_app()


if __name__=='__main__':
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada con  éxito 🎉🎉")    
    app.run(debug=True,host='0.0.0.0',port=5000)

